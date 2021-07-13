import os
import random
import grpc
from map_reduce.proto import distmr_pb2_grpc, distmr_pb2
from task_type import TaskType
from worker import map_task, reduce_task
from driver import log_format
import logging
from directory import INPUT_DIR, INTERMEDIATE_DIR, OUTPUT_DIR, LOG_DIR

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')
file_handler = logging.FileHandler(os.path.join(LOG_DIR, "client_logs.log"))
file_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(file_handler)


class MapReduceClient(object):
    def __init__(self):
        self.host = '[::]'
        self.port = 50051
        self.channel = grpc.insecure_channel(f'{self.host}:{self.port}')
        self.stub = distmr_pb2_grpc.MapReduceStub(self.channel)


if __name__ == '__main__':
    client = MapReduceClient()
    worker_id = random.randint(10, 100)
    logger.info(f"Starting up worker with id: {worker_id}")
    task_state = 1
    cnt = 1
    while True:
        logger.info(f"Building request {cnt}")
        cnt += 1
        request = distmr_pb2.WorkerState()
        request.worker_id = worker_id
        request.task_state = task_state
        task = client.stub.GetTask(request)
        if task.task_type == TaskType.MAP.value:
            logger.info(f"Running MAP task with: \n"
                        f"map_task_id = {task.task_id} \n"
                        f"input_filepath = {task.input_filepath} \n"
                        f"intermediate_dir = {task.output_filepath} \n")
            map_task(
                map_task_id=task.task_id,
                input_filepath=task.input_filepath,
                intermediate_dir=task.output_filepath,
                M=5  # TODO: remove hardcoded value
            )
        elif task.task_type == TaskType.REDUCE.value:
            logger.info(f"Running REDUCE task with: \n"
                        f"reduce_task_id = {task.task_id} \n"
                        f"intermediate_dir = {task.input_filepath} \n"
                        f"output_dir = {task.output_filepath} \n")
            reduce_task(
                reduce_task_id=task.task_id,
                intermediate_dir=task.input_filepath,
                output_dir=task.output_filepath
            )
