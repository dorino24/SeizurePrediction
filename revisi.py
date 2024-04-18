import matplotlib.pyplot as plt
import numpy as np
import function as fn 
import time

# import file
# 1
# file_paths = [
#     "chb01/chb01_01.edf",
#     "chb01/chb01_02.edf",
#     "chb01/chb01_03.edf",
#     "chb01/chb01_04.edf",
#     "chb01/chb01_05.edf",
#     "chb01/chb01_06.edf",
#     "chb01/chb01_07.edf",
#     "chb01/chb01_08.edf",
#     "chb01/chb01_09.edf",
#     "chb01/chb01_10.edf",
#     "chb01/chb01_11.edf",
#     "chb01/chb01_12.edf",
#     "chb01/chb01_13.edf",
#     "chb01/chb01_14.edf",
#     "chb01/chb01_15.edf",
#     "chb01/chb01_16.edf",
#     "chb01/chb01_17.edf",
#     "chb01/chb01_18.edf",
#     "chb01/chb01_19.edf",
#     "chb01/chb01_20.edf",
#     "chb01/chb01_21.edf",
#     "chb01/chb01_22.edf",
#     "chb01/chb01_23.edf",
#     "chb01/chb01_24.edf",
#     "chb01/chb01_25.edf",
#     "chb01/chb01_26.edf",
#     "chb01/chb01_27.edf",
#     "chb01/chb01_29.edf",
#     "chb01/chb01_30.edf",
#     "chb01/chb01_31.edf",
#     "chb01/chb01_32.edf",
#     "chb01/chb01_33.edf",
#     "chb01/chb01_34.edf",
#     "chb01/chb01_36.edf",
#     "chb01/chb01_37.edf",
#     "chb01/chb01_38.edf",
#     "chb01/chb01_39.edf",
#     "chb01/chb01_40.edf",
#     "chb01/chb01_41.edf",
#     "chb01/chb01_42.edf",
#     "chb01/chb01_43.edf",
#     "chb01/chb01_46.edf",
#     ]

# file_paths=[
#   "chb01/chb01_01.edf",
#   "chb01/chb01_02.edf",
#   "chb01/chb01_03.edf",
#   "chb01/chb01_04.edf",
# #   "chb02/chb02_16+.edf"
# #   "chb02/chb02_01.edf",
# #   "chb02/chb02_02.edf",
# ]

# 2
# file_paths = [
#     "chb02/chb02_01.edf",
#     "chb02/chb02_02.edf",
#     "chb02/chb02_03.edf",
#     "chb02/chb02_04.edf",
#     "chb02/chb02_05.edf",
#     "chb02/chb02_06.edf",
#     "chb02/chb02_07.edf",
#     "chb02/chb02_08.edf",
#     "chb02/chb02_09.edf",
#     "chb02/chb02_10.edf",
#     "chb02/chb02_11.edf",
#     "chb02/chb02_12.edf",
#     "chb02/chb02_13.edf",
#     "chb02/chb02_14.edf",
#     "chb02/chb02_15.edf",
#     "chb02/chb02_16.edf",
#     "chb02/chb02_16+.edf",
#     "chb02/chb02_17.edf",
#     "chb02/chb02_18.edf",
#     "chb02/chb02_19.edf",
#     "chb02/chb02_20.edf",
#     "chb02/chb02_21.edf",
#     "chb02/chb02_22.edf",
#     "chb02/chb02_23.edf",
#     "chb02/chb02_24.edf",
#     "chb02/chb02_25.edf",
#     "chb02/chb02_26.edf",
#     "chb02/chb02_27.edf",
#     "chb02/chb02_28.edf",
#     "chb02/chb02_29.edf",
#     "chb02/chb02_30.edf",
#     "chb02/chb02_31.edf",
#     "chb02/chb02_32.edf",
#     "chb02/chb02_33.edf",
#     "chb02/chb02_34.edf",
#     "chb02/chb02_35.edf"
#     ]

