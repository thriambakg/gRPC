Important commands:
1. python -m venv .venv //making virtal environment

2. .venv/scripts/activate //activating virtual environment

3. pip install grpcio grpcio-tools //installing grpc tools

4. python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto //compile proto file to create stub class (protect these files)
