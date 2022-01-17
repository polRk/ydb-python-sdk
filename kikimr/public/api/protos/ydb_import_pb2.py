# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ydb/public/api/protos/ydb_import.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ydb.public.api.protos.annotations import validation_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_annotations_dot_validation__pb2
from ydb.public.api.protos import ydb_operation_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ydb/public/api/protos/ydb_import.proto',
  package='Ydb.Import',
  syntax='proto3',
  serialized_options=b'\n\026com.yandex.ydb.import_\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)ydb/public/api/protos/ydb_import.proto\x12\nYdb.Import\x1a\x35ydb/public/api/protos/annotations/validation.proto\x1a,ydb/public/api/protos/ydb_operation.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xcd\x01\n\x0eImportProgress\"\xba\x01\n\x08Progress\x12\x18\n\x14PROGRESS_UNSPECIFIED\x10\x00\x12\x16\n\x12PROGRESS_PREPARING\x10\x01\x12\x1a\n\x16PROGRESS_TRANSFER_DATA\x10\x02\x12\x1a\n\x16PROGRESS_BUILD_INDEXES\x10\x03\x12\x11\n\rPROGRESS_DONE\x10\x04\x12\x19\n\x15PROGRESS_CANCELLATION\x10\x05\x12\x16\n\x12PROGRESS_CANCELLED\x10\x06\"\xa0\x01\n\x12ImportItemProgress\x12\x13\n\x0bparts_total\x18\x01 \x01(\r\x12\x17\n\x0fparts_completed\x18\x02 \x01(\r\x12.\n\nstart_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x9d\x03\n\x14ImportFromS3Settings\x12\x16\n\x08\x65ndpoint\x18\x01 \x01(\tB\x04\x90\xe6*\x01\x12\x37\n\x06scheme\x18\x02 \x01(\x0e\x32\'.Ydb.Import.ImportFromS3Settings.Scheme\x12\x14\n\x06\x62ucket\x18\x03 \x01(\tB\x04\x90\xe6*\x01\x12\x18\n\naccess_key\x18\x04 \x01(\tB\x04\x90\xe6*\x01\x12\x18\n\nsecret_key\x18\x05 \x01(\tB\x04\x90\xe6*\x01\x12<\n\x05items\x18\x06 \x03(\x0b\x32%.Ydb.Import.ImportFromS3Settings.ItemB\x06\x9a\xe6*\x02(\x01\x12\x1c\n\x0b\x64\x65scription\x18\x07 \x01(\tB\x07\xa2\xe6*\x03\x18\x80\x01\x12\x19\n\x11number_of_retries\x18\x08 \x01(\r\x1a\x43\n\x04Item\x12\x1b\n\rsource_prefix\x18\x01 \x01(\tB\x04\x90\xe6*\x01\x12\x1e\n\x10\x64\x65stination_path\x18\x02 \x01(\tB\x04\x90\xe6*\x01\".\n\x06Scheme\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x08\n\x04HTTP\x10\x01\x12\t\n\x05HTTPS\x10\x02\"\x14\n\x12ImportFromS3Result\"\xb9\x01\n\x14ImportFromS3Metadata\x12\x32\n\x08settings\x18\x01 \x01(\x0b\x32 .Ydb.Import.ImportFromS3Settings\x12\x35\n\x08progress\x18\x02 \x01(\x0e\x32#.Ydb.Import.ImportProgress.Progress\x12\x36\n\x0eitems_progress\x18\x03 \x03(\x0b\x32\x1e.Ydb.Import.ImportItemProgress\"\x8a\x01\n\x13ImportFromS3Request\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\x38\n\x08settings\x18\x02 \x01(\x0b\x32 .Ydb.Import.ImportFromS3SettingsB\x04\x90\xe6*\x01\"D\n\x14ImportFromS3Response\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.Operation\" \n\rYdbDumpFormat\x12\x0f\n\x07\x63olumns\x18\x01 \x03(\t\"\x12\n\x10ImportDataResult\"\xae\x01\n\x11ImportDataRequest\x12\x39\n\x10operation_params\x18\x01 \x01(\x0b\x32\x1f.Ydb.Operations.OperationParams\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x17\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x42\t\xa2\xe6*\x05\x18\x80\x80\x80\x04\x12-\n\x08ydb_dump\x18\x04 \x01(\x0b\x32\x19.Ydb.Import.YdbDumpFormatH\x00\x42\x08\n\x06\x66ormat\"B\n\x12ImportDataResponse\x12,\n\toperation\x18\x01 \x01(\x0b\x32\x19.Ydb.Operations.OperationB\x1b\n\x16\x63om.yandex.ydb.import_\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[kikimr_dot_public_dot_api_dot_protos_dot_annotations_dot_validation__pb2.DESCRIPTOR,kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_IMPORTPROGRESS_PROGRESS = _descriptor.EnumDescriptor(
  name='Progress',
  full_name='Ydb.Import.ImportProgress.Progress',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PROGRESS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROGRESS_PREPARING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROGRESS_TRANSFER_DATA', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROGRESS_BUILD_INDEXES', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROGRESS_DONE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROGRESS_CANCELLATION', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROGRESS_CANCELLED', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=211,
  serialized_end=397,
)
_sym_db.RegisterEnumDescriptor(_IMPORTPROGRESS_PROGRESS)