# 3
# file_paths = [
#     "chb03/chb03_01.edf",
#     "chb03/chb03_02.edf",
#     "chb03/chb03_03.edf",
#     "chb03/chb03_04.edf",
#     "chb03/chb03_05.edf",
#     "chb03/chb03_06.edf",
#     "chb03/chb03_07.edf",
#     "chb03/chb03_08.edf",
#     "chb03/chb03_09.edf",
#     "chb03/chb03_10.edf",
#     "chb03/chb03_11.edf",
#     "chb03/chb03_12.edf",
#     "chb03/chb03_13.edf",
#     "chb03/chb03_14.edf",
#     "chb03/chb03_15.edf",
#     "chb03/chb03_16.edf",
#     "chb03/chb03_17.edf",
#     "chb03/chb03_18.edf",
#     "chb03/chb03_19.edf",
#     "chb03/chb03_20.edf",
#     "chb03/chb03_21.edf",
#     "chb03/chb03_22.edf",
#     "chb03/chb03_23.edf",
#     "chb03/chb03_24.edf",
#     "chb03/chb03_25.edf",
#     "chb03/chb03_26.edf",
#     "chb03/chb03_27.edf",
#     "chb03/chb03_28.edf",
#     "chb03/chb03_29.edf",
#     "chb03/chb03_30.edf",
#     "chb03/chb03_31.edf",
#     "chb03/chb03_32.edf",
#     "chb03/chb03_33.edf",
#     "chb03/chb03_34.edf",
#     "chb03/chb03_35.edf",
#     "chb03/chb03_36.edf",
#     "chb03/chb03_37.edf",
#     "chb03/chb03_38.edf"]

# 5
# file_paths = [
#     "chb05/chb05_01.edf", 
#     "chb05/chb05_02.edf",
#     "chb05/chb05_03.edf",
#     "chb05/chb05_04.edf",
#     "chb05/chb05_05.edf",
#     "chb05/chb05_06.edf",
#     "chb05/chb05_07.edf",
#     "chb05/chb05_08.edf",
#     "chb05/chb05_09.edf",
#     "chb05/chb05_10.edf",
#     "chb05/chb05_11.edf",
#     "chb05/chb05_12.edf",
#     "chb05/chb05_13.edf",
#     "chb05/chb05_14.edf",
#     "chb05/chb05_15.edf",
#     "chb05/chb05_16.edf",
#     "chb05/chb05_17.edf",
#     "chb05/chb05_18.edf",
#     "chb05/chb05_19.edf",
#     "chb05/chb05_20.edf",
#     "chb05/chb05_21.edf",
#     "chb05/chb05_22.edf",
#     "chb05/chb05_23.edf",
#     "chb05/chb05_24.edf",
#     "chb05/chb05_25.edf",
#     "chb05/chb05_26.edf",
#     "chb05/chb05_27.edf",
#     "chb05/chb05_28.edf",
#     "chb05/chb05_29.edf",
#     "chb05/chb05_30.edf",
#     "chb05/chb05_31.edf",
#     "chb05/chb05_32.edf",
#     "chb05/chb05_33.edf",
#     "chb05/chb05_34.edf",
#     "chb05/chb05_35.edf",
#     "chb05/chb05_36.edf",
#     "chb05/chb05_37.edf",
#     "chb05/chb05_38.edf",
#     "chb05/chb05_39.edf"]

# 6
file_paths = [
    "chb06/chb06_01.edf",
    "chb06/chb06_02.edf",
    "chb06/chb06_03.edf",
    "chb06/chb06_04.edf",
    "chb06/chb06_05.edf",
    "chb06/chb06_06.edf",
    "chb06/chb06_07.edf",
    "chb06/chb06_08.edf",
    "chb06/chb06_09.edf",
    "chb06/chb06_10.edf",
    "chb06/chb06_12.edf",
    "chb06/chb06_13.edf",
    "chb06/chb06_14.edf",
    "chb06/chb06_15.edf",
    "chb06/chb06_16.edf",
    "chb06/chb06_17.edf",
    "chb06/chb06_18.edf",
    "chb06/chb06_24.edf"
    ]

