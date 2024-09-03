import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os

from matplotlib.figure import Figure
# import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import function as fn 
import time
import sys
import io
from PIL import Image

file_paths  = []
nb_file     = []
pre_file    = []
startN = 0
endN = 0
startP = 0
endP = 0


def about():
   messagebox.showinfo("About", "Made by Ridho Priambodo\n\n ridhopriambodo558@gmail.com \n\nUniversitas Sebelas Maret 2024")
   
def import_edf_files():
    global file_paths
    global is_empty
    if is_empty:
        new_file_paths = filedialog.askopenfilenames(title="Select EDF files", filetypes=[("EDF files", "*.edf")])
        if new_file_paths:
            button_import.configure(image=remove_img)
            is_empty = False
            file_paths.extend(new_file_paths)
            num_files = len(file_paths)
            file_names = [os.path.basename(file_path) for file_path in new_file_paths]
            if num_files < 4:
                input.config(text=f"{num_files} EDF files imported: {', '.join(file_names)}")
            else:
                input.config(text=f"{num_files} EDF files imported")  # Update label with file 
    else:
        button_import.configure(image=import_img)
        is_empty = True
        file_paths = []    
        input.config(text="All imported files have been removed.")

def import_edf_file_train(states):
    global nb_file
    global pre_file
    global is_nb_empty
    global is_pre_empty
    if (states == "nb"):
        if is_nb_empty:
            file_nb_path = filedialog.askopenfilename(title="Select EDF files", filetypes=[("EDF files", "*.edf")])
            if file_nb_path:
                button_import_nb.configure(image=remove_img_small)
                is_nb_empty = False
                nb_file = file_nb_path
                file_names = os.path.basename(file_nb_path)
                input_n.config(text=f"{file_names}")
        else:
            button_import_nb.configure(image=import_img_small)
            is_nb_empty = True
            nb_file = []    
            input_n.config(text="Files have been removed.")
            
    elif (states == 'pre'):
        if is_pre_empty:
            file_pre_path = filedialog.askopenfilename(title="Select EDF files", filetypes=[("EDF files", "*.edf")])
            if file_pre_path:
                button_import_pre.configure(image=remove_img_small)
                is_pre_empty = False
                pre_file = file_pre_path
                file_names = os.path.basename(file_pre_path)
                input_p.config(text=f"{file_names}")
        else:
            button_import_pre.configure(image=import_img_small)
            is_pre_empty = True
            pre_file = []    
            input_p.config(text="Files have been removed.")

