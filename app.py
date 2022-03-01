from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token='5159427931:AAGJPjcHJui0eg9twqPoNkseIUBUHydpJSA')
db = Dispatcher(bot=bot)


@db.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id

    # text = "Hello, World!"
    # sent_message = await bot.send_message(chat_id=chat_id, text=text)
    # print(sent_message.to_python())

    # sent_message = await bot.send_photo(
    #     chat_id=chat_id,
    #     photo='https://coub-anubis-a.akamaized.net/coub_storage/coub/simple/cw_image/62df0b5e836/87b40bd5ab15fb164667f/1591768473_00026.jpg'
    # )
    # print(sent_message.photo[-1].file_unique_id)

    # result = await bot.set_chat_title(
    #     chat_id=chat_id, title='The Real Slim Shady'
    # )
    # print(result)

    # invite_link = await bot.export_chat_invite_link(chat_id=chat_id)
    # print(invite_link)

    bot_user = await bot.get_me()
    print(bot_user.username)

executor.start_polling(dispatcher=db)
