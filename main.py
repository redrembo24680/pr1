import logging
import sys
import asyncio
from db import Data, Session
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from settings import Settings

form_router = Router()

class Form(StatesGroup):
    first_name = State()
    second_name = State()
    tel_number = State()


@form_router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.first_name)
    await message.answer(
        "Hi there! What's your first name?",
    )
    


@form_router.message(Form.first_name)
async def process_name(message: Message, state: FSMContext) -> None:
    await state.update_data(first_name=message.text)
    # async with state.proxy() as data:
    #     data['first_name'] = message.text
    await state.set_state(Form.second_name)
    await message.answer(
        "Hi there! What's your second name?",
    )

@form_router.message(Form.second_name)
async def process_name(message: Message, state: FSMContext) -> None:
    await state.update_data(second_name=message.text)
    # async with state.proxy() as data:
    #     data['second_name'] = message.text
    await state.set_state(Form.tel_number)
    await message.answer(
        "Hi there! What's your second Phone number?",
    )    

@form_router.message(Form.tel_number)
async def process_name(message: Message, state: FSMContext) -> None:
    data = await state.update_data(tal_number=message.text)
    # async with state.proxy() as data:
    #     data['tel_number'] = message.text
    
    with Session() as session:
        try:
            session.add(Data(**data))
            session.commit()
            message_text = f"{data['first_name']} you was add to db"

            
        # session.add(
        #     Data(first_name=data.get('first_name'), second_name=data.get('second_name'), tel_number=data.get('tel_number') ))
        # session.commit()
        # await message.reply(f"{data['first_name']} you was add to db")
        except Exception as e:
            session.rollback()
            message_text = f"{data['first_name']} you wasn't add to db. Error{e}"
            # await message.reply(f"{data['name']} you wasn't add to db. Error{e}")

    await state.finish()
    await message.answer(message_text)

async def main():
    bot = Bot(token=Settings.API_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(form_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())