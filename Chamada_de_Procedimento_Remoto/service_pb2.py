# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\x12\x07Service\"\x19\n\x06Pedido\x12\x0f\n\x07\x63omando\x18\x01 \x01(\t\"\x1d\n\x08Resposta\x12\x11\n\tresultado\x18\x01 \x01(\t2B\n\x07Service\x12\x37\n\x0f\x45xecutarComando\x12\x0f.Service.Pedido\x1a\x11.Service.Resposta\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PEDIDO._serialized_start=26
  _PEDIDO._serialized_end=51
  _RESPOSTA._serialized_start=53
  _RESPOSTA._serialized_end=82
  _SERVICE._serialized_start=84
  _SERVICE._serialized_end=150
# @@protoc_insertion_point(module_scope)