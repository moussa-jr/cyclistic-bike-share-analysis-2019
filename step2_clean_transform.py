import glob
import os
import pandas as pd

base_dir = r"D:\Projects\Cyclistic_2019_Project"
raw_folder = os.path.join(base_dir, "Raw_Data")
processed_folder = os.path.join(base_dir, "Processed_Data")
os.makedirs(processed_folder, exist_ok=True)

# 1. قراءة ودمج الأرباع الأربعة مع توحيد أعمدة Q2
csv_files = sorted(glob.glob(os.path.join(raw_folder, "*.csv")))
dfs = {}
for file_path in csv_files:
    dfs[os.path.basename(file_path)] = pd.read_csv(file_path)

q1_cols = list(dfs["Divvy_Trips_2019_Q1.csv"].columns)
q2_df = dfs["Divvy_Trips_2019_Q2.csv"]
dfs["Divvy_Trips_2019_Q2.csv"] = q2_df.rename(columns=dict(zip(q2_df.columns, q1_cols)))

df = pd.concat(dfs.values(), ignore_index=True)
print("الصفوف قبل التنظيف:", len(df))

# 2. إزالة الصفوف المكررة إن وجدت بناءً على trip_id
df = df.drop_duplicates(subset=["trip_id"]).copy()
print("الصفوف بعد إزالة التكرار:", len(df))

# 3. تحويل start_time و end_time إلى datetime
df["start_time"] = pd.to_datetime(df["start_time"], errors="coerce")
df["end_time"] = pd.to_datetime(df["end_time"], errors="coerce")

# 4. تنظيف tripduration (إزالة الفواصل وتحويله لرقم)
df["tripduration_clean"] = pd.to_numeric(
    df["tripduration"].astype(str).str.replace(",", "", regex=False),
    errors="coerce"
)

# حساب مدة الرحلة بالثواني من start_time و end_time للتحقق
df["calc_duration_sec"] = (df["end_time"] - df["start_time"]).dt.total_seconds()

# استبعاد الرحلات ذات المدة السالبة أو الصفرية أو الأقل من دقيقة (أو التواريخ الفاسدة)
valid_mask = (
    df["start_time"].notna()
    & df["end_time"].notna()
    & (df["calc_duration_sec"] > 0)
)
df = df[valid_mask].copy()
print("الصفوف بعد استبعاد المدد غير الصالحة:", len(df))

# 5. إضافة أعمدة تحليلية مفيدة
df["ride_length_sec"] = df["calc_duration_sec"]
df["ride_length_min"] = df["ride_length_sec"] / 60.0

# في pandas: dayofweek يبدأ من 0 (الاثنين) إلى 6 (الأحد)، و day_of_week هنا من 1 إلى 7
df["day_of_week"] = df["start_time"].dt.dayofweek + 1
df["day_name"] = df["start_time"].dt.day_name()
df["month"] = df["start_time"].dt.month
df["month_name"] = df["start_time"].dt.month_name()
df["start_hour"] = df["start_time"].dt.hour

# تنظيف نصوص usertype
df["usertype"] = df["usertype"].astype(str).str.strip()

# حذف الأعمدة المساعدة المؤقتة
df = df.drop(columns=["calc_duration_sec"])

# 6. حفظ الملف النظيف في Processed_Data
clean_path = os.path.join(processed_folder, "cyclistic_2019_cleaned.csv")
df.to_csv(clean_path, index=False)
print("\nتم حفظ الملف النظيف بنجاح في:", clean_path)

# ملخص سريع لنوع المستخدم
print("\nتوزيع أنواع المستخدمين (usertype):")
print(df["usertype"].value_counts())