_IMPORTFROMS3SETTINGS_SCHEME = _descriptor.EnumDescriptor(
  name='Scheme',
  full_name='Ydb.Import.ImportFromS3Settings.Scheme',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HTTP', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HTTPS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=930,
  serialized_end=976,
)
_sym_db.RegisterEnumDescriptor(_IMPORTFROMS3SETTINGS_SCHEME)


_IMPORTPROGRESS = _descriptor.Descriptor(
  name='ImportProgress',
  full_name='Ydb.Import.ImportProgress',
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
    _IMPORTPROGRESS_PROGRESS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=192,
  serialized_end=397,
)


_IMPORTITEMPROGRESS = _descriptor.Descriptor(
  name='ImportItemProgress',
  full_name='Ydb.Import.ImportItemProgress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parts_total', full_name='Ydb.Import.ImportItemProgress.parts_total', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parts_completed', full_name='Ydb.Import.ImportItemProgress.parts_completed', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='Ydb.Import.ImportItemProgress.start_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='Ydb.Import.ImportItemProgress.end_time', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=400,
  serialized_end=560,
)


_IMPORTFROMS3SETTINGS_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='Ydb.Import.ImportFromS3Settings.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_prefix', full_name='Ydb.Import.ImportFromS3Settings.Item.source_prefix', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\220\346*\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='destination_path', full_name='Ydb.Import.ImportFromS3Settings.Item.destination_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\220\346*\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=861,
  serialized_end=928,
)

