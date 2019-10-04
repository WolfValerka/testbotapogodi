import pyowm
import telebot


owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc', language = "ru")
bot = telebot.TeleBot("969905697:AAG_U507SPvlCk9XjgXDeUEBr7d6O1nr7GM")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place( message.text )
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]

    answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n\n"
    answer += "Температура сейчас в районе " + str(temp) + "\n\n"

    if temp < 10:
        answer += "Сейчас ппц как холодно, одевайся как танк!"
    elif temp < 20:
        answer += "Сейчас холодно, оденься потеплее."
    else:
        answer += "Температура норм"

    bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )