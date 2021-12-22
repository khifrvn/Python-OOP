import tkinter

main_window = tkinter.Tk()  #----> Tk adalah object dari tkinter

label1 = tkinter.Label(main_window, text="Label1")
label2 = tkinter.Label(main_window, text="Label2")

# Method positioning

label1.pack()
label2.pack()

# Method menampilkan GUI

main_window.mainloop()