_IMPORTFROMS3SETTINGS = _descriptor.Descriptor(
  name='ImportFromS3Settings',
  full_name='Ydb.Import.ImportFromS3Settings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endpoint', full_name='Ydb.Import.ImportFromS3Settings.endpoint', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\220\346*\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scheme', full_name='Ydb.Import.ImportFromS3Settings.scheme', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bucket', full_name='Ydb.Import.ImportFromS3Settings.bucket', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\220\346*\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_key', full_name='Ydb.Import.ImportFromS3Settings.access_key', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\220\346*\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='secret_key', full_name='Ydb.Import.ImportFromS3Settings.secret_key', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\220\346*\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='items', full_name='Ydb.Import.ImportFromS3Settings.items', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\232\346*\002(\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='Ydb.Import.ImportFromS3Settings.description', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\242\346*\003\030\200\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='number_of_retries', full_name='Ydb.Import.ImportFromS3Settings.number_of_retries', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_IMPORTFROMS3SETTINGS_ITEM, ],
  enum_types=[
    _IMPORTFROMS3SETTINGS_SCHEME,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=563,
  serialized_end=976,
)


_IMPORTFROMS3RESULT = _descriptor.Descriptor(
  name='ImportFromS3Result',
  full_name='Ydb.Import.ImportFromS3Result',
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=978,
  serialized_end=998,
)


_IMPORTFROMS3METADATA = _descriptor.Descriptor(
  name='ImportFromS3Metadata',
  full_name='Ydb.Import.ImportFromS3Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='settings', full_name='Ydb.Import.ImportFromS3Metadata.settings', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='progress', full_name='Ydb.Import.ImportFromS3Metadata.progress', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='items_progress', full_name='Ydb.Import.ImportFromS3Metadata.items_progress', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1001,
  serialized_end=1186,
)


_IMPORTFROMS3REQUEST = _descriptor.Descriptor(
  name='ImportFromS3Request',
  full_name='Ydb.Import.ImportFromS3Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Ydb.Import.ImportFromS3Request.operation_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='settings', full_name='Ydb.Import.ImportFromS3Request.settings', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\220\346*\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1189,
  serialized_end=1327,
)


_IMPORTFROMS3RESPONSE = _descriptor.Descriptor(
  name='ImportFromS3Response',
  full_name='Ydb.Import.ImportFromS3Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.Import.ImportFromS3Response.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1329,
  serialized_end=1397,
)


_YDBDUMPFORMAT = _descriptor.Descriptor(
  name='YdbDumpFormat',
  full_name='Ydb.Import.YdbDumpFormat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='columns', full_name='Ydb.Import.YdbDumpFormat.columns', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1399,
  serialized_end=1431,
)


_IMPORTDATARESULT = _descriptor.Descriptor(
  name='ImportDataResult',
  full_name='Ydb.Import.ImportDataResult',
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1433,
  serialized_end=1451,
)


_IMPORTDATAREQUEST = _descriptor.Descriptor(
  name='ImportDataRequest',
  full_name='Ydb.Import.ImportDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation_params', full_name='Ydb.Import.ImportDataRequest.operation_params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='Ydb.Import.ImportDataRequest.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='Ydb.Import.ImportDataRequest.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\242\346*\005\030\200\200\200\004', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ydb_dump', full_name='Ydb.Import.ImportDataRequest.ydb_dump', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='format', full_name='Ydb.Import.ImportDataRequest.format',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1454,
  serialized_end=1628,
)


_IMPORTDATARESPONSE = _descriptor.Descriptor(
  name='ImportDataResponse',
  full_name='Ydb.Import.ImportDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='Ydb.Import.ImportDataResponse.operation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1630,
  serialized_end=1696,
)

_IMPORTPROGRESS_PROGRESS.containing_type = _IMPORTPROGRESS
_IMPORTITEMPROGRESS.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_IMPORTITEMPROGRESS.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_IMPORTFROMS3SETTINGS_ITEM.containing_type = _IMPORTFROMS3SETTINGS
_IMPORTFROMS3SETTINGS.fields_by_name['scheme'].enum_type = _IMPORTFROMS3SETTINGS_SCHEME
_IMPORTFROMS3SETTINGS.fields_by_name['items'].message_type = _IMPORTFROMS3SETTINGS_ITEM
_IMPORTFROMS3SETTINGS_SCHEME.containing_type = _IMPORTFROMS3SETTINGS
_IMPORTFROMS3METADATA.fields_by_name['settings'].message_type = _IMPORTFROMS3SETTINGS
_IMPORTFROMS3METADATA.fields_by_name['progress'].enum_type = _IMPORTPROGRESS_PROGRESS
_IMPORTFROMS3METADATA.fields_by_name['items_progress'].message_type = _IMPORTITEMPROGRESS
_IMPORTFROMS3REQUEST.fields_by_name['operation_params'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_IMPORTFROMS3REQUEST.fields_by_name['settings'].message_type = _IMPORTFROMS3SETTINGS
_IMPORTFROMS3RESPONSE.fields_by_name['operation'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
_IMPORTDATAREQUEST.fields_by_name['operation_params'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATIONPARAMS
_IMPORTDATAREQUEST.fields_by_name['ydb_dump'].message_type = _YDBDUMPFORMAT
_IMPORTDATAREQUEST.oneofs_by_name['format'].fields.append(
  _IMPORTDATAREQUEST.fields_by_name['ydb_dump'])
_IMPORTDATAREQUEST.fields_by_name['ydb_dump'].containing_oneof = _IMPORTDATAREQUEST.oneofs_by_name['format']
_IMPORTDATARESPONSE.fields_by_name['operation'].message_type = kikimr_dot_public_dot_api_dot_protos_dot_ydb__operation__pb2._OPERATION
DESCRIPTOR.message_types_by_name['ImportProgress'] = _IMPORTPROGRESS
DESCRIPTOR.message_types_by_name['ImportItemProgress'] = _IMPORTITEMPROGRESS
DESCRIPTOR.message_types_by_name['ImportFromS3Settings'] = _IMPORTFROMS3SETTINGS
DESCRIPTOR.message_types_by_name['ImportFromS3Result'] = _IMPORTFROMS3RESULT
DESCRIPTOR.message_types_by_name['ImportFromS3Metadata'] = _IMPORTFROMS3METADATA
DESCRIPTOR.message_types_by_name['ImportFromS3Request'] = _IMPORTFROMS3REQUEST
DESCRIPTOR.message_types_by_name['ImportFromS3Response'] = _IMPORTFROMS3RESPONSE
DESCRIPTOR.message_types_by_name['YdbDumpFormat'] = _YDBDUMPFORMAT
DESCRIPTOR.message_types_by_name['ImportDataResult'] = _IMPORTDATARESULT
DESCRIPTOR.message_types_by_name['ImportDataRequest'] = _IMPORTDATAREQUEST
DESCRIPTOR.message_types_by_name['ImportDataResponse'] = _IMPORTDATARESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImportProgress = _reflection.GeneratedProtocolMessageType('ImportProgress', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTPROGRESS,
  '__module__' : 'ydb.public.api.protos.ydb_import_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Import.ImportProgress)
  })
_sym_db.RegisterMessage(ImportProgress)

ImportItemProgress = _reflection.GeneratedProtocolMessageType('ImportItemProgress', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTITEMPROGRESS,
  '__module__' : 'ydb.public.api.protos.ydb_import_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Import.ImportItemProgress)
  })
_sym_db.RegisterMessage(ImportItemProgress)

ImportFromS3Settings = _reflection.GeneratedProtocolMessageType('ImportFromS3Settings', (_message.Message,), {

  'Item' : _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
    'DESCRIPTOR' : _IMPORTFROMS3SETTINGS_ITEM,
    '__module__' : 'ydb.public.api.protos.ydb_import_pb2'
    # @@protoc_insertion_point(class_scope:Ydb.Import.ImportFromS3Settings.Item)
    })
  ,
  'DESCRIPTOR' : _IMPORTFROMS3SETTINGS,
  '__module__' : 'ydb.public.api.protos.ydb_import_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Import.ImportFromS3Settings)
  })
