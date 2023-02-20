import openai
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.methods.send_message import SendMessage

dp = Dispatcher()
openai.api_key = "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"


@dp.message(Command(commands=["start"]))
async def start(message: Message) -> None:
    await message.answer("Привет!\nЯ бот - ГЕЙ \nЛюблю ебаться в очко с СЕРГЕЕМ")
    return

@dp.message(Command(commands=["pnh"]))
async def start(message: Message) -> None:
    await message.answer("от @The_Dicer\nПошёл на ХУЙ!")
    return

@dp.message(Command(commands=["dota"]))
async def start(message: Message) -> None:
    await message.answer("@The_Dicer \n@WorldOwner \n@VaddDie \n@xishee \nmaybe @Tatarich5 \nGOOOOOOOOOOOOOO \n ВВВВВВВВВВВВВВВВ DOTU!")
    return
  
@dp.message(Command(commands=["chat"]))
async def ii(message: Message) -> None:
    message.text[6:]
    response = openai.Completion.create( 
     engine="text-davinci-003", 
     prompt='"""\n{}\n"""'.format(message.text), 
     temperature=0, 
     max_tokens=1200, 
     top_p=1, 
     frequency_penalty=0, 
     presence_penalty=0, 
     stop=['"""'])
    await bot.send_message(message.chat.id, f'\n{response["choices"][0]["text"]}', parse_mode='Markdown')
    return
    

bot = Bot("5887932935:AAFV98wnZOWd-BQatWNorowQwzP94b-3xBo")
dp.run_polling(bot)
