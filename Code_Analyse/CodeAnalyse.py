# kaio Guilherme
# Código do Analisador
import sys

import psutil
import matplotlib.pyplot as plt
from matplotlib import animation

arg = int(sys.argv[1])
PID = 0

def get_process_info(pid: int):
    """Retorna as informações de CPU e memória do processo com o PID dado"""
    Process = psutil.Process(pid)
    treads = Process.num_threads()
    time_exec = Process.cpu_times().user
    cpu_percent = Process.cpu_percent(interval=0.5)
    memory_usage = Process.memory_info().rss / (1024 ** 3)
    return [treads, time_exec, cpu_percent, memory_usage]


# Cria as listas para armazenar os valores dos gráficos
cpu_list = []
mem_list = []
time_list = []
treads_list = []

# Configuração do gráfico
fig, (grap1, grap2, grap3) = plt.subplots(3, 1)
fig.suptitle('analisando processo: ' + psutil.Process(arg).name())
grap1.set_ylabel('Uso de CPU (%)')
grap2.set_ylabel('Threads')
grap3.set_ylabel('Uso de Memória (%)')


# Função para atualizar os dados do gráfico
def update_graph(frame):
    global cpu_list, mem_list, time_list

    # Obtém as informações do processo
    tread, time_exec, cpu_percent, memory_usage = get_process_info(PID)

    # Armazena os valores nas listas
    cpu_list.append(cpu_percent)
    mem_list.append(memory_usage)
    time_list.append(time_exec)
    treads_list.append(tread)
    # Atualiza os dados do gráfico
    grap1.clear()
    grap1.set_ylabel('Uso de CPU (%)')
    grap1.set_xlabel('Tempo (s)')
    grap1.plot(time_list, cpu_list, color='blue')
    # grap1.tick_params(axis='x', rotation=90)

    grap2.clear()
    grap2.set_ylabel('Threads')
    grap2.set_xlabel('Tempo (s)')
    grap2.plot(time_list, treads_list, color='green')

    grap3.clear()
    grap3.set_ylabel('Uso de Memória (GB)')
    grap3.set_xlabel('Tempo (s)')
    grap3.plot(time_list, mem_list, color='red')
    # grap3.tick_params(axis='x', rotation=90)


def analyser(pid: int):
    global PID
    PID = pid
    anim = animation.FuncAnimation(fig, update_graph, interval=500)
    plt.show()

analyser(int(arg))
