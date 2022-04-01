# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: password.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0epassword.proto\"%\n\x0e\x45ncryptRequest\x12\x13\n\x0b\x62\x61se64_data\x18\x01 \x01(\t\")\n\x0f\x45ncryptResponse\x12\x16\n\x0e\x62\x61se64_encrypt\x18\x01 \x01(\t\"$\n\x14\x45ncryptStringRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"/\n\x15\x45ncryptStringResponse\x12\x16\n\x0e\x62\x61se64_encrypt\x18\x01 \x01(\t\".\n\x14\x44\x65\x63ryptStringRequest\x12\x16\n\x0e\x62\x61se64_encrypt\x18\x01 \x01(\t\"-\n\x15\x44\x65\x63ryptStringResponse\x12\x14\n\x0c\x64\x65\x63rypt_data\x18\x01 \x01(\t2\xb9\x01\n\tServerAes\x12,\n\x07\x45ncrypt\x12\x0f.EncryptRequest\x1a\x10.EncryptResponse\x12>\n\rEncryptString\x12\x15.EncryptStringRequest\x1a\x16.EncryptStringResponse\x12>\n\rDecryptString\x12\x15.DecryptStringRequest\x1a\x16.DecryptStringResponseB\nZ\x08../protob\x06proto3')



_ENCRYPTREQUEST = DESCRIPTOR.message_types_by_name['EncryptRequest']
_ENCRYPTRESPONSE = DESCRIPTOR.message_types_by_name['EncryptResponse']
_ENCRYPTSTRINGREQUEST = DESCRIPTOR.message_types_by_name['EncryptStringRequest']
_ENCRYPTSTRINGRESPONSE = DESCRIPTOR.message_types_by_name['EncryptStringResponse']
_DECRYPTSTRINGREQUEST = DESCRIPTOR.message_types_by_name['DecryptStringRequest']
_DECRYPTSTRINGRESPONSE = DESCRIPTOR.message_types_by_name['DecryptStringResponse']
EncryptRequest = _reflection.GeneratedProtocolMessageType('EncryptRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENCRYPTREQUEST,
  '__module__' : 'password_pb2'
  # @@protoc_insertion_point(class_scope:EncryptRequest)
  })
_sym_db.RegisterMessage(EncryptRequest)

EncryptResponse = _reflection.GeneratedProtocolMessageType('EncryptResponse', (_message.Message,), {
  'DESCRIPTOR' : _ENCRYPTRESPONSE,
  '__module__' : 'password_pb2'
  # @@protoc_insertion_point(class_scope:EncryptResponse)
  })
_sym_db.RegisterMessage(EncryptResponse)

EncryptStringRequest = _reflection.GeneratedProtocolMessageType('EncryptStringRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENCRYPTSTRINGREQUEST,
  '__module__' : 'password_pb2'
  # @@protoc_insertion_point(class_scope:EncryptStringRequest)
  })
_sym_db.RegisterMessage(EncryptStringRequest)

EncryptStringResponse = _reflection.GeneratedProtocolMessageType('EncryptStringResponse', (_message.Message,), {
  'DESCRIPTOR' : _ENCRYPTSTRINGRESPONSE,
  '__module__' : 'password_pb2'
  # @@protoc_insertion_point(class_scope:EncryptStringResponse)
  })
_sym_db.RegisterMessage(EncryptStringResponse)

DecryptStringRequest = _reflection.GeneratedProtocolMessageType('DecryptStringRequest', (_message.Message,), {
  'DESCRIPTOR' : _DECRYPTSTRINGREQUEST,
  '__module__' : 'password_pb2'
  # @@protoc_insertion_point(class_scope:DecryptStringRequest)
  })
_sym_db.RegisterMessage(DecryptStringRequest)

DecryptStringResponse = _reflection.GeneratedProtocolMessageType('DecryptStringResponse', (_message.Message,), {
  'DESCRIPTOR' : _DECRYPTSTRINGRESPONSE,
  '__module__' : 'password_pb2'
  # @@protoc_insertion_point(class_scope:DecryptStringResponse)
  })
_sym_db.RegisterMessage(DecryptStringResponse)

_SERVERAES = DESCRIPTOR.services_by_name['ServerAes']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\010../proto'
  _ENCRYPTREQUEST._serialized_start=18
  _ENCRYPTREQUEST._serialized_end=55
  _ENCRYPTRESPONSE._serialized_start=57
  _ENCRYPTRESPONSE._serialized_end=98
  _ENCRYPTSTRINGREQUEST._serialized_start=100
  _ENCRYPTSTRINGREQUEST._serialized_end=136
  _ENCRYPTSTRINGRESPONSE._serialized_start=138
  _ENCRYPTSTRINGRESPONSE._serialized_end=185
  _DECRYPTSTRINGREQUEST._serialized_start=187
  _DECRYPTSTRINGREQUEST._serialized_end=233
  _DECRYPTSTRINGRESPONSE._serialized_start=235
  _DECRYPTSTRINGRESPONSE._serialized_end=280
  _SERVERAES._serialized_start=283
  _SERVERAES._serialized_end=468
# @@protoc_insertion_point(module_scope)
