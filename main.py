from  aiogram import Bot,Dispatcher,types
from aiogram.utils import  executor
from tarjimon import  tarjima_uz,tarjima_en
from environs import Env

env = Env()
env.read_env()
t=env("token")
b=Bot(token=t)
dp=Dispatcher(bot=b)
global a
a=True

#start qism
@dp.message_handler(commands='start')
async  def start_bosilganda(xabar:types.Message):
    e=(xabar.from_user.last_name)
    print(xabar)
    await  xabar.answer(f"Xush kelibsiz {e}")

#help qism
@dp.message_handler(commands='help')
async  def yordam(xabar:types.Message):
    await xabar.answer("Biz sizga hech qanday yordam bera olmaymiz")
#ingliz tili tanlanganda
@dp.message_handler(commands="en")
async  def til(x:types.Message):
    global a
    a=True
    return a

#uz tili tanlanganda
@dp.message_handler(commands="uz")
async def til(x:types.Message):
    global a
    a = False
    return  a

#Yuborilgan matn olish
@dp.message_handler(content_types='text')
async  def xabar_kelganda(x:types.Message):
    f=x.text
    global a
    if a==True:
        natija=tarjima_en(f)
        g="TRUE ishladi"
    else:
        natija=tarjima_uz(f)
        g = "FALSE ishladi"
    await x.answer(natija)
    await x.answer(g)


if __name__=="__main__":
    executor.start_polling(dp)