def process_data():
    loading_label.configure(text="Loading... 0%")
    app.update()
    global file_paths
    global nb_file
    global pre_file
    global startN
    global endN
    global startP
    global endP
    
    print('importing edf file...')
    begining = time.time()
    start = time.time()
    all_signals = fn.import_edf(file_paths,loading_label=loading_label,app=app)
    
    signals1, n_channels1,n_samples1,sample_rate1 = fn.single_import_edf(nb_file)
    signals2, n_channels2,n_samples2,sample_rate2 = fn.single_import_edf(pre_file)
    sample_rate = sample_rate1
    max_signal1 = n_samples1 / sample_rate1
    max_signal2 = n_samples2 / sample_rate2
       
    if(startN > max_signal1 or endN > max_signal1 or startP > max_signal2 or endP > max_signal2):
        messagebox.showerror("Error", "Time range exceeds the signal duration!")
        kembali()
        return

    avg_signal = fn.avg_signal(all_signals)
    avg_signal_reff = fn.avg_signal_reff(signals1,n_channels1,n_samples1)
    avg_signal_reff2 = fn.avg_signal_reff(signals2,n_channels2,n_samples2)

    # time
    t = np.arange(len(avg_signal)) / sample_rate / 3600

    # normal baseline
    normal_baseline_signal = avg_signal_reff[int(startN*sample_rate):int(endN*sample_rate)]
    # preseizure baseline
    pre_baseline_signal = avg_signal_reff2[int(startP*sample_rate):int(endP*sample_rate)]

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
    loading_label.configure(text="Loading... 60%")
    app.update()
    
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
    
    end = time.time()
    print("time to feature extraction: ", end - start)

    # clasification
    print("classification")
    loading_label.configure(text="Loading... 80%")
    app.update()
    
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
    loading_label.configure(text="Loading... 90%")
    app.update()
    
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
    
    loading_label.configure(text="Loading... 100%")
    app.update()

    time_epoch = np.arange(0, len(epoch[0])) * 60 * 10 / 3600

    fig1 = Figure(figsize=(10,6), dpi=100,facecolor='#272B37',tight_layout=True)
    ax = fig1.add_subplot(111)
    ax.plot(t,avg_signal)
    ax.set_facecolor('#2D2D2D')
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white',labelrotation=45,labelsize=8)
    ax.set_xlabel('Time (h)', color='white', fontsize=11)
    
    fig2 = Figure(figsize=(10,6), dpi=100,tight_layout=True,facecolor='#272B37')
    ax2 = fig2.add_subplot(111)
    ax2.plot(time_epoch,nilai_prediksi)
    ax2.axhline(y=4, color='grey', linestyle='--', linewidth=1)
    ax2.set_facecolor('#2D2D2D')
    ax2.spines['bottom'].set_color('white')
    ax2.spines['top'].set_color('white')    
    ax2.spines['left'].set_color('white')
    ax2.spines['right'].set_color('white')
    ax2.tick_params(axis='x', colors='white')
    ax2.tick_params(axis='y', colors='white',pad=15,labelsize=11)
    ax2.set_xlabel('Time (h)', color='white', fontsize=11)
    
    fig3 = Figure(figsize=(10,6), dpi=100,facecolor='#272B37',tight_layout=True)
    
    ax3 = fig3.add_subplot(611)
    ax3.plot(time_epoch,epoch[0])
    ax3.axhline(y=batas_epoch, color='r', linestyle='--', label='Horizontal Line at y=0.5')
    ax3.set_facecolor('#2D2D2D')
    ax3.tick_params(axis='x', colors='white')
    ax3.tick_params(axis='y', colors='white',pad=15,labelsize=11)
    ax3.spines['bottom'].set_color('white')
    ax3.spines['top'].set_color('white')
    ax3.spines['left'].set_color('white')
    ax3.spines['right'].set_color('white')

    ax3 = fig3.add_subplot(612)
    ax3.plot(time_epoch,epoch[1])
    ax3.axhline(y=batas_epoch, color='r', linestyle='--', label='Horizontal Line at y=0.5')
    ax3.set_facecolor('#2D2D2D')
    ax3.tick_params(axis='x', colors='white')
    ax3.tick_params(axis='y', colors='white',pad=15,labelsize=11)
    ax3.spines['bottom'].set_color('white')
    ax3.spines['top'].set_color('white')
    ax3.spines['left'].set_color('white')
    ax3.spines['right'].set_color('white')

    ax3 = fig3.add_subplot(613)
    ax3.plot(time_epoch,epoch[2])
    ax3.axhline(y=batas_epoch, color='r', linestyle='--', label='Horizontal Line at y=0.5')
    ax3.set_facecolor('#2D2D2D')
    ax3.tick_params(axis='x', colors='white')
    ax3.tick_params(axis='y', colors='white',pad=15,labelsize=11)
    ax3.spines['bottom'].set_color('white')
    ax3.spines['top'].set_color('white')
    ax3.spines['left'].set_color('white')
    ax3.spines['right'].set_color('white')

    ax3 = fig3.add_subplot(614) 
    ax3.plot(time_epoch,epoch[3])
    ax3.axhline(y=batas_epoch, color='r', linestyle='--', label='Horizontal Line at y=0.5')
    ax3.set_facecolor('#2D2D2D')
    ax3.tick_params(axis='x', colors='white')
    ax3.tick_params(axis='y', colors='white',pad=15,labelsize=11)
    ax3.spines['bottom'].set_color('white')
    ax3.spines['top'].set_color('white')
    ax3.spines['left'].set_color('white')
    ax3.spines['right'].set_color('white')

    ax3 = fig3.add_subplot(615)
    ax3.plot(time_epoch,epoch[4])
    ax3.axhline(y=batas_epoch, color='r', linestyle='--', label='Horizontal Line at y=0.5')
    ax3.set_facecolor('#2D2D2D')
    ax3.tick_params(axis='x', colors='white')
    ax3.tick_params(axis='y', colors='white',pad=15,labelsize=11)
    ax3.spines['bottom'].set_color('white')
    ax3.spines['top'].set_color('white')
    ax3.spines['left'].set_color('white')
    ax3.spines['right'].set_color('white')
    
    ax3 = fig3.add_subplot(616)
    ax3.plot(time_epoch,epoch[5])
    ax3.set_facecolor('#2D2D2D')
    ax3.axhline(y=batas_epoch, color='r', linestyle='--', label='Horizontal Line at y=0.5')
    ax3.tick_params(axis='x', colors='white')
    ax3.tick_params(axis='y', colors='white',pad=15,labelsize=11)
    ax3.set_xlabel('Time (h)', color='white', fontsize=11)
    ax3.spines['bottom'].set_color('white')
    ax3.spines['top'].set_color('white')
    ax3.spines['left'].set_color('white')
    ax3.spines['right'].set_color('white')

    fig4 = Figure(figsize=(10,6), dpi=100,facecolor='#272B37',tight_layout=True)
    ax4 = fig4.add_subplot(611)
    ax4.plot(time_original,original_featureX[0], label='Shannon Entropy', color='blue')
    # ax4.set_ylim(5,11)
    ax4.legend()
    ax4.set_facecolor('#2D2D2D')
    ax4.tick_params(axis='x', colors='white')
    ax4.tick_params(axis='y', colors='white',pad=15,labelsize=11)
    ax4.spines['bottom'].set_color('white')
    ax4.spines['top'].set_color('white')
    ax4.spines['left'].set_color('white')
    ax4.spines['right'].set_color('white')
    
    ax4 = fig4.add_subplot(612)
    ax4.plot(time_original,filtered_featureX[1], label='Variance', color='green')
    ax4.legend()
    ax4.set_facecolor('#2D2D2D')
    ax4.tick_params(axis='x', colors='white')
    ax4.tick_params(axis='y', colors='white',pad=15,labelsize=11)
    ax4.spines['bottom'].set_color('white')
    ax4.spines['top'].set_color('white')
    ax4.spines['left'].set_color('white')
    ax4.spines['right'].set_color('white')
    
    ax4 = fig4.add_subplot(613)
    ax4.plot(time_original,filtered_featureX[2], label='Standard Deviation', color='red')
    ax4.legend()
    ax4.set_facecolor('#2D2D2D')
    ax4.tick_params(axis='x', colors='white')
    ax4.tick_params(axis='y', colors='white',pad=15,labelsize=11)
    ax4.spines['bottom'].set_color('white')
    ax4.spines['top'].set_color('white')
    ax4.spines['left'].set_color('white')
    ax4.spines['right'].set_color('white')
    
    ax4 = fig4.add_subplot(614)
    ax4.plot(time_original,filtered_featureX[3], label='Sum of Squares', color='brown')
    ax4.legend()
    ax4.set_facecolor('#2D2D2D')
    ax4.tick_params(axis='x', colors='white')
    ax4.tick_params(axis='y', colors='white',pad=15,labelsize=11)
    ax4.spines['bottom'].set_color('white')
    ax4.spines['top'].set_color('white')
    ax4.spines['left'].set_color('white')
    ax4.spines['right'].set_color('white')
    
    ax4 = fig4.add_subplot(615)
    ax4.plot(time_original,filtered_featureX[4], label='Min', color='purple')
    ax4.legend()
    ax4.set_facecolor('#2D2D2D')
    ax4.tick_params(axis='x', colors='white')
    ax4.tick_params(axis='y', colors='white',pad=15,labelsize=11)
    ax4.spines['bottom'].set_color('white')
    ax4.spines['top'].set_color('white')
    ax4.spines['left'].set_color('white')
    ax4.spines['right'].set_color('white')
    
    ax4 = fig4.add_subplot(616)
    ax4.plot(time_original,filtered_featureX[5], label='Max', color='orange')
    ax4.legend()
    ax4.set_facecolor('#2D2D2D')
    ax4.tick_params(axis='x', colors='white')
    ax4.tick_params(axis='y', colors='white',pad=15,labelsize=11)
    ax4.set_xlabel('Time (second)', color='white', fontsize=11)
    ax4.spines['bottom'].set_color('white')
    ax4.spines['top'].set_color('white')
    ax4.spines['left'].set_color('white')
    ax4.spines['right'].set_color('white')

    results_func(fig1,fig2,fig3,fig4)

