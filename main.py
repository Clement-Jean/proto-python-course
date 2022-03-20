from email import message
import proto.simple_pb2 as simple_pb2
import proto.complex_pb2 as complex_pb2
import proto.enumerations_pb2 as enum_pb2
import proto.oneofs_pb2 as oneofs_pb2
import proto.maps_pb2 as maps_pb2

def simple():
  message = simple_pb2.Simple(
    id=123,
    is_simple=True,
    name="My name",
    sample_lists=[3, 4, 5]
  )
  print(message)

def complex():
  message = complex_pb2.Complex()
  message.one_dummy.id = 42
  message.one_dummy.name = "My name"
  message.multiple_dummies.add(id=43, name="My name 2")
  message.multiple_dummies.add(id=44, name="My name 3")
  message.multiple_dummies.add(id=45, name="My name 4")
  print(message)

def enum():
  message = enum_pb2.Enumeration(
    eye_color=enum_pb2.EYE_COLOR_GREEN,
    #eye_color=1    
  )
  print(message)

def oneof():
  message = oneofs_pb2.Result()
  message.message = "message"
  print(message)

  message.id = 42
  print(message)

def maps():
  message = maps_pb2.MapExample()
  message.ids["myid"].id = 42
  message.ids["myid2"].id = 43
  message.ids["myid3"].id = 44
  print(message)

def main():
  simple()
  # complex()
  # enum()
  # oneof()
  # maps()

if __name__ == "__main__":
    main()