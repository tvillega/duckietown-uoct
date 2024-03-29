# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from sandbox/array.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import sandbox.msg

class array(genpy.Message):
  _md5sum = "91faa4ba0e0b5a49fa10b31bb254bdd0"
  _type = "sandbox/array"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """sandbox/layout layout
int16[] data # For aditional data realted

================================================================================
MSG: sandbox/layout
sandbox/dimension[] dim
int16[] clock

================================================================================
MSG: sandbox/dimension
string label # Name or id of stoplight station (Arduino)
int16[] street # Colors of RGB
int16[] cross # Colors of RGB
"""
  __slots__ = ['layout','data']
  _slot_types = ['sandbox/layout','int16[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       layout,data

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(array, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.layout is None:
        self.layout = sandbox.msg.layout()
      if self.data is None:
        self.data = []
    else:
      self.layout = sandbox.msg.layout()
      self.data = []

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
      length = len(self.layout.dim)
      buff.write(_struct_I.pack(length))
      for val1 in self.layout.dim:
        _x = val1.label
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.street)
        buff.write(_struct_I.pack(length))
        pattern = '<%sh'%length
        buff.write(struct.pack(pattern, *val1.street))
        length = len(val1.cross)
        buff.write(_struct_I.pack(length))
        pattern = '<%sh'%length
        buff.write(struct.pack(pattern, *val1.cross))
      length = len(self.layout.clock)
      buff.write(_struct_I.pack(length))
      pattern = '<%sh'%length
      buff.write(struct.pack(pattern, *self.layout.clock))
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sh'%length
      buff.write(struct.pack(pattern, *self.data))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.layout is None:
        self.layout = sandbox.msg.layout()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.layout.dim = []
      for i in range(0, length):
        val1 = sandbox.msg.dimension()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.label = str[start:end].decode('utf-8')
        else:
          val1.label = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sh'%length
        start = end
        end += struct.calcsize(pattern)
        val1.street = struct.unpack(pattern, str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sh'%length
        start = end
        end += struct.calcsize(pattern)
        val1.cross = struct.unpack(pattern, str[start:end])
        self.layout.dim.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sh'%length
      start = end
      end += struct.calcsize(pattern)
      self.layout.clock = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sh'%length
      start = end
      end += struct.calcsize(pattern)
      self.data = struct.unpack(pattern, str[start:end])
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
      length = len(self.layout.dim)
      buff.write(_struct_I.pack(length))
      for val1 in self.layout.dim:
        _x = val1.label
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        length = len(val1.street)
        buff.write(_struct_I.pack(length))
        pattern = '<%sh'%length
        buff.write(val1.street.tostring())
        length = len(val1.cross)
        buff.write(_struct_I.pack(length))
        pattern = '<%sh'%length
        buff.write(val1.cross.tostring())
      length = len(self.layout.clock)
      buff.write(_struct_I.pack(length))
      pattern = '<%sh'%length
      buff.write(self.layout.clock.tostring())
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sh'%length
      buff.write(self.data.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.layout is None:
        self.layout = sandbox.msg.layout()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.layout.dim = []
      for i in range(0, length):
        val1 = sandbox.msg.dimension()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.label = str[start:end].decode('utf-8')
        else:
          val1.label = str[start:end]
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sh'%length
        start = end
        end += struct.calcsize(pattern)
        val1.street = numpy.frombuffer(str[start:end], dtype=numpy.int16, count=length)
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sh'%length
        start = end
        end += struct.calcsize(pattern)
        val1.cross = numpy.frombuffer(str[start:end], dtype=numpy.int16, count=length)
        self.layout.dim.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sh'%length
      start = end
      end += struct.calcsize(pattern)
      self.layout.clock = numpy.frombuffer(str[start:end], dtype=numpy.int16, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sh'%length
      start = end
      end += struct.calcsize(pattern)
      self.data = numpy.frombuffer(str[start:end], dtype=numpy.int16, count=length)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