def results_func(fig1,fig2,fig3,fig4):
    print("results")
    canvas.coords(title, 620,100)
    canvas.itemconfig(title, image=title_img3 )
    canvas.delete(bg_image_id)
    canvas.configure(bg = "#272B37")
    loading_label.place_forget()
    text_signal = canvas.create_text(90.0, 150.0, anchor="w", text="Signal", fill="white", font=("DM Sans", 22, "normal"))
    canvas1 = FigureCanvasTkAgg(fig1, master=app)
    canvas1_widget = canvas1.get_tk_widget()
    # canvas1_widget.configure(width=800, height=200)
    canvas1_widget.place(x=40, y=175,width=1200, height=200)
    # canvas1_widget.pack()
    
    text_prediction = canvas.create_text(90.0, 400.0, anchor="w", text="Prediction", fill="white", font=("DM Sans", 22, "normal"))
    
    canvas2 = FigureCanvasTkAgg(fig2, master=app)
    canvas2_widget = canvas2.get_tk_widget()
    canvas2_widget.place(x=40, y=415,width=1200, height=200)
    
    
    home.configure(image=home_img,command=lambda: kembali(canvas1_widget,canvas2_widget,text_signal, text_prediction))
    home.place(x=820.0, y=630.0)
    global download_btn
    download_btn = tk.Button(app, image=download_img, border="0px", activebackground= "#272B37", background="#272B37", cursor="hand2", command=lambda: download(fig1,fig2,fig3,fig4),
                            relief="flat")
    download_btn.place(x=390.0, y=630.0)

