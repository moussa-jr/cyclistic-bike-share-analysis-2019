import glob
import os
import pandas as pd

base_dir = r"D:\Projects\Cyclistic_2019_Project"
raw_folder = os.path.join(base_dir, "Raw_Data")
processed_folder = os.path.join(base_dir, "Processed_Data")
os.makedirs(processed_folder, exist_ok=True)

csv_files = sorted(glob.glob(os.path.join(raw_folder, "*.csv")))

dfs = {}
for file_path in csv_files:
    file_name = os.path.basename(file_path)
    dfs[file_name] = pd.read_csv(file_path)

# نأخذ أسماء الأعمدة المرجعية من Q1
q1_cols = list(dfs["Divvy_Trips_2019_Q1.csv"].columns)

# نطابق أسماء أعمدة Q2 مع Q1 حسب الترتيب
q2_df = dfs["Divvy_Trips_2019_Q2.csv"]
rename_map = dict(zip(q2_df.columns, q1_cols))
dfs["Divvy_Trips_2019_Q2.csv"] = q2_df.rename(columns=rename_map)

# نتحقق الآن أن جميع الملفات أصبحت متطابقة في الأعمدة
all_match = all(list(d.columns) == q1_cols for d in dfs.values())
print("هل جميع الأعمدة متطابقة الآن بعد التوحيد؟", all_match)

if all_match:
    df_2019 = pd.concat(dfs.values(), ignore_index=True)
    print("إجمالي الصفوف بعد دمج Q1 إلى Q4:", len(df_2019))
    print("\nأسماء الأعمدة الموحدة:")
    print(list(df_2019.columns))
    print("\nأول 5 صفوف:")
    print(df_2019.head())
    print("\nعدد القيم المفقودة في كل عمود:")
    print(df_2019.isnull().sum())