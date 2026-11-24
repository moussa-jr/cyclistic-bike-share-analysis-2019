import os
import pandas as pd

base_dir = r"D:\Projects\Cyclistic_2019_Project"
processed_folder = os.path.join(base_dir, "Processed_Data")
clean_path = os.path.join(processed_folder, "cyclistic_2019_cleaned.csv")

# قراءة الملف النظيف
df = pd.read_csv(clean_path)

print("=== 1. مقارنة عامة بين Subscriber و Customer (مدة الرحلة بالدقائق) ===")
overall_summary = df.groupby("usertype")["ride_length_min"].agg(
    total_rides="count",
    mean_min="mean",
    median_min="median",
    max_min="max"
)
overall_summary["rides_share_pct"] = (
    overall_summary["total_rides"] / overall_summary["total_rides"].sum() * 100
).round(2)
print(overall_summary.round(2))

print("\n=== 2. عدد الرحلات ومتوسط المدة حسب أيام الأسبوع ===")
days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
by_day = (
    df.groupby(["usertype", "day_name"])["ride_length_min"]
    .agg(rides="count", avg_min="mean", median_min="median")
    .reset_index()
)
by_day["day_name"] = pd.Categorical(by_day["day_name"], categories=days_order, ordered=True)
by_day = by_day.sort_values(["usertype", "day_name"])
print(by_day.round(2).to_string(index=False))

print("\n=== 3. عدد الرحلات ومتوسط المدة حسب الشهور ===")
by_month = (
    df.groupby(["usertype", "month", "month_name"])["ride_length_min"]
    .agg(rides="count", avg_min="mean")
    .reset_index()
    .sort_values(["usertype", "month"])
)
print(by_month.round(2).to_string(index=False))

print("\n=== 4. أكثر 5 ساعات نشاطاً لكل فئة ===")
by_hour = (
    df.groupby(["usertype", "start_hour"])["ride_length_min"]
    .agg(rides="count", avg_min="mean")
    .reset_index()
)
for ut in by_hour["usertype"].unique():
    top_h = by_hour[by_hour["usertype"] == ut].sort_values("rides", ascending=False).head(5)
    print(f"\nأعلى 5 ساعات لـ {ut}:")
    print(top_h.round(2).to_string(index=False))

# حفظ الجداول الملخصة لاستخدامها في Tableau أو التقرير
by_day.to_csv(os.path.join(processed_folder, "summary_by_usertype_day.csv"), index=False)
by_month.to_csv(os.path.join(processed_folder, "summary_by_usertype_month.csv"), index=False)
by_hour.to_csv(os.path.join(processed_folder, "summary_by_usertype_hour.csv"), index=False)
print("\nتم حفظ ملفات الملخصات بنجاح في Processed_Data.")