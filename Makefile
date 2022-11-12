BIN_NAME = python3
PROTO_DIR = proto

ifeq ($(OS), Windows_NT)
	BIN = ${BIN_NAME}.exe
else
	BIN = ${BIN_NAME}
endif

run:	generate
	${BIN} main.py

generate:
	protoc -I${PROTO_DIR} --python_out=${PROTO_DIR} ${PROTO_DIR}/*.proto

bump:
	sed -i -e 's/==/>=/g' requirements.txt
	./venv/bin/python -m pip install -r requirements.txt --upgrade
	./venv/bin/python -m pip freeze > requirements.txt

clean:
	rm ${PROTO_DIR}/*_pb2.py
