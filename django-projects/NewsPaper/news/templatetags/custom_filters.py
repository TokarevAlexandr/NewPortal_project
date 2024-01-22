from django import template


register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.

def censor_filter(text):
    unwanted_words = ['редиска', 'дурак', 'козёл']  # список нежелательных слов
    for word in unwanted_words:
        text = text.replace(word, '*' * len(word))  # замена нежелательных слов на символ "*"
    return text