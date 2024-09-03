import matplotlib.pyplot as plt
import numpy as np
import function as fn 
import time

# import file
# 1
file_paths = [
    "chb01/chb01_01.edf",
    "chb01/chb01_02.edf",
    "chb01/chb01_03.edf",
    "chb01/chb01_04.edf",
    "chb01/chb01_05.edf",
    "chb01/chb01_06.edf",
    "chb01/chb01_07.edf",
    "chb01/chb01_08.edf",
    "chb01/chb01_09.edf",
    "chb01/chb01_10.edf",
    "chb01/chb01_11.edf",
    "chb01/chb01_12.edf",
    "chb01/chb01_13.edf",
    "chb01/chb01_14.edf",
    "chb01/chb01_15.edf",
    "chb01/chb01_16.edf",
    "chb01/chb01_17.edf",
    "chb01/chb01_18.edf",
    "chb01/chb01_19.edf",
    "chb01/chb01_20.edf",
    "chb01/chb01_21.edf",
    "chb01/chb01_22.edf",
    "chb01/chb01_23.edf",
    "chb01/chb01_24.edf",
    "chb01/chb01_25.edf",
    "chb01/chb01_26.edf",
    "chb01/chb01_27.edf",
    "chb01/chb01_29.edf",
    "chb01/chb01_30.edf",
    "chb01/chb01_31.edf",
    "chb01/chb01_32.edf",
    "chb01/chb01_33.edf",
    "chb01/chb01_34.edf",
    "chb01/chb01_36.edf",
    "chb01/chb01_37.edf",
    "chb01/chb01_38.edf",
    "chb01/chb01_39.edf",
    "chb01/chb01_40.edf",
    "chb01/chb01_41.edf",
    "chb01/chb01_42.edf",
    "chb01/chb01_43.edf",
    "chb01/chb01_46.edf",
    ]

# 2
# file_paths = [
# #     # "chb02/chb02_01.edf",
# #     # "chb02/chb02_02.edf",
# #     # "chb02/chb02_03.edf",
# #     # "chb02/chb02_04.edf",
# #     # "chb02/chb02_05.edf",
# #     # "chb02/chb02_06.edf",
# #     # "chb02/chb02_07.edf",
# #     # "chb02/chb02_08.edf",
# #     # "chb02/chb02_09.edf",
# #     # "chb02/chb02_10.edf",
# #     # "chb02/chb02_11.edf",
# #     # "chb02/chb02_12.edf",
# #     # "chb02/chb02_13.edf",
#     # "chb02/chb02_14.edf",
#     "chb02/chb02_15.edf",
#     "chb02/chb02_16.edf",
#     "chb02/chb02_16+.edf",
#     "chb02/chb02_17.edf",
#     "chb02/chb02_18.edf",
#     "chb02/chb02_19.edf",
#     "chb02/chb02_20.edf",
#     "chb02/chb02_21.edf",
#     "chb02/chb02_22.edf",
#     # "chb02/chb02_23.edf",
#     # "chb02/chb02_24.edf",
#     # "chb02/chb02_25.edf",
#     # "chb02/chb02_26.edf",
#     # "chb02/chb02_27.edf",
#     # "chb02/chb02_28.edf",
#     # "chb02/chb02_29.edf",
#     # "chb02/chb02_30.edf",
#     # "chb02/chb02_31.edf",
#     # "chb02/chb02_32.edf",
#     # "chb02/chb02_33.edf",
#     # "chb02/chb02_34.edf",
#     # "chb02/chb02_35.edf"
#     ]

# 3
# file_paths = [
#     "chb03/chb03_01.edf",
#     "chb03/chb03_02.edf",
#     "chb03/chb03_03.edf",
#     "chb03/chb03_04.edf",
#     "chb03/chb03_05.edf",
#     "chb03/chb03_06.edf",
#     # "chb03/chb03_07.edf",
#     # "chb03/chb03_08.edf",
#     # "chb03/chb03_09.edf",
#     # "chb03/chb03_10.edf",
#     # "chb03/chb03_11.edf",
#     # "chb03/chb03_12.edf",
#     # "chb03/chb03_13.edf",
#     # "chb03/chb03_14.edf",
#     # "chb03/chb03_15.edf",
#     # "chb03/chb03_16.edf",
#     # "chb03/chb03_17.edf",
#     # "chb03/chb03_18.edf",
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
#     # "chb03/chb03_30.edf",
#     # "chb03/chb03_31.edf",
#     # "chb03/chb03_32.edf",
#     # "chb03/chb03_33.edf",
#     # "chb03/chb03_34.edf",
#     # "chb03/chb03_35.edf",
#     # "chb03/chb03_36.edf",
#     # "chb03/chb03_37.edf",
#     # "chb03/chb03_38.edf"
#     ]

