# zdppy_grpc
Python实现的gRPC通信底层库

## 常用命令
生成代码
```shell
python -m grpc_tools.protoc --python_out=. --grpc_python_out=. -I. password.proto
```