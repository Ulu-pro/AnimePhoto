from aiogram import Bot, Dispatcher, executor, types
from time import time

import main
import env

bot = Bot(env.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, env.START)


@dp.message_handler(content_types=[types.ContentType.PHOTO])
async def photo(message: types.Message):
    chat_dir = f'{env.DIRECTORY}/{message.from_user.id}'
    file_dir = f'{chat_dir}/{int(time())}'

    main.check_dir(env.DIRECTORY)
    main.check_dir(chat_dir)
    main.check_dir(file_dir)

    path = f'{file_dir}/{env.FILE % 0}'
    await message.photo[-1].download(destination_file=path)
    await bot.send_message(message.from_user.id, env.WAIT)
    await photo_handler(message.from_user.id, f'{file_dir}/%s')


async def photo_handler(chat_id: int, path: str):
    array = []
    for i in range(env.COUNT + 1):
        file = env.FILE % i
        array.append(path % file)
    main.generate(array[0], array[1:])

    await types.ChatActions.upload_photo()
    media = types.MediaGroup()
    for image in array[1:]:
        media.attach_photo(types.InputFile(image))

    await bot.send_media_group(chat_id, media=media)
    await bot.send_message(chat_id, env.READY)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
