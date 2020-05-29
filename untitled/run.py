from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram import ParseMode, ChatAction
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters, RegexHandler
from untitled.Busca import searchPath
import logging
import networkx as nx



updater = Updater(token='1101037221:AAHYw9MDlyLCD_njw_ZsZTZHMjp1Wceu3h8', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    msg = "Olá eu sou o *Data2LearningBot*, vamos conversar?" \
          "\nEnvie uma imagem para que eu possa classifica-la. "

    context.bot.send_message(chat_id=update.message.chat_id, text=msg, parse_mode=ParseMode.MARKDOWN)


def busca(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    msg = searchPath('A', 'Q')

    context.bot.send_message(chat_id=update.message.chat_id, text=msg, parse_mode=ParseMode.MARKDOWN)



def echo(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    reply_keyboard = [['Sim', 'Não']]

    text = "No momento só reconheço imagens. Você deseja enviar uma imagem para que eu possa classifica-la?"


    update.message.reply_text(text, reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))

def unknown(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Desculpa, não entendi o comando digitado =/")


def register_new(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    text_answer = update.message.text

    if text_answer == "Sim":

        update.message.reply_text('É só anexar uma imagem :)',
                                  reply_markup=ReplyKeyboardRemove())
    else:
        update.message.reply_text('Tudo bem, mas quando quiser que eu reconheça uma imagem é só anexar.',
                                  reply_markup=ReplyKeyboardRemove())


start_handler = CommandHandler('start', start)

busca_handler = CommandHandler('busca', busca)
registernew_handler = MessageHandler(Filters.regex('(Sim|Não)$'), register_new)
echo_handler = MessageHandler(Filters.text, echo)
unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(busca_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(registernew_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(unknown_handler)

updater.start_polling()

updater.idle()
