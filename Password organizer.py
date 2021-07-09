import tkinter as tk
import hashlib

username = ""
all_info = []
current_data_read = ""


class App:
    def __init__(self, root):
        self.root = root

    def login(self):
        try:
            info = open(r"C:\Users\DELL\Desktop\Code\Python\Applications\Password organizer\Users\\" + self.username.get() + ".txt", "r")
            if info.read() == hashlib.sha256(self.password.get().encode('utf-8')).hexdigest():
                global username
                username = self.username.get()
                self.login_btn.place_forget()
                self.password.place_forget()
                self.pass_label.place_forget()
                self.user_label.place_forget()
                self.username.place_forget()
                self.register_btn.place_forget()
                self.dashboard()
            info.close()
        except:
            pass

    def register(self):
        self.confirm_pass_label = tk.Label(self.root, text="Confirm:")
        self.confirm_pass_label.place(x=2, y=90)
        self.confirm_password = tk.Entry(self.root)
        self.confirm_password.place(x=70, y=90)

        self.login_btn.place_forget()
        self.register_btn.place_forget()

        self.conf_login_btn = tk.Button(self.root, text="Confirm", border=2, command=lambda: self.register_account())
        self.conf_login_btn.place(x=75, y=130)

    def register_account(self):
        if str(self.password.get()) != str(self.confirm_password.get()):
            self.username.place_forget()
            self.password.place_forget()
            self.user_label.place_forget()
            self.pass_label.place_forget()
            self.create_login()

        new_acc = open(r"C:\Users\DELL\Desktop\Code\Python\Applications\Password organizer\Users\\" + str(self.username.get()) + ".txt", "w")
        save = hashlib.sha256(self.password.get().encode('utf-8')).hexdigest()
        new_acc.write(str(save))
        new_acc.close()
        self.username.place_forget()
        self.password.place_forget()
        self.user_label.place_forget()
        self.pass_label.place_forget()
        self.create_login()

    def create_login(self):
        self.user_label = tk.Label(self.root, text="Username:")
        self.user_label.place(x=2, y=30)
        self.username = tk.Entry(self.root)
        self.username.place(x=70, y=30)

        self.pass_label = tk.Label(self.root, text="Password:")
        self.pass_label.place(x=2, y=60)
        self.password = tk.Entry(self.root)
        self.password.place(x=70, y=60)

        try:
            self.login_btn.place(x=75, y=100)
            self.register_btn.place(x=70, y=130)
        except:
            self.login_btn = tk.Button(self.root, text="Login", border=2, command=lambda: self.login())
            self.login_btn.place(x=75, y=100)
            self.register_btn = tk.Button(self.root, text="Register", border=2, command=lambda: self.register())
            self.register_btn.place(x=70, y=130)
 
        try:
            self.conf_login_btn.place_forget()
            self.confirm_password.place_forget()
            self.confirm_pass_label.place_forget()
        except:
            pass

    def dashboard(self):
        self.receiver = tk.Entry(self.root)
        self.receiver.place(x=70, y=5)
        self.get_btn = tk.Button(self.root, text="Get", border=2, command=lambda: self.receive(), width=7, height=1)
        self.get_btn.place(x=2, y=6)
        self.save_btn = tk.Button(self.root, text="Save data", border=2, command=lambda: self.save(), width=7, height=1)
        self.save_btn.place(x=2, y=160)

    def save(self):
        self.receiver.place_forget()
        self.get_btn.place_forget()
        self.save_btn.place_forget()
    
        for verify in range(5):
            try:
                self.info_label.place_forget()
            except:
                break

        self.username_save = tk.Entry(self.root)
        self.username_save.place(x=70, y=5)
        self.username_save_label = tk.Label(self.root, text="Username:")
        self.username_save_label.place(x=2, y=5)

        self.password_save = tk.Entry(self.root)
        self.password_save.place(x=70, y=50)
        self.password_save_label = tk.Label(self.root, text="Password:")
        self.password_save_label.place(x=2, y=50)

        self.save_btn_confirm = tk.Button(self.root, text="Save", command=lambda: self.save_data())
        self.save_btn_confirm.place(x=2, y=160)

    def save_data(self):
        self.save_btn_confirm.place_forget()
        self.password_save.place_forget()
        self.password_save_label.place_forget()
        self.username_save.place_forget()
        self.username_save_label.place_forget()
        file = open(r"C:\Users\DELL\Desktop\Code\Python\Applications\Password organizer\Information\\" + hashlib.sha256(str(self.username.get() + "-" + self.username_save.get()).encode('utf-8')).hexdigest(), "w")
        file.write(str(self.username_save.get()) + " : " + str(self.password_save.get()))
        file.close()
        self.dashboard()

    def receive(self):
        try:
            global current_data_read
            info = open(r"C:\Users\DELL\Desktop\Code\Python\Applications\Password organizer\Information\\" + hashlib.sha256(str(self.username.get() + "-" + self.receiver.get()).encode('utf-8')).hexdigest(), "r")
            self.info_label = tk.Label(self.root, text=str(info.read()))
            self.info_label.place(x=0, y=60)
            current_data_read = str(info.read())
            info.close()
        except:
            nothing = tk.Label(self.root, text="Doesn't exist")
            nothing.place(w=0, y=30)

    def general_login(self):
        self.create_login()
        self.root.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.general_login()