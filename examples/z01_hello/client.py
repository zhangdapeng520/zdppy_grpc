import grpc
from proto import hello_pb2
from proto import hello_pb2_grpc


def run():
    # 连接 rpc 服务器
    channel = grpc.insecure_channel('localhost:50051')

    # 调用 rpc 服务
    stub = hello_pb2_grpc.GreeterStub(channel)

    # 发送请求获取响应
    response = stub.SayHello(hello_pb2.HelloRequest(name='张大鹏'))
    print("接收到服务器消息：" + response.message)

    # 请求另一个接口
    # response = stub.SayHelloAgain(hello_pb2.HelloRequest(name='张大鹏'))
    # print("接收到服务器消息：" + response.message)


if __name__ == '__main__':
    run()
