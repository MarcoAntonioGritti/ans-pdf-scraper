import os
import zipfile  # Não possui funções assíncronas
from .config import PASTA_PDF, PASTA_SAIDA

NOME_ARQUIVO_ZIP = os.path.join(PASTA_SAIDA, "documentos.zip")

# Função para criar o diretório se não existir
def criar_diretorio_saida():
    os.makedirs(PASTA_SAIDA, exist_ok=True)

# Faz a compactação dos PDFs baixados
def compactar_pdfs():

    criar_diretorio_saida()

    with zipfile.ZipFile(NOME_ARQUIVO_ZIP, "w", zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in os.listdir(PASTA_PDF):
            caminho_completo = os.path.join(PASTA_PDF, arquivo)
            zipf.write(caminho_completo, arquivo)

    print(f"✅ Arquivo ZIP criado com sucesso: {NOME_ARQUIVO_ZIP}")
