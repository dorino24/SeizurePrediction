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

file_paths=[
#  "chb04/chb04_chb04_01.edf",
#  "chb04/chb04_chb04_02.edf",
#  "chb04/chb04_chb04_03.edf",
#  "chb04/chb04_chb04_04.edf",
#  "chb04/chb04_chb04_07.edf",
#  "chb04/chb04_chb04_08.edf",
#  "chb04/chb04_chb04_09.edf",
#  "chb04/chb04_chb04_10.edf",
# "chb01\chb01_03.edf",
#   "chb02\chb02_14.edf",
#   "chb02\chb02_15.edf",
#   "chb02\chb02_16.edf",
#   "chb02\chb02_16+.edf",
#   "chb02\chb02_17.edf",
#   "chb02\chb02_18.edf",
#   "chb02\chb02_19.edf",
#   "chb02\chb02_20.edf",
#   "chb02\chb02_21.edf",
#   "chb03\chb03_33.edf",
#   "chb03\chb03_34.edf",
#   "chb03\chb03_35.edf",
#   "chb03\chb03_36.edf",
#   "chb03\chb03_37.edf",
#   "chb03\chb03_38.edf"
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
# #     # "chb02/chb02_14.edf",
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
#     # "chb03/chb03_28.edf",
#     # "chb03/chb03_29.edf",
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

# 4
# file_paths = [
#     # 'chb04\chb04_chb04_01.edf',
#     # 'chb04\chb04_chb04_02.edf',
#     # 'chb04\chb04_chb04_03.edf',
#     # 'chb04\chb04_chb04_04.edf',
#     # 'chb04\chb04_chb04_05.edf',
#     # 'chb04\chb04_chb04_06.edf',
#     'chb04\chb04_chb04_07.edf',
#     'chb04\chb04_chb04_08.edf',
#     # 'chb04\chb04_chb04_09.edf',
#     # 'chb04\chb04_chb04_10.edf',
#     # 'chb04\chb04_chb04_11.edf',
#     # 'chb04\chb04_chb04_12.edf',
#     # 'chb04\chb04_chb04_13.edf',
#     # 'chb04\chb04_chb04_14.edf',
#     # 'chb04\chb04_chb04_15.edf',
#     # 'chb04\chb04_chb04_16.edf',
#     # 'chb04\chb04_chb04_17.edf',
#     # 'chb04\chb04_chb04_18.edf',
#     # 'chb04\chb04_chb04_19.edf',
#     # 'chb04\chb04_chb04_21.edf',
#     # 'chb04\chb04_chb04_22.edf',
#     # 'chb04\chb04_chb04_23.edf',
#     # 'chb04\chb04_chb04_24.edf',
#     # 'chb04\chb04_chb04_25.edf',
#     # 'chb04\chb04_chb04_26.edf',
#     # 'chb04\chb04_chb04_27.edf',
#     # 'chb04\chb04_chb04_29.edf',
#     # 'chb04\chb04_chb04_30.edf',
#     # 'chb04\chb04_chb04_31.edf',
#     # 'chb04\chb04_chb04_32.edf',
#     # 'chb04\chb04_chb04_33.edf',
#     # 'chb04\chb04_chb04_34.edf',
#     # 'chb04\chb04_chb04_35.edf',
#     # 'chb04\chb04_chb04_36.edf',
#     # 'chb04\chb04_chb04_37.edf',
#     # 'chb04\chb04_chb04_38.edf',
#     # 'chb04\chb04_chb04_39.edf',
#     # 'chb04\chb04_chb04_40.edf',
#     # 'chb04\chb04_chb04_41.edf',
#     # 'chb04\chb04_chb04_42.edf',
#     # 'chb04\chb04_chb04_43.edf'
# ]

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

# 6
# file_paths = [
    # "chb06/chb06_01.edf",
    # "chb06/chb06_02.edf",
    # "chb06/chb06_03.edf",
    # "chb06/chb06_04.edf",
    # "chb06/chb06_05.edf",
    # "chb06/chb06_06.edf",
    # "chb06/chb06_07.edf",
    # "chb06/chb06_08.edf",
    # "chb06/chb06_09.edf",
    # "chb06/chb06_10.edf",
    # "chb06/chb06_12.edf",
    # "chb06/chb06_13.edf",
    # "chb06/chb06_14.edf",
    # "chb06/chb06_15.edf",
    # "chb06/chb06_16.edf",
    # "chb06/chb06_17.edf",
    # "chb06/chb06_18.edf",
    # "chb06/chb06_24.edf"
    # ]

# 8
# file_paths = [
#     "chb08/chb08_chb08_02.edf",
#     "chb08/chb08_chb08_03.edf",
#     "chb08/chb08_chb08_04.edf",
#     "chb08/chb08_chb08_05.edf",
#     # "chb08/chb08_chb08_10.edf",
#     # "chb08/chb08_chb08_11.edf",
#     # "chb08/chb08_chb08_12.edf",
#     # "chb08/chb08_chb08_13.edf",
#     # "chb08/chb08_chb08_14.edf",
#     # "chb08/chb08_chb08_15.edf",
#     # "chb08/chb08_chb08_16.edf",
#     # "chb08/chb08_chb08_17.edf",
#     # "chb08/chb08_chb08_18.edf",
#     # "chb08/chb08_chb08_19.edf",
#     "chb08/chb08_chb08_20.edf",
#     "chb08/chb08_chb08_21.edf",
#     "chb08/chb08_chb08_22.edf",
#     "chb08/chb08_chb08_23.edf",
#     "chb08/chb08_chb08_24.edf", 
#     # "chb08/chb08_chb08_29.edf",
#     ]

# 9
file_paths = [
    # "chb09/chb09_chb09_01.edf",
    # "chb09/chb09_chb09_02.edf",
    # "chb09/chb09_chb09_03.edf",
    # "chb09/chb09_chb09_04.edf",
    "chb09/chb09_chb09_05.edf",
    "chb09/chb09_chb09_06.edf",
    # "chb09/chb09_chb09_07.edf",
    # "chb09/chb09_chb09_08.edf",
    # "chb09/chb09_chb09_09.edf",
    # "chb09/chb09_chb09_10.edf",
    # "chb09/chb09_chb09_11.edf",
    # "chb09/chb09_chb09_12.edf",
    # "chb09/chb09_chb09_13.edf",
    # "chb09/chb09_chb09_14.edf",
    # "chb09/chb09_chb09_15.edf",
    # "chb09/chb09_chb09_16.edf",
    # "chb09/chb09_chb09_17.edf",
    # "chb09/chb09_chb09_18.edf",
    # "chb09/chb09_chb09_19.edf",
    ]

# 10
# file_paths = [
#     # "chb10/chb10_chb10_01.edf",
#     # "chb10/chb10_chb10_02.edf",
#     # "chb10/chb10_chb10_03.edf",
#     # "chb10/chb10_chb10_04.edf",
#     # "chb10/chb10_chb10_05.edf",
#     # "chb10/chb10_chb10_06.edf",
#     # "chb10/chb10_chb10_07.edf",
#     # "chb10/chb10_chb10_08.edf",
#     "chb10/chb10_chb10_12.edf",
#     # "chb10/chb10_chb10_13.edf",
#     # "chb10/chb10_chb10_14.edf",
#     # "chb10/chb10_chb10_15.edf",
#     # "chb10/chb10_chb10_16.edf",
#     # "chb10/chb10_chb10_17.edf",
#     # "chb10/chb10_chb10_18.edf",
#     # "chb10/chb10_chb10_19.edf",
#     # "chb10/chb10_chb10_20.edf",
#     # "chb10/chb10_chb10_21.edf",
#     # "chb10/chb10_chb10_22.edf",
#     # "chb10/chb10_chb10_27.edf",
#     # "chb10/chb10_chb10_28.edf",
#     # "chb10/chb10_chb10_30.edf",
#     # "chb10/chb10_chb10_31.edf",
#     # "chb10/chb10_chb10_38.edf",
#     # "chb10/chb10_chb10_89.edf",
#     ]

# 12
# file_paths = [
#     # "chb12/chb12_chb12_06.edf",
#     # "chb12/chb12_chb12_08.edf",
#     # "chb12/chb12_chb12_09.edf",
#     # "chb12/chb12_chb12_10.edf",
#     # "chb12/chb12_chb12_11.edf",
#     # "chb12/chb12_chb12_19.edf",
#     # "chb12/chb12_chb12_20.edf",
#     # "chb12/chb12_chb12_21.edf",
#     # "chb12/chb12_chb12_23.edf",
#     # "chb12/chb12_chb12_24.edf",
#     # "chb12/chb12_chb12_27.edf",
#     # "chb12/chb12_chb12_28.edf",
#     # "chb12/chb12_chb12_29.edf",
#     # "chb12/chb12_chb12_32.edf",
#     # "chb12/chb12_chb12_33.edf",
#     # "chb12/chb12_chb12_34.edf",
#     # "chb12/chb12_chb12_35.edf",
#     # "chb12/chb12_chb12_36.edf",
#     # "chb12/chb12_chb12_37.edf",
#     # "chb12/chb12_chb12_38.edf",
#     # "chb12/chb12_chb12_39.edf",
#     # "chb12/chb12_chb12_40.edf",
#     # "chb12/chb12_chb12_41.edf",
#     "chb12/chb12_chb12_42.edf"
#     ]

# 13
# file_paths = [
#     #16:43:14 - 7:44:48
#     # "chb13/chb13_chb13_02.edf",
#     # "chb13/chb13_chb13_03.edf",
#     # "chb13/chb13_chb13_04.edf",
#     # "chb13/chb13_chb13_05.edf",
#     # "chb13/chb13_chb13_06.edf",
#     # "chb13/chb13_chb13_07.edf",
#     # "chb13/chb13_chb13_08.edf",
#     # "chb13/chb13_chb13_09.edf",
#     # "chb13/chb13_chb13_10.edf",
#     # "chb13/chb13_chb13_11.edf",
#     # "chb13/chb13_chb13_12.edf",
#     # "chb13/chb13_chb13_13.edf",
#     # "chb13/chb13_chb13_14.edf",
#     # "chb13/chb13_chb13_15.edf",
#     # "chb13/chb13_chb13_16.edf",
    
#     # 08:14:20 - 15:15:19
#     # "chb13/chb13_chb13_18.edf",
#     # "chb13/chb13_chb13_19.edf",
#     # "chb13/chb13_chb13_21.edf",
#     # "chb13/chb13_chb13_21.edf",
#     # "chb13/chb13_chb13_22.edf",
#     # "chb13/chb13_chb13_24.edf",
    
#     # 20:16:00 - 21:16:00 
#     # "chb13/chb13_chb13_30.edf",
    
#     #  02:17:23 - 7:17:50
#     # "chb13/chb13_chb13_36.edf",
#     # "chb13/chb13_chb13_37.edf",
#     # "chb13/chb13_chb13_38.edf",
#     # "chb13/chb13_chb13_39.edf",
#     # "chb13/chb13_chb13_40.edf",
    
#     # 13:18:37 - 14:18:37
#     # "chb13/chb13_chb13_47.edf",
    
#     #  21:20:07 - 3:20:41
#     # "chb13/chb13_chb13_55.edf",
#     # "chb13/chb13_chb13_56.edf",
#     # "chb13/chb13_chb13_58.edf",
#     # "chb13/chb13_chb13_59.edf",
#     # "chb13/chb13_chb13_60.edf",
    
#     # 04:20:55 - 5:20:55
#     # "chb13/chb13_chb13_62.edf"
# ]

# 14
# file_paths = [
#     "chb14/chb14_chb14_01.edf",
#     "chb14/chb14_chb14_02.edf",
#     "chb14/chb14_chb14_03.edf",
#     "chb14/chb14_chb14_04.edf",
#     "chb14/chb14_chb14_06.edf",
#     "chb14/chb14_chb14_07.edf",
#     "chb14/chb14_chb14_11.edf",
#     "chb14/chb14_chb14_12.edf",
#     "chb14/chb14_chb14_13.edf",
#     "chb14/chb14_chb14_14.edf",
#     "chb14/chb14_chb14_16.edf",
#     "chb14/chb14_chb14_17.edf",
#     "chb14/chb14_chb14_18.edf",
#     "chb14/chb14_chb14_19.edf",
#     "chb14/chb14_chb14_20.edf",
#     "chb14/chb14_chb14_22.edf",
#     "chb14/chb14_chb14_24.edf",
#     "chb14/chb14_chb14_25.edf",
#     "chb14/chb14_chb14_26.edf",
#     "chb14/chb14_chb14_27.edf",
#     "chb14/chb14_chb14_29.edf",
#     "chb14/chb14_chb14_30.edf",
#     "chb14/chb14_chb14_32.edf",
#     "chb14/chb14_chb14_37.edf",
#     "chb14/chb14_chb14_39.edf",
#     "chb14/chb14_chb14_42.edf"
#     ]

# 15
# file_paths = [
    
#     # beda konfigurasi channel
#     # "chb15/chb15_chb15_01.edf", 
    
#     # # 19:23:43 - 11:25:27
#     # "chb15/chb15_chb15_02.edf",
#     # "chb15/chb15_chb15_03.edf",
#     # "chb15/chb15_chb15_04.edf",
#     # "chb15/chb15_chb15_05.edf",
#     # "chb15/chb15_chb15_06.edf",
#     # "chb15/chb15_chb15_07.edf",
#     # "chb15/chb15_chb15_08.edf",
#     # "chb15/chb15_chb15_09.edf",
#     # "chb15/chb15_chb15_10.edf",
#     # "chb15/chb15_chb15_11.edf",
#     # "chb15/chb15_chb15_12.edf",
#     # "chb15/chb15_chb15_13.edf",
#     # "chb15/chb15_chb15_14.edf",
#     # "chb15/chb15_chb15_15.edf",
#     # "chb15/chb15_chb15_16.edf",
#     # "chb15/chb15_chb15_17.edf",
    
#     # # 12:25:41 - 14:25:48
#     # "chb15/chb15_chb15_19.edf",
#     # "chb15/chb15_chb15_20.edf",
    
#     # # 15:26:02 - 16:26:02
#     # "chb15/chb15_chb15_22.edf",
    
#     # # 19:27:44 - 20:27:44
#     # "chb15/chb15_chb15_26.edf",
    
#     # #  21:27:58 - 3:28:32
#     # "chb15/chb15_chb15_28.edf",
#     # "chb15/chb15_chb15_29.edf",
#     # "chb15/chb15_chb15_30.edf",
#     # "chb15/chb15_chb15_31.edf",
#     # "chb15/chb15_chb15_32.edf",
#     # "chb15/chb15_chb15_33.edf",
    
#     # #  04:28:46 - 5:28:46
#     # "chb15/chb15_chb15_35.edf",
    
#     # #  06:29:00 - 7:29:00
#     # "chb15/chb15_chb15_37.edf",
    
#     # # 09:29:21 - 10:29:21
#     # "chb15/chb15_chb15_40.edf",
    
#     # #  14:30:00 -16:30:07
#     # "chb15/chb15_chb15_45.edf",
#     # "chb15/chb15_chb15_46.edf",
    
#     # # 18:38:05 -22:39:19
#     # "chb15/chb15_chb15_49.edf",
#     # "chb15/chb15_chb15_50.edf",
#     # "chb15/chb15_chb15_51.edf",
#     # "chb15/chb15_chb15_52.edf",
    
#     # # 23:39:54 - 24:39:54
#     # "chb15/chb15_chb15_54.edf",
    
#     # # 06:41:03 - 06:41:03
#     # "chb15/chb15_chb15_61.edf",
#     # "chb15/chb15_chb15_62.edf",
#     # "chb15/chb15_chb15_63.edf"
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

file_nb = 'chb09/chb09_chb09_05.edf'
file_pb ="chb09/chb09_chb09_06.edf"
start_nb =  7200
end_nb = 10800
start_pb = 9000
end_pb = 10800

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
t = np.arange(len(avg_signal)) / sample_rate /3600
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
time_original = np.arange(0, len(original_featureX[0])) * segment_duration /3600
time_filterd = np.arange(0, len(filtered_featureX[0])) * segment_duration
time_nb = np.arange(0, len(nb_featureX[0])) * segment_duration
time_pre = np.arange(0, len(pre_featureX[0])) * segment_duration
end = time.time()
print("time to feature extraction: ", end - start)

# clasification
print("classification")
start   = time.time()
prediction = []
# nb_shannon_x = [11.25,11.28,11.19,11.31,11.32,11.34,11.35,11.36,11.38,11.39,11.40,11.41,11.44]
# pre_shannon_x = [10.8,10.81,10.82,10.85,10.87,10.89,10.92,10.94,10.95,10.96,10.98,10.99,11.00,11.01,11.04]


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
batas_epoch = 50
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

# time_epoch = np.arange(1, len(epoch[0])+1) * 60 * 10 
# print(time_epoch)
# time_epoch = np.arange(0, len(epoch[0])) * 60 * 10 / 3600


time_epoch = np.arange(1, len(epoch[0])+1) * 60 * 10 /3600 
# time_epoch = np.arange(1, len(epoch[0])+1) * 60 * 10  

plt.figure('prediksi 2',figsize=(12,8))
plt.subplot(2,1,1) 
plt.plot(t,avg_signal)

# 1
# plt.axvline(x=2.8, color='g', linestyle='--')
# plt.axvline(x=3.4, color='g', linestyle='--')
# plt.axvline(x=14.30, color='g', linestyle='--')
# plt.axvline(x=15.17, color='g', linestyle='--') 
# plt.axvline(x=17.5, color='g', linestyle='--')
# plt.axvline(x=19.8, color='g', linestyle='--')
# plt.axvline(x=25.60, color='g', linestyle='--')

# 2
# plt.axvline(x=1.03, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.196, color='r', linestyle='--',linewidth=2)

# 3
# plt.axvline(x=0.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=1.2, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.61, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=33.55, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=34.7, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=35.47, color='r', linestyle='--',linewidth=2)

#4
# plt.axvline(x=(18.16), color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.27, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=15.64, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=16.68, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=21.65, color='r', linestyle='--',linewidth=2)

#5
# plt.axvline(x=5.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.27, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=15.64, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=16.68, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=21.65, color='r', linestyle='--',linewidth=2)

# plt.axvline(x=1.3, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.64, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.68, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.65, color='r', linestyle='--',linewidth=2)

#6
# plt.axvline(x=0.5, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.75, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=13.73, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=35.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=38.7, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=43.8, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=60.75, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=60.75, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=65.4, color='r', linestyle='--',linewidth=2)

# 8
# plt.axvline(x=0.75, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.8, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.83, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=7.68, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=15.58, color='r', linestyle='--',linewidth=2)

# 9
# plt.axvline(x=7.4, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.83, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=14.5, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=53.3, color='r', linestyle='--',linewidth=2)

# 12
# plt.axvline(x=0.4, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=0.94, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=1.4, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=1.45, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=1.54, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=1.78, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.85, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.98, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.16, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.22, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.3, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.07, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.12, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.2, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.25, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.3, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.48, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.53, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.66, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.72, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=11.05, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.15, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.32, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.38, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.52, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.98, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=14.6, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=14.67, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=17.18, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=19.43, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=19.777, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=19.82, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=19.87, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=19.93, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=23.19, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=23.26, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=23.325, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=23.46, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=23.61, color='r', linestyle='--',linewidth=2)

# 13
# plt.axvline(x=16.57, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=17.26, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=25, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=25.15, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=27.127, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=27.67, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=29.68, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=30.93, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=31.18, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=32.24, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=32.453, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=32.742, color='r', linestyle='--',linewidth=2)

# 14
# plt.axvline(x=2.55, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.38, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.783, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.53, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.51, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=11.9, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.28, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=19.78, color='r', linestyle='--',linewidth=2)

# 15
# plt.axvline(x=5.09, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=9.5, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=14.44, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=16.54, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=18.16, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=19.2, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=21.25, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=24.5, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=29.24, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=29.68, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=29.94, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=31.925, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=32.31, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=35.216, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=36.075, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=36.24, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=36.425, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=36.61, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=36.95, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=38.21, color='r', linestyle='--',linewidth=2)

# 18
# plt.axvline(x=28.95, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=29.15, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=30.58, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=31.19, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=34.26, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=34.78, color='r', linestyle='--',linewidth=2)

# plt.axvline(x=4.97, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.13, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.30, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=7.16, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.3, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.8, color='r', linestyle='--',linewidth=2)



# 20
# plt.axvline(x=9, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.4, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.694, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=11.55, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.11, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.47, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=13.62, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=27.38, color='r', linestyle='--',linewidth=2)

# 24
# plt.axvline(x=0.13, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=0.684, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.07, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.802, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.302, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.395, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.486, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.342, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.01, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.486, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.983, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.913, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=13.534, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=14.988, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=16.98, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=20.788, color='r', linestyle='--',linewidth=2)


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
# plt.axvline(x=25.60, color='r', linestyle='--',linewidth=2)

# # 2
# plt.axvline(x=1.03, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.196, color='r', linestyle='--',linewidth=2)

# 3
# plt.axvline(x=0.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=1.2, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.61, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=33.55, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=34.7, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=35.47, color='r', linestyle='--',linewidth=2)

# # 5
# plt.axvline(x=5.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.27, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=15.64, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=16.68, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=21.65, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=1.3, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.64, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.68, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.65, color='r', linestyle='--',linewidth=2)

# 6
# plt.axvline(x=0.5, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.75, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=13.73, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=35.1, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=38.7, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=43.8, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=60.75, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=60.75, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=65.4, color='r', linestyle='--',linewidth=2)

# 8
# plt.axvline(x=0.75, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.8, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.83, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=7.68, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=15.58, color='r', linestyle='--',linewidth=2)

# 9
# plt.axvline(x=7.4, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.83, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=14.5, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=53.3, color='r', linestyle='--',linewidth=2)


#12
# plt.axvline(x=0.4, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=0.94, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=1.4, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=1.45, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=1.54, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=1.78, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.85, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.98, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.16, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.22, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.3, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.07, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.12, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.2, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.25, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.3, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.48, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.53, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.66, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.72, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=11.05, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.15, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.32, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.38, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.52, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.98, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=14.6, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=14.67, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=17.18, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=19.43, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=19.777, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=19.82, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=19.87, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=19.93, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=23.19, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=23.26, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=23.325, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=23.46, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=23.61, color='r', linestyle='--',linewidth=2) 

# 13
# plt.axvline(x=16.57, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=17.26, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=25, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=25.15, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=27.127, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=27.67, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=29.68, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=30.93, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=31.18, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=32.24, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=32.453, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=32.742, color='r', linestyle='--',linewidth=2)

# 14
# plt.axvline(x=2.55, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.38, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.783, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=4.53, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.51, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=11.9, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.28, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=19.78, color='r', linestyle='--',linewidth=2)

# 15
# plt.axvline(x=5.09, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=9.5, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=14.44, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=16.54, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=18.16, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=19.2, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=21.25, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=24.5, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=29.24, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=29.68, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=29.94, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=31.925, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=32.31, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=35.216, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=36.075, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=36.24, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=36.425, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=36.61, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=36.95, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=38.21, color='r', linestyle='--',linewidth=2)

# 18
# plt.axvline(x=28.95, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=29.15, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=30.58, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=31.19, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=34.26, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=34.78, color='r', linestyle='--',linewidth=2)


# plt.axvline(x=4.97, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.13, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.30, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=7.16, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.3, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.8, color='r', linestyle='--',linewidth=2)

# 20
# plt.axvline(x=9, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.4, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.694, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=11.55, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.11, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.47, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=13.62, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=27.38, color='r', linestyle='--',linewidth=2)

# 24
# plt.axvline(x=0.13, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=0.684, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.07, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=2.802, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.302, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.395, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=3.486, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=5.342, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=6.01, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=8.486, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=10.983, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=12.913, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=13.534, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=14.988, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=16.98, color='r', linestyle='--',linewidth=2)
# plt.axvline(x=20.788, color='r', linestyle='--',linewidth=2)

plt.figure('epoch 2',figsize=(12,8))
plt.subplot(7,1,1) 
plt.plot(t,avg_signal)

plt.subplot(7,1,2) 
plt.plot(time_epoch,epoch[0])
plt.axhline(y=batas_epoch, color='r', linestyle='--', label='Horizontal Line at y=0.5')
plt.subplot(7,1,3) 
plt.plot(time_epoch,epoch[1])
plt.axhline(y=batas_epoch, color='r', linestyle='--', label='Horizontal Line at y=0.5')
plt.subplot(7,1,4) 
plt.plot(time_epoch,epoch[2])
plt.axhline(y=batas_epoch, color='r', linestyle='--', label='Horizontal Line at y=0.5')
plt.subplot(7,1,5) 
plt.plot(time_epoch,epoch[3])
plt.axhline(y=batas_epoch, color='r', linestyle='--', label='Horizontal Line at y=0.5')
plt.subplot(7,1,6) 
plt.plot(time_epoch,epoch[4])
plt.axhline(y=batas_epoch, color='r', linestyle='--', label='Horizontal Line at y=0.5')
plt.subplot(7,1,7) 
plt.plot(time_epoch,epoch[5])
plt.axhline(y=batas_epoch, color='r', linestyle='--', label='Horizontal Line at y=0.5')
plt.tight_layout()

plt.figure('filtered 2',figsize=(12,8))

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

# plt.figure('KNN',figsize=(12,8))

# plt.subplot(6,1,1)
# plt.plot(time_original,prediction[0], label='Shannon Entropy', color='blue')
# # plt.ylim(5,11)
# plt.legend()
# plt.subplot(6,1,2)
# plt.plot(time_original,prediction[1], label='Variance', color='green')
# plt.legend()
# plt.subplot(6,1,3)
# plt.plot(time_original,prediction[2], label='Standard Deviation', color='red')
# plt.legend()
# plt.subplot(6,1,4)
# plt.plot(time_original,prediction[3], label='Sum of Squares', color='brown')
# plt.legend()
# plt.subplot(6,1,5)
# plt.plot(time_original,prediction[4], label='Min', color='purple')
# plt.legend()
# plt.subplot(6,1,6)
# plt.plot(time_original,prediction[5], label='Max', color='orange')
# plt.legend()

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