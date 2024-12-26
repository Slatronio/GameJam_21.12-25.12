import telebot
from telebot import types
import time
from PIL import Image

bot = telebot.TeleBot('7785796329:AAF1j_FZFKKyPPhn_Fd0R0_s22U2bpkelOc')

buttons = []
lina = 0
katya = 0
aglaya = 0

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/start':
        storyline(message, 0)

def storyline(message, step):
    if step == 0:
        lina = 0
        katya = 0
        aglaya = 0
        bot.send_photo(message.from_user.id, Image.open('images/mirror1.jpg'), caption='Сегодня Саша жутко опаздывал в университет. Ему в очередной раз снились самолёты и баталии, но вместо людей были какие-то невнятные организмы. Подобные сны казались ему странными. С трудом согнав морок прошедшей ночи, он хотел как можно скорее выскочить на автобусную остановку, чтобы успеть на пару.')
        time.sleep(2)
        keyboard = types.InlineKeyboardMarkup()
        buttons = types.InlineKeyboardButton('— Ну и кто там пишет?!', callback_data='step_1')
        keyboard.add(buttons)
        bot.send_message(message.from_user.id, 'Би-и-п! Би-и-ип!', reply_markup=keyboard)

    elif step == 1:
        keyboard = telebot.types.InlineKeyboardMarkup()
        buttons = [
            telebot.types.InlineKeyboardButton('Сообщение от контакта "Лина бар Доски"', callback_data='choise_11'), 
            telebot.types.InlineKeyboardButton('Сообщение от контакта "Аглая Драмтеатр"', callback_data='choise_12'), 
            telebot.types.InlineKeyboardButton('Сообщение от контакта "Катя Староста"', callback_data='choise_13'), 
            telebot.types.InlineKeyboardButton('Сообщение от контакта "Димон"', callback_data='choise_14'), 
            ]
        for button in buttons:
            keyboard.add(button)
        time.sleep(0.5)
        bot.send_message(message.chat.id, 'Чьё сообщение прочитать?', reply_markup=keyboard)
    
@bot.callback_query_handler(func=lambda call: True) 
def button_pressed(call):

    if call.data.split('_')[0] == 'step':

        if call.data.split('_')[1] == '1':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None) 
            bot.send_message(call.message.chat.id, '— Ну и кто там пишет?!')
            storyline(call.message , 1)

        elif call.data.split('_')[1] == '2':
            pass

    elif call.data.split('_')[0] == 'choise':

        if call.data.split('_')[1] == '11':
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None) 
            bot.send_message(call.message.chat.id, 'Сообщение от контакта "Лина бар Доски"')
            bot.send_photo(call.message.chat.id, Image.open('images/lina1.png'), caption='Лина: Прив, че каво? Вечером го в Доски?')
            keyboard = telebot.types.InlineKeyboardMarkup()
            #buttons.pop(0)
            buttons_temp = [
            telebot.types.InlineKeyboardButton('Саша: Дарова, го)', callback_data='choise 111'), 
            telebot.types.InlineKeyboardButton('Проигнорировать', callback_data='choise 112'),  
                ]
            for button in buttons_temp:
                keyboard.add(button)
            time.sleep(0.5) 
            bot.send_message(call.message.chat.id, 'И что ей ответить?', reply_markup=keyboard)
          
bot.infinity_polling()
