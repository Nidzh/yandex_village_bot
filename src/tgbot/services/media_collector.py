import asyncio
import json
import os

from aiogram import Bot, Dispatcher
from aiogram.types import FSInputFile
from loguru import logger


async def upload_all_media(bot: Bot):
    media = {}
    admin_id = 694104488

    # UPLOAD IMAGES
    directory = "./media/image"
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file = FSInputFile(filepath)
            obj = await bot.send_photo(chat_id=admin_id, photo=file)
            media[filename] = obj.photo[-1].file_id

    # # UPLOAD VIDEO
    # directory = "./media/video"
    # for filename in os.listdir(directory):
    #     filepath = os.path.join(directory, filename)
    #     if os.path.isfile(filepath):
    #         file = FSInputFile(filepath)
    #         obj = await bot.send_video_note(chat_id=admin_id, video_note=file)
    #         media[filename] = obj.video_note.file_id
    #
    #
    # # UPLOAD AUDIO
    # directory = "./media/audio/opus"
    # for filename in os.listdir(directory):
    #     filepath = os.path.join(directory, filename)
    #     if os.path.isfile(filepath):
    #         file = FSInputFile(filepath)
    #         obj = await bot.send_voice(chat_id=admin_id, voice=file)
    #         media[filename] = obj.voice.file_id
    #
    # UPLOAD GIF
    directory = "./media/animation"
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file = FSInputFile(filepath)
            obj = await bot.send_animation(chat_id=admin_id, animation=file)
            media[filename] = obj.animation.file_id
    #
    # # UPLOAD DOCUMENTS
    # directory = "./media/documents"
    # for filename in os.listdir(directory):
    #     filepath = os.path.join(directory, filename)
    #     if os.path.isfile(filepath):
    #         file = FSInputFile(filepath)
    #         obj = await bot.send_document(chat_id=admin_id, document=file)
    #         media[filename] = obj.document.file_id


    with open('./media/media_map.json', 'w') as json_file:
        json.dump(media, json_file)

    logger.success("All media files uploaded successfully and saved to media_map.json")


async def read_media_map(dp: Dispatcher):
    with open('./media/media_map.json', 'r') as json_file:
        media = json.load(json_file)
        dp['media'] = media
        logger.info("Media map loaded successfully")
