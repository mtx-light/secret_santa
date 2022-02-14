from secret_santa.root import app
from secret_santa.utils.names import get_name, vocal
from secret_santa.utils.quotes import quotes
from random import shuffle


@app.handle(intent='start')
def start(request, responder):
    responder.params.target_dialogue_state = 'start2'

    frame_quotes = quotes[:]
    shuffle(frame_quotes)
    responder.frame['quotes'] = frame_quotes

    responder.reply('Привіт, я - маленький помічник Санти. Я тут, щоб допомогти Санті створити святкову атмосферу!')
    responder.reply('Можеш звати мене Ельф, а як звати тебе?')
    responder.reply('(і прізвище одразу не забудь вказати)')


@app.handle(targeted_only=True)
def start2(request, responder):
    name = get_name(request.text)
    responder.frame['name'] = name
    responder.reply(f'{vocal(name)}, приємно познайомитися.')
    responder.reply(f'Я можу:\n'
                    f'- Зіграти в Таємного Санту\n'
                    f'- Зіграти в Цитати\n'
                    f'- Поговорити про роботу\n'
                    f'- Обговорити твої персональні звершення\n'
                    f'- Смішно поколядувати')
    responder.reply("Audio: ./audio/Magic Moments.mp3")
    responder.reply('Вмикай музику і кажи, з чого розпочнемо?')


@app.handle(default=True)
@app.handle(intent='confirmation')
@app.handle(intent='competence')
def comp(request, responder):
    responder.reply(f'Я простенький бот і розумію короткі повідомлення.'
                    f'Я можу:\n'
                    f'- Зіграти в Таємного Санту\n'
                    f'- Зіграти в Цитати\n'
                    f'- Поговорити про роботу\n'
                    f'- Обговорити твої персональні звершення\n'
                    f'- Смішно поколядувати')
    responder.reply('Що бажаєш?')


@app.handle(intent='clarify')
def clarify(request, responder):
    responder.reply('Під "зіграти в Таємного Санту" я розумію внести твоє ім\'я у список охочих доєднатися до цієї гри,'
                    ' а також дізнатися, які подаруночки ти би хотів отримати.')
    responder.reply('Також можу поспілкуватися з тобою про веселе і сумне,'
                    ' що трапилося з тобою на роботі і в житті за минулий рік.')
    responder.reply('Цитати - весела гра, тобі сподобається.')
    responder.reply('А ще вмію смішно колядувати.')


@app.handle(intent='small_talk')
def small_talk(request, responder):
    facts = ['Деякі американці вірять, що українці прикрашають ялинки іграшковими павучками на павутині.',

             'Перша різдвяна листівка була виготовлена у Лондоні у 1843 році.'
             ' З тодішнього тиражу розміром у тисячу примірників до наших днів збереглися лише дванадцять екземплярів.'
             ' Приблизна оцінка кожної листівки 28.000 доларів.',

             'Італійці, особливо у провінції, дотримуються веселої традиції:'
             ' викидати старі речі через вікна у новорічну ніч.'
             ' Це має принести успіхи і матеріальні блага у прийдешньому році',

             'Раніше легендарну пісню Jingle Bells виконували на День Подяки.']
    responder.reply(facts)

    name = responder.frame.get('name')
    responder.reply(f'{vocal(name)}, отакий веселий факт. З Новим Роком і Різдвом')


@app.handle(intent='greet')
def greetings(request, responder):
    name = responder.frame.get('name')
    replies = [f'Вітаю, {vocal(name)}',
               f'Привіт, {vocal(name)}',
               f'Здоров, {vocal(name)}']
    responder.reply(replies)


@app.handle(intent='negative')
def negative(request, responder):
    replies = ['Ок. Сам наллю, вип\'ю і закушу. З Новим Роком!',

               'Знай: кожна відмова комунікувати з ельфом призводить до'
               ' збільшення шансів отримати різочку під подушку.',

               'Добре.']
    responder.reply(replies)


@app.handle(intent='thanks')
def thanks(request, responder):
    name = responder.frame.get('name')
    replies = ['На здоров\'я.',
               'Будь ласка.',
               f'{vocal(name)}, щасливого Нового Року і Різдва Христового!']
    responder.reply(replies)


@app.handle(intent='goodbye')
def goodbye(request, responder):
    name = responder.frame.get('name')
    replies = ['Have yourself a merry little Christmas.\n'
               'Так кажуть американці',

               'This is the message of Christmas: We are never alone.\n'
               'Це по-амеrykанськи.',

               f'До побачення, {vocal(name)}, усього найкращого у прийдешньому році.'
               f' Бережіть себе і своїх близьких']
    responder.reply(replies)
