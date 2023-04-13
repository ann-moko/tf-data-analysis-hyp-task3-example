import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import t

chat_id = 371784753 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool:
    alpha = 0.1
    threshold = 300
    n = len(x) 
    mean = np.mean(x)
    std = np.std(x, ddof=1)
    t_stat = (mean - threshold) / (std / np.sqrt(n))
    t_crit = t.ppf(1 - alpha, n - 1)
    return t_stat < t_crit
