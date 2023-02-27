"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np

predict_number = np.random.randint(1, 101) # загадываем число
count = 0

while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number: