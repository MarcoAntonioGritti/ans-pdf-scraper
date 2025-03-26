import os
from .config import PASTA_PDF

async def limpar_pdfs():
    arquivos_pdf = [f for f in os.listdir(PASTA_PDF) if f.endswith(".pdf")]
    for arquivo in arquivos_pdf:
        os.remove(os.path.join(PASTA_PDF, arquivo))
        print(f"🗑️ PDF removido: {arquivo}")
