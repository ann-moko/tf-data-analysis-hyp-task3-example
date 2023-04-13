import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import t

chat_id = 371784753 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: 
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.1
    t_statistic, p_value = stats.ttest_1samp(a=x, popmean=300)
    return (p_value < alpha)   # Ваш ответ, True или False
