# Simulação de DDOS

Este é um projeto que simula um ataque de negação de serviço distribuído (DDOS) em um servidor. 
O objetivo é sobrecarregar o servidor com um grande número de conexões simultâneas, causando lentidão ou queda do serviço.

## Tecnologias utilizadas

- Python 3

## Dependências

- psutil
- matplotlib

## Como executar o projeto

1. Abra dois terminais no diretório raiz do projeto.
2. Em um terminal, execute o arquivo `servidor.py` com o comando:

    ```python
    python3 servidor.py
    ```
3. Em outro terminal caso queira acompanhar o uso de CPU e memória do servidor, execute o arquivo `../Code_analyser/CodeAnalyser.py` com o comando:

    ```python
    python3 CodeAnalyse.py <pid do servidor>
    ```
   obs: o pid sera impresso no terminal onde o servidor foi executado.
4. Em outro terminal, execute o arquivo `cliente.py` com o comando:

    ```python
    python3 cliente.py <N° Clientes> <N° de mensagens por cliente> <Tamanho da mensagem em Bytes>
    ```
   
## Testes realizados

Teste executado com 100000 clientes e mensagens de 1000 bytes.
### Recursos utilizados
* CPU: Intel Core i5-10300H 
* RAM: 32 GB

![Teste 1](./images/teste1.png)

## Observações

Este projeto tem finalidade educativa e não deve ser utilizado para fins maliciosos.
O ataque simulado neste projeto é realizado em um ambiente controlado, utilizando apenas recursos próprios, sem causar danos a servidores externos ou interferir no tráfego de rede.
O projeto utiliza uma técnica de ataque simples e não representa a complexidade dos ataques reais.

## Autor

Este projeto foi desenvolvido por Kaio Guilherme como parte da disciplina de Sistemas Distribuídos do curso de Ciência da Computação da UFRR.