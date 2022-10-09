#Verion Beta

from telegram.ext import Updater, CommandHandler
from telegram import update, ChatAction
from Resources.credentials import tokentelegrambot as tokenbot

#Commands
def start(update, context):
    """Saluda a hikari"""
    
    from Functions.BasicFunctions import saludo

    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=update.effective_chat.id, text=saludo())
        #Debug
    print('Comando ejecutado: start')

def help(update, context):
    """ Acerca de Hikari Bot"""
    
    from Resources.DataBase import help
    
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=update.effective_chat.id, text=help)
    
        #Debub
    print('Comando ejecutado: help')

def rules(update, context):
    """Reglas de la comunidad AprenderPython"""

    from Resources.DataBase import rules
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=update.effective_chat.id, text=rules)
    print('Comando ejecutado: rules')

def quees(update, context):
    """Busqueda de definiciones"""
    from Functions.BasicFunctions import definiciones

    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    user_say = " ".join(context.args)
    answer = definiciones(user_say)
    update.message.reply_text(answer)   

    #Debug
    print('Comando ejecutado: quees ', user_say)

#Start Hikari
updater = Updater(token=tokenbot, use_context=True)

start_handler = CommandHandler("start", start)
updater.dispatcher.add_handler(start_handler)
help_handler = CommandHandler("help", help)
updater.dispatcher.add_handler(help_handler)
rules_handler = CommandHandler("rules", rules)
updater.dispatcher.add_handler(rules_handler)
quees_handler = CommandHandler("quees", quees)
updater.dispatcher.add_handler(quees_handler)

updater.start_polling()