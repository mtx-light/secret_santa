from secret_santa.root import app
from secret_santa.utils.names import get_name, vocal
from secret_santa.utils.quotes import get_quote, author_guessed

@app.handle(intent='play')
def play(request, responder):
    quotes_list = responder.frame.get('quotes')
    if quotes_list:
        quote = quotes_list.pop()
        responder.frame['quote'] = quote
        responder.reply(f'Круто! Тобі потрібно вгадати, хто з твоїх колег сказав цю фразу:\n'
                        f'{quote["quote"]}')
        responder.params.target_dialogue_state = 'play2'
    else:
        responder.reply('Більше цитат немає, почекаємо поки хтось ще щось гарне скаже.')

@app.handle(targeted_only=True)
def play2(request, responder):
    quote = responder.frame.get('quote')
    if 'не' in request.text.lower().split():
        responder.reply(f'Це {quote["author"]}')
    elif author_guessed(request.text, quote):
        responder.reply(f'Так, це {quote["author"]}')
    else:
        responder.reply(f'Ні, це {quote["author"]}')
    responder.params.target_dialogue_state = 'play3'
    responder.reply('Хочеш ще погратися?')

@app.handle(targeted_only=True)
def play3(request, responder):
    if request.intent == 'confirmation':
        quotes_list = responder.frame.get('quotes')
        if quotes_list:
            quote = quotes_list.pop()
            responder.frame['quote'] = quote
            responder.reply(f'Хто з твоїх колег сказав цю фразу:\n'
                            f'{quote["quote"]}')
            responder.params.target_dialogue_state = 'play2'
            return
        else:
            responder.reply('Поки що все, почекаємо поки хтось ще щось гарне скаже.')
            return
    else:
        responder.frame['quote'] = None
        responder.reply('Як собі знаєш!')