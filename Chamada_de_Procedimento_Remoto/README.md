# Chamada de Procedimento Remoto

Este projeto apresenta um exemplo simples de como fazer uma chamada de procedimento remoto (RPC) usando gRPC em Python. 
O RPC é uma forma de comunicação entre processos que permite que um programa chame um procedimento em outro programa (ou até mesmo em outra máquina) 
como se fosse um procedimento local. 

Aqui, temos um servidor que pode receber comandos de um cliente, executar esses comandos no servidor e enviar a saída de volta para o cliente. 
Para implementar isso, usamos o gRPC, um framework RPC de código aberto desenvolvido pelo Google.

Este projeto é composto por dois arquivos: `server.py` e `client.py`. O arquivo `server.py` contém o código do servidor e o arquivo `client.py` contém o código do cliente. Para executar o projeto, é necessário ter o Python instalado na máquina. Também é preciso instalar as dependências do projeto, que são o gRPC e o protobuf. 
## Arquitetura
Este projeto é composto por um servidor e um cliente que se comunicam através de gRPC. O servidor é responsável por receber os comandos enviados pelo cliente, executá-los e enviar a saída para o cliente. O cliente é responsável por enviar os comandos ao servidor e exibir a saída do comando.

## Requisitos
Para executar este projeto é necessário ter o Python 3 e as seguintes bibliotecas instaladas:
- grpc
- protobuf

## Execução
Para executar o projeto, primeiramente é necessário executar o servidor. Para isso, execute o arquivo `server.py`. O servidor irá iniciar e ficará aguardando conexões.

Em seguida, execute o arquivo `client.py`. O cliente irá solicitar o IP do servidor, digite o IP e pressione Enter. Em seguida, digite o comando a ser executado e pressione Enter. A saída do comando será exibida na tela. Repita este processo até que deseje finalizar o cliente.

## Exemplo

Este exemplo mostra a execução do comando `pwd` e `ls` no servidor. O servidor está sendo executado na mesma máquina que o cliente.

1. Inicie o servidor executando o arquivo `server.py` em um terminal:

   ```
   python server.py
   ```

2. Inicie o cliente em outro terminal, usando o endereço IP `localhost` ou `127.0.0.1` como o endereço do servidor:

   ```
   python client.py
   Digite o IP de destino >>> localhost
   Digite o comando a ser executado ('exit' para sair): pwd
   /home/usuario/projeto
   Digite o comando a ser executado ('exit' para sair): ls
   arquivo1.txt arquivo2.txt
   Digite o comando a ser executado ('exit' para sair): exit
   ``` 

   Observe que o cliente envia os comandos `pwd` e `ls` para o servidor e recebe a saída correspondente de cada comando. Quando o usuário digita `exit`, o cliente encerra.
## Autor
Este projeto foi desenvolvido por Kaio Guilherme como parte da disciplina de Sistemas Distribuídos do curso de Ciência da Computação da UFRR.