# 12
# file_paths = [
#     "chb012/chb012_chb012_06.edf",
#     "chb012/chb012_chb012_08.edf",
#     "chb012/chb012_chb012_09.edf",
#     "chb012/chb012_chb012_10.edf",
#     "chb012/chb012_chb012_11.edf",
#     "chb012/chb012_chb012_19.edf",
#     "chb012/chb012_chb012_20.edf",
#     "chb012/chb012_chb012_21.edf",
#     "chb012/chb012_chb012_23.edf",
#     "chb012/chb012_chb012_24.edf",
#     "chb012/chb012_chb012_27.edf",
#     "chb012/chb012_chb012_28.edf",
#     "chb012/chb012_chb012_29.edf",
#     "chb012/chb012_chb012_32.edf",
#     "chb012/chb012_chb012_33.edf",
#     "chb012/chb012_chb012_34.edf",
#     "chb012/chb012_chb012_35.edf",
#     "chb012/chb012_chb012_36.edf",
#     "chb012/chb012_chb012_37.edf",
#     "chb012/chb012_chb012_38.edf",
#     "chb012/chb012_chb012_39.edf",
#     "chb012/chb012_chb012_40.edf",
#     "chb012/chb012_chb012_41.edf",
#     "chb012/chb012_chb012_42.edf"]

# 13
# file_paths = [
#     "chb013/chb013_chb013_02.edf",
#     "chb013/chb013_chb013_03.edf",
#     "chb013/chb013_chb013_04.edf",
#     "chb013/chb013_chb013_05.edf",
#     "chb013/chb013_chb013_06.edf",
#     "chb013/chb013_chb013_07.edf",
#     "chb013/chb013_chb013_08.edf",
#     "chb013/chb013_chb013_09.edf",
#     "chb013/chb013_chb013_10.edf",
#     "chb013/chb013_chb013_11.edf",
#     "chb013/chb013_chb013_12.edf",
#     "chb013/chb013_chb013_13.edf",
#     "chb013/chb013_chb013_14.edf",
#     "chb013/chb013_chb013_15.edf",
#     "chb013/chb013_chb013_16.edf",
#     "chb013/chb013_chb013_18.edf",
#     "chb013/chb013_chb013_19.edf",
#     "chb013/chb013_chb013_21.edf",
#     "chb013/chb013_chb013_22.edf",
#     "chb013/chb013_chb013_24.edf",
#     "chb013/chb013_chb013_30.edf",
#     "chb013/chb013_chb013_36.edf",
#     "chb013/chb013_chb013_37.edf",
#     "chb013/chb013_chb013_38.edf",
#     "chb013/chb013_chb013_39.edf",
#     "chb013/chb013_chb013_40.edf",
#     "chb013/chb013_chb013_47.edf",
#     "chb013/chb013_chb013_55.edf",
#     "chb013/chb013_chb013_56.edf",
#     "chb013/chb013_chb013_58.edf",
#     "chb013/chb013_chb013_59.edf",
#     "chb013/chb013_chb013_60.edf",
#     "chb013/chb013_chb013_62.edf"]

# 14
# file_paths = [
#     "chb014/chb014_chb014_01.edf",
#     "chb014/chb014_chb014_02.edf",
#     "chb014/chb014_chb014_03.edf",
#     "chb014/chb014_chb014_04.edf",
#     "chb014/chb014_chb014_06.edf",
#     "chb014/chb014_chb014_07.edf",
#     "chb014/chb014_chb014_11.edf",
#     "chb014/chb014_chb014_12.edf",
#     "chb014/chb014_chb014_13.edf",
#     "chb014/chb014_chb014_14.edf",
#     "chb014/chb014_chb014_16.edf",
#     "chb014/chb014_chb014_17.edf",
#     "chb014/chb014_chb014_18.edf",
#     "chb014/chb014_chb014_19.edf",
#     "chb014/chb014_chb014_20.edf",
#     "chb014/chb014_chb014_22.edf",
#     "chb014/chb014_chb014_24.edf",
#     "chb014/chb014_chb014_25.edf",
#     "chb014/chb014_chb014_26.edf",
#     "chb014/chb014_chb014_27.edf",
#     "chb014/chb014_chb014_29.edf",
#     "chb014/chb014_chb014_30.edf",
#     "chb014/chb014_chb014_32.edf",
#     "chb014/chb014_chb014_37.edf",
#     "chb014/chb014_chb014_39.edf",
#     "chb014/chb014_chb014_42.edf"]