_sym_db.RegisterMessage(ImportFromS3Settings)
_sym_db.RegisterMessage(ImportFromS3Settings.Item)

ImportFromS3Result = _reflection.GeneratedProtocolMessageType('ImportFromS3Result', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTFROMS3RESULT,
  '__module__' : 'ydb.public.api.protos.ydb_import_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Import.ImportFromS3Result)
  })
_sym_db.RegisterMessage(ImportFromS3Result)

ImportFromS3Metadata = _reflection.GeneratedProtocolMessageType('ImportFromS3Metadata', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTFROMS3METADATA,
  '__module__' : 'ydb.public.api.protos.ydb_import_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Import.ImportFromS3Metadata)
  })
_sym_db.RegisterMessage(ImportFromS3Metadata)

ImportFromS3Request = _reflection.GeneratedProtocolMessageType('ImportFromS3Request', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTFROMS3REQUEST,
  '__module__' : 'ydb.public.api.protos.ydb_import_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Import.ImportFromS3Request)
  })
_sym_db.RegisterMessage(ImportFromS3Request)

ImportFromS3Response = _reflection.GeneratedProtocolMessageType('ImportFromS3Response', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTFROMS3RESPONSE,
  '__module__' : 'ydb.public.api.protos.ydb_import_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Import.ImportFromS3Response)
  })
_sym_db.RegisterMessage(ImportFromS3Response)

YdbDumpFormat = _reflection.GeneratedProtocolMessageType('YdbDumpFormat', (_message.Message,), {
  'DESCRIPTOR' : _YDBDUMPFORMAT,
  '__module__' : 'ydb.public.api.protos.ydb_import_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Import.YdbDumpFormat)
  })
_sym_db.RegisterMessage(YdbDumpFormat)

ImportDataResult = _reflection.GeneratedProtocolMessageType('ImportDataResult', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTDATARESULT,
  '__module__' : 'ydb.public.api.protos.ydb_import_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Import.ImportDataResult)
  })
_sym_db.RegisterMessage(ImportDataResult)

ImportDataRequest = _reflection.GeneratedProtocolMessageType('ImportDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTDATAREQUEST,
  '__module__' : 'ydb.public.api.protos.ydb_import_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Import.ImportDataRequest)
  })
_sym_db.RegisterMessage(ImportDataRequest)

ImportDataResponse = _reflection.GeneratedProtocolMessageType('ImportDataResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTDATARESPONSE,
  '__module__' : 'ydb.public.api.protos.ydb_import_pb2'
  # @@protoc_insertion_point(class_scope:Ydb.Import.ImportDataResponse)
  })
_sym_db.RegisterMessage(ImportDataResponse)


DESCRIPTOR._options = None
_IMPORTFROMS3SETTINGS_ITEM.fields_by_name['source_prefix']._options = None
_IMPORTFROMS3SETTINGS_ITEM.fields_by_name['destination_path']._options = None
_IMPORTFROMS3SETTINGS.fields_by_name['endpoint']._options = None
_IMPORTFROMS3SETTINGS.fields_by_name['bucket']._options = None
_IMPORTFROMS3SETTINGS.fields_by_name['access_key']._options = None
_IMPORTFROMS3SETTINGS.fields_by_name['secret_key']._options = None
_IMPORTFROMS3SETTINGS.fields_by_name['items']._options = None
_IMPORTFROMS3SETTINGS.fields_by_name['description']._options = None
_IMPORTFROMS3REQUEST.fields_by_name['settings']._options = None
_IMPORTDATAREQUEST.fields_by_name['data']._options = None
# @@protoc_insertion_point(module_scope)
