import telebot

TOKEN = '849135131:AAFtNwvNUAPfDrZHEGvbR9lMlvJoMLmOsDg'

bot = telebot.TeleBot(TOKEN)

usr_list = {
    'рома': '@ASX_4F',
    'антон': '@todayitsnotokay',
    'дима': '@blckwoods',
    'саша': '@Alsim'
}

print(usr_list, '\n\n')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет. \n'
                                      'Бот научился призывать коллегу в чат по имени\n'
                                      'Наши имена он знает по умолчанию \n\n'
                                        '/help - информация о командах')




@bot.message_handler(commands=['anton'])
def send_anton(message):
    bot.send_message(message.chat.id, '@todayitsnotokay - ты пидор')


@bot.message_handler(commands=['biba'])
def biba(message):
    bot.send_message(message.chat.id, 'хуиба, блять, иди работай')
    file = open('puten.png', 'rb')
    bot.send_photo(message.chat.id, file)



@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Для того, чтобы призвать кого-то в чат - напиши в чат призыв(по умолчанию имя) \n\n'
                                      '/anton - оскорбить Антона\n\n'
                                    '/add - подробно о добавлении призыва\n\n'
                                    '/del - подробно об удалении призыва\n\n'
                                    '/biba - хуиба')


@bot.message_handler(commands=['add'])
def add(message):
    bot.reply_to(message, '//add позволяет добавить пользователя в список призывов. \n\n'
                        'Для того, чтобы добавить призыв себя напиши:\n'
                        '//add [как тебя призвать], обязательно через пробел, иначе я съем первую букву.')

@bot.message_handler(commands=['del'])
def dell(message):
    bot.reply_to(message, '//del позволяет удалить призыв. \n\n'
                        'Для того, чтобы удалить свой напиши:\n'
                        '//del [существующий призыв], обязательно через пробел, иначе я съем первую букву.')
@bot.message_handler(content_types=['text'])
def call_usr(message):
    name = message.text
    name = name.lower()
    if name in usr_list:
        bot.send_message(message.chat.id, usr_list[name])

    txt = message.text
    if '//add ' in txt:
        usr = message.from_user.username
        txt = txt[6:]
        u_keys = usr_list.keys()
        if txt in u_keys:
            bot.reply_to(message, 'Такой призыв уже есть.')
        else:
            usr_list[txt] = f'@{usr}'
            print(usr_list)
            bot.reply_to(message, 'Призыв успешно добавлен.')

    if '//del ' in txt:
        txt = txt[6:]
        u_keys = usr_list.keys()
        if txt in u_keys:
            del usr_list[txt]
            bot.reply_to(message, 'Призыв успешно удален.')
            print(usr_list)
        else:
            bot.reply_to(message, 'Такого призыва нет.')


bot.polling(none_stop=True)