# 15
# file_paths = [
#     "chb015/chb015_chb015_01.edf",
#     "chb015/chb015_chb015_02.edf",
#     "chb015/chb015_chb015_03.edf",
#     "chb015/chb015_chb015_04.edf",
#     "chb015/chb015_chb015_05.edf",
#     "chb015/chb015_chb015_06.edf",
#     "chb015/chb015_chb015_07.edf",
#     "chb015/chb015_chb015_08.edf",
#     "chb015/chb015_chb015_09.edf",
#     "chb015/chb015_chb015_10.edf",
#     "chb015/chb015_chb015_11.edf",
#     "chb015/chb015_chb015_12.edf",
#     "chb015/chb015_chb015_13.edf",
#     "chb015/chb015_chb015_14.edf",
#     "chb015/chb015_chb015_15.edf",
#     "chb015/chb015_chb015_16.edf",
#     "chb015/chb015_chb015_17.edf",
#     "chb015/chb015_chb015_19.edf",
#     "chb015/chb015_chb015_20.edf",
#     "chb015/chb015_chb015_22.edf",
#     "chb015/chb015_chb015_26.edf",
#     "chb015/chb015_chb015_28.edf",
#     "chb015/chb015_chb015_29.edf",
#     "chb015/chb015_chb015_30.edf",
#     "chb015/chb015_chb015_31.edf",
#     "chb015/chb015_chb015_32.edf",
#     "chb015/chb015_chb015_33.edf",
#     "chb015/chb015_chb015_35.edf",
#     "chb015/chb015_chb015_37.edf",
#     "chb015/chb015_chb015_40.edf",
#     "chb015/chb015_chb015_45.edf",
#     "chb015/chb015_chb015_46.edf",
#     "chb015/chb015_chb015_49.edf",
#     "chb015/chb015_chb015_10.edf",
#     "chb015/chb015_chb015_51.edf",
#     "chb015/chb015_chb015_52.edf",
#     "chb015/chb015_chb015_54.edf",
#     "chb015/chb015_chb015_61.edf",
#     "chb015/chb015_chb015_62.edf",
#     "chb015/chb015_chb015_63.edf"
# ]

# 18
# file_paths = [
#     "chb18/chb18_chb18_01.edf",
#     "chb18/chb18_chb18_02.edf",
#     "chb18/chb18_chb18_03.edf",
#     "chb18/chb18_chb18_04.edf",
#     "chb18/chb18_chb18_05.edf",
#     "chb18/chb18_chb18_06.edf",
#     "chb18/chb18_chb18_07.edf",
#     "chb18/chb18_chb18_08.edf",
#     "chb18/chb18_chb18_09.edf",
#     "chb18/chb18_chb18_10.edf",
#     "chb18/chb18_chb18_11.edf",
#     "chb18/chb18_chb18_12.edf",
#     "chb18/chb18_chb18_13.edf",
#     "chb18/chb18_chb18_14.edf",
#     "chb18/chb18_chb18_15.edf",
#     "chb18/chb18_chb18_16.edf",
#     "chb18/chb18_chb18_17.edf",
#     "chb18/chb18_chb18_18.edf",
#     "chb18/chb18_chb18_19.edf",
#     "chb18/chb18_chb18_20.edf",
#     "chb18/chb18_chb18_21.edf",
#     "chb18/chb18_chb18_22.edf",
#     "chb18/chb18_chb18_23.edf",
#     "chb18/chb18_chb18_24.edf",
#     "chb18/chb18_chb18_25.edf",
#     "chb18/chb18_chb18_26.edf",
#     "chb18/chb18_chb18_27.edf",
#     "chb18/chb18_chb18_28.edf",
#     "chb18/chb18_chb18_29.edf",
#     "chb18/chb18_chb18_30.edf",
#     "chb18/chb18_chb18_31.edf",
#     "chb18/chb18_chb18_32.edf",
#     "chb18/chb18_chb18_33.edf",
#     "chb18/chb18_chb18_34.edf",
#     "chb18/chb18_chb18_35.edf",
#     "chb18/chb18_chb18_36.edf",
# ]

