run: 	generate
	python3 main.py

generate:
	protoc -Iproto --python_out=proto proto/*.proto

clean:
	rm proto/*_pb2.py
