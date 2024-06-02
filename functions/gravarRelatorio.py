from functions.abreArquivoNoNavegador import abreArquivoNoNavegador;

def gravarRelatorio(relatorio):
    with open("Relatorio.html", "w", encoding="utf-8") as file:
        file.write(relatorio);

    # Abre o arquivo no navegador
    msg = abreArquivoNoNavegador("Relatorio.html");
    print(msg);