# 20
# file_paths = [
#     "chb20/chb20_chb20_01.edf",
#     "chb20/chb20_chb20_02.edf",
#     "chb20/chb20_chb20_03.edf",
#     "chb20/chb20_chb20_04.edf",
#     "chb20/chb20_chb20_05.edf",
#     "chb20/chb20_chb20_06.edf",
#     "chb20/chb20_chb20_07.edf",
#     "chb20/chb20_chb20_08.edf",
#     "chb20/chb20_chb20_11.edf",
#     "chb20/chb20_chb20_12.edf",
#     "chb20/chb20_chb20_13.edf",
#     "chb20/chb20_chb20_14.edf",
#     "chb20/chb20_chb20_15.edf",
#     "chb20/chb20_chb20_16.edf",
#     "chb20/chb20_chb20_17.edf",
#     "chb20/chb20_chb20_21.edf",
#     "chb20/chb20_chb20_22.edf",
#     "chb20/chb20_chb20_23.edf",
#     "chb20/chb20_chb20_25.edf",
#     "chb20/chb20_chb20_26.edf",
#     "chb20/chb20_chb20_27.edf",
#     "chb20/chb20_chb20_28.edf",
#     "chb20/chb20_chb20_29.edf",
#     "chb20/chb20_chb20_30.edf",
#     "chb20/chb20_chb20_31.edf",
#     "chb20/chb20_chb20_34.edf",
#     "chb20/chb20_chb20_59.edf",
#     "chb20/chb20_chb20_60.edf",
#     "chb20/chb20_chb20_68.edf",
# ]

# 24
# file_paths = [
#     "chb24/chb24_chb24_01.edf",
#     "chb24/chb24_chb24_02.edf",
#     "chb24/chb24_chb24_03.edf",
#     "chb24/chb24_chb24_04.edf",
#     "chb24/chb24_chb24_05.edf",
#     "chb24/chb24_chb24_06.edf",
#     "chb24/chb24_chb24_07.edf",
#     "chb24/chb24_chb24_08.edf",
#     "chb24/chb24_chb24_09.edf",
#     "chb24/chb24_chb24_10.edf",
#     "chb24/chb24_chb24_11.edf",
#     "chb24/chb24_chb24_12.edf",
#     "chb24/chb24_chb24_13.edf",
#     "chb24/chb24_chb24_14.edf",
#     "chb24/chb24_chb24_15.edf",
#     "chb24/chb24_chb24_16.edf",
#     "chb24/chb24_chb24_17.edf",
#     "chb24/chb24_chb24_18.edf",
#     "chb24/chb24_chb24_19.edf",
#     "chb24/chb24_chb24_20.edf",
#     "chb24/chb24_chb24_21.edf",
#     "chb24/chb24_chb24_22.edf"
# ]


# file_paths = ["chb01/chb01_01.edf", "chb01/chb01_02.edf","chb01/chb01_03.edf","chb01/chb01_04.edf", "chb01/chb01_05.edf", ]
print('importing edf file...')
begining = time.time()
start = time.time()
all_signals = fn.import_edf(file_paths)
n_channels  = 23
sample_rate = 256


signals1, n_channels1,n_samples1,sample_rate1 = fn.single_import_edf('./chb01/chb01_03.edf')
signals2, n_channels2,n_samples2,sample_rate2 = fn.single_import_edf('./chb01/chb01_03.edf')
n_samples   = n_samples1

avg_signal = fn.avg_signal(all_signals,n_channels,n_samples)
avg_signal_reff = fn.avg_signal_reff(signals1,n_channels1,n_samples1)
avg_signal_reff2 = fn.avg_signal_reff(signals2,n_channels2,n_samples2)

