import grpc
import service_pb2
import service_pb2_grpc

def run():
    # Conecta com o servidor
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.ServiceStub(channel)
        # Solicita ao usuário para inserir um comando
        command = input("Digite o comando a ser executado: ")
        # Envia o comando para o servidor
        response = stub.ExecutarComando(service_pb2.CommandRequest(command=command))
        # Exibe a saída do comando
        print(response.output)

if __name__ == '__main__':
    run()
# em andamento com erro