import asyncio
import aiohttp
from .download_pdf import baixar_pdf
from .config import PDFS_DESEJADOS

async def baixar_pdfs():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(baixar_pdf(session, url) for url in PDFS_DESEJADOS))
