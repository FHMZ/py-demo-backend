# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: setup.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'setup.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bsetup.proto\x12\x05setup\"\xb9\x03\n\x0cSetupRequest\x12\x13\n\x0b\x62\x61nk_branch\x18\x01 \x01(\t\x12\x1b\n\x13\x62\x61nk_account_number\x18\x02 \x01(\t\x12\x18\n\x10\x63ompany_identity\x18\x03 \x01(\t\x12\x14\n\x0c\x63ompany_name\x18\x04 \x01(\t\x12\x15\n\raccount_digit\x18\x05 \x01(\t\x12\x14\n\x0c\x61\x63\x63ount_type\x18\x06 \x01(\x05\x12\x16\n\x0e\x61\x63\x63ount_office\x18\x07 \x01(\t\x12\x18\n\x10\x61\x63\x63ount_currency\x18\x08 \x01(\t\x12\x1d\n\x15\x61\x63\x63ount_manager_email\x18\t \x01(\t\x12\x1b\n\x13\x61\x63\x63ount_external_id\x18\n \x01(\t\x12\x17\n\x0fuser_first_name\x18\x0b \x01(\t\x12\x16\n\x0euser_last_name\x18\x0c \x01(\t\x12\x12\n\nuser_email\x18\r \x01(\t\x12\x1c\n\x14user_phone_area_code\x18\x0e \x01(\x05\x12\x19\n\x11user_phone_number\x18\x0f \x01(\x05\x12\x15\n\ruser_identity\x18\x10 \x01(\t\x12\x17\n\x0fuser_birth_date\x18\x11 \x01(\t\"\'\n\rSetupResponse\x12\x16\n\x0etransaction_id\x18\x01 \x01(\t2L\n\x16\x43\x65leroCustomLayerSetup\x12\x32\n\x05Setup\x12\x13.setup.SetupRequest\x1a\x14.setup.SetupResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'setup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SETUPREQUEST']._serialized_start=23
  _globals['_SETUPREQUEST']._serialized_end=464
  _globals['_SETUPRESPONSE']._serialized_start=466
  _globals['_SETUPRESPONSE']._serialized_end=505
  _globals['_CELEROCUSTOMLAYERSETUP']._serialized_start=507
  _globals['_CELEROCUSTOMLAYERSETUP']._serialized_end=583
# @@protoc_insertion_point(module_scope)