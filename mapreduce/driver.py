from queue import Queue
from itertools import product
import os
from map_reduce.proto import distmr_pb2, distmr_pb2_grpc
from directory import OUTPUT_DIR, INTERMEDIATE_DIR, INPUT_DIR, LOG_DIR
from task_type import TaskType
import logging


log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')

file_handler = logging.FileHandler(os.path.join(LOG_DIR, "driver_logs.log"))
file_handler.setFormatter(logging.Formatter(log_format))

logger.addHandler(file_handler)


class Driver:
    def __init__(self, N, M):
        self.n = N  # number of map tasks
        self.m = M  # number of reduce tasks
        logger.info("Calling create_input_queue function from task generator ...")
        self.input_queue = self.create_input_queue()
        logger.info(f"Input queue: {self.input_queue.queue}")
        self.gen_map_task_id = self.generate_task_id(TaskType.MAP.value)
        self.gen_red_task_id = self.generate_task_id(TaskType.REDUCE.value)

    @staticmethod
    def create_input_queue():
        logger.info("Creating input file queue...")
        q = Queue()
        for f in os.listdir(INPUT_DIR):
            q.put(f)
        return q

    def create_storage(self):
        """
        Create folders in the intermediate and output folders
        taking into consideration the number of map and reduce buckets
        :return: void
        """
        logger.info("Creating storage for map and reduce jobs...")
        # for map tasks
        for n, m in list(product(range(self.n), range(self.m))):
            with open(os.path.join(INTERMEDIATE_DIR, f'mr-{n}-{m}'), 'w') as f:
                f.close()
        # for reduce tasks
        for i in range(self.m):
            with open(os.path.join(OUTPUT_DIR, f'out-{i}'), 'w') as f:
                f.close()

    @staticmethod
    def create_task(task_id, task_type, input_filepath, output_filepath):
        logger.info(f"Creating Task: {task_id} of type {task_type} at {input_filepath} with output: {output_filepath}")
        task = distmr_pb2.Task()
        task.task_id = task_id
        task.task_type = task_type
        task.input_filepath = input_filepath
        task.output_filepath = output_filepath
        return task

    def generate_task_id(self, task_type):
        if task_type == TaskType.MAP.value:
            for i in range(self.n):
                logger.info(f"Generating MAP task_id: {i}")
                yield i
        elif task_type == TaskType.REDUCE.value:
            for j in range(self.m):
                logger.info(f"Generating REDUCE task_id: {j}")
                yield j
        else:
            logger.exception("Wrong task type!")

    def task_generator(self):
        if not self.input_queue.empty():
            return self.create_task(
                task_id=next(self.gen_map_task_id),
                task_type=TaskType.MAP.value,
                input_filepath=os.path.join(INPUT_DIR, self.input_queue.get()),
                output_filepath=INTERMEDIATE_DIR
            )
        else:
            task_id = next(self.gen_red_task_id)
            if task_id > self.m - 1:
                return -1
            else:
                return self.create_task(
                    task_id=task_id,
                    task_type=TaskType.REDUCE.value,
                    input_filepath=INTERMEDIATE_DIR,
                    output_filepath=OUTPUT_DIR
                )
