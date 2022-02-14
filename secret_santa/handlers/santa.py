from secret_santa.root import app
from secret_santa.utils.names import vocal
from secret_santa.utils.frame import save_fields

@app.handle(intent='santa')
def santa(request, responder):
    if request.frame.get('santa_passed'):
        responder.reply('Ми вже про це поговорили, більше вже не хочу.')
        return
    name = responder.frame.get('name')
    responder.params.target_dialogue_state = 'santa2'
    responder.reply(f'{vocal(name)}, перейдімо до головного - Таємного Санти!'
                    f' Хочеш стати Таємним Сантою для когось із своїх колег?')


@app.handle(targeted_only=True)
def santa2(request, responder):
    if request.intent == 'confirmation':
        responder.params.target_dialogue_state = 'santa3'
        responder.reply('Які подаруночки ти хочеш?\n\n'
                        'Я передам твоєму Таємному Санті.\n'
                        '(орієнтовно до 400 грн)')
        responder.reply('Не поспішай, подумай хвилинку і напиши подаруночок у наступному повідомленні.')
        return
    elif request.intent == 'clarify':
        responder.params.target_dialogue_state = 'santa2'
        responder.reply('Ти залишиш свій вішліст і хтось з колег стане твоїм Таємним Сантою.'
                        ' І ти для когось теж. Подаруночки приносимо на корпоратив.')
        responder.reply('Граємо?')
        return
    else:
        responder.reply('Що ж, не забудь завітати на таємну новорічну вечірку 22 грудня!'
                        ' Щасливого Нового Року і Різдва Христового!')
        return


@app.handle(targeted_only=True)
def santa3(request, responder):
    if any([(word in ['все', 'ні', 'досить', 'не', 'нічого', 'нет', 'не',
                      'неа', 'хватит', 'достаточно']) for word in request.text.lower().split()]):
        save_fields(responder.frame, ['name', 'wish_list'], 'santa.txt')
        responder.frame['santa_passed'] = True
        responder.reply('Добре. Завтра тобі на робочу пошту прийде лист з віш-лістом твого колеги.'
                        ' Ти станеш таємним Сантою для нього. Подаруночки приносимо на корпоратив.')
        responder.reply('Бажаеш погратись у щось ще?')
        return
    wish_list = responder.frame.get('wish_list')
    if not wish_list:
        wish_list = []
    wish_list.append(request.text)
    responder.frame['wish_list'] = wish_list

    responder.params.target_dialogue_state = 'santa4'
    name = responder.frame.get('name')
    responder.reply(f'{vocal(name)}, хочеш дописати ще щось?')


@app.handle(targeted_only=True)
def santa4(request, responder):
    if any([(word in ['все', 'ні', 'досить', 'не', 'нічого', 'нет', 'не',
                      'неа', 'хватит', 'достаточно']) for word in request.text.lower().split()]):
        save_fields(responder.frame, ['name', 'wish_list'], 'santa.txt')
        responder.frame['santa_passed'] = True
        responder.reply('Добре. Завтра тобі на робочу пошту прийде лист з віш-лістом твого колеги.'
                        ' Ти станеш таємним Сантою для нього. Подаруночки приносимо на корпоратив.')
        responder.reply('Бажаеш погратись у щось ще?')
        return
    else:
        responder.params.target_dialogue_state = 'santa3'
        responder.reply('Слухаю твої побажання далі...')
        return
