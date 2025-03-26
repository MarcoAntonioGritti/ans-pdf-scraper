import asyncio
from src.utils.clean_pdfs import limpar_pdfs
from src.utils.download_pdfs import baixar_pdfs
from src.utils.compress import compactar_pdfs

async def main():
    await limpar_pdfs()  # Remove PDFs antigos
    await baixar_pdfs()  # Faz download dos PDFs
    compactar_pdfs()  # Compacta os PDFs baixados

if __name__ == "__main__":
    asyncio.run(main())
