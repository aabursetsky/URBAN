from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# kb = ReplyKeyboardMarkup(resize_keyboard = True)
# button1 = KeyboardButton(text='Рассчитать')
# button2 = KeyboardButton(text='Информация')
# kb.add(button1)
# kb.add(button2)

kb1 = InlineKeyboardMarkup()
button3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button4 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')

kb1.add(button3)
kb1.add(button4)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


kb = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text='Рассчитать'),
        KeyboardButton(text='Информация')
        ]
], resize_keyboard = True
)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kb1)


@dp.message_handler(text='Информация')
async def inform(message):
    await message.answer('Расчет калорий для оптимального похудения или сохранения нормального веса.')


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.message.answer('для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161:')
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    data = await state.get_data()
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer("Ваша норма калорий "
                         f"{10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5}"
                         " если Вы мужчина")

    await message.answer("Ваша норма калорий "
                         f"{10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) - 161}"
                         " если Вы женщина")
    await state.finish()


@dp.message_handler()  # Реакция на всё остальное
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)