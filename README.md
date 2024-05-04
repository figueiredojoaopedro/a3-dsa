# a3-dsa

Cada grupo deverá implementar um algoritmo que determine o tempo médio que um cliente
permanece na fila de uma agência bancária. Quando um cliente entra na fila, o horário é
anotado. Quando ele sai, o tempo que ele permaneceu na fila é calculado e adicionado ao
tempo total de espera. Assim, no final do expediente, é possível determinar quanto tempo, em
média, cada cliente teve que aguardar para ser atendido.

# Cenário:

Na agência tem 3 guiches que atendem a uma única fila de clientes.
Na medida que um guiche fica livre, o primeiro da fila é atendido.
Inicialmente todos os guiches estão livres.
Quando um cliente inicia uma transação num deles, o tempo médio de ocupacao é determinado pelas suas atividades.

<table>
    <thead>
        <tr>
            <th>Transação</th>
            <th>Código</th>
            <th>Tempo Médio</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Saque</td>
            <td>0</td>
            <td>60 segundos</td>
        </tr>
        <tr>
            <td>Depósito</td>
            <td>1</td>
            <td>90 segundos</td>
        </tr>
        <tr>
            <td>Pagamento</td>
            <td>2</td>
            <td>120 segundos</td>
        </tr>
    </tbody>
</table>

# Algoritmo:

Há dois eventos importantes:

- Um cliente chega na agencia e entra na fila
- Um guiche é liberado, alguém entra da fila e o utiliza

Em cada instante de tempo isso pode ocorrer ou nenhum deles.

Término de expediente:
O término do expediente será indicado pelo cronômetro que marcará o tempo em segundos.
Período de atendimento é 6 horas ou 21600 segundos e o expediente terminar após esse tempo corrido.

Chegada do cliente aleatória - funcao aleatória que sorteia de 0 a 29, caso valor seja 0, o cliente chegou, caso contrário, nada acontece.

Um cliente será representado pelo horário e ao entrar na fila, logo o valor na fila será o tempo do cronometro no exato momento.

A transacao será calculada por um número aleatório entre 0 e 2.

No final do expediente, não entra mais nenhum cliente e todos os clientes na fila devem ser atendidos.

Após finalizar tudo, imprimir na tela as seguintes informações:

- Número total de clientes atendidos
- Número de clientes que fizeram saque, depósito e pagamento
- Tempo médio de espera na fila
- Tempo extra de expediente

# To do

<ul>
    <li>Implementar classe que cria uma fila - usar o próprio conceito de fila/queue. - ✅</li>
    <li>Criar funções que geram o número aleatório para indicar a chegada de clientes - ✅</li>
    <li>Criar funções que geram o número aleatório para indicar a transacao efetuada. - ✅</li>
    <li>Implementar chegada do cliente</li>
    <li>Implementar lógica dos guiches</li>
    <li>Implementar logica do expediente</li>
</ul>
