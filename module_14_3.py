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
    ],
        [KeyboardButton(text='Купить')]
    ], resize_keyboard=True
)

buy_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Продукт1", callback_data="product_buying"),
            InlineKeyboardButton(text="Продукт2", callback_data="product_buying"),
            InlineKeyboardButton(text="Продукт3", callback_data="product_buying"),
            InlineKeyboardButton(text="Продукт4", callback_data="product_buying")
        ]
    ]
)

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    product_name = ["Zn", "Mg", "Cr", "D3"]
    product_des = ["Цинк+Витамин C", "Магний хелат", "Хром хелат", "Витамин D3"]
    for i in range(4):
        await message.answer_photo(open(f"{i +1}.png", "rb"),
                                   f"Название: {product_name[i]} | Описание: {product_des[i]} | Цена: {100 * (i + 1)}")
    # with open("1.png", "rb") as Zn:
    #     await message.answer_photo(Zn, f"Название: Product1 | Описание: Цинк+Витамин C | Цена: {1 * 100}")
    # with open("2.png", "rb") as Mg:
    #     await message.answer_photo(Mg, f"Название: Product2 | Описание: Магний хелат | Цена: {2 * 100}")
    # with open("3.png", "rb") as Cr:
    #     await message.answer_photo(Cr, f"Название: Product3 | Описание: Хром хелат | Цена: {3 * 100}")
    # with open("4.png", "rb") as D3:
    #     await message.answer_photo(D3, f"Название: Product4 | Описание: Витамин D3 | Цена: {4 * 100}")
    await message.answer("Выберите продукт для покупки:", reply_markup=buy_menu)


@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


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
