"""
اليوم الأول: الأساس وتصميم التجربة والتوزيع الثابت وفحوصات الثقة
"""
import hashlib
from scipy.stats import chi2_contingency

def assign_variant(user_id, exp_name="push_notification_exp"):
    """توزيع المستخدم ثابتاً باستخدام الـ Hash لضمان عدم تغير النسخة"""
    key = f"{user_id}_{exp_name}".encode('utf-8')
    hash_val = int(hashlib.md5(key).hexdigest(), 16)
    return 'B' if (hash_val % 100) < 50 else 'A'

def check_srm(contingent_a, contingent_b):
    """فحص نسبة التوزيع (Sample Ratio Mismatch - SRM)"""
    obs = [[contingent_a, contingent_b], [50000, 50000]]
    chi2, p_val, _, _ = chi2_contingency(obs)
    print(f"[Day 1] SRM Test -> Chi2: {chi2:.4f}, p-value: {p_val:.4f}")
    if p_val < 0.001:
        print("تحذير: يوجد خلل في التوزيع (SRM Detected)!")
    else:
        print("توزيع العينة سليم ولا يوجد SRM.")

if __name__ == "__main__":
    print("--- تشغيل اليوم الأول: التصميم والتوزيع ---")
    print(f"المستخدم user_123 في النسخة: {assign_variant('user_123')}")
    check_srm(50150, 49850)