# 5
# file_paths = [
#     # "chb05/chb05_01.edf", 
#     # "chb05/chb05_02.edf",
#     # "chb05/chb05_03.edf",
#     # "chb05/chb05_04.edf",
#     # "chb05/chb05_05.edf",
#     # "chb05/chb05_06.edf",
#     # "chb05/chb05_07.edf",
#     # "chb05/chb05_08.edf",
#     # "chb05/chb05_09.edf",
#     # "chb05/chb05_10.edf",
#     # "chb05/chb05_11.edf",
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
#     # "chb05/chb05_28.edf",
#     # "chb05/chb05_29.edf",
#     # "chb05/chb05_30.edf",
#     # "chb05/chb05_31.edf",
#     # "chb05/chb05_32.edf",
#     # "chb05/chb05_33.edf",
#     # "chb05/chb05_34.edf",
#     # "chb05/chb05_35.edf",
#     # "chb05/chb05_36.edf",
#     # "chb05/chb05_37.edf",
#     # "chb05/chb05_38.edf",
#     # "chb05/chb05_39.edf"
#     ]

# 13
# file_paths = [
# #     #16:43:14 - 7:44:48
# #     # "chb13/chb13_chb13_02.edf",
# #     # "chb13/chb13_chb13_03.edf",
# #     # "chb13/chb13_chb13_04.edf",
# #     # "chb13/chb13_chb13_05.edf",
# #     # "chb13/chb13_chb13_06.edf",
# #     # "chb13/chb13_chb13_07.edf",
# #     # "chb13/chb13_chb13_08.edf",
# #     # "chb13/chb13_chb13_09.edf",
# #     # "chb13/chb13_chb13_10.edf",
# #     # "chb13/chb13_chb13_11.edf",
# #     # "chb13/chb13_chb13_12.edf",
# #     # "chb13/chb13_chb13_13.edf",
# #     # "chb13/chb13_chb13_14.edf",
# #     # "chb13/chb13_chb13_15.edf",
# #     # "chb13/chb13_chb13_16.edf",
    
# #     # 08:14:20 - 15:15:19
#     "chb13/chb13_chb13_18.edf",
#     "chb13/chb13_chb13_19.edf",
#     "chb13/chb13_chb13_21.edf",
#     "chb13/chb13_chb13_22.edf",
#     "chb13/chb13_chb13_24.edf",
    
# #     # 20:16:00 - 21:16:00 
# #     # "chb13/chb13_chb13_30.edf",
    
# #     #  02:17:23 - 7:17:50
# #     # "chb13/chb13_chb13_36.edf",
# #     # "chb13/chb13_chb13_37.edf",
# #     # "chb13/chb13_chb13_38.edf",
# #     # "chb13/chb13_chb13_39.edf",
# #     # "chb13/chb13_chb13_40.edf",
    
# #     # 13:18:37 - 14:18:37
# #     # "chb13/chb13_chb13_47.edf",
    
# #     #  21:20:07 - 3:20:41
# #     # "chb13/chb13_chb13_55.edf",
# #     # "chb13/chb13_chb13_56.edf",
# #     # "chb13/chb13_chb13_58.edf",
# #     # "chb13/chb13_chb13_59.edf",
# #     # "chb13/chb13_chb13_60.edf",
    
# #     # 04:20:55 - 5:20:55
# #     # "chb13/chb13_chb13_62.edf"
# ]

