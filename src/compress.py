import os 
import zipfile

PASTA_PDFS = "../data"
PASTA_SAIDA = "../output"
NOME_ARQUIVO_ZIP = os.path.join(PASTA_SAIDA, "documentos.zip")


# Criar diretório caso não exista
os.makedirs(PASTA_SAIDA, exist_ok=True)

def compactar_pdfs():
    with zipfile.ZipFile(NOME_ARQUIVO_ZIP,"w",zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in os.listdir(PASTA_PDFS):
            caminho_completo = os.path.join(PASTA_PDFS, arquivo)
            zipf.write(caminho_completo, arquivo)

    print(f"✅ Arquivo ZIP criado com sucesso: {NOME_ARQUIVO_ZIP}")
