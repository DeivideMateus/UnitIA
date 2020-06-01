from telegram import ParseMode, ChatAction
from telegram.ext import Updater
from telegram.ext import CommandHandler
from untitled.BotAnaliseSentimento.AnaliseSentimento import analisaSentimento
import logging

updater = Updater(token='1101037221:AAHYw9MDlyLCD_njw_ZsZTZHMjp1Wceu3h8', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    msg = "Olá, eu sou o Bot IA. Digite o comando desejado:\n" \
          "1 - /sentimento FR: Analisa o possível sentimento da frase informada.\n" \
          "Ex: /sentimento Estou feliz (deve retornar positivo)"

    context.bot.send_message(chat_id=update.message.chat_id, text=msg, parse_mode=ParseMode.MARKDOWN)


def sentimento(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    lista = context.args
    v1 = ""

    for i in lista:
        v1 = v1 + i + " "

    msg = "Este texto possui um sentimento " + analisaSentimento(v1)

    #print(msg)
    context.bot.send_message(chat_id=update.message.chat_id, text=msg, parse_mode=ParseMode.MARKDOWN)


start_handler = CommandHandler('start', start)
sentimento_handler = CommandHandler('sentimento', sentimento, pass_args=True)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(sentimento_handler)

updater.start_polling()

updater.idle()
