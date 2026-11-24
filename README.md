# 🚲 Cyclistic Bike-Share Analysis (2019)

![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Tools](https://img.shields.io/badge/Tools-Python%20%7C%20Tableau%20%7C%20Excel-blue)

An end-to-end data analytics and visualization project analyzing over **3.81 million** bike-share trips from Cyclistic's 2019 historical dataset (`Q1`–`Q4`) to uncover behavioral differences between annual members (`Subscriber`) and casual riders (`Customer`).

**Author:** Mohamed Moussa  
**Date:** November 2026

---

## 📌 Project Overview

Converting casual riders into annual subscribers is a key growth driver for bike-share programs. This project cleans, validates, and analyzes 2019 trip data to provide actionable insights into weekly riding habits, trip durations, seasonal trends, and top station hotspots across Chicago.

---

## 📊 Key Insights & Visualizations

### 1. Rider Volume & Weekly Usage Patterns
* **Overall Distribution:** Annual `Subscribers` accounted for **76.9%** of total cleaned rides (`2,937,360` trips), while casual `Customers` generated **23.1%** (`880,631` trips).
* **Weekday Commuters vs. Weekend Leisure:** `Subscribers` maintained high, steady ride volumes from Monday to Friday, whereas `Customers` peaked significantly on **Saturdays and Sundays**.

### 2. Trip Duration & Segmentation
* **Short Commutes vs. Extended Rides:** **71.86%** of `Subscriber` trips lasted under 15 minutes (with a daily median of ~9.5–10.7 minutes).
* **Longer Casual Trips:** `Customers` took noticeably longer rides across the `15–30 min` (34.61%), `30–60 min` (24.49%), and `60+ min` (16.52%) segments.

### 3. Seasonal Trends & Geographic Hotspots
* **Summer Surge:** Both rider segments climbed steadily from spring into summer, peaking in **July and August** before tapering off in autumn and winter.
* **Station Concentration:** `Customer` trips clustered around waterfront and recreational landmarks (e.g., *Streeter Dr & Grand Ave*, *Lake Shore Dr & Monroe St*, *Millennium Park*), while `Subscriber` trips centered near downtown business and transit hubs (e.g., *Canal St & Adams St*, *Clinton St & Madison St*).

### 4. Interactive Tableau Dashboard
* Connects weekly patterns, seasonal trends, duration segments, and top starting stations in one unified view.
* **Live Dashboard:** [Cyclistic Bike-Share 2019: Subscriber vs. Customer Behavior](https://public.tableau.com/views/CyclisticBike-Share2019Subscribervs_CustomerBehavior_/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

---

## 🎯 Key Takeaways & Next Steps

* **Weekend & Leisure-Focused Promotions:** Introduce targeted annual membership offers triggered after weekend rides or near high-traffic waterfront and park stations.
* **Pre-Peak Seasonal Campaigns:** Launch digital and in-app campaigns in late spring (May–June) ahead of the July–August summer peak to convert repeat casual riders.
* **Future Work:** Incorporate weather data and multi-year comparisons (2019 vs. 2020+) to evaluate post-2019 shifts in rider behavior.

---

## 📁 Repository Structure

* `step1_inspect_merge.py` — Inspects quarterly schemas, aligns `Q2` headers, and merges `Q1`–`Q4` raw CSV files.
* `step2_clean_transform.py` — Removes invalid durations, validates `3,817,991` trips, and engineers time/date features.
* `step3_analyze.py` — Generates aggregated summaries by user type, day of week, month, and hour.
* `step4_extra_summaries.py` — Extracts top 10 starting stations per user type and trip duration buckets.
* `summary_*.csv` — Aggregated summary datasets powering the Tableau Public dashboard.
* `README.md` — Full project documentation and key findings.