# 18
# file_paths = [
#     # "chb18/chb18_chb18_01.edf",
#     # "chb18/chb18_chb18_02.edf",
#     # "chb18/chb18_chb18_03.edf",
#     # "chb18/chb18_chb18_04.edf",
#     # "chb18/chb18_chb18_05.edf",
#     # "chb18/chb18_chb18_06.edf",
#     # "chb18/chb18_chb18_07.edf",
#     # "chb18/chb18_chb18_08.edf",
#     # "chb18/chb18_chb18_09.edf",
#     # "chb18/chb18_chb18_10.edf",
#     # "chb18/chb18_chb18_11.edf",
#     # "chb18/chb18_chb18_12.edf",
#     # "chb18/chb18_chb18_13.edf",
#     # "chb18/chb18_chb18_14.edf",
#     # "chb18/chb18_chb18_15.edf",
#     "chb18/chb18_chb18_16.edf",
#     "chb18/chb18_chb18_17.edf",
#     "chb18/chb18_chb18_18.edf",
#     "chb18/chb18_chb18_19.edf",
#     # "chb18/chb18_chb18_20.edf",
#     # "chb18/chb18_chb18_21.edf",
#     # "chb18/chb18_chb18_22.edf",
#     # "chb18/chb18_chb18_23.edf",   
#     # "chb18/chb18_chb18_24.edf",
#     # "chb18/chb18_chb18_25.edf",
#     # "chb18/chb18_chb18_26.edf",
#     # "chb18/chb18_chb18_27.edf",
#     # "chb18/chb18_chb18_28.edf",
#     "chb18/chb18_chb18_29.edf",
#     "chb18/chb18_chb18_30.edf",
#     "chb18/chb18_chb18_31.edf",
#     "chb18/chb18_chb18_32.edf",
#     # "chb18/chb18_chb18_33.edf",
#     # "chb18/chb18_chb18_34.edf",
#     "chb18/chb18_chb18_35.edf",
#     "chb18/chb18_chb18_36.edf",
# ]

# 20
# file_paths = [
#     # "chb20/chb20_chb20_01.edf",
#     # "chb20/chb20_chb20_02.edf",
#     # "chb20/chb20_chb20_03.edf",
#     # "chb20/chb20_chb20_04.edf",
#     # "chb20/chb20_chb20_05.edf",
#     # "chb20/chb20_chb20_06.edf",
#     # "chb20/chb20_chb20_07.edf",
#     # "chb20/chb20_chb20_08.edf",
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
#     # "chb20/chb20_chb20_28.edf",
#     # "chb20/chb20_chb20_29.edf",
#     # "chb20/chb20_chb20_30.edf",
#     # "chb20/chb20_chb20_31.edf",
#     # "chb20/chb20_chb20_34.edf",
#     # "chb20/chb20_chb20_59.edf",
#     # "chb20/chb20_chb20_60.edf",
#     "chb20/chb20_chb20_68.edf",
# ]

# 21
# file_paths =[
# #    'chb21/chb21_chb21_01.edf', 
# #    'chb21/chb21_chb21_02.edf', 
# #    'chb21/chb21_chb21_03.edf', 
# #    'chb21/chb21_chb21_04.edf', 
# #    'chb21/chb21_chb21_05.edf', 
# #    'chb21/chb21_chb21_06.edf', 
# #    'chb21/chb21_chb21_07.edf', 
# #    'chb21/chb21_chb21_08.edf', 
# #    'chb21/chb21_chb21_09.edf', 
# #    'chb21/chb21_chb21_10.edf', 
# #    'chb21/chb21_chb21_11.edf', 
# #    'chb21/chb21_chb21_12.edf', 
# #    'chb21/chb21_chb21_13.edf', 
# #    'chb21/chb21_chb21_14.edf', 
#    'chb21/chb21_chb21_15.edf', 
#    'chb21/chb21_chb21_16.edf', 
#    'chb21/chb21_chb21_17.edf', 
#    'chb21/chb21_chb21_18.edf', 
#    'chb21/chb21_chb21_19.edf', 
#    'chb21/chb21_chb21_20.edf', 
#    'chb21/chb21_chb21_21.edf', 
#    'chb21/chb21_chb21_22.edf', 
#    'chb21/chb21_chb21_23.edf', 
# #    'chb21/chb21_chb21_24.edf', 
# #    'chb21/chb21_chb21_25.edf', 
# #    'chb21/chb21_chb21_26.edf', 
# #    'chb21/chb21_chb21_27.edf', 
# #    'chb21/chb21_chb21_28.edf', 
# #    'chb21/chb21_chb21_29.edf', 
# #    'chb21/chb21_chb21_30.edf', 
# #    'chb21/chb21_chb21_31.edf', 
# #    'chb21/chb21_chb21_32.edf', 
# #    'chb21/chb21_chb21_33.edf' 
# ]

