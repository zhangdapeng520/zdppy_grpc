# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jwt.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tjwt.proto\"j\n\x12\x43reateTokenRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08usertype\x18\x03 \x01(\t\x12\x0c\n\x04role\x18\x04 \x01(\x05\x12\x11\n\tjson_data\x18\x05 \x01(\t\"$\n\x13\x43reateTokenResponse\x12\r\n\x05token\x18\x01 \x01(\t\"\"\n\x11ParseTokenRequest\x12\r\n\x05token\x18\x01 \x01(\t\"j\n\x12ParseTokenResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08usertype\x18\x03 \x01(\t\x12\x0c\n\x04role\x18\x04 \x01(\x05\x12\x11\n\tjson_data\x18\x05 \x01(\t\"$\n\x13RefreshTokenRequest\x12\r\n\x05token\x18\x01 \x01(\t\"%\n\x14RefreshTokenResponse\x12\r\n\x05token\x18\x01 \x01(\t2\xb9\x01\n\tServerJwt\x12\x38\n\x0b\x43reateToken\x12\x13.CreateTokenRequest\x1a\x14.CreateTokenResponse\x12\x35\n\nParseToken\x12\x12.ParseTokenRequest\x1a\x13.ParseTokenResponse\x12;\n\x0cRefreshToken\x12\x14.RefreshTokenRequest\x1a\x15.RefreshTokenResponseB\nZ\x08../protob\x06proto3')



_CREATETOKENREQUEST = DESCRIPTOR.message_types_by_name['CreateTokenRequest']
_CREATETOKENRESPONSE = DESCRIPTOR.message_types_by_name['CreateTokenResponse']
_PARSETOKENREQUEST = DESCRIPTOR.message_types_by_name['ParseTokenRequest']
_PARSETOKENRESPONSE = DESCRIPTOR.message_types_by_name['ParseTokenResponse']
_REFRESHTOKENREQUEST = DESCRIPTOR.message_types_by_name['RefreshTokenRequest']
_REFRESHTOKENRESPONSE = DESCRIPTOR.message_types_by_name['RefreshTokenResponse']
CreateTokenRequest = _reflection.GeneratedProtocolMessageType('CreateTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATETOKENREQUEST,
  '__module__' : 'jwt_pb2'
  # @@protoc_insertion_point(class_scope:CreateTokenRequest)
  })
_sym_db.RegisterMessage(CreateTokenRequest)

CreateTokenResponse = _reflection.GeneratedProtocolMessageType('CreateTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATETOKENRESPONSE,
  '__module__' : 'jwt_pb2'
  # @@protoc_insertion_point(class_scope:CreateTokenResponse)
  })
_sym_db.RegisterMessage(CreateTokenResponse)

ParseTokenRequest = _reflection.GeneratedProtocolMessageType('ParseTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _PARSETOKENREQUEST,
  '__module__' : 'jwt_pb2'
  # @@protoc_insertion_point(class_scope:ParseTokenRequest)
  })
_sym_db.RegisterMessage(ParseTokenRequest)

ParseTokenResponse = _reflection.GeneratedProtocolMessageType('ParseTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _PARSETOKENRESPONSE,
  '__module__' : 'jwt_pb2'
  # @@protoc_insertion_point(class_scope:ParseTokenResponse)
  })
_sym_db.RegisterMessage(ParseTokenResponse)

RefreshTokenRequest = _reflection.GeneratedProtocolMessageType('RefreshTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _REFRESHTOKENREQUEST,
  '__module__' : 'jwt_pb2'
  # @@protoc_insertion_point(class_scope:RefreshTokenRequest)
  })
_sym_db.RegisterMessage(RefreshTokenRequest)

RefreshTokenResponse = _reflection.GeneratedProtocolMessageType('RefreshTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _REFRESHTOKENRESPONSE,
  '__module__' : 'jwt_pb2'
  # @@protoc_insertion_point(class_scope:RefreshTokenResponse)
  })
_sym_db.RegisterMessage(RefreshTokenResponse)

_SERVERJWT = DESCRIPTOR.services_by_name['ServerJwt']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\010../proto'
  _CREATETOKENREQUEST._serialized_start=13
  _CREATETOKENREQUEST._serialized_end=119
  _CREATETOKENRESPONSE._serialized_start=121
  _CREATETOKENRESPONSE._serialized_end=157
  _PARSETOKENREQUEST._serialized_start=159
  _PARSETOKENREQUEST._serialized_end=193
  _PARSETOKENRESPONSE._serialized_start=195
  _PARSETOKENRESPONSE._serialized_end=301
  _REFRESHTOKENREQUEST._serialized_start=303
  _REFRESHTOKENREQUEST._serialized_end=339
  _REFRESHTOKENRESPONSE._serialized_start=341
  _REFRESHTOKENRESPONSE._serialized_end=378
  _SERVERJWT._serialized_start=381
  _SERVERJWT._serialized_end=566
# @@protoc_insertion_point(module_scope)
