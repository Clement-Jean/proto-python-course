import google.protobuf.json_format as json_format

import proto.complex_pb2 as complex_pb2
import proto.enumerations_pb2 as enum_pb2
import proto.maps_pb2 as maps_pb2
import proto.oneofs_pb2 as oneofs_pb2
import proto.simple_pb2 as simple_pb2


def simple() -> simple_pb2.Simple:
    return simple_pb2.Simple(
        id=42,
        is_simple=True,
        name="My name",
        sample_lists=[3, 4, 5]
    )


def complex() -> complex_pb2.Complex:
    message = complex_pb2.Complex()
    message.one_dummy.id = 42
    message.one_dummy.name = "My name"
    message.multiple_dummies.add(id=43, name="My name 2")
    message.multiple_dummies.add(id=44, name="My name 3")
    message.multiple_dummies.add(id=45, name="My name 4")
    return message


def enum():
    return enum_pb2.Enumeration(
        eye_color=enum_pb2.EYE_COLOR_GREEN,
        # eye_color=1
    )


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


def file(message):
    path = "simple.bin"

    print("Write to file")
    print(message)
    with open(path, "wb") as f:
        bytes_as_str = message.SerializeToString()
        f.write(bytes_as_str)

    print("Read from file")
    with open(path, "rb") as f:
        t = type(message)
        message = t().FromString(f.read())

    print(message)


def json(message: simple_pb2.Simple):
    json_str = json_format.MessageToJson(message)

    print(json_str)
    print(json_format.Parse(json_str, simple_pb2.Simple()))


def main():
    print(simple())
    # print(complex())
    # print(enum())
    # oneof()
    # maps()
    # file(simple())
    # json(simple())


if __name__ == "__main__":
    main()