# 23
# file_paths =[
#     'chb23/chb23_chb23_06.edf',
#     'chb23/chb23_chb23_07.edf',
#     'chb23/chb23_chb23_08.edf',
#     'chb23/chb23_chb23_09.edf',
#     # 'chb23/chb23_chb23_10.edf',
# #     'chb23/chb23_chb23_16.edf',
# #     'chb23/chb23_chb23_17.edf',
# #     'chb23/chb23_chb23_19.edf',
# #     'chb23/chb23_chb23_20.edf',
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

file_nb = "chb01/chb01_03.edf"
start_nb =  1000
end_nb = 1600

# file_nb = "chb02/chb02_17.edf"
# start_nb =  828
# end_nb = 1188

# file_nb = "chb03/chb03_03.edf"
# start_nb =  1440
# end_nb = 1900

# file_nb = "chb05/chb05_19.edf"
# start_nb =  900
# end_nb = 1800

# file_nb = "chb13/chb13_chb13_21.edf"
# start_nb =  1330
# end_nb = 1512

# file_nb = "chb18/chb18_chb18_16.edf"
# start_nb =  3240
# end_nb = 3600

# file_nb = "chb20/chb20_chb20_11.edf"
# start_nb =  1080
# end_nb = 2160

# file_nb = "chb21/chb21_chb21_16.edf"
# start_nb =  1280
# end_nb = 1800

# file_nb = "chb23/chb23_chb23_09.edf"
# start_nb =  6768
# end_nb = 7056

# file_nb = "chb24/chb24_chb24_02.edf"
# start_nb =  2350
# end_nb = 2800

# PB

file_pb = "chb01/chb01_03.edf"
start_pb = 2100
end_pb = 2700

# file_pb = "chb02/chb02_19.edf"
# start_pb = 900
# end_pb = 1440

# file_pb = "chb03/chb03_04.edf"
# start_pb = 100
# end_pb = 700

# file_pb = "chb05/chb05_17.edf"
# start_pb = 900
# end_pb = 1800

# file_pb = "chb13/chb13_chb13_21.edf"
# start_pb = 180
# end_pb = 756

# file_pb = "chb18/chb18_chb18_35.edf"
# start_pb = 360
# end_pb = 1080

# file_pb = "chb20/chb20_chb20_11.edf"
# start_pb = 2700
# end_pb = 3500

# file_pb = "chb21/chb21_chb21_18.edf"
# start_pb = 540
# end_pb = 1440

# file_pb = "chb23/chb23_chb23_09.edf"
# start_pb = 7200
# end_pb = 7620

# file_pb = "chb24/chb24_chb24_01.edf"
# start_pb = 1800
# end_pb = 2350


print('importing edf file...')
begining = time.time()
start = time.time()
all_signals = fn.import_edf(file_paths)
sample_rate = 256

signals1, n_channels1,n_samples1,sample_rate1 = fn.single_import_edf(file_nb)
signals2, n_channels2,n_samples2,sample_rate2 = fn.single_import_edf(file_pb)

n_samples   = n_samples1

avg_signal = fn.avg_signal(all_signals)

avg_signal_reff = fn.avg_signal_reff(signals1,n_channels1,n_samples1)
avg_signal_reff2 = fn.avg_signal_reff(signals2,n_channels2,n_samples2)

# avg_signal = all_signals
# avg_signal_reff = signals1[0]
# time
# t = np.arange(len(avg_signal)) / sample_rate 
t = np.arange(len(avg_signal)) / sample_rate / 3600
# t = np.arange(len(all_signals[0])) / sample_rate 

# normal baseline
normal_baseline_signal = avg_signal_reff[int(start_nb*sample_rate):int(end_nb*sample_rate)]
time_nb  = t[int(start_nb*sample_rate):int(end_nb*sample_rate)]

# preseizure baseline
pre_baseline_signal = avg_signal_reff2[int(start_pb*sample_rate):int(end_pb*sample_rate)]
time_pre  = t[int(start_pb*sample_rate):int(end_pb*sample_rate)]

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
pre_featureX = fn.feature_extraction(segment_duration,filtered_signal_pre,sample_rate)

pre_shannon = fn.feature_extraction(segment_duration,pre_baseline_signal,sample_rate)


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
batas_epoch = 48
nilai_prediksi = []
for i in range(len(epoch[0])):
    sum = 0
    for j in range( len(epoch)):
        if epoch[j][i] >= batas_epoch:
            sum += 1
    nilai_prediksi.append(sum)
