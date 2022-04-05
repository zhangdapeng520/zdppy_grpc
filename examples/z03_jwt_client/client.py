import json

import grpc
from proto import jwt_pb2
from proto import jwt_pb2_grpc


def run():
    # 连接 rpc 服务器
    channel = grpc.insecure_channel('localhost:50051')

    # 调用 rpc 服务
    stub = jwt_pb2_grpc.ServerJwtStub(channel)

    # 发送创建token请求
    data = {"a": "111", "b": "222", "c": "333"}
    json_data = json.dumps(data)
    response = stub.CreateToken(jwt_pb2.CreateTokenRequest(
        user_id=1,
        username="zhangdapeng",
        usertype="username",
        role=1,
        json_data=json_data
    ))
    token = response.token
    print("创建token：" + token)

    # 发送解析token请求
    response = stub.ParseToken(jwt_pb2.ParseTokenRequest(token=response.token))
    print("解析token：",
          response.username,
          response.user_id,
          response.role,
          response.usertype,
          response.json_data)

    # 发送刷新token请求
    response = stub.RefreshToken(jwt_pb2.RefreshTokenRequest(token=token))
    print("刷新token：", response.token)


if __name__ == '__main__':
    run()
