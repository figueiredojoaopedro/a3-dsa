import webbrowser
import os

def abreArquivoNoNavegador(path):
    try:
        # Open the file in the default web browser
        abs_path = os.path.abspath(path)
        webbrowser.open('file://' + abs_path)
        return "Abrindo arquivo no navegador..."
    except IOError as e:
        return f"Error: {e}"