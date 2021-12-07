slovar = dict()
slovar['Bad'] = 'Плохой'
slovar['Good'] = 'Хороший'
slovar['Big'] = 'Большой'
slovar['Small'] = 'Маленький'
print('Какое слово вы ищите?')
slovo = input()
if slovo in slovar:
    print('Перевод вашего слова', slovar[slovo])
else:
    print('Такого слова нет')