from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import update, ChatAction
# Fuciones -> Functions/
from Functions.BasicFunctions import config, definiciones, test
# Importamos los mensajes 
import resources

token = config()
updater = Updater(token=token, use_context=True)

#Commands
def start(update, context):
    # Saluda a hikari 
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    usuario = update.effective_user['first_name']
    saludos = resources.saludo() + " @" +usuario
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
    # Enviamos pequeños datos a la hora de enviar codigo 
    consideracion = resources.test()
    context.bot.send_message(chat_id=update.effective_chat.id, text=consideracion)
    # Testeador de codigo
    username = update.effective_user['first_name']
    codigo = update.message.text
    salida = codigo.replace('/testcode',"#")
    print(f'/testcode\nUsername: {username} \nCodigo:\n{salida}')
    answer = test(salida)
    update.message.reply_text(answer)#texto   

#Listeners 
start_handler = CommandHandler("start", start)
help_handler = CommandHandler("help", help)
rules_handler = CommandHandler("rules", rules)
quees_handler = CommandHandler("quees", quees)
testcode_handler = MessageHandler(Filters.text, testcode)

#Commands
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(help_handler)
updater.dispatcher.add_handler(rules_handler)
updater.dispatcher.add_handler(quees_handler)
updater.dispatcher.add_handler(testcode_handler)

updater.start_polling()
