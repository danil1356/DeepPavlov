import telebot;

from deeppavlov.core.common.file import read_json
from telebot import types
from deeppavlov import build_model, configs

bot = telebot.TeleBot('5727073564:AAFrGtRuqYwxrgN0Tj5SVv6_DQU5WZ2nvn4');
file = open('text.txt','r', encoding="utf-8")
context = file.read();

model_config = read_json('squad_ru_bert_infer.json')
model = build_model(model_config, download=True)


@bot.message_handler(content_types=['text']) #слушатель
def answer_text(message):
    answer = model([context], [message.text])
    if answer[0][0] == '':
        bot.send_message(message.from_user.id, 'ответа в тексте не найдено')
    else:
        bot.send_message(message.from_user.id, model([context], [message.text]))



bot.polling(none_stop=True, interval= 0)