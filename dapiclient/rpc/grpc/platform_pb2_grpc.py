# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import platform_pb2 as platform__pb2


class PlatformStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.applyStateTransition = channel.unary_unary(
        '/org.dash.platform.dapi.v0.Platform/applyStateTransition',
        request_serializer=platform__pb2.ApplyStateTransitionRequest.SerializeToString,
        response_deserializer=platform__pb2.ApplyStateTransitionResponse.FromString,
        )
    self.getIdentity = channel.unary_unary(
        '/org.dash.platform.dapi.v0.Platform/getIdentity',
        request_serializer=platform__pb2.GetIdentityRequest.SerializeToString,
        response_deserializer=platform__pb2.GetIdentityResponse.FromString,
        )
    self.getDataContract = channel.unary_unary(
        '/org.dash.platform.dapi.v0.Platform/getDataContract',
        request_serializer=platform__pb2.GetDataContractRequest.SerializeToString,
        response_deserializer=platform__pb2.GetDataContractResponse.FromString,
        )
    self.getDocuments = channel.unary_unary(
        '/org.dash.platform.dapi.v0.Platform/getDocuments',
        request_serializer=platform__pb2.GetDocumentsRequest.SerializeToString,
        response_deserializer=platform__pb2.GetDocumentsResponse.FromString,
        )


class PlatformServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def applyStateTransition(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getIdentity(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getDataContract(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getDocuments(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PlatformServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'applyStateTransition': grpc.unary_unary_rpc_method_handler(
          servicer.applyStateTransition,
          request_deserializer=platform__pb2.ApplyStateTransitionRequest.FromString,
          response_serializer=platform__pb2.ApplyStateTransitionResponse.SerializeToString,
      ),
      'getIdentity': grpc.unary_unary_rpc_method_handler(
          servicer.getIdentity,
          request_deserializer=platform__pb2.GetIdentityRequest.FromString,
          response_serializer=platform__pb2.GetIdentityResponse.SerializeToString,
      ),
      'getDataContract': grpc.unary_unary_rpc_method_handler(
          servicer.getDataContract,
          request_deserializer=platform__pb2.GetDataContractRequest.FromString,
          response_serializer=platform__pb2.GetDataContractResponse.SerializeToString,
      ),
      'getDocuments': grpc.unary_unary_rpc_method_handler(
          servicer.getDocuments,
          request_deserializer=platform__pb2.GetDocumentsRequest.FromString,
          response_serializer=platform__pb2.GetDocumentsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'org.dash.platform.dapi.v0.Platform', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
