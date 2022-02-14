from secret_santa.root import app
from secret_santa.utils.names import vocal
from random import choice
from secret_santa.utils.frame import save_fields


@app.handle(intent='personal')
def personal(request, responder):
    if request.frame.get('personal_passed'):
        responder.reply('Ми вже про це поговорили, більше вже не хочу.')
        return
    name = responder.frame.get('name')
    responder.params.target_dialogue_state = 'personal2'
    responder.reply(f'{vocal(name)}, чим  тобі запам\'ятався 2021?')


@app.handle(targeted_only=True)
def personal2(request, responder):
    responder.frame['memories'] = request.text
    responder.params.target_dialogue_state = 'personal3'
    responder.reply('Моїм найкращим спогадом є повернення групи чорноногих тхорів у дику природу.'
                    ' Минулий рік став для цієї породи вирішальним: зоологам, зоохасникам і нам, ельфам,'
                    ' вдалося досягти збільшення популяції цієї тварини до 300 осіб. Лише глянь на них.')
    responder.reply('Photo: ./photos/1.jpg')
    responder.reply('Такі милашки як і ти:)')
    responder.reply('До речі, яка пісня асоціюється в тебе з 2020?')


@app.handle(targeted_only=True)
def personal3(request, responder):
    responder.frame['song'] = request.text
    responder.reply('Вау, яка чудова пісня!')

    songs = ["https://www.youtube.com/watch?v=aAkMkVFwAoo",
             "https://www.youtube.com/watch?v=aAkMkVFwAoo",
             "https://www.youtube.com/watch?v=_VJlHWESyLI",
             "https://www.youtube.com/watch?v=n9kfdEyV3RQ",
             "https://www.youtube.com/watch?v=E8gmARGvPlI",
             "https://www.youtube.com/watch?v=0bhsXykXxfg",
             "https://www.youtube.com/watch?v=j9jbdgZidu8",

             "https://www.youtube.com/watch?v=YiadNVhaGwk",
             "https://www.youtube.com/watch?v=gFtb3EtjEic",
             "https://www.youtube.com/watch?v=qPoHul8ngNw"]
    name = responder.frame.get('name')
    responder.params.target_dialogue_state = 'personal4'
    responder.reply(f'А ось моя улюблена: {choice(songs)}')
    responder.reply(f'Під цю пісню добре пити глінтвейн і пританцьовувати. '
                    f'{vocal(name)}, яким(и) своїм(и) досягненням(и) у 2021 ти пишаєшся?')


@app.handle(targeted_only=True)
def personal4(request, responder):
    responder.frame['achievements'] = request.text
    responder.params.target_dialogue_state = 'personal5'
    responder.reply('Оце так-так. А вже поставив цілі на наступний рік? Поділишся? (Я нікому не скажу)')


@app.handle(targeted_only=True)
def personal5(request, responder):
    responder.frame['goals'] = request.text

    save_fields(responder.frame, ['name', 'memories', 'song', 'achievements', 'goals'], 'personal.txt')
    responder.frame['personal_passed'] = True
    name = responder.frame.get('name')
    responder.reply(f'{vocal(name)}, триматиму за тебе кулачки.'
                    ' А ще, будь ласка, не забувай повноцінно харчуватися і спати мінімум вісім.'
                    ' (хєхє, здорове харчування і сон це, звісно, щось фантастичне).')
