def criaStringRelatorio(totalClientesAtendidos, totalSaquesRealizados, totalDepositosRealizados, totalPagamentosRealizados, tempoExtra, mediaEspera):
    relatorio = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório do Dia</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 20px;
        }}
        h1 {{
            color: #007BFF;
        }}
        ul {{
            list-style-type: none;
            padding: 0;
        }}
        li {{
            background: #fff;
            margin: 10px 0;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }}
    </style>
</head>
<body>
    <h1>Relatório do Dia</h1>
    <ul>
        <li>Total de Clientes Atendidos: {totalClientesAtendidos}</li>
        <li>Total de Saques Realizadas: {totalSaquesRealizados}</li>
        <li>Total de Depósitos Realizadas: {totalDepositosRealizados}</li>
        <li>Total de Pagamentos Realizadas: {totalPagamentosRealizados}</li>
        <li>Tempo Extra de Simulação: {tempoExtra:.2f} minuto(s)</li>
        <li>Tempo Médio de Espera na Fila: {mediaEspera:.2f} minuto(s)</li>
    </ul>
</body>
</html>
    """.format(
        totalClientesAtendidos=totalClientesAtendidos,
        totalSaquesRealizados=totalSaquesRealizados,
        totalDepositosRealizados=totalDepositosRealizados,
        totalPagamentosRealizados=totalPagamentosRealizados,
        tempoExtra=tempoExtra,
        mediaEspera=mediaEspera
    )
    
    return relatorio
