# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import controllers.proto.company_pb2 as company__pb2

GRPC_GENERATED_VERSION = '1.68.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in company_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class CompanyStub(object):
    """Definição do serviço Company
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateCompany = channel.unary_unary(
                '/company.Company/CreateCompany',
                request_serializer=company__pb2.CreateCompanyRequest.SerializeToString,
                response_deserializer=company__pb2.CompanyCommandResponse.FromString,
                _registered_method=True)
        self.DeactivateCompany = channel.unary_unary(
                '/company.Company/DeactivateCompany',
                request_serializer=company__pb2.DeactivateCompanyRequest.SerializeToString,
                response_deserializer=company__pb2.CompanyCommandResponse.FromString,
                _registered_method=True)
        self.ReactivateCompany = channel.unary_unary(
                '/company.Company/ReactivateCompany',
                request_serializer=company__pb2.ReactivateCompanyRequest.SerializeToString,
                response_deserializer=company__pb2.CompanyCommandResponse.FromString,
                _registered_method=True)


class CompanyServicer(object):
    """Definição do serviço Company
    """

    def CreateCompany(self, request, context):
        """Criação de uma nova empresa
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeactivateCompany(self, request, context):
        """Desativação da licença de uma empresa
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReactivateCompany(self, request, context):
        """Reativação da licença de uma empresa
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CompanyServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateCompany': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCompany,
                    request_deserializer=company__pb2.CreateCompanyRequest.FromString,
                    response_serializer=company__pb2.CompanyCommandResponse.SerializeToString,
            ),
            'DeactivateCompany': grpc.unary_unary_rpc_method_handler(
                    servicer.DeactivateCompany,
                    request_deserializer=company__pb2.DeactivateCompanyRequest.FromString,
                    response_serializer=company__pb2.CompanyCommandResponse.SerializeToString,
            ),
            'ReactivateCompany': grpc.unary_unary_rpc_method_handler(
                    servicer.ReactivateCompany,
                    request_deserializer=company__pb2.ReactivateCompanyRequest.FromString,
                    response_serializer=company__pb2.CompanyCommandResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'company.Company', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('company.Company', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Company(object):
    """Definição do serviço Company
    """

    @staticmethod
    def CreateCompany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/company.Company/CreateCompany',
            company__pb2.CreateCompanyRequest.SerializeToString,
            company__pb2.CompanyCommandResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeactivateCompany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/company.Company/DeactivateCompany',
            company__pb2.DeactivateCompanyRequest.SerializeToString,
            company__pb2.CompanyCommandResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ReactivateCompany(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/company.Company/ReactivateCompany',
            company__pb2.ReactivateCompanyRequest.SerializeToString,
            company__pb2.CompanyCommandResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
