import os
import asyncio
import aiohttp
import aiofiles
from http import HTTPStatus
from compress import compactar_pdfs  # Função externa para compactar PDFs

# Configurações de diretórios
PASTA_PDF = "../data"

# Lista de URLs para download
PDFS_DESEJADOS = [
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"
]

# Headers para evitar bloqueios
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Criar diretório, se necessário
os.makedirs(PASTA_PDF, exist_ok=True)

# Remove todos os PDFs da pasta antes de baixar novos."
async def limpar_pdfs():
    arquivos_pdf = [f for f in os.listdir(PASTA_PDF) if f.endswith(".pdf")]
    for arquivo in arquivos_pdf:
        os.remove(os.path.join(PASTA_PDF, arquivo))
        print(f"🗑️ PDF removido: {arquivo}")

# Baixa um único PDF de forma assíncrona."
async def baixar_pdf(session, url):
    nome_arquivo = os.path.basename(url)  # Extrai o nome do arquivo
    caminho_arquivo = os.path.join(PASTA_PDF, nome_arquivo)

    print(f"📥 Baixando: {nome_arquivo}...")

    try:
        async with session.get(url, headers=HEADERS) as resposta:
            if resposta.status == HTTPStatus.OK and 'application/pdf' in resposta.headers.get('Content-Type', ''):
                async with aiofiles.open(caminho_arquivo, "wb") as f:
                    async for chunk in resposta.content.iter_chunked(1024):
                        await f.write(chunk)
                print(f"✅ Download concluído: {nome_arquivo}")
            else:
                print(f"⚠️ O link {url} não contém um PDF válido. Status: {resposta.status}")

    except Exception as e:
        print(f"❌ Erro ao baixar {nome_arquivo}: {e}")

# Baixa todos os PDFs da lista de forma assíncrona.
async def baixar_pdfs():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(baixar_pdf(session, url) for url in PDFS_DESEJADOS))

async def main():
    await limpar_pdfs()  #  Remove PDFs antigos
    await baixar_pdfs()  #  Faz download dos PDFs
    compactar_pdfs()  #  Compacta os PDFs baixados

if __name__ == "__main__":
    asyncio.run(main())  #  Executa a aplicação assíncrona
