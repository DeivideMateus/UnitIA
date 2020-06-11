from telegram import ParseMode, ChatAction
from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging

from untitled.BotRecomendacao.Recomendacao import get_imdb_id, get_movie_title, getRecomendacao

updater = Updater(token='1101037221:AAHYw9MDlyLCD_njw_ZsZTZHMjp1Wceu3h8', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    msg = "Olá, eu sou o Bot IA. Digite o comando desejado:\n" \
          "1 - /filmes id: Retorna uma lista de filmes recomendados para um determinado usuário de 1 a 20.\n" \
          "Ex: /filmes 1 (vai retornar uma lista de filmes recomendados para o usuário 1)"

    context.bot.send_message(chat_id=update.message.chat_id, text=msg, parse_mode=ParseMode.MARKDOWN)


def filmes(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    id_user = context.args[0]

    user = int(id_user)

    msg = getRecomendacao(user)



    context.bot.send_message(chat_id=update.message.chat_id, text=msg, parse_mode=ParseMode.MARKDOWN)


start_handler = CommandHandler('start', start)
filmes_handler = CommandHandler('filmes', filmes, pass_args=True)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(filmes_handler)

updater.start_polling()

updater.idle()
