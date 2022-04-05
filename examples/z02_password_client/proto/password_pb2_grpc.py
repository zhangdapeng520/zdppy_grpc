# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import password_pb2 as password__pb2


class ServerAesStub(object):
    """AES加密服务
    服务名
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Encrypt = channel.unary_unary(
                '/ServerAes/Encrypt',
                request_serializer=password__pb2.EncryptRequest.SerializeToString,
                response_deserializer=password__pb2.EncryptResponse.FromString,
                )
        self.EncryptString = channel.unary_unary(
                '/ServerAes/EncryptString',
                request_serializer=password__pb2.EncryptStringRequest.SerializeToString,
                response_deserializer=password__pb2.EncryptStringResponse.FromString,
                )
        self.DecryptString = channel.unary_unary(
                '/ServerAes/DecryptString',
                request_serializer=password__pb2.DecryptStringRequest.SerializeToString,
                response_deserializer=password__pb2.DecryptStringResponse.FromString,
                )


class ServerAesServicer(object):
    """AES加密服务
    服务名
    """

    def Encrypt(self, request, context):
        """加密
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EncryptString(self, request, context):
        """加密字符串
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DecryptString(self, request, context):
        """加密字符串
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServerAesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Encrypt': grpc.unary_unary_rpc_method_handler(
                    servicer.Encrypt,
                    request_deserializer=password__pb2.EncryptRequest.FromString,
                    response_serializer=password__pb2.EncryptResponse.SerializeToString,
            ),
            'EncryptString': grpc.unary_unary_rpc_method_handler(
                    servicer.EncryptString,
                    request_deserializer=password__pb2.EncryptStringRequest.FromString,
                    response_serializer=password__pb2.EncryptStringResponse.SerializeToString,
            ),
            'DecryptString': grpc.unary_unary_rpc_method_handler(
                    servicer.DecryptString,
                    request_deserializer=password__pb2.DecryptStringRequest.FromString,
                    response_serializer=password__pb2.DecryptStringResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ServerAes', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ServerAes(object):
    """AES加密服务
    服务名
    """

    @staticmethod
    def Encrypt(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ServerAes/Encrypt',
            password__pb2.EncryptRequest.SerializeToString,
            password__pb2.EncryptResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EncryptString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ServerAes/EncryptString',
            password__pb2.EncryptStringRequest.SerializeToString,
            password__pb2.EncryptStringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DecryptString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ServerAes/DecryptString',
            password__pb2.DecryptStringRequest.SerializeToString,
            password__pb2.DecryptStringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