# avg_signal = all_signals
# avg_signal_reff = signals1[0]
# time
t = np.arange(len(avg_signal)) / sample_rate /3600
# t = tr[int(100*sample_rate):int(1900*sample_rate)]
# t = np.arange(len(all_signals[0])) / sample_rate 



# normal baseline

normal_baseline_signal = avg_signal_reff[int(1000*sample_rate):int(1600*sample_rate)]
time_nb  = t[int(1000*sample_rate):int(1600*sample_rate)]
# normal_baseline_signal = avg_signal_reff2[int(2000*sample_rate):int(3000*sample_rate)]
# time_nb  = t[int(2000*sample_rate):int(3000*sample_rate)]

# preseizure baseline
# pre_baseline_signal = avg_signal_reff[int(100*sample_rate):int(1900*sample_rate)]
# time_pre  = t[int(100*sample_rate):int(1900*sample_rate)]
pre_baseline_signal = avg_signal_reff[int(2100*sample_rate):int(2700*sample_rate)]
time_pre  = t[int(2100*sample_rate):int(2700*sample_rate)]

end = time.time()
print("time to import edf file: ", end - start)

# preprocessing
print("preprocessing")
start = time.time()
filtered_signal = fn.filtering(avg_signal,sample_rate , lowcut=0.5, highcut=40.0)
filtered_signal_nb = fn.filtering(normal_baseline_signal,sample_rate , lowcut=0.5, highcut=40.0)
filtered_signal_pre = fn.filtering(pre_baseline_signal,sample_rate , lowcut=0.5, highcut=40.0)
end = time.time()
print("time to filter: ", end - start)

# feature_extraction
print("feature_extraction")
start = time.time()
segment_duration = 10
original_featureX = fn.feature_extraction(segment_duration,avg_signal,sample_rate)
filtered_featureX = fn.feature_extraction(segment_duration,filtered_signal,sample_rate)
nb_shannon = fn.feature_extraction(segment_duration,normal_baseline_signal,sample_rate)
nb_featureX = fn.feature_extraction(segment_duration,filtered_signal_nb,sample_rate)
pre_shannon = fn.feature_extraction(segment_duration,pre_baseline_signal,sample_rate)
pre_featureX = fn.feature_extraction(segment_duration,filtered_signal_pre,sample_rate)


# time feature
time_original = np.arange(0, len(original_featureX[0])) * segment_duration
time_filterd = np.arange(0, len(filtered_featureX[0])) * segment_duration
time_nb = np.arange(0, len(nb_featureX[0])) * segment_duration
time_pre = np.arange(0, len(pre_featureX[0])) * segment_duration
end = time.time()
print("time to feature extraction: ", end - start)

# clasification
print("classification")
start   = time.time()
prediction = []
pred_one = fn.classification(nb_shannon[0],pre_shannon[0],original_featureX[0])
prediction.append(pred_one)
for i in range(1,len(filtered_featureX)):
    pred_one = fn.classification(nb_featureX[i],pre_featureX[i],filtered_featureX[i])
    prediction.append(pred_one)
end = time.time()
print("time to classification: ", end - start)

