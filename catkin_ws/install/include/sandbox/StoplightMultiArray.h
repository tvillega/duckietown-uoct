// Generated by gencpp from file sandbox/StoplightMultiArray.msg
// DO NOT EDIT!


#ifndef SANDBOX_MESSAGE_STOPLIGHTMULTIARRAY_H
#define SANDBOX_MESSAGE_STOPLIGHTMULTIARRAY_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <sandbox/Stoplight.h>

namespace sandbox
{
template <class ContainerAllocator>
struct StoplightMultiArray_
{
  typedef StoplightMultiArray_<ContainerAllocator> Type;

  StoplightMultiArray_()
    : StoplightMultiArray()
    , traffic_lights()
    , deface(0)
    , clock()  {
    }
  StoplightMultiArray_(const ContainerAllocator& _alloc)
    : StoplightMultiArray(_alloc)
    , traffic_lights(_alloc)
    , deface(0)
    , clock(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _StoplightMultiArray_type;
  _StoplightMultiArray_type StoplightMultiArray;

   typedef std::vector< ::sandbox::Stoplight_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::sandbox::Stoplight_<ContainerAllocator> >::other >  _traffic_lights_type;
  _traffic_lights_type traffic_lights;

   typedef int16_t _deface_type;
  _deface_type deface;

   typedef std::vector<int16_t, typename ContainerAllocator::template rebind<int16_t>::other >  _clock_type;
  _clock_type clock;





  typedef boost::shared_ptr< ::sandbox::StoplightMultiArray_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sandbox::StoplightMultiArray_<ContainerAllocator> const> ConstPtr;

}; // struct StoplightMultiArray_

typedef ::sandbox::StoplightMultiArray_<std::allocator<void> > StoplightMultiArray;

typedef boost::shared_ptr< ::sandbox::StoplightMultiArray > StoplightMultiArrayPtr;
typedef boost::shared_ptr< ::sandbox::StoplightMultiArray const> StoplightMultiArrayConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::sandbox::StoplightMultiArray_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::sandbox::StoplightMultiArray_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace sandbox

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'sandbox': ['/home/tomvillegasm/duckietown-uoct/catkin_ws/src/sandbox/msg'], 'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::sandbox::StoplightMultiArray_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sandbox::StoplightMultiArray_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sandbox::StoplightMultiArray_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sandbox::StoplightMultiArray_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sandbox::StoplightMultiArray_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sandbox::StoplightMultiArray_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::sandbox::StoplightMultiArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "36040492c6f40acc8475256baa3fc1e7";
  }

  static const char* value(const ::sandbox::StoplightMultiArray_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x36040492c6f40accULL;
  static const uint64_t static_value2 = 0x8475256baa3fc1e7ULL;
};

template<class ContainerAllocator>
struct DataType< ::sandbox::StoplightMultiArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sandbox/StoplightMultiArray";
  }

  static const char* value(const ::sandbox::StoplightMultiArray_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::sandbox::StoplightMultiArray_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header StoplightMultiArray\n"
"sandbox/Stoplight[] traffic_lights\n"
"int16 deface\n"
"int16[] clock# syncronized clock for all stoplights\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: sandbox/Stoplight\n"
"Header Stoplight\n"
"string type # cross, street, blink warning\n"
"string direction # norht2south, east2west, up2down\n"
"int16[] colors # [red,gree,blue,custom]\n"
;
  }

  static const char* value(const ::sandbox::StoplightMultiArray_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::sandbox::StoplightMultiArray_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.StoplightMultiArray);
      stream.next(m.traffic_lights);
      stream.next(m.deface);
      stream.next(m.clock);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct StoplightMultiArray_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sandbox::StoplightMultiArray_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::sandbox::StoplightMultiArray_<ContainerAllocator>& v)
  {
    s << indent << "StoplightMultiArray: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.StoplightMultiArray);
    s << indent << "traffic_lights[]" << std::endl;
    for (size_t i = 0; i < v.traffic_lights.size(); ++i)
    {
      s << indent << "  traffic_lights[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::sandbox::Stoplight_<ContainerAllocator> >::stream(s, indent + "    ", v.traffic_lights[i]);
    }
    s << indent << "deface: ";
    Printer<int16_t>::stream(s, indent + "  ", v.deface);
    s << indent << "clock[]" << std::endl;
    for (size_t i = 0; i < v.clock.size(); ++i)
    {
      s << indent << "  clock[" << i << "]: ";
      Printer<int16_t>::stream(s, indent + "  ", v.clock[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // SANDBOX_MESSAGE_STOPLIGHTMULTIARRAY_H
