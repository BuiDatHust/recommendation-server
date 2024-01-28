from  concurrent import futures
import grpc
from config.environment import AppConfig
import grpcs.message.user_pb2_grpc as user_service
from services.userGrpc import UserGrpcService

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

def grpc_server():
    port = getattr(AppConfig, 'GRPC_PORT')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),options={})

    # Register user service
    user_serve = UserGrpcService()
    user_service.add_UserServicer_to_server(user_serve, server)

    # This is just for testing onyl ( Not recommended in production )
    p = server.add_insecure_port('[::]:' + port)
    server.start()
    print('GRPC running on port ' + port)

    server.wait_for_termination(_ONE_DAY_IN_SECONDS)