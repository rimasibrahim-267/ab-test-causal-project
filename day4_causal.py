"""
اليوم الرابع: الرسوم السببية، وقاعدة القرار، والتقرير
"""
def decision_rule(estimate, ci_lower, ci_upper, mde):
    print(f"\n[Day 4] تحليل القرار - التقدير: {estimate}, فترة الثقة: [{ci_lower}, {ci_upper}]")
    if ci_lower > 0 and ci_lower >= mde:
        print("القرار: 1. فوز واضح -> نطلق الميزة بسلام.")
    elif ci_upper < 0:
        print("القرار: 4. ضرر -> لا نطلق الميزة.")
    else:
        print("القرار: 2. نتيجة غير حاسمة -> نمدد التجربة أو نعدل التصميم.")

if __name__ == "__main__":
    print("--- تشغيل اليوم الرابع: قاعدة القرار والتقرير النهائي ---")
    decision_rule(estimate=1.31, ci_lower=0.69, ci_upper=1.93, mde=0.5)
