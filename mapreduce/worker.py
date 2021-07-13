import os
import re
import logging
from collections import Counter
from driver import log_format
from directory import LOG_DIR

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')
file_handler = logging.FileHandler(os.path.join(LOG_DIR, "worker_logs.log"))
file_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(file_handler)


def map_task(map_task_id, input_filepath, intermediate_dir, M) -> None:
    logger.info(f"Starting MAP task for {input_filepath}")
    with open(input_filepath, 'r') as f:
        for line in f:
            if line:
                line = re.sub(r'[^a-zA-Z\s]+', '', line)
                line = re.sub(r'\s+', ' ', line)
                line = re.sub('\n', ' ', line)
                words = line.strip().split(" ")
                counts = list(map(lambda x: f"{x} 1", words))
                for pair in counts:
                    bucket_id = ord(pair[0]) % M
                    with open(os.path.join(intermediate_dir, f'mr-{map_task_id}-{bucket_id}'), 'a') as g:
                        g.write(pair)
                        g.write('\n')


def reduce_task(reduce_task_id, intermediate_dir, output_dir) -> None:
    logger.info(f"Starting REDUCE task for {intermediate_dir} - {reduce_task_id}")
    reduce_files = [x for x in os.listdir(intermediate_dir) if x.split('-')[2] == reduce_task_id]
    logger.info(f"MAP files to REDUCE for {reduce_task_id}: {' '.join(reduce_files)}")
    counter = Counter()
    for reduce_file in reduce_files:
        logger.info(f"Reducing for {reduce_file} ...")
        _cnt = dict()
        with open(os.path.join(intermediate_dir, reduce_file), 'r') as f:
            for line in f:
                word, _ = line.split(" ")
                if word in _cnt:
                    _cnt[word] += 1
                else:
                    _cnt[word] = 1
        counter.update(_cnt)
    logger.info(f"Writing output of REDUCE task to out-{reduce_task_id}")
    with open(os.path.join(output_dir, f'out-{reduce_task_id}'), 'a') as g:
        for k, v in counter.items():
            g.write(f"{k} {v}")
            g.write("\n")
