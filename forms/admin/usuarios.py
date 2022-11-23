import tkinter as tk
from tkinter.font import BOLD
from tkinter import ttk, messagebox
import conexion
import util.generic as utl
import bcrypt
from ..admin import form_admin as fa
from forms import form_login as fl

# USUARIOS
class User:
    def allUsers(self):
        db = conexion.get_db()

        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Total de Usuarios')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.NO, fill=tk.BOTH)

        #Frame superior, ocupado por el texto Menú administrador.
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Total de Usuarios", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        listado = ttk.Treeview(frame_form_access, columns=('#0', '#1'))
        listado.pack(fill=tk.X, padx=20, pady=5)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Times', 14))
        style.configure("Treeview.Heading", font=('Times', 15))

        
        #Nombre de las columnas 
        listado.heading('#0', text="ID Usuario")
        listado.heading('#1', text="Nombre Usuario")
        listado.heading('#2', text="Contraseña")
        

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirGestionUsuarios)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirGestionUsuarios()))

        users = db.trabajadorUsers.find({})
        for user in users:
            listado.insert( "", 
                            tk.END,
                            text=user["_id"],
                            values = (user["nombreUsuario"], "******") 
                            )
            

        self.ventana.mainloop()


    def addUsuarioTrabajador(self):

        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Agregar Usuario Trabajador')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.NO, fill=tk.BOTH)

        #Frame superior, ocupado por el texto de título
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Agregar Usuarios", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="top", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)


        ####### POR CONFIGURAR.

        # Inserción de ID, con un Entry para escribir
        etiqueta_id = tk.Label(frame_form_access, text="Inserte ID", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_id.pack(fill=tk.X, padx=20, pady=5)
        self.id = ttk.Entry(frame_form_access, font=('Times', 14))
        self.id.pack(fill=tk.BOTH, padx=20, pady=10)

        #Inserción de Nombre de Usuario, con un Entry para escribir
        etiqueta_nombreUsuario = tk.Label(frame_form_access, text="Inserte Nombre de usuario", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_nombreUsuario.pack(fill=tk.X, padx=20, pady=5)
        self.nombreUsuario = ttk.Entry(frame_form_access, font=('Times', 14))
        self.nombreUsuario.pack(fill=tk.BOTH, padx=20, pady=10)
    

        #Inserción de contraseña, con un Entry para escribir
        etiqueta_contrasena = tk.Label(frame_form_access, text="Inserte Contraseña", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_contrasena.pack(fill=tk.X, padx=20, pady=5)
        self.contra = ttk.Entry(frame_form_access, font=('Times', 14))
        self.contra.pack(fill=tk.BOTH, padx=20, pady=10)
        self.contra.config(show="*")
        

        agregar = tk.Button(frame_form_access, text="Agregar Usuario", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonAgregar)
        agregar.pack(fill=tk.X, padx=20, pady=20)
        agregar.bind("<Return>", (lambda event: self.botonAgregar()))

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirGestionUsuarios)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirGestionUsuarios()))
            

        self.ventana.mainloop()

    def modificarUsuario(self):
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Modificar Usuario Trabajador')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.NO, fill=tk.BOTH)

        #Frame superior, ocupado por el texto de título
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Modificar Usuarios", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="top", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        #SOLICITUD DE LA ID DEL USUARIO A MODIFICAR
        etiqueta_id = tk.Label(frame_form_access, text="Inserte ID del usuario a modificar", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_id.pack(fill=tk.X, padx=20, pady=5)
        self.idModificarUser = ttk.Entry(frame_form_access, font=('Times', 14))
        self.idModificarUser.pack(fill=tk.BOTH, padx=20, pady=10)

        etiqueta_nombreUsuario = tk.Label(frame_form_access, text="Modificar Nombre de Usuario (opcional)", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_nombreUsuario.pack(fill=tk.X, padx=20, pady=5)
        self.modUsuario = ttk.Entry(frame_form_access, font=('Times', 14))
        self.modUsuario.pack(fill=tk.BOTH, padx=20, pady=10)
        #boton modificar nombre de usuario
        modNomUsuario =  tk.Button(frame_form_access, text="Modificar Nombre de Usuario", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonModificarNomUsu)
        modNomUsuario.pack(fill=tk.X, padx=20, pady=20)
        modNomUsuario.bind("<Return>", (lambda event: self.botonModificarNomUsu()))


        etiqueta_contrasena = tk.Label(frame_form_access, text="Modificar Contraseña (opcional)", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_contrasena.pack(fill=tk.X, padx=20, pady=5)
        self.modContrasena = ttk.Entry(frame_form_access, font=('Times', 14))
        self.modContrasena.pack(fill=tk.BOTH, padx=20, pady=10)
        self.modContrasena.config(show="*")
        #boton modificar contraseña de usuario
        modContrasenaUsuario =  tk.Button(frame_form_access, text="Modificar Contraseña", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.botonModificarContrasenaUsu)
        modContrasenaUsuario.pack(fill=tk.X, padx=20, pady=20)
        modContrasenaUsuario.bind("<Return>", (lambda event: self.botonModificarContrasenaUsu()))

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirGestionUsuarios)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirGestionUsuarios()))

        self.ventana.mainloop()

    def eliminarUsuario(self):
        db = conexion.get_db()
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Eliminar Usuario Trabajador')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.NO, fill=tk.BOTH)

        #Frame superior, ocupado por el texto de título
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Eliminar Usuario Trabajador", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="top", expand=tk.YES, fill=tk.NONE)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        #SOLICITUD DE LA ID DEL USUARIO A MODIFICAR
        etiqueta_id = tk.Label(frame_form_access, text="Inserte ID del usuario a eliminar", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_id.pack(fill=tk.X, padx=20, pady=5)
        self.idEliminarUser = ttk.Entry(frame_form_access, font=('Times', 14))
        self.idEliminarUser.pack(fill=tk.BOTH, padx=20, pady=10)

        deleteUsuario =  tk.Button(frame_form_access, text="Eliminar Usuario", font=('Times', 14, BOLD), bg='#3a7ff6', bd=0, fg="#fff", command= self.botonEliminarUser)
        deleteUsuario.pack(fill=tk.X, padx=20, pady=20)
        deleteUsuario.bind("<Return>", (lambda event: self.botonEliminarUser()))

        listadoUsers = tk.Label(frame_form_access, text="Listado completo de usuarios", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        listadoUsers.pack(fill=tk.X, padx=20, pady=5)
        listado = ttk.Treeview(frame_form_access, columns=('#0'))
        listado.pack(fill=tk.X, padx=20, pady=20)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", font=('Times', 14))
        style.configure("Treeview.Heading", font=('Times', 15))

        
        #Nombre de las columnas 
        listado.heading('#0', text="ID Usuario")
        listado.heading('#1', text="Nombre Usuario")

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirGestionUsuarios)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirGestionUsuarios()))

        users = db.trabajadorUsers.find({})
        for user in users:
            listado.insert( "", 
                            tk.END,
                            text=user["_id"],
                            values = (user["nombreUsuario"]) 
                            )

        self.ventana.mainloop()

            #FUNCIONES DE BOTONES
    def menuAnterior(self):
        self.ventana.destroy()
        fa.AdminMenus.menuAdmin(self)

    def abrirGestionUsuarios(self):
        self.ventana.destroy()
        fa.AdminMenus.menuUsuariosAdm(self)

    def abrirGestionItinerarios(self):
        self.ventana.destroy()
        fa.AdminMenus().menuItinerariosAdm()

    def abrirVisualizacionItinerarios(self):
        self.ventana.destroy()
        fa.AdminMenus().menuItinerariosFiltros(self)

    def abrirAllUsuarios(self):
        self.ventana.destroy()
        self.allUsers()

    def abrirAgregarUsuario(self):
        self.ventana.destroy()
        self.addUsuarioTrabajador()

    def abrirModificarUsuario(self):
        self.ventana.destroy()
        self.modificarUsuario()

    def abrirEliminarUsuario(self):
        self.ventana.destroy()
        self.eliminarUsuario()

    def abririniciosesion(self):
        self.ventana.destroy()
        fl.App()


    #FUNCIONES MONGODB
    def botonAgregar(self):
        db = conexion.get_db()
        idUser = self.id.get()
        nomUsu =self.nombreUsuario.get()
        passw = self.contra.get()
        passw = passw.encode()
        sal = bcrypt.gensalt()
        passw_hasheada = bcrypt.hashpw(passw, sal)

        tusers = db.trabajadorUsers.find({},{"nombreUsuario": 1, "_id": 0})
        for user in tusers:
            username = (str.format(user["nombreUsuario"]))

            if idUser == "" or nomUsu == "" or passw == "":
                messagebox.showerror(message="No puede insertar valores vacíos", title="Error")
                return tusers
            if nomUsu == username:
                messagebox.showerror(message="El nombre de usuario se encuentra ocupado", title="Error")
                return tusers
            else:
                if len(passw) < 4:
                    messagebox.showerror(message="La contraseña debe contener al menos 4 caracteres.", title="Error")
                    return
                else: 
                    insertarUser  = db.trabajadorUsers.insert_one(
                    {
                        "_id": idUser,
                        "nombreUsuario": nomUsu,
                        "password": passw_hasheada
                    })
                    messagebox.showinfo(message="Usuario agregado correctamente", title="Felicidades")
                    
                    self.abrirAllUsuarios()
                    return insertarUser


        

    def botonModificarNomUsu(self):
        db = conexion.get_db()
        idUser = self.idModificarUser.get()
        nomUsua = self.modUsuario.get()
        itinerarios = db.trabajadorUsers.find({})
        for itin in itinerarios:
            itinid = (str.format(itin["_id"]))
            if idUser == itinid:
                if nomUsua == "": 
                    messagebox.showerror(message="No puede insertar valores vacíos", title="Error")
                else:
                    moduser = db.trabajadorUsers.update_one(
                        {"_id": {"$regex": idUser, "$options": "i"}},
                        {
                            '$set': {
                                "nombreUsuario": nomUsua
                            }
                        }
                    )
                    messagebox.showinfo(message="Nombre de Usuario Modificado Correctamente", title="Felicidades")

                    self.abrirAllUsuarios()
                    return moduser
        else:
            messagebox.showinfo(message="El id del user no existe", title="Error")

    def botonModificarContrasenaUsu(self):
        db = conexion.get_db()
        idUser = self.idModificarUser.get()
        modPass = self.modContrasena.get()
        itinerarios = db.trabajadorUsers.find({})
        for itin in itinerarios:
            itinid = (str.format(itin["_id"]))
            if idUser == itinid: 
                if modPass == "":
                    messagebox.showerror(message="No puede insertar valores vacíos", title="Error")
                    return itinerarios
                else:
                    if len(modPass) < 4:
                        messagebox.showerror(message="La contraseña debe contener al menos 4 caracteres.", title="Error")
                        return itinerarios
                    else:
                        modPass = modPass.encode()
                        sal = bcrypt.gensalt()
                        passw_hasheada1 = bcrypt.hashpw(modPass, sal)
                        moduser = db.trabajadorUsers.update_one(
                            {"_id": {"$regex": idUser, "$options": "i"}},
                            {
                                '$set': {
                                    "password": passw_hasheada1
                                }
                            }
                        )
                        messagebox.showinfo(message="Contraseña Modificada Correctamente", title="Felicidades")

                        self.abrirAllUsuarios()
                        return moduser
        else:
            messagebox.showinfo(message="El id del user no existe", title="Error")

    def botonEliminarUser(self):
        db = conexion.get_db()
        idUser = self.idEliminarUser.get()
        itinerarios = db.trabajadorUsers.find({})
        for itin in itinerarios:
            itinid = (str.format(itin["_id"]))
            if idUser == itinid: 
                deleteuser = db.trabajadorUsers.delete_one({"_id": {"$regex": idUser, "$options": "i"}})
                messagebox.showinfo(message="Usuario Eliminado Correctamente.", title="Felicidades")
                self.abrirEliminarUsuario()
                return deleteuser
        else:
            messagebox.showinfo(message="El id del user no existe", title="Error")