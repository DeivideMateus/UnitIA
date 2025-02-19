from telegram import ParseMode, ChatAction
from telegram.ext import Updater
from telegram.ext import CommandHandler
from untitled.BotBusca.Busca import searchPath
import logging

updater = Updater(token='1101037221:AAHYw9MDlyLCD_njw_ZsZTZHMjp1Wceu3h8', use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    msg = "Olá, eu sou o Bot IA. Digite o comando desejado:\n" \
          "1 - /busca P1 P2: Retorna o caminho e custo entre 2 pontos de A até U.\n" \
          "Ex: /busca C T (vai retornar o caminho e custo entre o ponto C e T)"

    context.bot.send_message(chat_id=update.message.chat_id, text=msg, parse_mode=ParseMode.MARKDOWN)


def busca(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    v1 = context.args[0].upper()
    v2 = context.args[1].upper()
    msg = searchPath(v1, v2)

    context.bot.send_message(chat_id=update.message.chat_id, text=msg, parse_mode=ParseMode.MARKDOWN)


start_handler = CommandHandler('start', start)
busca_handler = CommandHandler('busca', busca, pass_args=True)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(busca_handler)

updater.start_polling()

updater.idle()

