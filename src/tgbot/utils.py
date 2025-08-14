from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery, Message, InputMediaPhoto
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def smart_edit(
    callback: CallbackQuery | Message,
    title: str,
    kb: InlineKeyboardBuilder | None = None,
    media: str | None = None,
):
    markup = kb.as_markup() if kb else None

    if isinstance(callback, Message):
        if media:
            await callback.answer_photo(media, caption=title, reply_markup=markup)
        else:
            await callback.answer(title, reply_markup=markup)

        await callback.delete()

    if isinstance(callback, CallbackQuery):
        try:
            if media:
                await callback.message.edit_media(InputMediaPhoto(media=media, caption=title), reply_markup=markup)
            else:
                if callback.message.photo:
                    await callback.message.answer(text=title, reply_markup=markup)
                    await callback.message.delete()
                else:
                    await callback.message.edit_text(text=title, reply_markup=markup)

        except TelegramBadRequest as e:
            await callback.message.answer(title, reply_markup=markup)

        finally:
            try:
                await callback.answer()
            except Exception:
                pass
