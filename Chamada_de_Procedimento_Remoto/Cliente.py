#Kaio Guilherme
# Código do cliente

import grpc
import service_pb2
import service_pb2_grpc

def run():
    #pega o ip do server
    ip = str(input("Digite o IP de destino >>> "))
    # Conecta com o servidor
    with grpc.insecure_channel(ip + ':50051') as channel:
        stub = service_pb2_grpc.ServiceStub(channel)
        while True:
            # Solicita ao usuário para inserir um comando
            command = input("Digite o comando a ser executado ('exit' para sair): ")
            if command == "exit":
                break
            # Envia o comando para o servidor
            try:
                response = stub.ExecutarComando(service_pb2.Pedido(comando=command))
                print(response.resultado)
            except grpc.RpcError as e:
                print(f" {e.details()}")
            # Exibe a saída do comando


if __name__ == '__main__':
    run()
