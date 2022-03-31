from concurrent import futures
import time
import grpc
from proto import hello_pb2
from proto import hello_pb2_grpc


# 实现 proto 文件中定义的 GreeterServicer
class Greeter(hello_pb2_grpc.GreeterServicer):
    # 实现 proto 文件中定义的 rpc 调用
    def SayHello(self, request, context):
        # 返回响应
        return hello_pb2.HelloReply(message='你好 {msg}'.format(msg=request.name))

    def SayHelloAgain(self, request, context):
        return hello_pb2.HelloReply(message='你好 {msg}'.format(msg=request.name))


def serve():
    # 启动 rpc 服务
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # 注册服务到server
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)

    # 设置监听的端口号
    server.add_insecure_port('[::]:50051')

    # 启动服务
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)  # 运行一天
    except KeyboardInterrupt:  # 接收到键盘终止信号
        server.stop(0)


if __name__ == '__main__':
    serve()
