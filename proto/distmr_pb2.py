# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: distmr.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='distmr.proto',
  package='distmr',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x64istmr.proto\x12\x06\x64istmr\"4\n\x0bWorkerState\x12\x11\n\tworker_id\x18\x01 \x01(\x05\x12\x12\n\ntask_state\x18\x02 \x01(\x05\"[\n\x04Task\x12\x0f\n\x07task_id\x18\x01 \x01(\x05\x12\x11\n\ttask_type\x18\x02 \x01(\x05\x12\x16\n\x0einput_filepath\x18\x03 \x01(\t\x12\x17\n\x0foutput_filepath\x18\x04 \x01(\t2;\n\tMapReduce\x12.\n\x07GetTask\x12\x13.distmr.WorkerState\x1a\x0c.distmr.Task\"\x00\x62\x06proto3'
)




_WORKERSTATE = _descriptor.Descriptor(
  name='WorkerState',
  full_name='distmr.WorkerState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='worker_id', full_name='distmr.WorkerState.worker_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_state', full_name='distmr.WorkerState.task_state', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=76,
)


_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='distmr.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='distmr.Task.task_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='task_type', full_name='distmr.Task.task_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='input_filepath', full_name='distmr.Task.input_filepath', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_filepath', full_name='distmr.Task.output_filepath', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=169,
)

DESCRIPTOR.message_types_by_name['WorkerState'] = _WORKERSTATE
DESCRIPTOR.message_types_by_name['Task'] = _TASK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WorkerState = _reflection.GeneratedProtocolMessageType('WorkerState', (_message.Message,), {
  'DESCRIPTOR' : _WORKERSTATE,
  '__module__' : 'distmr_pb2'
  # @@protoc_insertion_point(class_scope:distmr.WorkerState)
  })
_sym_db.RegisterMessage(WorkerState)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {
  'DESCRIPTOR' : _TASK,
  '__module__' : 'distmr_pb2'
  # @@protoc_insertion_point(class_scope:distmr.Task)
  })
_sym_db.RegisterMessage(Task)



_MAPREDUCE = _descriptor.ServiceDescriptor(
  name='MapReduce',
  full_name='distmr.MapReduce',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=171,
  serialized_end=230,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTask',
    full_name='distmr.MapReduce.GetTask',
    index=0,
    containing_service=None,
    input_type=_WORKERSTATE,
    output_type=_TASK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MAPREDUCE)

DESCRIPTOR.services_by_name['MapReduce'] = _MAPREDUCE

# @@protoc_insertion_point(module_scope)
