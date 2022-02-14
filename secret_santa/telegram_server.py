from datetime import datetime

from telebot import TeleBot

from secret_santa.__init__ import app
from mindmeld.components.dialogue import Conversation
import random
import string

bot = TeleBot('5065049288:AAE1C_5pgiyUSrIMa3WyAu7J9w4EYlfIfCI')

conversations = {}


@bot.message_handler(commands=['restart'])
def reload(message):
    try:
        username = message.chat.id
    except:
        username = ''.join(random.choices(string.ascii_uppercase, k=5))

    conversations[username] = {}
    conversations[username]['data'] = {'username': username}
    conversations[username]['conversation'] = Conversation(app=app, context=conversations[username]['data'])

    print(f"{username} has new session")
    print("==========================")
    bot.send_message(message.chat.id, "restarted")


@bot.message_handler(func= lambda m: True)
def reply(message):
    request_text = message.text
    try:
        username = message.chat.id
    except:
        username = ''.join(random.choices(string.ascii_uppercase, k=5))

    if username not in conversations:
        conversations[username] = {}
        conversations[username]['data'] = {'username': username}
        conversations[username]['conversation'] = Conversation(app=app, context=conversations[username]['data'])

    resps = conversations[username]['conversation'].say(request_text)
    # if not resps:
    #     raise ValueError(f"No responses for {request_text}")

    for resp in resps:
        print(username)
        print(request_text)
        if resp.startswith('Photo: '):
            print(resp)
            print('=================================')
            resp = resp.replace('Photo: ', '')
            with open(resp, 'rb') as file:
                bot.send_photo(message.chat.id, file)
        elif resp.startswith('Audio: '):
            print(resp)
            print('=================================')
            resp = resp.replace('Audio: ', '')
            with open(resp, 'rb') as file:
                bot.send_audio(message.chat.id, file)
        else:
            # history = conversations[username]['conversation'].history
            # if history:
            #     intent = history[0]['request']['intent']
            #     resp += f"\n[{intent}]"
            #     if history[0]['request']['entities']:
            #         resp += "\nEntities"
            #         for e in history[0]['request']['entities']:
            #             resp += f"\n{e}"

            # logger.write(":::\n".join(str(l) for l in [timestamp(), username, request_text, resp, LOGEND]))
            print(resp)
            print('=================================')
            bot.send_message(message.chat.id, resp)

bot.infinity_polling()