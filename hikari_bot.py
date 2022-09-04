#Verion Beta

from telegram.ext import Updater, CommandHandler
from telegram import update, ChatAction

#Librerias locales
from Functions.BasicFunctions import config, definiciones
from Functions.TestCode import test 



token = config()
updater = Updater(token=token, use_context=True)

#Commands
def start(update, context):
    """Saluda a hikari"""
    
    from Functions.BasicFunctions import saludo
    saludos = saludo()

    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=update.effective_chat.id, text=saludos)
        #Debug
    print('Comando ejecutado: start')

def help(update, context):
    """ Acerca de Hikari Bot"""
    
    from Functions.BasicFunctions import help
    
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=update.effective_chat.id, text=help)
    
        #Debub
    print('Comando ejecutado: help')

def rules(update, context):
    # Reglas de la comunidad AprenderPython
    from Functions.BasicFunctions import rules
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

def testcode(update, context):
    # Testeador de codigo
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
