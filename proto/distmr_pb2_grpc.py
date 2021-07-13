# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import map_reduce.proto.distmr_pb2 as distmr__pb2


class MapReduceStub(object):
    """
    MapReduce: rpc to get tasks from the driver
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTask = channel.unary_unary(
                '/distmr.MapReduce/GetTask',
                request_serializer=distmr__pb2.WorkerState.SerializeToString,
                response_deserializer=distmr__pb2.Task.FromString,
                )


class MapReduceServicer(object):
    """
    MapReduce: rpc to get tasks from the driver
    """

    def GetTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MapReduceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTask': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTask,
                    request_deserializer=distmr__pb2.WorkerState.FromString,
                    response_serializer=distmr__pb2.Task.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'distmr.MapReduce', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MapReduce(object):
    """
    MapReduce: rpc to get tasks from the driver
    """

    @staticmethod
    def GetTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/distmr.MapReduce/GetTask',
            distmr__pb2.WorkerState.SerializeToString,
            distmr__pb2.Task.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)