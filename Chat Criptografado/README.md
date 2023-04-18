# 

# Projeto de Sistemas Distribuídos - Chat Criptografado

Este projeto consiste em uma aplicação que permite a comunicação entre clientes e um servidor usando sockets e criptografia simétrica.

## Arquitetura

A aplicação é composta por dois componentes principais:

- Um script Python chamado **`client.py`** que cria um socket do cliente e se conecta ao servidor. Ele envia e recebe mensagens criptografadas usando uma chave simétrica pré-compartilhada.
- Um script Python chamado **`server.py`** que cria um socket do servidor e aceita conexões de clientes. Ele recebe e reenvia as mensagens criptografadas para todos os clientes conectados.

A figura abaixo ilustra a arquitetura da aplicação:

## Requisitos

Para executar este projeto, você precisa ter instalado em sua máquina:

- Python 3
- Cryptography

Você também precisa ter a mesma chave simétrica em ambos os scripts.

## Execução

Para executar este projeto, siga os seguintes passos:

1. Clone este repositório em sua máquina.
2. Navegue até a pasta do projeto e abra dois terminais diferentes.
3. Em um dos terminais, execute o comando **`python server.py`** para iniciar o script do servidor.
4. Em outro terminal, execute o comando **`python client.py`** para iniciar o script do cliente.
5. Digite a mensagem que deseja enviar no terminal do cliente e pressione Enter.
6. Veja a mensagem recebida no terminal do servidor e nos outros terminais dos clientes.
7. Para encerrar a conexão, digite “exit” no terminal do cliente.

## Autor

Este projeto foi desenvolvido por Kaio Guilherme como parte da disciplina de Sistemas Distribuídos do curso de Ciência da Computação da UFRR.