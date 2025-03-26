import os
import aiofiles
from http import HTTPStatus
from .config import PASTA_PDF, HEADERS

async def baixar_pdf(session, url):
    nome_arquivo = os.path.basename(url)
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
