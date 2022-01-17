# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from ydb.public.api.protos import yq_pb2 as kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2


class YandexQueryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateQuery = channel.unary_unary(
                '/YandexQuery.V1.YandexQueryService/CreateQuery',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.CreateQueryRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.CreateQueryResponse.FromString,
                )
        self.ListQueries = channel.unary_unary(
                '/YandexQuery.V1.YandexQueryService/ListQueries',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListQueriesRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListQueriesResponse.FromString,
                )
        self.DescribeQuery = channel.unary_unary(
                '/YandexQuery.V1.YandexQueryService/DescribeQuery',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeQueryRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeQueryResponse.FromString,
                )
        self.GetQueryStatus = channel.unary_unary(
                '/YandexQuery.V1.YandexQueryService/GetQueryStatus',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.GetQueryStatusRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.GetQueryStatusResponse.FromString,
                )
        self.ModifyQuery = channel.unary_unary(
                '/YandexQuery.V1.YandexQueryService/ModifyQuery',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ModifyQueryRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ModifyQueryResponse.FromString,
                )
        self.DeleteQuery = channel.unary_unary(
                '/YandexQuery.V1.YandexQueryService/DeleteQuery',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DeleteQueryRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DeleteQueryResponse.FromString,
                )
        self.ControlQuery = channel.unary_unary(
                '/YandexQuery.V1.YandexQueryService/ControlQuery',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ControlQueryRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ControlQueryResponse.FromString,
                )
        self.GetResultData = channel.unary_unary(
                '/YandexQuery.V1.YandexQueryService/GetResultData',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.GetResultDataRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.GetResultDataResponse.FromString,
                )
        self.ListJobs = channel.unary_unary(
                '/YandexQuery.V1.YandexQueryService/ListJobs',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListJobsRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListJobsResponse.FromString,
                )
        self.DescribeJob = channel.unary_unary(
                '/YandexQuery.V1.YandexQueryService/DescribeJob',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeJobRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeJobResponse.FromString,
                )
        self.CreateConnection = channel.unary_unary(
                '/YandexQuery.V1.YandexQueryService/CreateConnection',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.CreateConnectionRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.CreateConnectionResponse.FromString,
                )
        self.ListConnections = channel.unary_unary(
                '/YandexQuery.V1.YandexQueryService/ListConnections',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListConnectionsRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListConnectionsResponse.FromString,
                )
        self.DescribeConnection = channel.unary_unary(
                '/YandexQuery.V1.YandexQueryService/DescribeConnection',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeConnectionRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeConnectionResponse.FromString,
                )
        self.ModifyConnection = channel.unary_unary(
                '/YandexQuery.V1.YandexQueryService/ModifyConnection',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ModifyConnectionRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ModifyConnectionResponse.FromString,
                )
        self.DeleteConnection = channel.unary_unary(
                '/YandexQuery.V1.YandexQueryService/DeleteConnection',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DeleteConnectionRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DeleteConnectionResponse.FromString,
                )
        self.CreateBinding = channel.unary_unary(
                '/YandexQuery.V1.YandexQueryService/CreateBinding',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.CreateBindingRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.CreateBindingResponse.FromString,
                )
        self.ListBindings = channel.unary_unary(
                '/YandexQuery.V1.YandexQueryService/ListBindings',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListBindingsRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListBindingsResponse.FromString,
                )
        self.DescribeBinding = channel.unary_unary(
                '/YandexQuery.V1.YandexQueryService/DescribeBinding',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeBindingRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeBindingResponse.FromString,
                )
        self.ModifyBinding = channel.unary_unary(
                '/YandexQuery.V1.YandexQueryService/ModifyBinding',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ModifyBindingRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ModifyBindingResponse.FromString,
                )
        self.DeleteBinding = channel.unary_unary(
                '/YandexQuery.V1.YandexQueryService/DeleteBinding',
                request_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DeleteBindingRequest.SerializeToString,
                response_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DeleteBindingResponse.FromString,
                )


class YandexQueryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateQuery(self, request, context):
        """Query
        Query is the text of an SQL request, the results of the last run and the state after the last run (partitions offsets, consumer in YDS)
        Create a query object with a given SQL
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListQueries(self, request, context):
        """Get a list of brief queries objects
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeQuery(self, request, context):
        """Get full information about the object of the query
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetQueryStatus(self, request, context):
        """Get status of the query
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModifyQuery(self, request, context):
        """Change the attributes of the query (acl, name, ...)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteQuery(self, request, context):
        """Completely delete the query
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ControlQuery(self, request, context):
        """Change the state of the query lifecycle
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetResultData(self, request, context):
        """Get a results page
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListJobs(self, request, context):
        """Job
        Job - appears immediately after starting the request and contains the request metadata
        Get a list of jobs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeJob(self, request, context):
        """Get information about the job
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateConnection(self, request, context):
        """Connection
        Connection - entity that describes connection points. This can be imagined as an analogue of a network address.
        Create a connection object (ObjectStorage, YDB, YDS, ...)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListConnections(self, request, context):
        """Get a list of connections objects
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeConnection(self, request, context):
        """Get information about the object of the connection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModifyConnection(self, request, context):
        """Change the attributes of the connection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteConnection(self, request, context):
        """Completely delete the connection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateBinding(self, request, context):
        """Binding
        Binding - entity using which a schema is assigned to non-schematic data
        Create a binding object - bind schema with ObjectStorage object or YDS stream
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBindings(self, request, context):
        """Get a list of bindings objects
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DescribeBinding(self, request, context):
        """Get information about the object of the binding
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModifyBinding(self, request, context):
        """Change the attributes of the binding
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBinding(self, request, context):
        """Completely delete the binding
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_YandexQueryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateQuery,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.CreateQueryRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.CreateQueryResponse.SerializeToString,
            ),
            'ListQueries': grpc.unary_unary_rpc_method_handler(
                    servicer.ListQueries,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListQueriesRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListQueriesResponse.SerializeToString,
            ),
            'DescribeQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeQuery,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeQueryRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeQueryResponse.SerializeToString,
            ),
            'GetQueryStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetQueryStatus,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.GetQueryStatusRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.GetQueryStatusResponse.SerializeToString,
            ),
            'ModifyQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.ModifyQuery,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ModifyQueryRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ModifyQueryResponse.SerializeToString,
            ),
            'DeleteQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteQuery,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DeleteQueryRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DeleteQueryResponse.SerializeToString,
            ),
            'ControlQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.ControlQuery,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ControlQueryRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ControlQueryResponse.SerializeToString,
            ),
            'GetResultData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetResultData,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.GetResultDataRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.GetResultDataResponse.SerializeToString,
            ),
            'ListJobs': grpc.unary_unary_rpc_method_handler(
                    servicer.ListJobs,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListJobsRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListJobsResponse.SerializeToString,
            ),
            'DescribeJob': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeJob,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeJobRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeJobResponse.SerializeToString,
            ),
            'CreateConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateConnection,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.CreateConnectionRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.CreateConnectionResponse.SerializeToString,
            ),
            'ListConnections': grpc.unary_unary_rpc_method_handler(
                    servicer.ListConnections,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListConnectionsRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListConnectionsResponse.SerializeToString,
            ),
            'DescribeConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeConnection,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeConnectionRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeConnectionResponse.SerializeToString,
            ),
            'ModifyConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.ModifyConnection,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ModifyConnectionRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ModifyConnectionResponse.SerializeToString,
            ),
            'DeleteConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteConnection,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DeleteConnectionRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DeleteConnectionResponse.SerializeToString,
            ),
            'CreateBinding': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateBinding,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.CreateBindingRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.CreateBindingResponse.SerializeToString,
            ),
            'ListBindings': grpc.unary_unary_rpc_method_handler(
                    servicer.ListBindings,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListBindingsRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListBindingsResponse.SerializeToString,
            ),
            'DescribeBinding': grpc.unary_unary_rpc_method_handler(
                    servicer.DescribeBinding,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeBindingRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeBindingResponse.SerializeToString,
            ),
            'ModifyBinding': grpc.unary_unary_rpc_method_handler(
                    servicer.ModifyBinding,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ModifyBindingRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ModifyBindingResponse.SerializeToString,
            ),
            'DeleteBinding': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteBinding,
                    request_deserializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DeleteBindingRequest.FromString,
                    response_serializer=kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DeleteBindingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'YandexQuery.V1.YandexQueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class YandexQueryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YandexQuery.V1.YandexQueryService/CreateQuery',
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.CreateQueryRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.CreateQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListQueries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YandexQuery.V1.YandexQueryService/ListQueries',
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListQueriesRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListQueriesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YandexQuery.V1.YandexQueryService/DescribeQuery',
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeQueryRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetQueryStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YandexQuery.V1.YandexQueryService/GetQueryStatus',
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.GetQueryStatusRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.GetQueryStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ModifyQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YandexQuery.V1.YandexQueryService/ModifyQuery',
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ModifyQueryRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ModifyQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YandexQuery.V1.YandexQueryService/DeleteQuery',
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DeleteQueryRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DeleteQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ControlQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YandexQuery.V1.YandexQueryService/ControlQuery',
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ControlQueryRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ControlQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetResultData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YandexQuery.V1.YandexQueryService/GetResultData',
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.GetResultDataRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.GetResultDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListJobs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YandexQuery.V1.YandexQueryService/ListJobs',
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListJobsRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListJobsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YandexQuery.V1.YandexQueryService/DescribeJob',
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeJobRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeJobResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YandexQuery.V1.YandexQueryService/CreateConnection',
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.CreateConnectionRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.CreateConnectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListConnections(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YandexQuery.V1.YandexQueryService/ListConnections',
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListConnectionsRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListConnectionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YandexQuery.V1.YandexQueryService/DescribeConnection',
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeConnectionRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeConnectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ModifyConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YandexQuery.V1.YandexQueryService/ModifyConnection',
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ModifyConnectionRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ModifyConnectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YandexQuery.V1.YandexQueryService/DeleteConnection',
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DeleteConnectionRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DeleteConnectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateBinding(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YandexQuery.V1.YandexQueryService/CreateBinding',
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.CreateBindingRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.CreateBindingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListBindings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YandexQuery.V1.YandexQueryService/ListBindings',
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListBindingsRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ListBindingsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DescribeBinding(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YandexQuery.V1.YandexQueryService/DescribeBinding',
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeBindingRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DescribeBindingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ModifyBinding(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YandexQuery.V1.YandexQueryService/ModifyBinding',
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ModifyBindingRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.ModifyBindingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteBinding(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/YandexQuery.V1.YandexQueryService/DeleteBinding',
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DeleteBindingRequest.SerializeToString,
            kikimr_dot_public_dot_api_dot_protos_dot_yq__pb2.DeleteBindingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
