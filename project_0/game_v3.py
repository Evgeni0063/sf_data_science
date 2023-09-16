import numpy as np

def half_division(number:int=1) -> int:
    """Угадываем число методом половинного деления

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    min_bound = 1 # Нижний диапазон поиска
    max_bound = 101 #Верхний диапазон поиска
    
    while True:
        count += 1
        predict_number = round(min_bound+max_bound) / 2 # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
        if number > predict_number: # Корректируем нижнию границу поиска
            min_bound = predict_number
        if number < predict_number: # Корректируем верхнюю границу поиска
            max_bound = predict_number
    return(count)

print(f'Количество попыток: {half_division()}')

def score_game(half_division) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(half_division(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    score_game(half_division)
    