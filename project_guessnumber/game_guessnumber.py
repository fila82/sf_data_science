"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    
    count = 0
    min_number = 0
    max_number = 100
    flag = 0
    
    while True:
        while max_number-min_number>10:
            if number>=(min_number+max_number)/2:
                min_number=(min_number+max_number)/2
                count+=1
                if min_number == number:
                    break # выход из цикла, если угадали 
            else:
                max_number=(min_number+max_number)/2
                if max_number == number:
                    break # выход из цикла, если угадали         
        
        for min_number in range (int(min_number), int(max_number)+1):
            predict_number = min_number
            count+=1
            if predict_number == number:
                break # выход из цикла, если угадали   
        break
    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)

#print(f'Количество попыток: {random_predict()}')