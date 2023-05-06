# Analisador de Processos

Este é um projeto que utiliza a biblioteca psutil do Python para analisar o desempenho de um processo em execução no sistema operacional. A partir das informações de CPU e memória, é criado um gráfico em tempo real que permite visualizar o comportamento do processo ao longo do tempo.

## Tecnologias utilizadas

- Python 3
- psutil
- matplotlib

## Como executar o projeto

1. Abra um terminal no diretório raiz do projeto.
2. Execute o arquivo `CodeAnalyser.py` com o comando:

    ```python
    python3 CodeAnalyse.py <pid do processo>
    ```

   Substitua `<pid do processo>` pelo número de identificação do processo que deseja analisar. O PID pode ser obtido a partir do gerenciador de tarefas do sistema operacional.
   
3. Aguarde o gráfico ser exibido no terminal. Ele será atualizado em tempo real com as informações de CPU e memória do processo analisado.

## Autor

- Kaio Guilherme (@kaio-guilherme)