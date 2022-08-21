import asyncio
from pytgcalls import idle
from config import call_py
from Miq.التشغيل import arq
async def main():
    await call_py.start()
    print("""    ------------------
   |𝑺𝑶𝑼𝑹𝑪𝑬 𝑪𝑹𝒀𝑺𝑻𝑰𝑳 شــغال ! |
    ------------------"""    )
    await idle()
    await arq.close()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
