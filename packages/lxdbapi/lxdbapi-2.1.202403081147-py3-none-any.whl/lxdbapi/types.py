# Copyright 2015 Lukas Lalinsky
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time
import base64
import datetime
from decimal import Decimal
from ._vendor.DateTime.DateTime import long
from ._vendor import pytz
from lxdbapi.common_pb2 import Rep
from lxdbapi.errors import ArrayTypeException
from lxdbapi import common_pb2

__all__ = [
    'Date', 'Time', 'Timestamp', 'DateFromTicks', 'TimeFromTicks', 'TimestampFromTicks',
    'Binary', 'STRING', 'BINARY', 'NUMBER', 'DATETIME', 'ROWID', 'BOOLEAN', 'javaTypetoNative',
    'nativeToParamType', 'datetimeToTimezoneUtc', 'timezoneFromDatetimeUtc', 'LXARRAY',
    'typed_value_2_native', 'native_2_typed_value'
]


def Date(year, month, day):
    """Constructs an object holding a date value."""
    return datetime.date(year, month, day)


def Time(hour, minute, second):
    """Constructs an object holding a time value."""
    return datetime.time(hour, minute, second)


def Timestamp(year, month, day, hour, minute, second):
    """Constructs an object holding a datetime/timestamp value."""
    return datetime.datetime(year, month, day, hour, minute, second)


def DateFromTicks(ticks):
    """Constructs an object holding a date value from the given UNIX timestamp."""
    return Date(*time.localtime(ticks)[:3])


def TimeFromTicks(ticks):
    """Constructs an object holding a time value from the given UNIX timestamp."""
    return Time(*time.localtime(ticks)[3:6])


def TimestampFromTicks(ticks):
    """Constructs an object holding a datetime/timestamp value from the given UNIX timestamp."""
    return Timestamp(*time.localtime(ticks)[:6])


def Binary(value):
    """Constructs an object capable of holding a binary (long) string value."""
    if isinstance(value, _BinaryString):
        return value
    return _BinaryString(base64.b64encode(value))

def time_from_java_sql_time(n):
    dt = datetime.datetime(1970, 1, 1) + datetime.timedelta(milliseconds=n)
    return dt.time()


def time_to_java_sql_time(t):
    return long(((t.hour * 60 + t.minute) * 60 + t.second) * 1000 + t.microsecond / 1000)


def date_from_java_sql_date(n):
    return datetime.date(1970, 1, 1) + datetime.timedelta(days=n)


def date_to_java_sql_date(d):
    if isinstance(d, datetime.datetime):
        d = d.date()
    td = d - datetime.date(1970, 1, 1)
    return td.days


def datetime_from_java_sql_timestamp(n):
    return datetime.datetime(1970, 1, 1, tzinfo=pytz.utc) + datetime.timedelta(milliseconds=n)


def datetime_to_java_sql_timestamp(d):
    td = d - datetime.datetime(1970, 1, 1).replace(tzinfo=pytz.utc)
    return long(td.microseconds / 1000 + (td.seconds + td.days * 24 * 3600) * 1000)


class _BinaryString(str):
    pass


class ColumnType(object):

    def __init__(self, eq_types):
        self.eq_types = tuple(eq_types)
        self.eq_types_set = set(eq_types)

    def __cmp__(self, other):
        if other in self.eq_types_set:
            return 0
        if other < self.eq_types:
            return 1
        else:
            return -1


STRING = ColumnType(['VARCHAR', 'CHAR'])
"""Type object that can be used to describe string-based columns."""

BINARY = ColumnType(['BINARY', 'VARBINARY'])
"""Type object that can be used to describe (long) binary columns."""

NUMBER = ColumnType(['INTEGER', 'UNSIGNED_INT', 'BIGINT', 'UNSIGNED_LONG', 'TINYINT', 'UNSIGNED_TINYINT', 'SMALLINT', 'UNSIGNED_SMALLINT', 'FLOAT', 'UNSIGNED_FLOAT', 'DOUBLE', 'UNSIGNED_DOUBLE', 'DECIMAL'])
"""Type object that can be used to describe numeric columns."""

DATETIME = ColumnType(['TIME', 'DATE', 'TIMESTAMP', 'UNSIGNED_TIME', 'UNSIGNED_DATE', 'UNSIGNED_TIMESTAMP'])
"""Type object that can be used to describe date/time columns."""

ROWID = ColumnType([])
"""Only implemented for DB API 2.0 compatibility, not used."""

BOOLEAN = ColumnType(['BOOLEAN'])
"""Type object that can be used to describe boolean columns. This is a lxdbapi-specific extension."""

# XXX ARRAY
class LXARRAY():
    __value = []
    __type = None
    def __init__(self, value, type):
        self.__value = value
        self.__type = type

    def getvalue(self):
        return self.__value
    def setvalue(self, value):
        self.__value = value

    def gettype(self):
        return self.__type

    def settype(self, type):
        self.__type = type