def download(fig1,fig2,fig3,fig4):
    buffer1 = io.BytesIO()
    buffer2 = io.BytesIO()
    buffer3 = io.BytesIO()
    buffer4 = io.BytesIO()
    fig1.suptitle('Signal', fontsize=16, color='white')
    fig2.suptitle('Prediction', fontsize=16, color='white')
    fig3.suptitle('Epoch', fontsize=16, color='white')
    fig4.suptitle('Feature Extraction', fontsize=16, color='white')
    fig1.savefig(buffer1, format='png')
    fig2.savefig(buffer2, format='png')
    fig3.savefig(buffer3, format='png')
    fig4.savefig(buffer4, format='png')
    buffer1.seek(0)
    buffer2.seek(0)
    buffer3.seek(0)
    buffer4.seek(0)
    image1 = Image.open(buffer1)
    image2 = Image.open(buffer2)
    image3 = Image.open(buffer3)
    image4 = Image.open(buffer4)
    new_height = 2 * image1.height

    image3 = image3.resize((image3.width, new_height))
    image4 = image4.resize((image4.width, new_height))
    combined_image = Image.new('RGB', ((image1.width + image3.width + image4.width) , image1.height * 2))

    combined_image.paste(image1, (0, 0))
    combined_image.paste(image2, (0, image1.height))
    combined_image.paste(image3, (image1.width, 0))
    combined_image.paste(image4, ((image1.width+image3.width), 0))

    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        combined_image.save(file_path)
        messagebox.showinfo("Success", "File has been saved successfully")
        buffer1.close()
        buffer2.close()
        buffer3.close()
        buffer4.close()
    else:
        messagebox.showerror("Error", "Please select a file path")
        
