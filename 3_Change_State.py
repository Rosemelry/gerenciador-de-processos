
import psutil

#Função que Permite Alterar Estado de um Processo
#Receber o PID do processo e o estado desejado (bloquear, continuar, executar, reiniciar ou finalizar)
def change_process_state(pid, estado):
    proc = psutil.Process(pid) 
    if estado == "bloquear":
        proc.suspend()
    elif estado == "continuar":
        proc.resume()
    elif estado == "executar":
        proc.resume()
    elif estado == "reiniciar":
        proc.kill()
        proc.wait()
        proc.start()
    elif estado == "finalizar":
        proc.kill()