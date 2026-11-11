"""
اليوم الثالث: الأخطاء الشائعة والأساليب شبه التجريبية (الفروق في الفروق)
"""
import numpy as np

def check_peeking_risk(looks=10):
    false_positive_rate = 1 - (1 - 0.05) ** looks
    print(f"[Day 3] عدد مرات الاطلاع ({looks}): احتمال الخطأ الكاذب يرتفع إلى {false_positive_rate*100:.1f}%")

def diff_in_diff(treat_pre, treat_post, ctrl_pre, ctrl_post):
    return (np.mean(treat_post) - np.mean(treat_pre)) - (np.mean(ctrl_post) - np.mean(ctrl_pre))

if __name__ == "__main__":
    print("\n--- تشغيل اليوم الثالث: مخاطر الاطلاع والفروق في الفروق ---")
    check_peeking_risk(4)
    effect = diff_in_diff([105.5], [122.5], [104.6], [113.4])
    print(f"تقدير أثر السياسة عبر الفروق في الفروق (DiD): {effect:.2f}")
