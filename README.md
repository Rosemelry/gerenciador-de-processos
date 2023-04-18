GERENCIADOR DE PROCESSOS

## 📝 Introdução
Como sabemos, um processo é uma instância de programa em execução e,
quando utilizamos um computador, necessariamente, estamos utilizando vários
processos. Com o desenvolvimento das técnicas de integração de circuitos e avanços das
técnicas nos Sistemas Operacionais (SOs) para gerenciamento de hardware, é possível
que executemos vários processos “em paralelo”. O SO tem, desta forma, que gerenciar o
tempo de processador (time slice) em que cada processo/thread terá disponível para
execução de tarefas, e com isso, o escalonamento de tarefas (alocação do processador
para determinado processo/thread) (time sharing).
Geralmente, os SOs trazem ferramentas de suporte ao gerenciamento de
processos. Com essas ferramentas, o administrador do sistema, e os usuários em geral,
pode, por exemplo, consultar informações (proprietário, identificador, tempo de execução,
prioridade de execução, memória consumida, etc), iniciar, bloquear/continuar e encerrar,
bem como alterar prioridades de execução.

## 🔀 Especificação
Este projeto é essencialmente um exercício pratico objetivando não apenas
solidificar os conhecimentos teóricos vistos em sala de aula, mas, principalmente,
propiciar ao estudante uma oportunidade para verticalização dos conhecimentos de
gerenciamento de processos, essenciais para o domínio e desenvolvimento de Sistemas
Distribuídos.

O exercício consiste no projeto e implementação de um Gerenciador de Processos
(GP) para o sistema operacional GNU/Linux. O GP a ser desenvolvido deverá ter as
seguintes características:

* Listar processos de um determinado usuário;

* Permitir consulta de informações sobre um determinado processo , tais como:

- Identificador de Processo (PID);
- Prioridade de execução (NICE);
- Proprietário (USER);
- Tempo total de execução (TIME);
- Estado (STATUS).

* Permitir alterar o estado de um processo:

- Bloquear;
- Continuar (caso o processo esteja bloqueado);
- Executar;
- Reiniciar;
- Finalizar.

* Trocar prioridade de execução;

- De um processo em execução ou
- Antes de executar um processo.