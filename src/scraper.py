import os
import time
import requests
from http import HTTPStatus as H
from compress import compactar_pdfs

# Diretório de saída
PASTA_PDF = "../data"

# Lista dos PDFs desejados com os links diretos
PDFS_DESEJADOS = [
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"
]

# Headers para evitar bloqueios
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Criar a pasta caso não exista
if not os.path.exists(PASTA_PDF):
    os.makedirs(PASTA_PDF)

def limpar_pdfs():
    """Remove todos os PDFs existentes na pasta antes de baixar novos."""
    if os.path.exists(PASTA_PDF): # Verifica se a pasta existe
        for arquivo in os.listdir(PASTA_PDF): #Interage com os arquivos da pasta
            if arquivo.endswith(".pdf"): # Identifica os arquivos PDF
                os.remove(os.path.join(PASTA_PDF, arquivo))# Remove os arquivos PDF
                print(f"🗑️ PDF removido: {arquivo}")

def baixar_pdfs():
    """Baixa os PDFs diretamente dos links desejados."""
    for link in PDFS_DESEJADOS:
        nome_arquivo = link.split("/")[-1]  # Extrai o nome do arquivo

        print(f"📥 Baixando PDF: {link}")
        resposta = requests.get(link, headers=headers, stream=True)# Faz uma requisição GET para o link

        if resposta.status_code == H.OK:
            if 'application/pdf' in resposta.headers.get('Content-Type', ''):# Verifica se o conteúdo é um PDF
                caminho_arquivo = os.path.join(PASTA_PDF, nome_arquivo)# Prepara o caminho para salvar o arquivo
                with open(caminho_arquivo, "wb") as f:  # Abrir arquivo para escrita binária
                    for chunk in resposta.iter_content(1024):# Carrega o conteúdo do PDF em chunks de 1024 bytes
                        f.write(chunk)
                print(f"✅ PDF baixado com sucesso: {caminho_arquivo}")
            else:
                print(f"❌ O conteúdo de {link} não é um PDF válido.")
        else:
            print(f"❌ Erro ao baixar {nome_arquivo}, Status Code: {resposta.status_code}")

        # Espera 2 segundos entre os downloads para evitar bloqueio
        time.sleep(2)

if __name__ == "__main__":
    limpar_pdfs()  # Apaga os PDFs antigos antes de baixar novos
    baixar_pdfs()  # Baixa os novos PDFs
    compactar_pdfs()  # Compacta os PDFs baixados em um arquivo ZIP