def typedValueToNative(v):
    if Rep.Name(v.type) == "BOOLEAN" or Rep.Name(v.type) == "PRIMITIVE_BOOLEAN":
        return v.bool_value

    elif Rep.Name(v.type) == "STRING" or Rep.Name(v.type) == "PRIMITIVE_CHAR" or Rep.Name(v.type) == "CHARACTER" or Rep.Name(v.type) == "BIG_DECIMAL":
        return v.string_value

    elif Rep.Name(v.type) == "FLOAT" or Rep.Name(v.type) == "PRIMITIVE_FLOAT" or Rep.Name(v.type) == "DOUBLE" or Rep.Name(v.type) == "PRIMITIVE_DOUBLE":
        return v.double_value

    elif Rep.Name(v.type) == "LONG" or Rep.Name(v.type) == "PRIMITIVE_LONG" or Rep.Name(v.type) == "INTEGER" or Rep.Name(v.type) == "PRIMITIVE_INT" or \
                    Rep.Name(v.type) == "BIG_INTEGER" or Rep.Name(v.type) == "NUMBER" or Rep.Name(v.type) == "BYTE" or Rep.Name(v.type) == "PRIMITIVE_BYTE" or \
                    Rep.Name(v.type) == "SHORT" or Rep.Name(v.type) == "PRIMITIVE_SHORT":
        return v.number_value

    elif Rep.Name(v.type) == "BYTE_STRING":
        return v.bytes_value

    else:
        return None

def javaTypetoNative(java_type):
    if java_type == 'java.math.BigDecimal':
        return ('BIG_DECIMAL', None, "string_value")
    elif java_type == 'java.lang.Float':
        return ('FLOAT', float, "double_value")
    elif java_type == 'java.lang.Double':
        return ('DOUBLE', None, "double_value")
    elif java_type == 'java.lang.Long':
        return ('LONG', None, "number_value")
    elif java_type == 'java.lang.Integer':
        return ('INTEGER', int, "number_value")
    elif java_type == 'java.lang.Short':
        return ('SHORT', int, "number_value")
    elif java_type == 'java.lang.Byte':
        return ('BYTE', Binary, "bytes_value")
    elif java_type == 'java.lang.Boolean':
        return ('BOOLEAN', bool, "bool_value")
    elif java_type == 'java.lang.String':
        return ('STRING', None, "string_value")
    elif java_type == 'java.sql.Time':
        return ('JAVA_SQL_TIME', time_from_java_sql_time, "number_value")
    elif java_type == 'java.sql.Date':
        return ('JAVA_SQL_DATE', date_from_java_sql_date, "number_value")
    elif java_type == 'java.sql.Timestamp':
        return ('JAVA_SQL_TIMESTAMP', datetime_from_java_sql_timestamp, "number_value")
    elif java_type == '[B':
        return ('BYTE_STRING', bytes, "bytes_value")
    else:
        return ('NULL', None)

def nativeToParamType(value, isArray=False):
    if isinstance(value, int):
        if(abs(value) <= 0x7FFFFFFF and not isArray):
            return ('INTEGER', int, "number_value")
        else:
            return ('LONG', int, "number_value")
    elif isinstance(value, float):
        return ('DOUBLE', float, "double_value")
    elif isinstance(value, bool):
        return ('BOOLEAN', bool, "bool_value")
    elif isinstance(value, str):
        return ('STRING', str, "string_value")
    elif isinstance(value, datetime.time):
        return ('JAVA_SQL_TIME', time_to_java_sql_time, "number_value")
    elif isinstance(value, datetime.datetime):  # TODO check: important to put this case before datetime.date as datetimes also match in date clause
        return ('JAVA_SQL_TIMESTAMP', datetime_to_java_sql_timestamp, "number_value")
    elif isinstance(value, datetime.date):
        return ('JAVA_SQL_DATE', date_to_java_sql_date, "number_value")
    elif isinstance(value, bytes):
        return ('BYTE_STRING', bytes, "bytes_value")
    elif isinstance(value, LXARRAY):
        return ('ARRAY', None, "array_value")
    elif value == None:
        return ('NULL', None, "null")
    else:
        return ('STRING', str, "string_value")


def lxarray2tv(value: LXARRAY):
    result = common_pb2.TypedValue()  # parent typed value
    result.type = common_pb2.Rep.Value('ARRAY')
    if value.gettype() is int:
        result.component_type = common_pb2.Rep.Value("LONG")
    elif value.gettype() is float:
        result.component_type = common_pb2.Rep.Value("DOUBLE")
    elif value.gettype() is str:
        result.component_type = common_pb2.Rep.Value("STRING")
    else:
        raise ArrayTypeException("Array cannot be of type: {}".format(value.gettype()))

    for item in value.getvalue():
        type_param = nativeToParamType(item, isArray=True)  # int bigint varchar ???
        v_temp = common_pb2.TypedValue()
        v_temp.type = common_pb2.Rep.Value(type_param[0])
        if item != None:
            setattr(v_temp, type_param[2], type_param[1](item))
        else:
            setattr(v_temp, type_param[2], 1)  # 1 for True
        result.array_value.append(v_temp)
    return result


