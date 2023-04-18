
import psutil

#Função Consultar Informações de um Processo
def consult_process(pid):
    proc = psutil.Process(pid)