import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
import function as fn 
import time
import os


file_paths = []

def import_edf_files():
    global file_paths
    new_file_paths = filedialog.askopenfilenames(title="Select EDF files", filetypes=[("EDF files", "*.edf")])
    if new_file_paths:
        file_paths.extend(new_file_paths)
        num_files = len(file_paths)
        file_names = [os.path.basename(file_path) for file_path in new_file_paths]
        label.config(text=f"{num_files} EDF files imported: {', '.join(file_names)}")  # Update label with file names
        button_import.pack_forget()
        button_start.pack()
        button_remove.pack()

def remove_files():
    global file_paths
    print("File has been removed")
    file_paths = []
    label.config(text="All imported files have been removed.")
    button_remove.pack_forget()
    button_start.pack_forget()
    button_import.pack()

def process_data():
    # import file
    global file_paths
    # file_paths = ["chb01/chb01_01.edf", "chb01/chb01_02.edf","chb01/chb01_03.edf","chb01/chb01_04.edf", "chb01/chb01_05.edf", ]
    print('importing edf file...')
    begining = time.time()
    start = time.time()
    all_signals = fn.import_edf(file_paths)
    # n_channels  = 23
    sample_rate = 256

    signals1, n_channels1,n_samples1,sample_rate1 = fn.single_import_edf('./chb01/chb01_03.edf')
    # n_samples   = n_samples1

    # avg_signal = fn.avg_signal(all_signals,n_channels,n_samples)
    # avg_signal_reff = fn.avg_signal(signals1,n_channels1,n_samples1)

    avg_signal = all_signals
    avg_signal_reff = signals1[0]
    # time
    t = np.arange(len(all_signals)) / sample_rate / 3600

    # normal baseline
    normal_baseline_signal = avg_signal_reff[int(1000*sample_rate):int(1600*sample_rate)]
    # time_nb  = t[int(1000*sample_rate):int(1600*sample_rate)]

    # preseizure baseline
    pre_baseline_signal = avg_signal_reff[int(2100*sample_rate):int(2700*sample_rate)]
    # time_pre  = t[int(2100*sample_rate):int(2700*sample_rate)]

    end = time.time()
    print("time to import edf file: ", end - start)

    # preprocessing
    print("preprocessing")
    start = time.time()
    filtered_signal = fn.filtering(avg_signal,sample_rate , lowcut=0.5, highcut=40.0)
    end = time.time()
    print("time to filter: ", end - start)

    # feature_extraction
    print("feature_extraction")
    start = time.time()
    segment_duration = 10
    original_featureX = fn.feature_extraction(segment_duration,avg_signal,sample_rate)
    filtered_featureX = fn.feature_extraction(segment_duration,filtered_signal,sample_rate)
    nb_featureX = fn.feature_extraction(segment_duration,normal_baseline_signal,sample_rate)
    pre_featureX = fn.feature_extraction(segment_duration,pre_baseline_signal,sample_rate)

    # time feature
    time_original = np.arange(0, len(original_featureX[0])) * segment_duration
    # time_filterd = np.arange(0, len(filtered_featureX[0])) * segment_duration
    # time_nb = np.arange(0, len(nb_featureX[0])) * segment_duration
    # time_pre = np.arange(0, len(pre_featureX[0])) * segment_duration
    end = time.time()
    print("time to feature extraction: ", end - start)

    # clasification
    print("classification")
    start   = time.time()
    prediction = []
    pred_one = fn.classification(nb_featureX[0],pre_featureX[0],original_featureX[0])
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
            if epoch[j][i] > 40:
                sum += 1
        nilai_prediksi.append(sum)

    ending = time.time()
    print("total time: ", ending - begining)
    print("plotting")

    time_epoch = np.arange(0, len(epoch[0])) * 60 * 10 / 3600

    plt.figure('prediksi',figsize=(12,8))
    plt.subplot(2,1,1) 
    plt.plot(t,avg_signal)
    # for i in range(0, int((len(all_signals)/ sample_rate / 3600))):
    #     plt.axvline(x=i, color='r', linestyle='--')
    # plt.axvline(x=2.8, color='g', linestyle='--')
    # plt.axvline(x=3.4, color='g', linestyle='--')
    # plt.axvline(x=14.30, color='g', linestyle='--')
    # plt.axvline(x=15.17, color='g', linestyle='--')
    # plt.axvline(x=17.5, color='g', linestyle='--')
    # plt.axvline(x=19.8, color='g', linestyle='--')
    # plt.axvline(x=25.25, color='g', linestyle='--')

    plt.subplot(2,1,2) 
    plt.plot(time_epoch,nilai_prediksi)
    plt.axhline(y=4, color='grey', linestyle='--', linewidth=1)
    # plt.axvline(x=2.8, color='r', linestyle='--',linewidth=2)
    # plt.axvline(x=3.4, color='r', linestyle='--',linewidth=2)
    # plt.axvline(x=14.30, color='r', linestyle='--',linewidth=2)
    # plt.axvline(x=15.17, color='r', linestyle='--',linewidth=2)
    # plt.axvline(x=17.5, color='r', linestyle='--',linewidth=2)
    # plt.axvline(x=19.8, color='r', linestyle='--',linewidth=2)
    # plt.axvline(x=25.25, color='r', linestyle='--',linewidth=2)


    plt.figure('original',figsize=(12,8))
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

    plt.figure('filtered',figsize=(12,8))

    plt.subplot(6,1,1)
    plt.plot(time_original,original_featureX[0], label='Shannon Entropy', color='blue')
    plt.ylim(5,11)
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

    plt.show()

def start_processing():
    # Call the process_data function when the start button is clicked
    process_data()


# Create the main application window
app = tk.Tk()
app.title("Epileptic Seizure Detection System")
app.geometry("800x600")
app.configure(bg = "#202020")

canvas = tk.Canvas(
    app,
    bg = "#202020",
    height = 800,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)


# Create and pack a label widget
label = tk.Label(app, text="")
label.pack()

# Create and pack a button widget for importing EDF files
button_import = tk.Button(app, text="Import EDF Files", command=import_edf_files)
button_import.pack()

button_start = tk.Button(app, text="Start Processing", command=start_processing)

# Create and pack a button widget for removing the imported EDF files
button_remove = tk.Button(app, text="Remove EDF Files", command=remove_files)

# Start the main event loop
app.mainloop()
