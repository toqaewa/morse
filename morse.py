import winsound
import time

def Clean_stroke(content):
    result = []
    content = str(content).lower()

    for element in content:
        if ord(element) >= 1072 and ord(element) <= 1103:
            result.append(element)
    
    return result

def Russian_to_Morse(content):
    rus_to_morse = {
        'а': '.-',
        'б': '-...',
        'в': '.--',
        'г': '--.',
        'д': '-..',
        'е': '.',
        'ж': '...-',
        'з': '--..',
        'и': '..',
        'й': '.---',
        'к': '-.-',
        'л': '.-..',
        'м': '--',
        'н': '-.',
        'о': '---',
        'п': '.--.',
        'р': '.-.',
        'с': '...',
        'т': '-',
        'у': '..-',
        'ф': '..-.',
        'х': '....',
        'ц': '-.-.',
        'ч': '---.',
        'ш': '----',
        'щ': '--.-',
        'ъ': '.--.-.',
        'ы': '-.--',
        'ь': '-..-',
        'э': '..-..',
        'ю': '..--',
        'я': '.-.-'
    }

    content = Clean_stroke(content)
    result = []

    for element in content:
        result.append(rus_to_morse[element])

    return result

frequency = 1000
input = input('Введите строку для распознавания: ')
content = Russian_to_Morse(input)

for set in content:
    for symbol in set:
        if symbol == '.':
            winsound.Beep(frequency, 100)
        elif symbol == '-':
            winsound.Beep(frequency, 700)
    print()
    time.sleep(0.2)