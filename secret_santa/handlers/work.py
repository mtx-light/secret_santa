from secret_santa.root import app
from secret_santa.utils.names import vocal
from secret_santa.utils.frame import save_fields


@app.handle(intent='work')
def work(request, responder):
    if request.frame.get('work_passed'):
        responder.reply('Ми вже про це поговорили, більше вже не хочу.')
        return
    name = responder.frame.get('name')
    responder.params.target_dialogue_state = 'work2'
    responder.reply(f"{vocal(name)}, давай подивимося яким був 2021 рік для Smiddle."
                    f" Я знаю, що ви дуже багато фіксили Волю і ходили на корпоративи.")
    responder.reply('Photo: ./photos/2.jpg')
    responder.reply('А який твій улюблений корпоратив нашої компанії?')


@app.handle(targeted_only=True)
def work2(request, responder):
    responder.frame['party'] = request.text
    responder.params.target_dialogue_state = 'work3'
    responder.reply(
        'Як шкода, що мене з вами не було. Скажу по секрету, ельфи працюють лише взимку, увесь інший час ми святкуємо,'
        ' відпочиваємо і об\'їдаємося. А яким був твій найщасливіший день на роботі у 2021?'
        ' (напиши одним повідомленням)')


@app.handle(targeted_only=True)
def work3(request, responder):
    responder.frame['best_work_day'] = request.text
    responder.params.target_dialogue_state = 'work4'
    responder.reply('Отакої! А що було найскладнішим для тебе у роботі в 2021?')


@app.handle(targeted_only=True)
def work4(request, responder):
    responder.frame['hard_day'] = request.text
    responder.params.target_dialogue_state = 'work5'
    name = responder.frame.get('name')
    responder.reply(f'{vocal(name)}, давай перемкнемося на щось веселе.'
                    f' Уяви, що Сміддл наступного року зможе взятися за будь-який проєкт у світі.'
                    f' Поділися своїм ідеальним проєктом для наступного року.'
                    f' (спробуй одним повідомленням)')


@app.handle(targeted_only=True)
def work5(request, responder):
    responder.frame['dream_project'] = request.text
    save_fields(responder.frame, ['name', 'party', 'hard_day', 'dream_project'], 'work.txt')
    responder.frame['work_passed'] = True
    responder.reply('Амбітно! Що ж, бажаю тобі веселих свят і проєкту твоєї мрії!')
