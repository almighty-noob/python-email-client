import tkinter as tk
def DAILY_BTN_PRESSED():
    main_window.quit()
    return True
main_window = tk.Tk()
main_window.title("Send Reports")
Daily_BTN = tk.Button(main_window, text="Send Daily Report", command=DAILY_BTN_PRESSED)
Status = tk.IntVar()
Status_BTN = tk.Checkbutton(main_window, text="Completed", variable=Status)
password = tk.StringVar()
password_field= tk.Entry(main_window, show="*",width=20, textvariable=password)

password_field.pack()
Daily_BTN.pack(padx=20, pady=20)
Status_BTN.pack(padx=20, pady=20)

main_window.mainloop()