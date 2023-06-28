import tkinter as tk
from tkinter import filedialog, messagebox

import TreeTop_prediction as T

root = tk.Tk()

root.title("My Window")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 600
window_height = 225

x = int((screen_width - window_width) / 2)
y = int((screen_height - window_height) / 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

def open_file():
    file_path = filedialog.askopenfilename()
    print("Selected file:", file_path)
    set_text(file_path)

def set_text(txt):
    path_lbl.config(text="Image path: " + txt, anchor=tk.CENTER)
    path_lbltmp.config(text=txt) # Invisible lbl just to save the path value

def startDetection():

    detection_lbl.config(text="Number of trees detected:  ")

    label_value = path_lbltmp.cget("text")
    
    #marbles_img = T.skimage.io.imread(r"C:\Users\vicar\Downloads\test TFG con Rafa\maskrcnn\tree-detection\img\test img\DJI_0401.JPG")
    marbles_img = T.skimage.io.imread(label_value)
    # plt.imshow(marbles_img) #Por ahora no necesito ver la imagen a detectar

    detected = T.model.detect([marbles_img])
    results = detected[0]
    class_names = ['BG', 'tree'] 

    #Comentada por ahora
    """ T.display_instances(marbles_img, results['rois'], results['masks'], 
                    results['class_ids'], class_names, results['scores']) """

    detection_lbl.config(text="Number of trees detected:  " + str(len(results['rois'])))

    desition = messagebox.askyesno("Confirmation", "Do you want to see the image of the detection?")
    if desition == True:
        T.display_instances(marbles_img, results['rois'], results['masks'], 
                  results['class_ids'], class_names, results['scores'])

# Labels
label = tk.Label(root, text="Treetop Detector",font=("Arial", 20))
label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Buttons
btn = tk.Button(root, text="Click to select an image", font=("Arial", 10), command=open_file)
btn.pack(pady=60)

frame = tk.Frame(root, width=550, height=30, bg="white",  highlightbackground="grey", highlightthickness=1)
frame.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

path_lbl = tk.Label(frame,text="Image path: " , font=("Arial", 10), bg="white")
path_lbl.place(relx=0.01, rely=0.1)
path_lbltmp = tk.Label(frame,text="Image path: " , font=("Arial", 10), bg="white") # Invisible lbl

button2 = tk.Button(root, text="Start process", bg="green", fg="white", font=("Arial", 15), command=startDetection)
button2.place(relx=0.04, rely=0.75)

detection_lbl = tk.Label(root,text="Number of trees detected:  " , font=("Arial", 15))
detection_lbl.place(relx=0.45, rely=0.78)

root.mainloop()
