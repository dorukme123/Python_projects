import math
#-----------------------------------------------------------------------------------------
question1 = """
Написать программу, которая итерируется по тексту и выбирает 
все триплеты (множества из подряд идущих букв). 
B триплетах не может быть пробелов, знаков пунктуации. 
Пример триплетов из фразы "Мама, мыла раму?": 
мамама, мыла, мыла, раму, раму
""";
# test = input("enter test text:")
def question1_answer(text1):
    output_q1 = [];
    text2 = text1.replace(" ","").replace(",","").replace(".","");
    # parsing the text by 3 elements each and pushing inside and array to store them.
    print(f"text you entered was:|{text2}|");
    n = 3;
    for i in range(0,len(text2),3):
        output_q1.append(text2[i:i+n]);
    print(f"output: {output_q1}");
# question1_answer(test);
#-----------------------------------------------------------------------------------------
question2 = """
Создать программу, которая выбирает из текста все даты, 
которые записаны в формате: 
dd.mm.yyyy и сохранить их в формате datetime
"""
test = '''
ben 18.07.1999 da dogdum
o 19.09.1881 de dogdu
''';
import datefinder
def question2_answer(text1):
    dates = datefinder.find_dates(text1);
    for date in dates:
        print(f"Date: {date}");
# or:
import re, datetime
def question2_answer2(text1):
    matches = re.search('\d{2}.\d{2}.\d{4}', text1);
    if matches is None:
        return None;
    date = datetime.datetime.strptime(matches.group(), '%d.%m.%Y').date()
    print(date); 
# question2_answer(test);
#-----------------------------------------------------------------------------------------
question3 = """
N учеников поровну делят K яблок, оставив оставшиеся яблоки в корзине. 
Сколько яблок получит каждый ученик? 
Вход: состоит из целых чисел N и K. N,
 K <10000 Вывод должен быть целым числом.
"""
students = int(input("Number of Students:"));
apples = int(input("Number of Apples:"));
if apples >= 10000:
    print("apples must be less than 10000");
elif apples <= 0:
    print("apples cannot be equal or less than 0");
left_apples = apples % students;
apples_each_student_gets = (apples - left_apples)/students;
print(f"apples that each student gets: {apples_each_student_gets} | apples left: {left_apples}"); 
#-----------------------------------------------------------------------------------------
question4 = """
Вывести последнюю цифру целого числа N. 
Ввод: целое число N. Вывод: последняя цифра N (179-9)
"""
number = int(input("Enter a number: "));
last_digit_of_number = number % 10;
print(f"last digit of {number} = {last_digit_of_number}");
#-----------------------------------------------------------------------------------------
question5 = """
Задано число N. 
С начала дня (00:00) прошло N минут. 
Преобразуйте время в этот момент в часы и минуты, которые покажут цифровые часы. 
Ввод: 0 <N <10 EXP 7. 
Вывод: часы и минуты. часы: 0-24 минуты: 0-60
"""
N = int(input("Enter number of minutes that have passed:"));

minutes = int(N % 60);
hours = int((N - minutes) / 60);
if hours > 24:
    hours = hours % 24;
if hours == 24 and minutes > 0:
    hours = 0;
def get_time(hours,minutes):
    if minutes < 10 and hours < 10:
        return f"current time: 0{hours}:0{minutes}";
    elif minutes < 10 and hours > 10:
        return f"current time: {hours}:0{minutes}";
    elif minutes > 10 and hours < 10:
        return f"current time: 0{hours}:{minutes}";
    else:
        return f"current time: {hours}:{minutes}";

print(get_time(hours,minutes));
#-----------------------------------------------------------------------------------------
question6 = """
Даны три целых числа. Определите, сколько из них совпадают. 
Три целых числа. 
Вывод: • 3, если все совпадают • 2, если совпадают два из них • 0 - если все числа разные
"""
number1 = int(input("number1:"));
number2 = int(input("number2:"));
number3 = int(input("number3:"));

def switch(number1,number2,number3):
    if(number1 == number2 == number3):
        return f"3 numbers are matching";
    elif(number1 != number2 != number3):
        return f"0 numbers are matching";
    elif(number1 == number2 or number1 == number3 or number2 == number3):
        return f"2 numbers are matching";
    else:
        return f"Error";

print(switch(number1,number2,number3));
#-----------------------------------------------------------------------------------------
question7 = """
Даны два ящика размерами A1 × B1 × C1 и A2 × B2 × C2. 
Можно ли разместить одну коробку внутри другой, 
имея параллельные стороны коробок? 
Ввод: A1, B1, C1, A2, B2, C2. 
Вывод:Программа должна вывести одну из следующих фраз: 
• Ячейки равны 
• Первое поле меньше второго 
• Первое поле больше второго 
• Ящики несопоставимы (ПРИМЕР 1 2 3 3 2 1 Ящики равны)
"""
A1 = int(input("enter A1: "));
B1 = int(input("enter B1: "));
C1 = int(input("enter C1: "));
A2 = int(input("enter A2: "));
B2 = int(input("enter B2: "));
C2 = int(input("enter C2: "));


size_of_box1 = A1*B1*C1;
size_of_box2 = A2*B2*C2;

def switch_boxes(size_of_box1,size_of_box2):
    if size_of_box1 == size_of_box2:
        return f"box1:{size_of_box1}=box2:{size_of_box2}|The cells are equal";
    elif size_of_box1 < size_of_box2:
        return f"box1:{size_of_box1}<box2:{size_of_box2}|The first field is less than the second";
    elif size_of_box1 > size_of_box2:
        return f"box1:{size_of_box1}>box2:{size_of_box2}|The first field is greater than the second";
    else:
        return f"box1:{size_of_box1}!=box2:{size_of_box2}|The boxes are not comparable";

print(switch_boxes(size_of_box1,size_of_box2));
#-----------------------------------------------------------------------------------------
question8 = """
Для заданных n <100 завершают русскую фразу «На лугу пасется ...» 
одним из следующих окончаний: «n коров», «nкорова», «n коровый». Ввод: Целое число n. 
Вывод: Выведите один из следующих фразы: • n коров • n корова • n коровы
"""
N = int(input("Enter number of коров: "));

if(N < 100 and N > 0):
    picker = N % 10;
    if(picker == 0 or picker >= 5):
        print(f"{N} коров");
    elif(picker == 1):
        print(f"{N} коровa");
    elif(picker > 1 or picker < 5):
        print(f"{N} коровы");
else:
    print("Error");
#-----------------------------------------------------------------------------------------
