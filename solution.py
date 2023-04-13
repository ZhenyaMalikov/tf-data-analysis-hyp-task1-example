import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 516575251 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.09
    successes = np.array([x_success, y_success])
    alls = np.array([x_cnt, y_cnt])
    p_val = proportions_ztest(successes, alls, alternative='larger')[1]
    return True if p_val < alpha else False
