import pandas as pd
import numpy as np
import os


title = "Sample E with QHY600"
notes = "test"

# PVs

folder_name_pv = "BL10:Det:Q1:TIFF1:FilePath"
file_name_pv = "BL10:Det:Q1:TIFF1:FileName"

# rotation stages
motor1_pv = "BL10:Mot:rot1"
motor2_pv = "BL10:Mot:rot2"
motor3_pv = "BL10:Mot:rot3"
motor4_pv = "BL10:Mot:rot4"
motor_pv = motor4_pv   # we are using this one right now

qhy_acquisition_pv = "BL10:Det:Q1:AcquireTime"
qhy_acquisition_time = 180   # s

qhy_acquire_pv = "BL10:Det:Q1:Acquire"

delay_before = 10  # s
delay_after = 20  # s

folder_path = "/SNSlocal/data/IPTS-33531/images/qhy600/ct_scans/November8_2024_PlantE/"
file_name = title.replace(" ", "_")

table_scan_file_name, ext = os.path.splitext(file_name)
table_scan_file_name += ".csv"

golden_ratio_file = f"golden_ratio_360degrees_500projections.csv"

# No editing after this line

df = pd.read_csv(golden_ratio_file)
list_golden_ratio_angles = np.array(df['angles'])

# first row
table = [["Title", folder_name_pv, file_name_pv, motor_pv, "Delay", qhy_acquisition_pv, qhy_acquire_pv, "Delay"]]

for _angle in list_golden_ratio_angles:
    _str_angle = f"{_angle:03.2f}"
    _first_part, _second_part = _str_angle.split(".")
    _new_str_angle = f"{int(_first_part):03d}_{int(_second_part):03d}"
    _row = [f"{title}", f"{folder_path}", f"{file_name}_{_new_str_angle}", float(f"{_angle}"), delay_before, qhy_acquisition_time, 1, delay_after]
    table.append(_row)

# export table scan csv file
df_out = pd.DataFrame(table)
df_out.to_csv(table_scan_file_name, index=False, header=False)

print(f"{table_scan_file_name}")