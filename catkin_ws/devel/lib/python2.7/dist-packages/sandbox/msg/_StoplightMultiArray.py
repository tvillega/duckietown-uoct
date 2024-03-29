# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from sandbox/StoplightMultiArray.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import sandbox.msg
import std_msgs.msg

class StoplightMultiArray(genpy.Message):
  _md5sum = "36040492c6f40acc8475256baa3fc1e7"
  _type = "sandbox/StoplightMultiArray"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """Header StoplightMultiArray
sandbox/Stoplight[] traffic_lights
int16 deface
int16[] clock# syncronized clock for all stoplights

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: sandbox/Stoplight
Header Stoplight
string type # cross, street, blink warning
string direction # norht2south, east2west, up2down
int16[] colors # [red,gree,blue,custom]
"""
  __slots__ = ['StoplightMultiArray','traffic_lights','deface','clock']
  _slot_types = ['std_msgs/Header','sandbox/Stoplight[]','int16','int16[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       StoplightMultiArray,traffic_lights,deface,clock

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(StoplightMultiArray, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.StoplightMultiArray is None:
        self.StoplightMultiArray = std_msgs.msg.Header()
      if self.traffic_lights is None:
        self.traffic_lights = []
      if self.deface is None:
        self.deface = 0
      if self.clock is None:
        self.clock = []
    else:
      self.StoplightMultiArray = std_msgs.msg.Header()
      self.traffic_lights = []
      self.deface = 0
      self.clock = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.StoplightMultiArray.seq, _x.StoplightMultiArray.stamp.secs, _x.StoplightMultiArray.stamp.nsecs))
      _x = self.StoplightMultiArray.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.traffic_lights)
      buff.write(_struct_I.pack(length))
      for val1 in self.traffic_lights:
        _v1 = val1.Stoplight
        buff.write(_get_struct_I().pack(_v1.seq))
        _v2 = _v1.stamp
        _x = _v2
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v1.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.type
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.direction
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.colors)
        buff.write(_struct_I.pack(length))
        pattern = '<%sh'%length
        buff.write(struct.pack(pattern, *val1.colors))
      buff.write(_get_struct_h().pack(self.deface))
      length = len(self.clock)
      buff.write(_struct_I.pack(length))
      pattern = '<%sh'%length
      buff.write(struct.pack(pattern, *self.clock))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.StoplightMultiArray is None:
        self.StoplightMultiArray = std_msgs.msg.Header()
      if self.traffic_lights is None:
        self.traffic_lights = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.StoplightMultiArray.seq, _x.StoplightMultiArray.stamp.secs, _x.StoplightMultiArray.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.StoplightMultiArray.frame_id = str[start:end].decode('utf-8')
      else:
        self.StoplightMultiArray.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.traffic_lights = []
      for i in range(0, length):
        val1 = sandbox.msg.Stoplight()
        _v3 = val1.Stoplight
        start = end
        end += 4
        (_v3.seq,) = _get_struct_I().unpack(str[start:end])
        _v4 = _v3.stamp
        _x = _v4
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v3.frame_id = str[start:end].decode('utf-8')
        else:
          _v3.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.type = str[start:end].decode('utf-8')
        else:
          val1.type = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.direction = str[start:end].decode('utf-8')
        else:
          val1.direction = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sh'%length
        start = end
        end += struct.calcsize(pattern)
        val1.colors = struct.unpack(pattern, str[start:end])
        self.traffic_lights.append(val1)
      start = end
      end += 2
      (self.deface,) = _get_struct_h().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sh'%length
      start = end
      end += struct.calcsize(pattern)
      self.clock = struct.unpack(pattern, str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.StoplightMultiArray.seq, _x.StoplightMultiArray.stamp.secs, _x.StoplightMultiArray.stamp.nsecs))
      _x = self.StoplightMultiArray.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.traffic_lights)
      buff.write(_struct_I.pack(length))
      for val1 in self.traffic_lights:
        _v5 = val1.Stoplight
        buff.write(_get_struct_I().pack(_v5.seq))
        _v6 = _v5.stamp
        _x = _v6
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v5.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.type
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1.direction
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.colors)
        buff.write(_struct_I.pack(length))
        pattern = '<%sh'%length
        buff.write(val1.colors.tostring())
      buff.write(_get_struct_h().pack(self.deface))
      length = len(self.clock)
      buff.write(_struct_I.pack(length))
      pattern = '<%sh'%length
      buff.write(self.clock.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.StoplightMultiArray is None:
        self.StoplightMultiArray = std_msgs.msg.Header()
      if self.traffic_lights is None:
        self.traffic_lights = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.StoplightMultiArray.seq, _x.StoplightMultiArray.stamp.secs, _x.StoplightMultiArray.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.StoplightMultiArray.frame_id = str[start:end].decode('utf-8')
      else:
        self.StoplightMultiArray.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.traffic_lights = []
      for i in range(0, length):
        val1 = sandbox.msg.Stoplight()
        _v7 = val1.Stoplight
        start = end
        end += 4
        (_v7.seq,) = _get_struct_I().unpack(str[start:end])
        _v8 = _v7.stamp
        _x = _v8
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v7.frame_id = str[start:end].decode('utf-8')
        else:
          _v7.frame_id = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.type = str[start:end].decode('utf-8')
        else:
          val1.type = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.direction = str[start:end].decode('utf-8')
        else:
          val1.direction = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sh'%length
        start = end
        end += struct.calcsize(pattern)
        val1.colors = numpy.frombuffer(str[start:end], dtype=numpy.int16, count=length)
        self.traffic_lights.append(val1)
      start = end
      end += 2
      (self.deface,) = _get_struct_h().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sh'%length
      start = end
      end += struct.calcsize(pattern)
      self.clock = numpy.frombuffer(str[start:end], dtype=numpy.int16, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_h = None
def _get_struct_h():
    global _struct_h
    if _struct_h is None:
        _struct_h = struct.Struct("<h")
    return _struct_h
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
