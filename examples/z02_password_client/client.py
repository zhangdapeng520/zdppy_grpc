import grpc
from proto import password_pb2
from proto import password_pb2_grpc


def run():
    # 连接 rpc 服务器
    channel = grpc.insecure_channel('localhost:50051')

    # 调用 rpc 服务
    stub = password_pb2_grpc.ServerAesStub(channel)

    # 发送请求获取响应
    response = stub.Encrypt(password_pb2.EncryptRequest(base64_data='张大鹏'))
    print("接收到服务器消息：" + response.base64_encrypt)


if __name__ == '__main__':
    run()
