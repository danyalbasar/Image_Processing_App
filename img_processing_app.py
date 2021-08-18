from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import ttk
import PIL
from PIL import Image
import os
 
img= ""

def clear_all():
	ent.delete(0, END)
	ent_2.delete(0, END)
	ent_3.delete(0, END)
	ent_4.delete(0, END)
	ent_5.delete(0, END)
	ent_6.delete(0, END)
	combo_resize.delete(0, END)

def browse_img():
	try:
		ent.delete(0, END)	
		ent_2.delete(0, END)	
		ent_3.delete(0, END)	
		ent_4.delete(0, END)
		ent_5.delete(0, END)
		ent_6.delete(0, END)
		combo_resize.delete(0, END)
		global img
		fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Browse Image File", filetypes=( ("All files", "*.*"), ("JPG Image", "*jpg"), ("PNG Image", "*png")))
		if len(fln) == 0:
			messagebox.showerror("Error", "No Image selected")
		else:
			t1.set(fln)
			img = PIL.Image.open(fln)
			w.set(img.size[0])
			h.set(img.size[1])
			img_type_temp = ent_4.get()
			img_type = "." + (img.format).lower()
			ent_4.insert(0, img_type)
			combo_resize.insert(0, img_type)

	except Exception as e:
		messagebox.showerror("Error", str(e))
 
def preview_img():
	try:
		browse_img_temp_1 = ent.get()
		if len(browse_img_temp_1) == 0:
			messagebox.showerror("Error", "No Image selected")
		else:
			img.show()

	except Exception as e:
		messagebox.showerror("Error", str(e))

def recalc():
	try:
		perc_temp = ent_5.get()
		if (len(perc_temp) == 0):
			messagebox.showerror("Error", "Enter the percentage of dimension by which the image is to be resized")
		elif (not perc_temp.isdigit()):
			messagebox.showerror("Error", "Percentage of dimension by which the image is to be resized should be a number between 1-100")
		elif (int(perc_temp) > 100):
			messagebox.showerror("Error", "Percentage of dimension by which the image is to be resized should be between 1-100")
		else:
			p = int(perc.get())
			nw = int(int(w.get()) * p / 100)
			nh = int(int(h.get()) * p / 100)
			w.set(nw)
			h.set(nh)

	except Exception as e:
		messagebox.showerror("Error", str(e))
 
def preview_new_img():
	try:
		browse_img_temp_2 = ent.get()
		if len(browse_img_temp_2) == 0:
			messagebox.showerror("Error", "No Image selected")
		else:
			nw = int(w.get())
			nh = int(h.get())
			img3 = img.resize((nw, nh), PIL.Image.ANTIALIAS)
			img4 = img3.convert("RGB")
			img4.show()

	except Exception as e:
		messagebox.showerror("Error", str(e))
 
def save_new_img():
	try:
		browse_img_temp_3 = ent.get()
		if len(browse_img_temp_3) == 0:
			messagebox.showerror("Error", "No Image selected")
		else:
			fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save Image", filetypes=(("All files", "*.*"), ("JPG Image", "*jpg"), ("JPEG Image", "*jpeg"), ("PNG Image", "*png"))) 
			if len(fln) == 0:
				messagebox.showerror("Error", "No File name provided")
			else:
				quality_val_check = ent_6.get() 
				if (len(quality_val_check) == 0):
					messagebox.showerror("Error", "Enter quality of image to be saved")
				elif (not quality_val_check.isdigit()):
					messagebox.showerror("Error", "Quality percentage of image to be saved should be a number between 1-100")
				elif (int(quality_val_check) > 100):
					messagebox.showerror("Error", "Quality percentage of image to be saved should be between 1-100")
				else:
					nw = int(w.get())
					nh = int(h.get())
					quality_val = int(qua.get())
					option_selected = option.get()
					img3 = img.resize((nw, nh), PIL.Image.ANTIALIAS)
					img4 = img3.convert("RGB")
					img4.save(fln + option_selected, quality=quality_val)
					messagebox.showinfo("Image Saved", "Image has been saved as "+os.path.basename(fln)+" successfully.")

	except Exception as e:
		messagebox.showerror("Error", str(e))
 
main_window = Tk()
main_window.title("Image Resizer")
main_window.iconbitmap("download.ico")
main_window.geometry("800x750+500+130")
main_window.configure(bg="black")
 
t1 = StringVar()
w = StringVar()
h = StringVar()
img_type = StringVar()
perc = StringVar()
qua = StringVar()
option = StringVar()

font_1 = ("arial", 15, "bold")
font_2 = ("arial", 13, "bold")
color_1 = "yellow"
color_2 = "black"
 
wrapper = LabelFrame(main_window, text="Source File", font=font_1, fg="yellow", bg="black")
wrapper.pack(fill="both", expand="yes", padx=20, pady=20)
 
lbl = Label(wrapper, text="Source File", font=font_1, fg="yellow", bg="black")
lbl.pack(side=LEFT, padx=10, pady=10)
 
ent = Entry(wrapper, textvariable=t1, bd=3.5, bg="yellow", font=font_2, width= 32)
ent.pack(side=LEFT, padx=10, pady=10, ipady=5)
 
btn = Button(wrapper, text="Browse", command=browse_img, width=8, bg="yellow", font=font_1, bd=3.5)
btn.pack(side=LEFT, padx=10, pady=10)
 
