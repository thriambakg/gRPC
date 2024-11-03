import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc
import time

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.a + request.b
        return calculator_pb2.AddResponse(result=result)
    
    def Subtract(self, request, context):
        result = request.a - request.b
        return calculator_pb2.SubtractResponse(result=result)
    
    def Multiply(self, request, context):
        result = request.a * request.b
        return calculator_pb2.MultiplyResponse(result=result)
    
    def Divide(self, request, context):
        if request.b == 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Division by zero is not allowed.")
            return calculator_pb2.DivideResponse()
        
        result = request.a / request.b
        return calculator_pb2.DivideResponse(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Press Ctrl+C to stop.")
    
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Shutting down server...")
        server.stop(grace=0)  # Set grace period as desired (e.g., grace=5 for a 5-second grace period)
if __name__ == '__main__':
    serve()
