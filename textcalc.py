import math

def calc(string):

    def sin(n):
        return math.sin(n)
    def cos(n):
        return math.cos(n)
    def tan(n):
        return math.tan(n)
    def pi():
        return round(math.pi, 8)
    

    # данные для перевода из текста в математический вид
    operations = {
        'плюс': '+',
        'минус': '-',
        'умножить': '*',
        'остаток': '%',
        'разделить': '/'
    }
    numbers_input = {
        'ноль': 0, 'один': 1, 'два':  2, 'три':  3, 'четыре': 4, 'пять': 5, 'шесть': 6, 
        'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10, 'одинадцать': 11, 'двенадцать': 12,
        'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать': 15, 'шестнадцать': 16, 'семнадцать': 17,
        'восемнадцать': 18, 'девятнадцать': 19, 'двадцать': 20, 'тридцать': 30, 'сорок': 40,
        'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80, 'девяносто': 90,
        'одна': 1, 'две': 2
        }
    numbers_output = {
        '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть',
        '7': 'семь', '8': 'восемь', '9': 'девять','10': 'десять','11': 'одиннадцать', '12': 'двенадцать',
        '13': 'тринадцать', '14': 'четырнадцать', '15': 'пятнадцать', '16': 'шестнадцать', '17': 'семнадцать',
        '18': 'восемнадцать', '19': 'девятнадцать', '20': 'двадцать', '30': 'тридцать', '40': 'сорок', '50': 'пятьдесят',
        '60': 'шестьдесят', '70': 'семьдесят', '80': 'восемьдесят', '90': 'девяносто', '100': 'сто', '200': 'двести',
        '300': 'триста', '400': 'четыреста', '500': 'пятьсот', '600': 'шестьсот', '700': 'семьсот', '800': 'восемьсот',
        '900': 'девятьсот', '1000': 'тысяча', '2000': 'две тысячи', '3000': 'три тысячи', '4000': 'четыре тысячи',
        '5000': 'пять тысяч', '6000': 'шесть тысяч', '7000': 'семь тысяч', '8000': 'восемь тысяч', '9000': 'девять тысяч',
        }
    # основные переменные, над которыми будут выполняться дествия
    operation = ''

    # перевод входных данных в приемлемый числовой вид и вносим арифметическую операцию в переменную
    mas = string.split()
    tni = 0
    fl = 0
    y = 0
    for i in mas:
        if i in ('плюс', 'минус', 'умножить', 'остаток', 'разделить'):
            if (len(operation) > 0) and (operation[len(operation) - 1] == ')'):
                operation += operations[i]
            elif (len(operation) > 0) and (operation[len(operation) - 1] in ('-', '+', '/', '*', '%')) and (i in ('-', '+')):
                operation += operations[i]
                tni = 0
            else:
                operation += str(tni)
                operation += operations[i]
                tni = 0
        elif i == 'пи':
            operation += str(pi())
            tni = 0
        elif i == 'в':
            operation += str(tni)
            tni = 0          
        elif i == 'степени':
            operation += '**'
        elif i == 'от':
            y = 1
            continue
        elif i == 'синус':
            operation += 'sin('
        elif i == 'косинус':
            operation += 'cos('
        elif i == 'тангенс':
            operation += 'tan('
        elif i == 'скобка':
            continue
        elif i == 'открывается':
            operation += '('
        elif i == 'закрывается':
            operation += str(tni)
            operation += ')'
            tni = 0
        elif i == 'и':
            tni = tni / 1
        elif i == 'на':
            continue
        elif i in ('десятых', 'десятая', 'сотых', 'сотая', 'тысячных', 'тысячная'):
            if '.' in str(tni):
                if i in ('десятых', 'десятая'):
                    fl = fl / 10
                    tni += fl
                if i in ('сотых', 'сотая'):
                    fl = fl / 100
                    tni += fl
                if i in ('тысячных', 'тысячная'):
                    fl = fl / 1000
                    tni += fl
            else:
                if i in ('десятых', 'десятая'):
                    tni = tni / 10
                if i in ('сотых', 'сотая'):
                    tni = tni / 100
                if i in ('тысячных', 'тысячная'):
                    tni = tni / 1000
        else:
            if '.' in str(tni):
                fl += numbers_input[i]
            else:
                tni += numbers_input[i]
    operation += str(tni)
    if y == 1:
        operation += ')'
    # решение
    result_int = round(eval(operation), 3)
    if result_int < 0:
        minplu = -1
        result_int = minplu * result_int
    else:
        minplu = 1
    result_flo = round(result_int - int(result_int), 3)
    

    result_int = int(result_int)
    answer = ''
    if result_flo == 0:
        zp = False
    else:
        zp = True
    
    result_flo = str(result_flo)[2:]




    # !!! вывод !!!
    # обходим целую часть
    if result_int in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000):
        answer = numbers_output[str(result_int)]
    else:
        result_string = ''

        if result_int > 1000:
            index = str(result_int // 1000 * 1000)
            if index != '0':
                result_string += numbers_output[index]
                result_string += ' '

        if result_int > 100:
            index = str(result_int // 100)
            index = str(int(index[len(index) - 1]) * 100)
            if index != '0':
                result_string += numbers_output[index]
                result_string += ' '

        k = 1
        if result_int > 20:
            if 10 < result_int % 100 < 20:
                k = 0
                index = str(result_int % 100)
                result_string += numbers_output[index]
                result_string += ' '
            else:
                index = str(result_int // 10)
                index = str(int(index[(len(index) - 1)]) * 10)
                if index != '0':
                    result_string += numbers_output[index]
                    result_string += ' '
        if k == 1:
            if result_int >= 1:
                index = str(result_int)
                index = index[len(index) - 1]
                if index != '0':
                    result_string += numbers_output[index]
                    result_string += ' '
        
        answer = result_string
    
    # обходим дробную часть
    if zp == True:
        answer += ' и'
        answer += ' '
        if len(result_flo) == 1:
            if result_flo[0] == '1':
                answer += 'одна десятая'
            elif result_flo[0] == '2':
                answer += 'две десятых'
            else:
                answer = answer + numbers_output[result_flo[0]] + ' десятых'
        elif len(result_flo) == 2:
            if result_flo[0] == '0':
                if result_flo[1] == '1':
                    answer += 'одна сотая'
                elif result_flo[1] == '2':
                    answer += 'две сотых'
                else:
                    answer = answer + numbers_output[result_flo[1]] + ' сотых'
            else:
                if (result_flo[0] + result_flo[1]) in ('11', '12', '13', '14', '15', '16', '17', '18', '19'):
                    answer += numbers_output[result_flo[0] + result_flo[1]] + ' сотых'
                else:
                    answer = answer + numbers_output[str(int(result_flo) // 10 * 10)] + ' ' + numbers_output[str(int(result_flo) % 10)] + ' сотых'
        else:
            if result_flo[0] == result_flo[1] == '0':
                if result_flo[2] == '1':
                    answer += 'одна тысячная'
                elif result_flo[2] == '2':
                    answer += 'две тысячных'
                else:
                    answer = answer + numbers_output[result_flo[2]] + ' тысячных' 
            elif result_flo[0] == '0':
                if (result_flo[1] + result_flo[2]) in ('11', '12', '13', '14', '15', '16', '17', '18', '19'):
                    answer += numbers_output[result_flo[1] + result_flo[2]] + ' тысячных'
                else:
                    answer = answer + numbers_output[str(int(result_flo[1]) * 10)] + ' ' + numbers_output[result_flo[2]] + ' тысячных'
            else:
                if (result_flo[1] + result_flo[2]) in ('11', '12', '13', '14', '15', '16', '17', '18', '19'):
                    answer += numbers_output[str(int(result_flo) // 100 * 100)] + ' ' + numbers_output[result_flo[1] + result_flo[2]] + ' тысячных'
                elif (result_flo[1] + result_flo[2]) in ('03', '04', '05', '06', '07', '08', '09'):
                    answer += numbers_output[str(int(result_flo) // 100 * 100)] + ' ' + numbers_output[(result_flo[1] + result_flo[2])[1]] + ' тысячных'
                elif (result_flo[1] + result_flo[2]) == '01':
                    answer += numbers_output[str(int(result_flo) // 100 * 100)] + ' одна тысячная'
                elif (result_flo[1] + result_flo[2]) == '02':
                    answer += numbers_output[str(int(result_flo) // 100 * 100)] + ' две тысячных'
                else:
                    answer = answer + numbers_output[str(int(result_flo) // 100 * 100)] + ' ' + numbers_output[str(int(result_flo[1]) * 10)] + ' ' + numbers_output[result_flo[2]] + ' тысячных'
    
    if minplu == -1:
        answer = 'минус ' + answer

    
    return answer



string = input()
print(calc(string))
