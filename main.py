import telebot


bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, "Здарова, ебать")

    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        bot.send_message(message.chat.id,  "Ты высрал: " + message.text)
bot.polling(none_stop=True, interval=0)