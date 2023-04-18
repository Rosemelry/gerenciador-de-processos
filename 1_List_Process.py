
import psutil

#Função Listar Processos do Usuário
def list_user_processes(username):
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        if proc.info['username'] == username:
            print(f"PID: {proc.info['pid']}, Nome: {proc.info['name']}")