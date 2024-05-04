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

# To do

## Implementar classe que cria uma fila - usar o próprio conceito de fila/queue.
