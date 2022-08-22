from telegram.ext import Updater, CommandHandler
from telegram import update, ChatAction
# Fuciones -> Functions/
from Functions.BasicFunctions import config, definiciones
from Functions.TestCode import test 
# Funciones de Login -> Admin/
from Admin import database 
import sqlite3 as sql
# Importamos los mensajes 
import resources

token = config()
updater = Updater(token=token, use_context=True)

#Commands
def start(update, context):
    # Saluda a hikari 
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    saludos = resources.saludo()
    context.bot.send_message(chat_id=update.effective_chat.id, text=saludos)
    print('/start')

def help(update, context):
    # Acerca de Hikari Bot
    help = resources.help() 
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=update.effective_chat.id, text=help)
    print('/help')

def rules(update, context):
    # Reglas de la comunidad AprenderPython
    rules = resources.rules() 
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=update.effective_chat.id, text=rules)
    print('/rules')

def quees(update, context):
    # Busqueda de definiciones
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    user_say = " ".join(context.args)
    answer = definiciones(user_say)
    update.message.reply_text(answer)   
    print('/quees', user_say)

def testcode(update, context):
    # Testeador de codigo
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    user_say = " ".join(context.args)
    answer = test(user_say)
    update.message.reply_text(answer)   
    print('/testcode\nCodigo:', user_say)

def login(update, context):
    # Trabajando
    # Registro de Admins
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    user_say = " ".join(context.args)
    answer = test(user_say)
    update.message.reply_text(answer)   
    print('/testcode\nCodigo:', user_say) 

#Listeners 
start_handler = CommandHandler("start", start)
help_handler = CommandHandler("help", help)
rules_handler = CommandHandler("rules", rules)
quees_handler = CommandHandler("quees", quees)
testcode_handler = CommandHandler("testcode", testcode)

updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(help_handler)
updater.dispatcher.add_handler(rules_handler)
updater.dispatcher.add_handler(quees_handler)
updater.dispatcher.add_handler(testcode_handler)

updater.start_polling()
