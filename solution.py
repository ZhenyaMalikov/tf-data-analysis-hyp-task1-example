import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 516575251 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.09
    control_conversion = x_success/x_cnt
    test_conversion = y_success/y_cnt
    #находим общую конверсию
    total_conversion = (x_success + y_success)/(x_cnt + y_cnt)
    #вычисляем стандартную ошибку
    se = (total_conversion * (1 - total_conversion) * (1/x_cnt + 1/y_cnt))
    #находим z-статистику
    z = (control_conversion - test_conversion)/se
    #находим критическое значение z-статистики
    critical_value = norm.ppf(1 - alpha/2)
    #отклоняем нулевую гипотезу, если pval < уровня значимости (то есть pval < alpha => True)
    return abs(z) > critical_value
