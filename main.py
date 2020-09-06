import tkinter as tk
import tkinter.font as tkFont



class MainMenu:
        def __init__(self):
            #Se crea la ventana
            self.mainWindow = tk.Tk()
            self.mainWindow.title("Login")
            self.mainWindow.geometry("360x240")
            self.mainWindow.resizable(0,0)
            self.mainWindow.configure(bg="#36393f")
            self.customFont=tkFont.Font(family="Uni Sans Heavy",weight="bold")
            self.customFont2 = tkFont.Font(family="Uni Sans")



            # Se crea el cuadro de ID y pass.
            self.login = tk.LabelFrame(self.mainWindow, text="Login:",bg="#36393f",fg="Dim Gray",font=self.customFont)
            self.login.grid(column=0, row=0, padx=5, pady=10)

            #Se crea el cuadro añadir usuario.
            self.registro = tk.LabelFrame(self.mainWindow, text="¿No tienes usuario?",bg="#36393f",fg="Dim Gray", font=self.customFont)
            self.registro.grid(column=0, row=1, padx=8, pady=10)




            #Se crea el campo ID
            self.ID=tk.Label(self.login,text=" Nombre de usuario: ",bg="#36393f",fg="white", font=self.customFont2)
            self.ID.grid(column=0,row=0,padx=4,pady=4)
            self.ID_Valor=tk.Entry(self.login)
            self.ID_Valor.grid(column=1, row=0, padx=4, pady=4)
            #Se crea el campo Pass
            self.Password = tk.Label(self.login, text=" Contraseña: ",bg="#36393f",fg="white", font=self.customFont2)
            self.Password.grid(column=0, row=1, padx=4, pady=4)
            self.Password_Valor = tk.Entry(self.login, show="*")
            self.Password_Valor.grid(column=1, row=1, padx=4, pady=4)
            #Se crea el Boton entrar
            self.Entrar_button= tk.Button(self.login, text="Entrar",bg="#36393f",fg="white", font=self.customFont2, commamd=self.validate(self.ID_Valor.get(), self.Password_Valor.get()))
            self.Entrar_button.grid(column=1, row=2, padx=4, pady=10)
            #Se crea el boton agregar Usuario
            self.addUser= tk.Button(self.registro, text=" Registrate! ",bg="#36393f",fg="white", font=self.customFont2)
            self.addUser.grid(column=0, row=2, padx=8, pady=8,ipadx=85)

            self.mainWindow.mainloop()

        def validate(self, id, password):
            self.id=id
            self.password=password

            
gestor = MainMenu()