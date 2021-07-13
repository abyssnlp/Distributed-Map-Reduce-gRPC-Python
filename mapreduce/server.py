import grpc
import os
import sys
import argparse
import logging
from collections import Counter
from concurrent import futures
from map_reduce.proto import distmr_pb2_grpc
from driver import Driver, LOG_DIR, log_format
from task_type import TaskType
from directory import INPUT_DIR, INTERMEDIATE_DIR, OUTPUT_DIR

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')
file_handler = logging.FileHandler(os.path.join(LOG_DIR, "server_logs.log"))
file_handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(file_handler)

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--num_maps", type=int)
parser.add_argument("-m", "--num_reduce", type=int)
args = parser.parse_args()

N = args.num_maps
M = args.num_reduce


class MapReduceServer(distmr_pb2_grpc.MapReduceServicer):
    def __init__(self):
        logger.info("Initializing Server with number of map and reduce jobs...")
        self.driver = Driver(N, M)
        self.driver.create_storage()

    def GetTask(self, request, context):
        worker_id = request.worker_id
        worker_state = request.task_state
        logger.info(f"Generating next task for {worker_id} with state: {worker_state}")
        next_task = self.driver.task_generator()
        if worker_state != -1 and next_task != -1:
            return next_task
        elif next_task == -1:
            logger.warning("No task found! Exiting...")
            sys.exit(1)
        else:
            raise AttributeError(f"{worker_id}: Worker not ready!")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    distmr_pb2_grpc.add_MapReduceServicer_to_server(
        MapReduceServer(),
        server
    )
    server.add_insecure_port('[::]:50051')
    logger.info("Starting Server on port 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
