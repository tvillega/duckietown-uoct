// Generated by gencpp from file sandbox/MultiArrayLayout.msg
// DO NOT EDIT!


#ifndef SANDBOX_MESSAGE_MULTIARRAYLAYOUT_H
#define SANDBOX_MESSAGE_MULTIARRAYLAYOUT_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <sandbox/MultiArraySubDimension.h>

namespace sandbox
{
template <class ContainerAllocator>
struct MultiArrayLayout_
{
  typedef MultiArrayLayout_<ContainerAllocator> Type;

  MultiArrayLayout_()
    : stoplights()
    , deface(0)  {
    }
  MultiArrayLayout_(const ContainerAllocator& _alloc)
    : stoplights(_alloc)
    , deface(0)  {
  (void)_alloc;
    }



   typedef std::vector< ::sandbox::MultiArraySubDimension_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::sandbox::MultiArraySubDimension_<ContainerAllocator> >::other >  _stoplights_type;
  _stoplights_type stoplights;

   typedef int16_t _deface_type;
  _deface_type deface;





  typedef boost::shared_ptr< ::sandbox::MultiArrayLayout_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sandbox::MultiArrayLayout_<ContainerAllocator> const> ConstPtr;

}; // struct MultiArrayLayout_

typedef ::sandbox::MultiArrayLayout_<std::allocator<void> > MultiArrayLayout;

typedef boost::shared_ptr< ::sandbox::MultiArrayLayout > MultiArrayLayoutPtr;
typedef boost::shared_ptr< ::sandbox::MultiArrayLayout const> MultiArrayLayoutConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::sandbox::MultiArrayLayout_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::sandbox::MultiArrayLayout_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::sandbox::MultiArrayLayout_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sandbox::MultiArrayLayout_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sandbox::MultiArrayLayout_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sandbox::MultiArrayLayout_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sandbox::MultiArrayLayout_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sandbox::MultiArrayLayout_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::sandbox::MultiArrayLayout_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c71496406d4b1a871cb3ce7d7daa62da";
  }

  static const char* value(const ::sandbox::MultiArrayLayout_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc71496406d4b1a87ULL;
  static const uint64_t static_value2 = 0x1cb3ce7d7daa62daULL;
};

template<class ContainerAllocator>
struct DataType< ::sandbox::MultiArrayLayout_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sandbox/MultiArrayLayout";
  }

  static const char* value(const ::sandbox::MultiArrayLayout_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::sandbox::MultiArrayLayout_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sandbox/MultiArraySubDimension[] stoplights # colection of stoplights to send message\n"
"int16 deface\n"
"\n"
"================================================================================\n"
"MSG: sandbox/MultiArraySubDimension\n"
"string label # cross, street, blink warning\n"
"int16[] colors # [red,gree,blue,custom]\n"
;
  }

  static const char* value(const ::sandbox::MultiArrayLayout_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::sandbox::MultiArrayLayout_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.stoplights);
      stream.next(m.deface);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MultiArrayLayout_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sandbox::MultiArrayLayout_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::sandbox::MultiArrayLayout_<ContainerAllocator>& v)
  {
    s << indent << "stoplights[]" << std::endl;
    for (size_t i = 0; i < v.stoplights.size(); ++i)
    {
      s << indent << "  stoplights[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::sandbox::MultiArraySubDimension_<ContainerAllocator> >::stream(s, indent + "    ", v.stoplights[i]);
    }
    s << indent << "deface: ";
    Printer<int16_t>::stream(s, indent + "  ", v.deface);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SANDBOX_MESSAGE_MULTIARRAYLAYOUT_H