ending = time.time()
print("total time: ", ending - begining)
print("plotting")   


time_epoch = np.arange(1, len(epoch[0])+1) * 60 * 10 / 3600
# time_epoch = np.arange(1, len(epoch[0])+1) * 60 * 10  

plt.figure('prediksi 2',figsize=(12,8))
plt.subplot(2,1,1) 
plt.plot(t,avg_signal)
plt.xlabel('Waktu (detik)')

# 1
# plt.axvline(x=2.8, color='g', linestyle='--')
# plt.axvline(x=3.4, color='g', linestyle='--')
# plt.axvline(x=14.30, color='g', linestyle='--')
# plt.axvline(x=15.17, color='g', linestyle='--') 
# plt.axvline(x=17.5, color='g', linestyle='--')
# plt.axvline(x=19.8, color='g', linestyle='--')
# plt.axvline(x=25.60, color='g', linestyle='--')

# 2
plt.axvline(x=1.03, color='r', linestyle='--',linewidth=2)
plt.axvline(x=2.1, color='r', linestyle='--',linewidth=2)
plt.axvline(x=5.196, color='r', linestyle='--',linewidth=2)

# 3
# plt.axvline(x=0.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=1.2, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.61, color='r', linestyle='--',linewidth=2)

#5
# plt.axvline(x=1.3, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.64, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.68, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.65, color='r', linestyle='--',linewidth=2)

# 13
# plt.axvline(x=1.58, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.33, color='r', linestyle='--',linewidth=2)

# 18
# plt.axvline(x=4.97, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.13, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.30, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=7.16, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.3, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.8, color='r', linestyle='--',linewidth=2)

# 20
# plt.axvline(x=1.02, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.45, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.77, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.55, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.11, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.47, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.62, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.38, color='r', linestyle='--',linewidth=2)

# 21
# plt.axvline(x=4.35, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.7, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.55, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=7.7, color='r', linestyle='--',linewidth=2)

# 23
# plt.axvline(x=1.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.8, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.5, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.38, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=7.49, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.02, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.32, color='r', linestyle='--',linewidth=2)

# 24
# plt.axvline(x=0.13, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=0.684, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.07, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.802, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.502, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.595, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.686, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.2, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.01, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.486, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.983, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.913, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=13.534, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=14.988, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=16.98, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=20.788, color='r', linestyle='--',linewidth=2)


plt.subplot(2,1,2) 
plt.plot(time_epoch,nilai_prediksi, linestyle='-')
plt.axhline(y=4, color='grey', linestyle='--', linewidth=1)
plt.ylabel('Nilai prediksi')

# 1
# plt.axvline(x=2.8, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.4, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=14.30, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=15.17, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=17.5, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=19.8, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=25.60, color='r', linestyle='--',linewidth=2)

# # 2
plt.axvline(x=1.03, color='r', linestyle='--',linewidth=2)
plt.axvline(x=2.1, color='r', linestyle='--',linewidth=2)
plt.axvline(x=5.196, color='r', linestyle='--',linewidth=2)

# 3
# plt.axvline(x=0.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=1.2, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.6, color='r', linestyle='--',linewidth=2)

# # 5
# plt.axvline(x=1.3, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.64, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.68, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.65, color='r', linestyle='--',linewidth=2)

# 13
# plt.axvline(x=1.58, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.33, color='r', linestyle='--',linewidth=2)

# 18
# plt.axvline(x=4.97, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.13, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.30, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=7.16, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.3, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.8, color='r', linestyle='--',linewidth=2)

# 20
# plt.axvline(x=1.02, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.45, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.77, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.55, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.11, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.47, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.62, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.38, color='r', linestyle='--',linewidth=2)

# 21
# plt.axvline(x=4.35, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.7, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.55, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=7.7, color='r', linestyle='--',linewidth=2)

# 23
# plt.axvline(x=1.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.8, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.5, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.38, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=7.49, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.02, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.32, color='r', linestyle='--',linewidth=2)

# 24
# plt.axvline(x=0.13, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=0.684, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.07, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.802, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.502, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.595, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.686, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.2, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.01, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.486, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.983, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.913, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=13.534, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=14.988, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=16.98, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=20.788, color='r', linestyle='--',linewidth=2)

plt.figure('prediksi 3',figsize=(12,8))
plt.subplot(2,1,1) 
plt.plot(t,avg_signal)
plt.xlabel('Waktu (detik)')
plt.ylabel('Nilai prediksi')