print("epoching")
start = time.time()
epoch = []
for j in range(0,6):
    epoch1 = []
    for i in range(0,len(prediction[0])//60):
        epoch1.append(np.sum(prediction[j][i*60:(i+1)*60]))
    epoch.append(epoch1)
end = time.time()
print("time to epoching: ", end - start)

nilai_prediksi = []
for i in range(len(epoch[0])):
    sum = 0
    for j in range( len(epoch)):
        if epoch[j][i] > 50:
            sum += 1
    nilai_prediksi.append(sum)
ending = time.time()
print("total time: ", ending - begining)
print("plotting")

time_epoch = np.arange(1, len(epoch[0])+1) * 60 * 10 /3600
# print(time_epoch)
# time_epoch = np.arange(0, len(epoch[0])) * 60 * 10 / 3600

plt.figure('prediksi',figsize=(12,8))
plt.subplot(2,1,1) 
plt.plot(t,avg_signal)

# 1
# plt.axvline(x=15.1, color='g', linestyle='--')
# plt.axvline(x=3.4, color='g', linestyle='--')
# plt.axvline(x=14.30, color='g', linestyle='--')
# plt.axvline(x=15.17, color='g', linestyle='--') 
# plt.axvline(x=17.5, color='g', linestyle='--')
# plt.axvline(x=19.8, color='g', linestyle='--')
# plt.axvline(x=25.25, color='g', linestyle='--')

# 2
# plt.axvline(x=15, color='g', linestyle='--')
# plt.axvline(x=16, color='g', linestyle='--')
# plt.axvline(x=19.1, color='g', linestyle='--')

# 3
# #plt.axvline(x=0.1, color='g', linestyle='--',linewidth=2)
# plt.axvline(x=1.2, color='g', linestyle='--',linewidth=2)
# plt.axvline(x=2.1, color='g', linestyle='--',linewidth=2)
# plt.axvline(x=3.58, color='g', linestyle='--',linewidth=2)
# plt.axvline(x=33.55, color='g', linestyle='--',linewidth=2)
# plt.axvline(x=34.7, color='g', linestyle='--',linewidth=2)
# plt.axvline(x=35.47, color='g', linestyle='--',linewidth=2)

#5
# plt.axvline(x=5.1, color='g', linestyle='--',linewidth=2)
# plt.axvline(x=12.27, color='g', linestyle='--',linewidth=2)
# plt.axvline(x=15.64, color='g', linestyle='--',linewidth=2)
# plt.axvline(x=16.68, color='g', linestyle='--',linewidth=2)
# plt.axvline(x=21.65, color='g', linestyle='--',linewidth=2)

#6
plt.axvline(x=5.1, color='g', linestyle='--',linewidth=2)
plt.axvline(x=12.27, color='g', linestyle='--',linewidth=2)
plt.axvline(x=15.64, color='g', linestyle='--',linewidth=2)
plt.axvline(x=16.68, color='g', linestyle='--',linewidth=2)
plt.axvline(x=21.65, color='g', linestyle='--',linewidth=2)

plt.subplot(2,1,2) 
plt.plot(time_epoch,nilai_prediksi)
plt.axhline(y=4, color='grey', linestyle='--', linewidth=1)

# 1
# plt.axvline(x=2.8, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.4, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=14.30, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=15.17, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=17.5, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=19.8, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=25.25, color='r', linestyle='--',linewidth=2)

# # 2
# plt.axvline(x=14, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=16, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=18.1, color='r', linestyle='--',linewidth=2)

# 3
# plt.axvline(x=0.1, color='g', linestyle='--',linewidth=2)
# plt.axvline(x=1.2, color='g', linestyle='--',linewidth=2)
# plt.axvline(x=2.1, color='g', linestyle='--',linewidth=2)
# plt.axvline(x=3.58, color='g', linestyle='--',linewidth=2)
# plt.axvline(x=33.55, color='g', linestyle='--',linewidth=2)
# plt.axvline(x=34.7, color='g', linestyle='--',linewidth=2)
# plt.axvline(x=35.47, color='g', linestyle='--',linewidth=2)

# # 5
# plt.axvline(x=5.1, color='g', linestyle='--',linewidth=2)
# plt.axvline(x=12.27, color='g', linestyle='--',linewidth=2)
# plt.axvline(x=15.64, color='g', linestyle='--',linewidth=2)
# plt.axvline(x=16.68, color='g', linestyle='--',linewidth=2)
# plt.axvline(x=21.65, color='g', linestyle='--',linewidth=2)

# 6
plt.axvline(x=5.1, color='g', linestyle='--',linewidth=2)
plt.axvline(x=12.27, color='g', linestyle='--',linewidth=2)
plt.axvline(x=15.64, color='g', linestyle='--',linewidth=2)
plt.axvline(x=16.68, color='g', linestyle='--',linewidth=2)
plt.axvline(x=21.65, color='g', linestyle='--',linewidth=2)

plt.figure('epoch',figsize=(12,8))
plt.subplot(7,1,1) 
plt.plot(t,avg_signal)

plt.subplot(7,1,2) 
plt.plot(time_epoch,epoch[0])
plt.axhline(y=50, color='r', linestyle='--', label='Horizontal Line at y=0.5')
plt.subplot(7,1,3) 
plt.plot(time_epoch,epoch[1])
plt.axhline(y=50, color='r', linestyle='--', label='Horizontal Line at y=0.5')
plt.subplot(7,1,4) 
plt.plot(time_epoch,epoch[2])
plt.axhline(y=50, color='r', linestyle='--', label='Horizontal Line at y=0.5')
plt.subplot(7,1,5) 
plt.plot(time_epoch,epoch[3])
plt.axhline(y=50, color='r', linestyle='--', label='Horizontal Line at y=0.5')
plt.subplot(7,1,6) 
plt.plot(time_epoch,epoch[4])
plt.axhline(y=50, color='r', linestyle='--', label='Horizontal Line at y=0.5')
plt.subplot(7,1,7) 
plt.plot(time_epoch,epoch[5])
plt.axhline(y=50, color='r', linestyle='--', label='Horizontal Line at y=0.5')
plt.tight_layout()

plt.figure('filtered',figsize=(12,8))

plt.subplot(6,1,1)
plt.plot(time_original,original_featureX[0], label='Shannon Entropy', color='blue')
# plt.ylim(5,11)
plt.legend()
plt.subplot(6,1,2)
plt.plot(time_original,filtered_featureX[1], label='Variance', color='green')
plt.legend()
plt.subplot(6,1,3)
plt.plot(time_original,filtered_featureX[2], label='Standard Deviation', color='red')
plt.legend()
plt.subplot(6,1,4)
plt.plot(time_original,filtered_featureX[3], label='Sum of Squares', color='brown')
plt.legend()
plt.subplot(6,1,5)
plt.plot(time_original,filtered_featureX[4], label='Min', color='purple')
plt.legend()
plt.subplot(6,1,6)
plt.plot(time_original,filtered_featureX[5], label='Max', color='orange')
plt.legend()

# plt.figure('nb',figsize=(12,8))
# plt.subplot(6,1,1)
# plt.plot(time_nb,nb_shannon[0], label='Shannon Entropy', color='blue')
# # plt.ylim(5,11)
# plt.legend()
# plt.subplot(6,1,2)
# plt.plot(time_nb,nb_featureX[1], label='Variance', color='green')
# plt.legend()
# plt.subplot(6,1,3)
# plt.plot(time_nb,nb_featureX[2], label='Standard Deviation', color='red')
# plt.legend()
# plt.subplot(6,1,4)
# plt.plot(time_nb,nb_featureX[3], label='Sum of Squares', color='brown')
# plt.legend()
# plt.subplot(6,1,5)
# plt.plot(time_nb,nb_featureX[4], label='Min', color='purple')
# plt.legend()
# plt.subplot(6,1,6)
# plt.plot(time_nb,nb_featureX[5], label='Max', color='orange')
# plt.legend()

# plt.figure('pre',figsize=(12,8))
# plt.subplot(6,1,1)
# plt.plot(time_pre,pre_shannon[0], label='Shannon Entropy', color='blue')
# # plt.ylim(5,11)
# plt.legend()
# plt.subplot(6,1,2)
# plt.plot(time_pre,pre_featureX[1], label='Variance', color='green')
# plt.legend()
# plt.subplot(6,1,3)
# plt.plot(time_pre,pre_featureX[2], label='Standard Deviation', color='red')
# plt.legend()
# plt.subplot(6,1,4)
# plt.plot(time_pre,pre_featureX[3], label='Sum of Squares', color='brown')
# plt.legend()
# plt.subplot(6,1,5)
# plt.plot(time_pre,pre_featureX[4], label='Min', color='purple')
# plt.legend()
# plt.subplot(6,1,6)
# plt.plot(time_pre,pre_featureX[5], label='Max', color='orange')
# plt.legend()

plt.show()