import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(calculator_pb2.AddRequest(a=5, b=10))
        print("Addition:", response.result)

        response = stub.Subtract(calculator_pb2.SubtractRequest(a=15, b=10))
        print("Subtraction:", response.result)

        response = stub.Multiply(calculator_pb2.MultiplyRequest(a=5, b=10))
        print("Multiplication:", response.result)

        response = stub.Divide(calculator_pb2.DivideRequest(a=15, b=10))
        print("Division:", response.result)

if __name__ == '__main__':
    run()
