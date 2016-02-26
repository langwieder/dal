import re
f = open('/Users/langwieder/Downloads/dal_part.txt', 'r', encoding='utf-8')
text = f.read()


# функция для обработки статьи
def parce_article(text):
    # заглавное слово
    headword = re.findall('^[А-Я --,\?]+', text)[0]
    # примечания
    notes = re.findall('\[.+\]', text)
    # разные значения слова
    sense = text.split('|')
    sense[0] = sense[0][len(headword):]
    # род
    gender = re.findall(' (м\.|ж\.|ср\.) ', text)
    print(gender)
    print(text)


articles = str.split(text, '\n')
for article in articles:
    if article != '' and len(article) > 1:
        parce_article(article)


