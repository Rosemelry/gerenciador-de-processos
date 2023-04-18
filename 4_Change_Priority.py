
import psutil

#Função que Troca Prioridade de Execução
def change_priority(pid, prioridade):
    proc = psutil.Process(pid)
    proc.nice(prioridade)