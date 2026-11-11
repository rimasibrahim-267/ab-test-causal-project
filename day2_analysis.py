"""
اليوم الثاني: حجم العينة، التحليل الإحصائي، وتطبيق طريقة CUPED
"""
import numpy as np

def calculate_sample_size(p=0.10, mde=0.01):
    """حساب حجم العينة التقريبي لكل مجموعة"""
    z_alpha = 1.96
    z_beta = 0.84
    n = (16 * p * (1 - p) * ((z_alpha + z_beta) ** 2)) / (mde ** 2)
    return int(n)

def apply_cuped(y, x):
    """طريقة CUPED لتقليل التباين باستخدام القياس القبلي"""
    theta = np.cov(x, y)[0, 1] / np.var(x)
    return y - theta * (x - np.mean(x))

if __name__ == "__main__":
    print("\n--- تشغيل اليوم الثاني: العينة وتحليل النتائج و CUPED ---")
    print(f"حجم العينة المطلوب في كل مجموعة تقريباً: {calculate_sample_size():,} مستخدم")
    
    np.random.seed(42)
    x_pre = np.random.normal(100, 20, 1000)
    y_post = x_pre * 0.8 + np.random.normal(50, 10, 1000)
    reduction = (1 - np.var(apply_cuped(y_post, x_pre)) / np.var(y_post)) * 100
    print(f"انخفاض التباين بعد تطبيق CUPED بنسبة: {reduction:.2f}%")
