
import telebot

token = '1543927823:AAFYwCSBepoLPt61Le-jYHPbbf_uwaPdAbk'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)