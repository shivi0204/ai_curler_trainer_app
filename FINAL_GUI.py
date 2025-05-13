import SquatCounter
import main

def squat_analysis():
    SquatCounter.main()

def arm_curl_counter():
    main.main()

#####                                           CODE FOR GUI
#####                                              STARTS    
#####                                               NOW    

import customtkinter as cs
import tkinter as tk
import tkinter.messagebox
import tkinterDnD
from tkinter import filedialog as fd

cs.set_ctk_parent_class(tkinterDnD.Tk)
cs.set_appearance_mode("Dark")  
cs.set_default_color_theme("blue")  

root=cs.CTk()
root.geometry("1000x500")
root.title("AI FITNESS TRACKER")

#def squat_analysis():

frame=cs.CTkFrame(master=root)
frame.pack(pady=20,padx=60, fill="both", expand=True)

label = cs.CTkLabel(master=frame, text="AI Fitness Tracker", justify=cs.LEFT)
label.pack(pady=10, padx=10)

tabview_1 = cs.CTkTabview(master=frame, width=400, height=250,)
tabview_1.pack(pady=10, padx=10)

tab1=tabview_1.add("Arm Curl Counter")
button1=cs.CTkButton(master=tab1, text="Run Model", command=arm_curl_counter)
button1.pack(pady=12, padx=10)
label_1 = cs.CTkLabel(master=tab1,text="",justify=cs.LEFT)
label_1.pack(pady=10, padx=10)

tab3=tabview_1.add("Squat Counter")
button3=cs.CTkButton(master=tab3, text="Run Model", command=squat_analysis)
button3.pack(pady=12, padx=10)
label_3 = cs.CTkLabel(master=tab3,text="",justify=cs.LEFT)
label_3.pack(pady=10, padx=10)

root.mainloop()