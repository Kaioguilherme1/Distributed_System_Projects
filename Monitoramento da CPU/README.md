
# Projeto de Sistemas Distribuídos - Monitoramento da CPU

Este projeto consiste em uma aplicação que monitora a temperatura da CPU e dispara um alarme em caso de sobreaquecimento.

## Arquitetura

A aplicação é composta por quatro componentes principais:

- Um script Python chamado **`sensor.py`** que obtém a temperatura da CPU e envia para uma queue chamada ‘cpu_temp’.
- Um script Python chamado **`alert.py`** que recebe a temperatura da CPU da queue ‘cpu_temp’ e verifica se ela está acima de um limite (por exemplo, 70 graus Celsius). Caso a temperatura esteja acima do limite, o script envia uma mensagem para uma queue chamada ‘alerts’, indicando que foi detectado um incêndio.
- Um script Python chamado **`alarm.py`** que recebe a mensagem da queue ‘alerts’ e dispara um alarme sonoro usando o módulo pygame. Ele também envia uma mensagem para a mesma queue, indicando que o sistema de prevenção de incêndio deve ser ativado.
- Um script Python chamado **`monitor.py`** que exibe todo o trafego dentro das queues do rabbitMQ.

A figura abaixo ilustra a arquitetura da aplicação:

## Requisitos

Para executar este projeto, você precisa ter instalado em sua máquina:


- Python 3
- Pika
- Pygame
- Tabulate
- Docker
- Docker Compose

## Execução

Para executar este projeto, siga os seguintes passos:

1. Clone este repositório em sua máquina.
2. Navegue até a pasta do projeto e abra quatro terminais diferentes.
3. Em um dos terminais, execute o comando **`python sensor.py`** para iniciar o script que envia a temperatura da CPU para a queue ‘cpu_temp’.
4. Em outro terminal, execute o comando **`python alert.py`** para iniciar o script que verifica se a temperatura da CPU está acima do limite e envia uma mensagem para a queue ‘alerts’.
5. Em outro terminal, execute o comando **`python alarm.py`** para iniciar o script que recebe a mensagem da queue ‘alerts’ e dispara um alarme sonoro e uma mensagem para a mesma queue.
6. Em outro terminal, execute o comando **`python monitor.py`** para iniciar o script exibe todo o trafego das queues.

Você pode acompanhar o funcionamento da aplicação pelo terminal que executa o alarm.py.

OBS: Você pode testar o funcionamento da aplicação stressando a CPU a partir deste [link](https://cpux.net/cpu-stress-test-online).

## Autor

Este projeto foi desenvolvido por kaio guilherme como parte da disciplina de Sistemas Distribuídos do curso de Ciência da Computação da UFRR.