btn_2 = Button(wrapper, text="Preview", command=preview_img, width=8, bg="yellow", font=font_1, bd=3.5)
btn_2.pack(side=LEFT, padx=10, pady=10)
 
wrapper_2 = LabelFrame(main_window, text="Image Details", font=font_1, fg="yellow", bg="black")
wrapper_2.pack(fill="both", expand="yes", padx=20, pady=20)
 
lbl_2 = Label(wrapper_2, text="Dimension:", font=font_1, fg="yellow", bg="black")
lbl_2.pack(side=LEFT, padx=10, pady=10)
 
ent_2 = Entry(wrapper_2, textvariable=w, bd=3.5, bg="yellow", font=font_2, width=10)
ent_2.pack(side=LEFT, padx=10, pady=10, ipady=5)
 
lbl_3 = Label(wrapper_2, text="X", font=font_1, fg="yellow", bg="black")
lbl_3.pack(side=LEFT, padx=10, pady=10)
 
ent_3 = Entry(wrapper_2, textvariable=h, bd=3.5, bg="yellow", font=font_2, width=10)
ent_3.pack(side=LEFT, padx=10, pady=10, ipady=5)

lbl_4 = Label(wrapper_2, text="Image Type:", font=font_1, fg="yellow", bg="black")
lbl_4.pack(side=LEFT, padx=10, pady=10)

ent_4 = Entry(wrapper_2, textvariable=img_type, bd=3.5, bg="yellow", font=font_2, width=10)
ent_4.bind("<Key>", lambda a: "break")
ent_4.pack(side=LEFT, padx=10, pady=10, ipady=5)

wrapper_3 = LabelFrame(main_window, text="Pixel Safe", font=font_1, fg="yellow", bg="black")
wrapper_3.pack(fill="both", expand="yes", padx=20, pady=20)
 
lbl_5 = Label(wrapper_3, text="Percentage:",font=font_1, fg="yellow", bg="black")
lbl_5.pack(side=LEFT, padx=10, pady=10)
 
ent_5 = Entry(wrapper_3, textvariable=perc, bd=3.5, bg="yellow", font=font_2, width=10)
ent_5.pack(side=LEFT, padx=10, pady=10, ipady=5)

lbl_6 = Label(wrapper_3, text="%", font=font_1, fg="yellow", bg="black")
lbl_6.pack(side=LEFT, padx=10, pady=10)
 
btn_3 = Button(wrapper_3, text="Recalculate Dimension", command=recalc, font=font_1, bg="yellow", bd=3.5)
btn_3.pack(side=LEFT, padx=10, pady=10)

wrapper_4 = LabelFrame(main_window, text="Changes", font=font_1, fg="yellow", bg="black")
wrapper_4.pack(fill="both", expand="yes", padx=20, pady=20)

lbl_7 = Label(wrapper_4, text="Quality:", font=font_1, fg="yellow", bg="black")
lbl_7.pack(side=LEFT, padx=10, pady=10)

ent_6 = Entry(wrapper_4, textvariable=qua, bd=3.5, bg="yellow", font=font_2, width=10)
ent_6.pack(side=LEFT, padx=10, pady=10, ipady=5)

lbl_8 = Label(wrapper_4, text="%", font=font_1, fg="yellow", bg="black")
lbl_8.pack(side=LEFT, padx=10, pady=10)

lbl_9 = Label(wrapper_4, text="Image type:", font=font_1, fg="yellow", bg="black")
lbl_9.pack(side=LEFT, padx=10, pady=10)

style = ttk.Style()
style.theme_use('alt')
style.configure('combo_resize.TCombobox', fieldbackground='yellow', selectbackground='blue', background='black', arrowcolor='yellow', arrowsize=15)

combo_resize = ttk.Combobox(wrapper_4, textvariable=option, style='combo_resize.TCombobox', font=font_2, width=7)
combo_resize["values"] = [".jpg", ".jpeg", ".png", ".ico", ".pdf"]
combo_resize.bind("<Key>", lambda a: "break")
combo_resize.option_add("*TCombobox*Listbox*Font", font_2)
combo_resize.option_add("*TCombobox*Listbox*selectBackground", color_2)
combo_resize.option_add("*TCombobox*Listbox*selectForeground", color_1)
combo_resize.option_add("*TCombobox*Listbox*background", color_1)
combo_resize.pack(side=LEFT, padx=10, pady=10, ipady=6)
combo_resize.current(0)

wrapper_5 = LabelFrame(main_window, text="Actions", font=font_1, fg="yellow", bg="black")
wrapper_5.pack(fill="both", expand="yes", padx=20, pady=20)
 
btn_4 = Button(wrapper_5, text="Preview", command=preview_new_img, width=8, font=font_1, bg="yellow", bd=3.5)
btn_4.pack(side=LEFT, padx=10, pady=10)
 
btn_5 = Button(wrapper_5, text="Save", command=save_new_img, width=8, font=font_1, bg="yellow", bd=3.5)
btn_5.pack(side=LEFT, padx=10, pady=10)
 
btn_6 = Button(wrapper_5, text="Clear", command=clear_all, width=8, font=font_1, bg="yellow", bd=3.5)
btn_6.pack(side=LEFT, padx=10, pady=10)

btn_7 = Button(wrapper_5, text="Exit", bd=3.5, width=8, font=font_1, bg="yellow", command=main_window.destroy)
btn_7.pack(side=LEFT, padx=10, pady=10)

main_window.mainloop()