def generate():
    if len(file_paths) == 0 or len(nb_file) == 0 or len(pre_file) == 0 or  entry_startN.get() == '' or entry_endN.get() == '' or entry_startP.get() == '' or entry_endP.get() == '' :
        if len(file_paths) == 0 or len(nb_file) == 0 or len(pre_file) == 0:
            messagebox.showerror("Error", "Please import EDF files first")
        else:
            messagebox.showerror("Error", "Please input the time range first")
    elif int(entry_startN.get()) >= int(entry_endN.get()) or int(entry_startP.get()) >= int(entry_endP.get()):
        messagebox.showerror("Error", "Invalid time range")
    else:
        global startN
        global endN
        global startP
        global endP
        startN = int(entry_startN.get())
        startP = int(entry_startP.get())
        endN = int(entry_endN.get())
        endP = int(entry_endP.get())
        
        entry_startN.place_forget()
        entry_endN.place_forget()
        entry_startP.place_forget()
        entry_endP.place_forget()
        
        canvas.itemconfig(title, image=title_img2)
        canvas.coords(title, 400,250)
        button_import.place_forget()
        button_import_nb.place_forget()
        button_import_pre.place_forget()
        input.place_forget()
        input_p.place_forget()
        input_n.place_forget()
        
        input_rectangle_lb.place_forget()
        input_rectangle_N.place_forget()
        input_rectangle_P.place_forget()
        
        button_generate.place_forget()
        canvas.itemconfig(input_image,state= "hidden")
        canvas.itemconfig(input_image_normalText,state= "hidden")
        canvas.itemconfig(input_image_preText,state= "hidden")
        canvas.itemconfig(input_image_startN,state= "hidden")
        canvas.itemconfig(input_image_startP,state= "hidden")
        canvas.itemconfig(input_image_endN,state= "hidden")
        canvas.itemconfig(input_image_endP,state= "hidden")
        
        loading_label.place(x=300, y=580)
        process_data()
        
def on_closing():
    app.destroy()
    sys.exit()
    
def kembali(canvas1_widget= None,canvas2_widget= None,text_signal= None, text_prediction= None):
    if canvas1_widget is not None and canvas2_widget is not None and text_signal is not None and text_prediction is not None:
        home.configure(image='',command='')
        home.place_forget()
        download_btn.place_forget()
        canvas.coords(title, 400,220)
        canvas.itemconfig(text_signal, text="")
        canvas.itemconfig(text_prediction, text="")
        canvas1_widget.destroy()
        canvas2_widget.destroy()        
        global bg_image_id
        bg_image_id= canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)
        canvas.tag_lower(bg_image_id)
        
    canvas.itemconfig(title, image=title_img )
    button_import.place( x=600.0, y=380.0)
    button_import_nb.place( x=330.0, y=465.0)
    button_import_pre.place( x=330.0, y=536.0)
    
    canvas.itemconfig(input_image,state= "normal")
    canvas.itemconfig(input_image_normalText,state= "normal")
    canvas.itemconfig(input_image_preText,state= "normal")
    canvas.itemconfig(input_image_startN,state= "normal")
    canvas.itemconfig(input_image_startP,state= "normal")
    canvas.itemconfig(input_image_endN,state= "normal")
    canvas.itemconfig(input_image_endP,state= "normal")
    
    input.place(x=125.0, y=370.0, width=500.0, height=50.0)
    input_n.place(x=125.0, y=460.0, width=230.0, height=35.0)
    input_p.place(x=125.0, y=530.0, width=230.0, height=35.0)
    button_generate.place(x=110.0, y=580.0)
    
    entry_startN.place(x=400.0, y=460.0, width=100.0, height=35.0)
    entry_endN.place(x=530.0, y=460.0, width=100.0, height=35.0)    
    entry_startP.place(x=400.0, y=530.0, width=100.0, height=35.0)
    entry_endP.place(x=530.0, y=530.0, width=100.0, height=35.0)
    
    input_rectangle_lb.place( x=110.0, y=370.0)
    input_rectangle_N.place( x=110.0, y=460.0)
    input_rectangle_P.place( x=110.0, y=530.0)

