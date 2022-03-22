BIN = proto-python-course
PROTO_DIR = proto

run: generate
	python3 main.py

generate:
	protoc -I${PROTO_DIR} --python_out=${PROTO_DIR} ${PROTO_DIR}/*.proto

clean:
	rm ${PROTO_DIR}/*_pb2.py