# 1
# plt.axvline(x=2.8, color='g', linestyle='--')
# plt.axvline(x=3.4, color='g', linestyle='--')
# plt.axvline(x=14.30, color='g', linestyle='--')
# plt.axvline(x=15.17, color='g', linestyle='--') 
# plt.axvline(x=17.5, color='g', linestyle='--')
# plt.axvline(x=19.8, color='g', linestyle='--')
# plt.axvline(x=25.60, color='g', linestyle='--')

# 2
plt.axvline(x=1.03, color='r', linestyle='--',linewidth=2)
plt.axvline(x=2.1, color='r', linestyle='--',linewidth=2)
plt.axvline(x=5.196, color='r', linestyle='--',linewidth=2)

# 3
# plt.axvline(x=0.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=1.2, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.61, color='r', linestyle='--',linewidth=2)

#5
# plt.axvline(x=1.3, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.64, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.68, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.65, color='r', linestyle='--',linewidth=2)

# 13
#  plt.axvline(x=1.58, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.33, color='r', linestyle='--',linewidth=2)

# 18
# plt.axvline(x=4.97, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.13, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.30, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=7.16, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.3, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.8, color='r', linestyle='--',linewidth=2)

# 20
# plt.axvline(x=1.02, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.45, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.77, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.55, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.11, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.47, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.62, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.38, color='r', linestyle='--',linewidth=2)

# 21
# plt.axvline(x=4.35, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.7, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.55, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=7.7, color='r', linestyle='--',linewidth=2)

# 23
# plt.axvline(x=1.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.8, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.5, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.38, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=7.49, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.02, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.32, color='r', linestyle='--',linewidth=2)

# 24
# plt.axvline(x=0.13, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=0.684, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.07, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.802, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.502, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.595, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.686, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.2, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.01, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.486, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.983, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.913, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=13.534, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=14.988, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=16.98, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=20.788, color='r', linestyle='--',linewidth=2)


plt.subplot(2,1,2) 
plt.plot(time_epoch,nilai_prediksi,'o', linestyle='-')
plt.axhline(y=4, color='grey', linestyle='--', linewidth=1)

# 1
# plt.axvline(x=2.8, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.4, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=14.30, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=15.17, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=17.5, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=19.8, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=25.60, color='r', linestyle='--',linewidth=2)

# # 2
plt.axvline(x=1.03, color='r', linestyle='--',linewidth=2)
plt.axvline(x=2.1, color='r', linestyle='--',linewidth=2)
plt.axvline(x=5.196, color='r', linestyle='--',linewidth=2)

# 3
# plt.axvline(x=0.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=1.2, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.6, color='r', linestyle='--',linewidth=2)

# # 5
# plt.axvline(x=1.3, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.64, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.68, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.65, color='r', linestyle='--',linewidth=2)

# 13
# plt.axvline(x=1.58, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.33, color='r', linestyle='--',linewidth=2)

# 18
# plt.axvline(x=4.97, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.13, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.30, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=7.16, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.3, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.8, color='r', linestyle='--',linewidth=2)

# 20
# plt.axvline(x=1.02, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.45, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.77, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.55, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.11, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.47, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.62, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.38, color='r', linestyle='--',linewidth=2)

# 21
# plt.axvline(x=4.35, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.7, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.55, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=7.7, color='r', linestyle='--',linewidth=2)

# 23
# plt.axvline(x=1.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.8, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.5, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.38, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=7.49, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.02, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.32, color='r', linestyle='--',linewidth=2)

# 24
# plt.axvline(x=0.13, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=0.684, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.07, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.802, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.502, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.595, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.686, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.2, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.01, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.486, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.983, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.913, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=13.534, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=14.988, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=16.98, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=20.788, color='r', linestyle='--',linewidth=2)


# plt.figure('epoch 2',figsize=(12,8))
# plt.subplot(7,1,1) 
# plt.plot(t,avg_signal)

