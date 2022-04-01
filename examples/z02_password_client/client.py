import grpc
from proto import password_pb2
from proto import password_pb2_grpc


def run():
    # 连接 rpc 服务器
    channel = grpc.insecure_channel('localhost:50051')

    # 调用 rpc 服务
    stub = password_pb2_grpc.ServerAesStub(channel)
    data = "abc 123 张大鹏 *&^"
    print("原始：", data)

    # 发送加密请求
    response = stub.EncryptString(password_pb2.EncryptStringRequest(data=data))
    print("加密：" + response.base64_encrypt)

    # 发送解密请求
    response = stub.DecryptString(password_pb2.DecryptStringRequest(base64_encrypt=response.base64_encrypt))
    print("解密：" + response.decrypt_data)


if __name__ == '__main__':
    run()
