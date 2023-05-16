#kaio Guilherme
# Código do servidor

import subprocess
from concurrent import futures

import grpc
import service_pb2
import service_pb2_grpc


class CommandService(service_pb2_grpc.ServiceServicer):
    def ExecutarComando(self, request, context):
        # Executa o comando no servidor e retorna a saída
        output = subprocess.check_output(request.comando.split(), stderr=subprocess.STDOUT)
        return service_pb2.Resposta(resultado=output.decode())


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_ServiceServicer_to_server(CommandService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Servidor em execução...')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
