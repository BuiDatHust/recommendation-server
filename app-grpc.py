from db import connectMilvus

if __name__ == "__main__":
    connectMilvus()
    
    from config.grpcServer import grpc_server
    grpc_server()