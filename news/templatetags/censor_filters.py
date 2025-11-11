from django import template
import re

register = template.Library()

@register.filter(name='censor')
def censor(value):
    """
    Фильтр для замены нежелательных слов на символы '*'
    """
    if not isinstance(value, str):
        return value

    # Список нежелательных слов (можно расширить)
    unwanted_words = [
        'плохое', 'ужасное', 'отвратительное', 'мерзкое',
        'bad', 'terrible', 'awful', 'horrible',
        'спам', 'реклама', 'вирус', 'взлом',
        'spam', 'advertisement', 'virus', 'hack'
    ]

    # Создаем копию текста для обработки
    censored_text = value

    # Заменяем каждое нежелательное слово на символы '*'
    for word in unwanted_words:
        # Используем регулярное выражение для поиска слова с учетом регистра
        pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
        # Заменяем на символы '*' по длине слова
        censored_text = pattern.sub('*' * len(word), censored_text)

    return censored_text