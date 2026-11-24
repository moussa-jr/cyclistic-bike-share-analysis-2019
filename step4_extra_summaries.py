import os
import pandas as pd

base_dir = r"D:\Projects\Cyclistic_2019_Project"
processed_folder = os.path.join(base_dir, "Processed_Data")
clean_path = os.path.join(processed_folder, "cyclistic_2019_cleaned.csv")

df = pd.read_csv(clean_path)

# 1. أكثر 10 محطات انطلاق لكل فئة مستخدم
top_stations = (
    df.dropna(subset=["from_station_name"])
    .groupby(["usertype", "from_station_name"])["trip_id"]
    .count()
    .reset_index(name="rides")
    .sort_values(["usertype", "rides"], ascending=[True, False])
)

top_10_each = top_stations.groupby("usertype").head(10)
print("=== أكثر 10 محطات انطلاق لكل فئة ===")
print(top_10_each.to_string(index=False))

top_10_each.to_csv(
    os.path.join(processed_folder, "summary_top10_stations_by_usertype.csv"),
    index=False
)

# 2. تقسيم مدة الرحلة إلى شرائح زمنية (Duration Buckets)
bins = [0, 15, 30, 60, float("inf")]
labels = ["0-15 min", "15-30 min", "30-60 min", "60+ min"]
df["duration_bucket"] = pd.cut(df["ride_length_min"], bins=bins, labels=labels)

duration_dist = (
    df.groupby(["usertype", "duration_bucket"], observed=False)["trip_id"]
    .count()
    .reset_index(name="rides")
)
duration_dist["pct_within_usertype"] = (
    duration_dist.groupby("usertype")["rides"]
    .transform(lambda x: (x / x.sum() * 100).round(2))
)

print("\n=== توزيع شرائح مدة الرحلة لكل فئة ===")
print(duration_dist.to_string(index=False))

duration_dist.to_csv(
    os.path.join(processed_folder, "summary_duration_buckets.csv"),
    index=False
)

print("\nتم حفظ الملخصات الإضافية بنجاح في Processed_Data.")