app = tk.Tk()
app.title("Seizure Detection System")
app.resizable(False, False)
app.geometry("1280x720")
app.configure(bg = "#272B37")


is_empty = True
is_nb_empty = True 
is_pre_empty = True

bg_image = tk.PhotoImage(file="gui/asset/bg.png")
download_img= tk.PhotoImage(file="gui/asset/download.png")

canvas = tk.Canvas(
    app,
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

# canvas.pack()
canvas.place(x = 0, y = 0)
bg_image_id = canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

title_img = tk.PhotoImage(file="gui/asset/title.png")
title_img2 = tk.PhotoImage(file="gui/asset/analyze.png")
title_img3 = tk.PhotoImage(file="gui/asset/result.png")

title = canvas.create_image(
    400.0,
    220.0,
    image= title_img
)
loading_label = tk.Label(app,text="",anchor="center",background="#272B37", borderwidth=0, fg="white", font=("Comic Sans MS", 22, "normal"))
loading_label.place(x=300, y=610) 

about_img = tk.PhotoImage(file="gui/asset/about.png")

about = tk.Button(
    image=about_img,
    border="0px",
    activebackground= "#272B37",
    background="#272B37",
    cursor="hand2",
    command=about,
    relief="flat"
)
about.place(
    x=50.0,
    y=50.0,
)   

home_img = tk.PhotoImage(file="gui/asset/home.png")

home = tk.Button(
    border="0px",
    activebackground= "#272B37",
    background="#272B37",
    cursor="hand2",
    # command=back_home,
    relief="flat"
)
# input file text
input_img = tk.PhotoImage(
    file="gui/asset/inputText.png")
input_image = canvas.create_image(
    150.0,
    350.0,
    image= input_img
)

# input normal state
input_img_normalText = tk.PhotoImage(
    file="gui/asset/InputNormalText.png")
input_image_normalText = canvas.create_image(
    175.0,
    445.0,
    image= input_img_normalText
)

# start normal time text
input_img_startN = tk.PhotoImage(
    file="gui/asset/Start(s).png")
input_image_startN = canvas.create_image(
    450.0,
    445.0,
    image= input_img_startN
)

# ends normal time
input_img_endN = tk.PhotoImage(
    file="gui/asset/End(s).png")
input_image_endN = canvas.create_image(
    580.0,
    445.0,
    image= input_img_endN
)

# input preseizure state 
input_img_preText = tk.PhotoImage(
    file="gui/asset/InputPreseizureText.png")
input_image_preText = canvas.create_image(
    185.0,
    515.0,
    image= input_img_preText
)
# start preseizure time text
input_img_startP = tk.PhotoImage(
    file="gui/asset/Start(s).png")
input_image_startP = canvas.create_image(
    450.0,
    515.0,
    image= input_img_startP
)

# ends preseizure time
input_img_endP = tk.PhotoImage(
    file="gui/asset/End(s).png")
input_image_endP = canvas.create_image(
    580.0,
    515.0,
    image= input_img_endP
)

# rectangle 
input_rectangle = tk.PhotoImage(file="gui/asset/rectangle.png")
input_rectangle2 = tk.PhotoImage(file="gui/asset/Rectangle_kecil.png")
input_rectangle3 = tk.PhotoImage(file="gui/asset/Rectangle_kecil.png")

input_rectangle_lb = tk.Label(
    image=input_rectangle,
    bg="#272B37",
    bd=0,
    fg="#FFFFFF",
)
input_rectangle_lb.place( x=110.0, y=370.0)

input_rectangle_N = tk.Label(
    image=input_rectangle2,
    bg="#272B37",
    bd=0,
    fg="#FFFFFF",
)
input_rectangle_N.place( x=110.0, y=460.0)

input_rectangle_P = tk.Label(
    image=input_rectangle3,
    bg="#272B37",
    bd=0,
    fg="#FFFFFF",
)
input_rectangle_P.place( x=110.0, y=530.0)

input = tk.Label(
    bd=0,
    bg="#464952",
    fg="#FFFFFF",
    highlightthickness=0
)
input.place(
    x=125.0,
    y=370.0,
    width=500.0,
    height=50.0
)

input_n = tk.Label(
    bd=0,
    bg="#464952",
    fg="#FFFFFF",
    highlightthickness=0
)
input_n.place(
    x=125.0,
    y=460.0,
    width=230.0,
    height=35.0
)

input_p = tk.Label(
    bd=0,
    bg="#464952",
    fg="#FFFFFF",
    highlightthickness=0
)

input_p.place(
    x=125.0,
    y=530.0,
    width=230.0,
    height=35.0
)

entry_startN=tk.Entry(app, width=25, bg="#464952", fg="#FFFFFF", font=("DM Sans", 12, "normal"), borderwidth=0, highlightthickness=0,)
entry_startN.place(x=400.0, y=460.0, width=100.0, height=35.0)

entry_endN=tk.Entry(app, width=25, bg="#464952", fg="#FFFFFF", font=("DM Sans", 12, "normal"), borderwidth=0, highlightthickness=0)
entry_endN.place(x=530.0, y=460.0, width=100.0, height=35.0)

entry_startP=tk.Entry(app, width=25, bg="#464952", fg="#FFFFFF", font=("DM Sans", 12, "normal"), borderwidth=0, highlightthickness=0)
entry_startP.place(x=400.0, y=530.0, width=100.0, height=35.0)

entry_endP=tk.Entry(app, width=25, bg="#464952", fg="#FFFFFF", font=("DM Sans", 12, "normal"), borderwidth=0, highlightthickness=0)
entry_endP.place(x=530.0, y=530.0, width=100.0, height=35.0)

import_img = tk.PhotoImage(file="gui/asset/import.png")
import_img_small = tk.PhotoImage(file="gui/asset/import_kecil.png")

remove_img = tk.PhotoImage(file="gui/asset/remove.png")
remove_img_small = tk.PhotoImage(file="gui/asset/remove_kecil.png")

button_import = tk.Button(
    image=import_img,
    border="0px",
    activebackground= "#464952",
    background="#464952",
    cursor="hand2",
    command=import_edf_files,
    relief="flat"
)

button_import_nb = tk.Button(
    image=import_img_small,
    border="0px",
    activebackground= "#464952",
    background="#464952",
    cursor="hand2",
    command=lambda: import_edf_file_train("nb"),
    relief="flat"
)

button_import_pre = tk.Button(
    image=import_img_small,
    border="0px",
    activebackground= "#464952",
    background="#464952",
    cursor="hand2",
    command=lambda: import_edf_file_train("pre"),
    relief="flat"
)

button_import.place(
    x=600.0,
    y=380.0,
)   

button_import_nb.place(
    x=330.0,
    y=465.0,
)   

button_import_pre.place(
    x=330.0,
    y=536.0,
)   


generate_img = tk.PhotoImage(file="gui/asset/generate.png")
button_generate = tk.Button(
    image=generate_img,
    border="0px",
    background="#272B37",
    activebackground= "#272B37",
    cursor="hand2",
    command=generate,
    relief="flat"
)

button_generate.place(
    x=110.0,
    y=600.0,
)   

app.protocol("WM_DELETE_WINDOW", on_closing)
# Start the main event loop
app.mainloop()