def typed_value_2_native(typed_value: common_pb2.TypedValue):
    func = _rep_to_native_funcs[_rep_index_to_name[typed_value.type]]
    if func is None:
        _unsupported_typed_value(typed_value)
        return None
    return func(typed_value)

def _bool_value_2_native(typed_value: common_pb2.TypedValue):
    return bool(typed_value.bool_value)


def _string_value_2_native(typed_value: common_pb2.TypedValue):
    return str(typed_value.string_value)

def _big_decimal_value_2_native(typed_value: common_pb2.TypedValue):
    value = str(typed_value.string_value)
    if '.' not in value and ',' not in value:
        return int(value)
    return Decimal(value)

def _bytes_value_2_native(typed_value: common_pb2.TypedValue):
    return bytes(typed_value.bytes_value)


def _number_value_2_native(typed_value: common_pb2.TypedValue):
    return int(typed_value.number_value)


def _double_value_2_native(typed_value: common_pb2.TypedValue):
    return float(typed_value.double_value)


def _null_value_2_native(typed_value: common_pb2.TypedValue):
    return None


def _unsupported_typed_value(typed_value: common_pb2.TypedValue):
    raise NotImplementedError("Not supported: " + _rep_index_to_name[typed_value.type])


_rep_index_to_name = ['PRIMITIVE_BOOLEAN',
                      'PRIMITIVE_BYTE',
                      'PRIMITIVE_CHAR',
                      'PRIMITIVE_SHORT',
                      'PRIMITIVE_INT',
                      'PRIMITIVE_LONG',
                      'PRIMITIVE_FLOAT',
                      'PRIMITIVE_DOUBLE',
                      'BOOLEAN',
                      'BYTE',
                      'CHARACTER',
                      'SHORT',
                      'INTEGER',
                      'LONG',
                      'FLOAT',
                      'DOUBLE',
                      'JAVA_SQL_TIME',
                      'JAVA_SQL_TIMESTAMP',
                      'JAVA_SQL_DATE',
                      'JAVA_UTIL_DATE',
                      'BYTE_STRING',
                      'STRING',
                      'NUMBER',
                      'OBJECT',
                      'NULL',
                      'BIG_INTEGER',
                      'BIG_DECIMAL',
                      'ARRAY',
                      'STRUCT',
                      'MULTISET']


_rep_to_native_funcs = {'ARRAY': _unsupported_typed_value,
                        'BIG_DECIMAL': _big_decimal_value_2_native,
                        'BIG_INTEGER': _bytes_value_2_native,
                        'BOOLEAN': _bool_value_2_native,
                        'BYTE': _number_value_2_native,
                        'BYTE_STRING': _bytes_value_2_native,
                        'CHARACTER': _string_value_2_native,
                        'DOUBLE': _double_value_2_native,
                        'FLOAT': _double_value_2_native,
                        'INTEGER': _number_value_2_native,
                        'JAVA_SQL_DATE': _number_value_2_native,
                        'JAVA_SQL_TIME': _number_value_2_native,
                        'JAVA_SQL_TIMESTAMP': _number_value_2_native,
                        'JAVA_UTIL_DATE': _number_value_2_native,
                        'LONG': _number_value_2_native,
                        'MULTISET': _unsupported_typed_value,
                        'NULL': _null_value_2_native,
                        'NUMBER': _number_value_2_native,
                        'OBJECT': _unsupported_typed_value,
                        'PRIMITIVE_BOOLEAN': _bool_value_2_native,
                        'PRIMITIVE_BYTE': _number_value_2_native,
                        'PRIMITIVE_CHAR': _string_value_2_native,
                        'PRIMITIVE_DOUBLE': _number_value_2_native,
                        'PRIMITIVE_FLOAT': _double_value_2_native,
                        'PRIMITIVE_INT': _number_value_2_native,
                        'PRIMITIVE_LONG': _number_value_2_native,
                        'PRIMITIVE_SHORT': _number_value_2_native,
                        'SHORT': _number_value_2_native,
                        'STRING': _string_value_2_native,
                        'STRUCT': _unsupported_typed_value}


def native_2_typed_value(value, ctx):
    type_param = nativeToParamType(value)
    if value is None:
        return common_pb2.TypedValue(null=True, type=common_pb2.Rep.Value('NULL'))
    if isinstance(value, LXARRAY):
        return lxarray2tv(value)

    result = common_pb2.TypedValue()
    result.type = common_pb2.Rep.Value(type_param[0])
    if type_param[1] is not None:
        if isinstance(value, datetime.datetime):
            if value.tzinfo is None:
                value = value.replace(tzinfo=ctx._connection.tzinfo)
        setattr(result, type_param[2], type_param[1](value))
    else:
        setattr(result, type_param[2], value)
    return result