# plt.subplot(7,1,2) 
# plt.plot(time_epoch,epoch[0])
# plt.axhline(y=batas_epoch, color='r', linestyle='--', label='Horizontal Line at y=0.5')
# plt.xlabel('Waktu (detik)')
# plt.ylabel('Nilai Threshold')
# plt.subplot(7,1,3) 
# plt.plot(time_epoch,epoch[1])
# plt.axhline(y=batas_epoch, color='r', linestyle='--', label='Horizontal Line at y=0.5')
# plt.xlabel('Waktu (detik)')
# plt.ylabel('Nilai Threshold')
# plt.subplot(7,1,4) 
# plt.plot(time_epoch,epoch[2])
# plt.axhline(y=batas_epoch, color='r', linestyle='--', label='Horizontal Line at y=0.5')
# plt.xlabel('Waktu (detik)')
# plt.ylabel('Nilai Threshold')
# plt.subplot(7,1,5) 
# plt.plot(time_epoch,epoch[3])
# plt.axhline(y=batas_epoch, color='r', linestyle='--', label='Horizontal Line at y=0.5')
# plt.xlabel('Waktu (detik)')
# plt.ylabel('Nilai Threshold')
# plt.subplot(7,1,6) 
# plt.plot(time_epoch,epoch[4])
# plt.axhline(y=batas_epoch, color='r', linestyle='--', label='Horizontal Line at y=0.5')
# plt.xlabel('Waktu (detik)')
# plt.ylabel('Nilai Threshold')
# plt.subplot(7,1,7) 
# plt.plot(time_epoch,epoch[5])
# plt.axhline(y=batas_epoch, color='r', linestyle='--', label='Horizontal Line at y=0.5')
# plt.xlabel('Waktu (detik)')
# plt.ylabel('Nilai Threshold')
# plt.tight_layout()

# plt.figure('filtered 2',figsize=(12,8))

# plt.subplot(6,1,1)
# plt.plot(time_original,original_featureX[0], label='Shannon Entropy', color='blue')
# plt.xlabel('Waktu (detik)')
# plt.ylabel('Nilai Shannon')
# plt.legend()
# plt.subplot(6,1,2)
# plt.plot(time_original,filtered_featureX[1], label='Variance', color='green')
# plt.xlabel('Waktu (detik)')
# plt.ylabel('Nilai Variance')
# plt.legend()
# plt.subplot(6,1,3)
# plt.plot(time_original,filtered_featureX[2], label='Standard Deviation', color='red')
# plt.xlabel('Waktu (detik)')
# plt.ylabel('Nilai STD')
# plt.legend()
# plt.subplot(6,1,4)
# plt.plot(time_original,filtered_featureX[3], label='Sum of Squares', color='brown')
# plt.xlabel('Waktu (detik)')
# plt.ylabel('Nilai SoS')
# plt.legend()
# plt.subplot(6,1,5)
# plt.plot(time_original,filtered_featureX[4], label='Min', color='purple')
# plt.xlabel('Waktu (detik)')
# plt.ylabel('Nilai Min')
# plt.legend()
# plt.subplot(6,1,6)
# plt.plot(time_original,filtered_featureX[5], label='Max', color='orange')
# plt.xlabel('Waktu (detik)')
# plt.ylabel('Nilai Max')
# plt.legend()
# plt.tight_layout()

# plt.figure('KNN',figsize=(12,8))

# plt.subplot(6,1,1)
# plt.plot(time_original,prediction[0], label='Shannon Entropy', color='blue')
# plt.xlabel('Waktu (detik)')
# plt.ylabel('Nilai prediksi')
# # plt.ylim(5,11)
# plt.legend()
# plt.subplot(6,1,2)
# plt.plot(time_original,prediction[1], label='Variance', color='green')
# plt.xlabel('Waktu (detik)')
# plt.ylabel('Nilai prediksi')
# plt.legend()
# plt.subplot(6,1,3)
# plt.plot(time_original,prediction[2], label='Standard Deviation', color='red')
# plt.xlabel('Waktu (detik)')
# plt.ylabel('Nilai prediksi')
# plt.legend()
# plt.subplot(6,1,4)
# plt.plot(time_original,prediction[3], label='Sum of Squares', color='brown')
# plt.xlabel('Waktu (detik)')
# plt.ylabel('Nilai prediksi')
# plt.legend()
# plt.subplot(6,1,5)
# plt.plot(time_original,prediction[4], label='Min', color='purple')
# plt.xlabel('Waktu (detik)')
# plt.ylabel('Nilai prediksi')
# plt.legend()
# plt.subplot(6,1,6)
# plt.plot(time_original,prediction[5], label='Max', color='orange')
# plt.xlabel('Waktu (detik)')
# plt.ylabel('Nilai prediksi')
# plt.legend()
# plt.tight_layout()

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