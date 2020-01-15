import random

def get_random_phrase():
    weather_phrases_list = [
        'отличный солнечный день',
        'дождливо и пасмурно',
        'пасмурно, но дождя не ожидается',
        'ледяной дождь',
        'гололедица и сильный ветер',
        'морозно: одевайтесь теплее',
        'прекрасный день: можно искупаться'
    ]
    return random.choice(weather_phrases_list)

if __name__=="__main__":
    r = get_random_phrase()
    print(r)