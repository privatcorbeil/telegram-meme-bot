import os
import random
from telegram import Update, InputFile, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

MEME_FOLDER = "memes"

# Список дій
actions = [
    "Напиши серйозне зізнання на стикері й залиш його на дзеркалі в туалеті.",
    "Запитай у незнайомця: 'Як думаєш, сьогодні хороший день, щоб втекти в Тібет?'",
    "Наклей очі на банани в магазині. Хай трохи поживуть.",
    "Сфоткай себе з серйозним обличчям біля м’яса: 'Я вибрала тебе'.",
    "Прогуляйся з написом: 'Питаю дорогу лише в кішок. Людям не довіряю.'",
    "Постав таймер і почни танцювати, де б не була.",
    "Напиши комусь 'Це знак' — і зникни.",
    "Фото ложки: 'Мій психолог. Завжди слухає.'",
    "Голосове з філософією — голосом білки.",
    "Прочитай випадкову фразу з книжки в маршрутці.",
    "Намалюй 'портал в інший вимір' крейдою.",
    "Фейкове інтерв’ю: 'Що скажете про день лимона?'",
    "Роздрукуй мем і наклей на стовп.",
    "Запиши TikTok: 'Я — реінкарнація СуперМикити.'",
    "Напиши 'Це був лише сон', порви і віддай перехожому.",
    "Подзвони другу: 'Скажи кодове слово — борщ!'",
    "Опитування в інсті: 'Богиня чи булочка?'",
    "Сторіс з пафосом: ніби ти на Оскарі.",
    "Надішли 'Ха! Я все знаю!' і мовчи.",
    "Закричи: 'Я люблю життя, навіть крінжове!'",
    "Рилс: 'Мій ранок як у кіно', а там носок.",
    "Гороскоп, наче вирок.",
    "Назви свою ложку і поговори з нею.",
    "Фотосесія для бутерброда. З ім’ям.",
    "Будильник 17:07 — чекай, що станеться."
]

# Список афірмацій
affirmations = [
    "Не чекай понеділка. Світ рятують у п’ятницю ввечері.",
    "Роби, як хочеш. Потім буде 'так і планувалось'.",
    "Ти не втомився — ти заряджаєшся. Як Wi-Fi після грози.",
    "Якщо світ не підкорився — підкор себе.",
    "Головне не згоріти, а світити.",
    "Мозок хоче спати, серце — революції. Обирай серце.",
    "Не шукай себе. Створи себе.",
    "Твої факапи — трейлер до кіно. Не зливай прем’єру.",
    "Натхнення — це ти в капюшоні з музикою.",
    "Можна чекати знак. А можна бути ним.",
    "Кажи 'а що, якби я вже зробив?'",
    "Селфі, щоб згадати, звідки почав.",
    "Залиш трохи хаосу — щоб було куди підкидати ідеї.",
    "Світ не готовий до твого рівня вогню.",
    "Натисни 'play' на собі.",
    "Кажи 'воу', а не 'ой'.",
    "Мотивація — це ти в дзеркалі з очима тигра."
]

keyboard = ReplyKeyboardMarkup(
    [["🖼 Мем дня", "⚡️ Не жди — дій!"],
     ["💬 Нагадування для душі", "🤝 Зворотний зв’язок"]],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Я — КОЛЕСО ХАУСУ 🌀 Обери кнопку:", reply_markup=keyboard)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🖼 Мем дня":
        meme_files = os.listdir(MEME_FOLDER)
        if meme_files:
            meme = random.choice(meme_files)
            with open(os.path.join(MEME_FOLDER, meme), "rb") as f:
                await update.message.reply_photo(photo=InputFile(f))
        else:
            await update.message.reply_text("Немає мемів у папці.")

    elif text == "⚡️ Не жди — дій!":
        await update.message.reply_text(random.choice(actions))

    elif text == "💬 Нагадування для душі":
        await update.message.reply_text(random.choice(affirmations))

    elif text == "🤝 Зворотний зв’язок":
        await update.message.reply_text("Надішли будь-яке повідомлення, і я передам його далі!")

    else:
        await update.message.reply_text("Дякую! Твоє повідомлення отримано ✅")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
