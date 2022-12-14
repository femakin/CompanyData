# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/internal/test_bad_identifiers.proto

from cloudsdk.google.protobuf import descriptor as _descriptor
from cloudsdk.google.protobuf import message as _message
from cloudsdk.google.protobuf import reflection as _reflection
from cloudsdk.google.protobuf import symbol_database as _symbol_database
from cloudsdk.google.protobuf import service as _service
from cloudsdk.google.protobuf import service_reflection
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/internal/test_bad_identifiers.proto',
  package='protobuf_unittest',
  syntax='proto2',
  serialized_options=b'\220\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3google/protobuf/internal/test_bad_identifiers.proto\x12\x11protobuf_unittest\"\x1e\n\x12TestBadIdentifiers*\x08\x08\x64\x10\x80\x80\x80\x80\x02\"\x10\n\x0e\x41notherMessage2\x10\n\x0e\x41notherService:;\n\x07message\x12%.protobuf_unittest.TestBadIdentifiers\x18\x64 \x01(\t:\x03\x66oo:>\n\ndescriptor\x12%.protobuf_unittest.TestBadIdentifiers\x18\x65 \x01(\t:\x03\x62\x61r:>\n\nreflection\x12%.protobuf_unittest.TestBadIdentifiers\x18\x66 \x01(\t:\x03\x62\x61z:;\n\x07service\x12%.protobuf_unittest.TestBadIdentifiers\x18g \x01(\t:\x03quxB\x03\x90\x01\x01'
)


MESSAGE_FIELD_NUMBER = 100
message = _descriptor.FieldDescriptor(
  name='message', full_name='protobuf_unittest.message', index=0,
  number=100, type=9, cpp_type=9, label=1,
  has_default_value=True, default_value=b"foo".decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
DESCRIPTOR_FIELD_NUMBER = 101
descriptor = _descriptor.FieldDescriptor(
  name='descriptor', full_name='protobuf_unittest.descriptor', index=1,
  number=101, type=9, cpp_type=9, label=1,
  has_default_value=True, default_value=b"bar".decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
REFLECTION_FIELD_NUMBER = 102
reflection = _descriptor.FieldDescriptor(
  name='reflection', full_name='protobuf_unittest.reflection', index=2,
  number=102, type=9, cpp_type=9, label=1,
  has_default_value=True, default_value=b"baz".decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
SERVICE_FIELD_NUMBER = 103
service = _descriptor.FieldDescriptor(
  name='service', full_name='protobuf_unittest.service', index=3,
  number=103, type=9, cpp_type=9, label=1,
  has_default_value=True, default_value=b"qux".decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)


_TESTBADIDENTIFIERS = _descriptor.Descriptor(
  name='TestBadIdentifiers',
  full_name='protobuf_unittest.TestBadIdentifiers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(100, 536870912), ],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=104,
)


_ANOTHERMESSAGE = _descriptor.Descriptor(
  name='AnotherMessage',
  full_name='protobuf_unittest.AnotherMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=122,
)

DESCRIPTOR.message_types_by_name['TestBadIdentifiers'] = _TESTBADIDENTIFIERS
DESCRIPTOR.message_types_by_name['AnotherMessage'] = _ANOTHERMESSAGE
DESCRIPTOR.extensions_by_name['message'] = message
DESCRIPTOR.extensions_by_name['descriptor'] = descriptor
DESCRIPTOR.extensions_by_name['reflection'] = reflection
DESCRIPTOR.extensions_by_name['service'] = service
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestBadIdentifiers = _reflection.GeneratedProtocolMessageType('TestBadIdentifiers', (_message.Message,), {
  'DESCRIPTOR' : _TESTBADIDENTIFIERS,
  '__module__' : 'google.protobuf.internal.test_bad_identifiers_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestBadIdentifiers)
  })
_sym_db.RegisterMessage(TestBadIdentifiers)

AnotherMessage = _reflection.GeneratedProtocolMessageType('AnotherMessage', (_message.Message,), {
  'DESCRIPTOR' : _ANOTHERMESSAGE,
  '__module__' : 'google.protobuf.internal.test_bad_identifiers_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest.AnotherMessage)
  })
_sym_db.RegisterMessage(AnotherMessage)

TestBadIdentifiers.RegisterExtension(message)
TestBadIdentifiers.RegisterExtension(descriptor)
TestBadIdentifiers.RegisterExtension(reflection)
TestBadIdentifiers.RegisterExtension(service)

DESCRIPTOR._options = None

_ANOTHERSERVICE = _descriptor.ServiceDescriptor(
  name='AnotherService',
  full_name='protobuf_unittest.AnotherService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=124,
  serialized_end=140,
  methods=[
])
_sym_db.RegisterServiceDescriptor(_ANOTHERSERVICE)

DESCRIPTOR.services_by_name['AnotherService'] = _ANOTHERSERVICE

AnotherService = service_reflection.GeneratedServiceType('AnotherService', (_service.Service,), dict(
  DESCRIPTOR = _ANOTHERSERVICE,
  __module__ = 'google.protobuf.internal.test_bad_identifiers_pb2'
  ))

AnotherService_Stub = service_reflection.GeneratedServiceStubType('AnotherService_Stub', (AnotherService,), dict(
  DESCRIPTOR = _ANOTHERSERVICE,
  __module__ = 'google.protobuf.internal.test_bad_identifiers_pb2'
  ))


# @@protoc_insertion_point(module_scope)
