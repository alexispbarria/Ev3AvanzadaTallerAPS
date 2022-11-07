from email.utils import parsedate_tz
from textwrap import fill
import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
from ..admin import usuarios as u
from  ..admin import itinerarios as i
from forms import form_login as fl


class AdminMenus:
    
    def menuAdmin(self):

        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Menú Administrador')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.YES, fill=tk.BOTH)

        #Frame superior, ocupado por el texto Menú administrador.
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Menú Administrador", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.Y)

        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)

        #Gestión de usuarios
        
        gestionUsuarios = tk.Button(frame_form_access, text="Gestionar Usuarios", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirGestionUsuarios)
        gestionUsuarios.pack(fill=tk.X, padx=20, pady=20)
        gestionUsuarios.bind("<Return>", (lambda event: self.abrirGestionUsuarios()))

        #Gestión de itinerarios
        
        gestionItinerarios = tk.Button(frame_form_access, text="Gestionar Itinerarios", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirGestionItinerarios)
        gestionItinerarios.pack(fill=tk.X, padx=20, pady=20)
        gestionItinerarios.bind("<Return>", (lambda event: self.abrirGestionItinerarios()))

        #Cerrar sesión
        cerrarSesion = tk.Button(frame_form_access, text="Cerrar sesión", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abririniciosesion)
        cerrarSesion.pack(fill=tk.X, padx=20, pady=20)
        gestionItinerarios.bind("<Return>", (lambda event: self.abririniciosesion()))

        self.ventana.mainloop()

    def menuUsuariosAdm(self):
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Gestión de Usuarios')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.YES, fill=tk.BOTH)

        #Frame superior, ocupado por el texto Menú administrador.
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Gestión de Usuarios", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.Y)

        #Imágen
        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)


        #Ver usuarios
        verUsuarios = tk.Button(frame_form_access, text="Ver Usuarios", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirAllUsuarios)
        verUsuarios.pack(fill=tk.X, padx=20, pady=20)
        verUsuarios.bind("<Return>", (lambda event: u.User.abrirAllUsuarios()))

        #Agregar usuario
        
        agregarUsuario = tk.Button(frame_form_access, text="Agregar Usuario", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirAgregarUsuario)
        agregarUsuario.pack(fill=tk.X, padx=20, pady=20)
        agregarUsuario.bind("<Return>", (lambda event: u.User.abrirAgregarUsuario()))

        #Modificar usuario
        
        modificarUsuario = tk.Button(frame_form_access, text="Modificar Usuario", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirModificarUsuario)
        modificarUsuario.pack(fill=tk.X, padx=20, pady=20)
        modificarUsuario.bind("<Return>", (lambda event: u.User.abrirModificarUsuario()))

        #Eliminar usuario
        
        eliminarUsuario = tk.Button(frame_form_access, text="Eliminar Usuario", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirEliminarUsuario)
        eliminarUsuario.pack(fill=tk.X, padx=20, pady=20)
        eliminarUsuario.bind("<Return>", (lambda event: u.User.abrirEliminarUsuario()))

        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.menuAnterior)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.menuAnterior()))

        self.ventana.mainloop()

    def menuItinerariosAdm(self):
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Gestión de Itinerarios')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.YES, fill=tk.BOTH)

        #Frame superior, ocupado por el texto Menú administrador.
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Gestión de Itinerarios", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.Y)

        #Imágen
        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)


         #Visualizar Itinerarios
        
        verItinerarios = tk.Button(frame_form_access, text="Visualizar Itinerarios", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirVisualizacionItinerarios)
        verItinerarios.pack(fill=tk.X, padx=20, pady=20)
        verItinerarios.bind("<Return>", (lambda event: self.abrirVisualizacionItinerarios()))

        #Agregar itinerarios
        
        agregarItinerario = tk.Button(frame_form_access, text="Agregar Itinerario", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirAddItinerario)
        agregarItinerario.pack(fill=tk.X, padx=20, pady=20)
        agregarItinerario.bind("<Return>", (lambda event: self.abrirAddItinerario()))

        #Modificar Itinerarios
        
        modificarItinerario = tk.Button(frame_form_access, text="Modificar Itinerario", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirModificarItinerario)
        modificarItinerario.pack(fill=tk.X, padx=20, pady=20)
        modificarItinerario.bind("<Return>", (lambda event: self.abrirModificarItinerario()))

        #Eliminar itinerarios
        
        eliminarItinerario = tk.Button(frame_form_access, text="Eliminar Itinerario", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirEliminarItinerario)
        eliminarItinerario.pack(fill=tk.X, padx=20, pady=20)
        eliminarItinerario.bind("<Return>", (lambda event: self.abrirEliminarItinerario()))


        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.menuAnterior)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.menuAnterior()))

        self.ventana.mainloop()

    def menuItinerariosFiltros(self):
        #Configuración básica de la ventana
        self.ventana = tk.Tk()                             
        self.ventana.title('Visualizar Itinerarios')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()                                    
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        #frame para el título.
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(expand=tk.YES, fill=tk.BOTH)

        #Frame superior, ocupado por el texto Menú administrador.
        frame_form_top = tk.Frame(frame_form, height=20, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack (side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text= "Visualizar Itinerarios", font=('Times', 30, BOLD), fg='#fcfcfc', bg="#3a7ff6", pady=50)
        title.pack(expand=tk.NO, fill=tk.BOTH)

        #Botones de acceso.
        frame_form_access = tk.Frame(frame_form, height= 50, bd=0, relief=tk.SOLID, bg ='#fcfcfc')
        frame_form_access.pack(side="bottom", expand=tk.YES, fill=tk.Y)


        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        labelLogo = tk.Label(frame_form_access, image=logo, bg='#fcfcfc')
        labelLogo.pack(fill=tk.X, padx=20, pady=10)


         #Visualizar Itinerarios totales
        
        totalItinerarios = tk.Button(frame_form_access, text="Visualizar total de Itinerarios", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirAllItinerarios)
        totalItinerarios.pack(fill=tk.X, padx=20, pady=20)
        totalItinerarios.bind("<Return>", (lambda event: self.abrirAllItinerarios()))

        #Buscar por código
        
        verCodItinerario = tk.Button(frame_form_access, text="Buscar Itinerario por código", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command= self.abrirBuscarItinCodigo)
        verCodItinerario.pack(fill=tk.X, padx=20, pady=20)
        verCodItinerario.bind("<Return>", (lambda event: i.itinera.abrirBuscarItinCodigo()))

        #Buscar por fecha
        
        verFechaItinerario = tk.Button(frame_form_access, text="Buscar itinerario por fecha", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirBuscarItinFecha)
        verFechaItinerario.pack(fill=tk.X, padx=20, pady=20)
        verFechaItinerario.bind("<Return>", (lambda event: i.itinera.abrirBuscarItinFecha()))


        #Volver al menú anterior
        menuAnterior = tk.Button(frame_form_access, text="Volver al Menú Anterior", font=('Times', 15, BOLD),fg='#fcfcfc', bg="#3a7ff6", command=self.abrirGestionItinerarios)
        menuAnterior.pack(fill=tk.X, padx=20, pady=20)
        menuAnterior.bind("<Return>", (lambda event: self.abrirGestionItinerarios()))

        self.ventana.mainloop()



    #FUNCIONES DE BOTONES
    def menuAnterior(self):
        self.ventana.destroy()
        self.menuAdmin()

    def abrirGestionUsuarios(self):
        self.ventana.destroy()
        self.menuUsuariosAdm()

    def abrirGestionItinerarios(self):
        self.ventana.destroy()
        self.menuItinerariosAdm()

    def abrirVisualizacionItinerarios(self):
        self.ventana.destroy()
        self.menuItinerariosFiltros()

    def abrirAllItinerarios(self):
        self.ventana.destroy()
        i.itinera.allItinerarios(self)

    def abrirAllUsuarios(self):
        self.ventana.destroy()
        u.User.allUsers(self)

    def abrirAgregarUsuario(self):
        self.ventana.destroy()
        u.User().addUsuarioTrabajador()

    def abrirModificarUsuario(self):
        self.ventana.destroy()
        u.User().modificarUsuario()

    def abrirEliminarUsuario(self):
        self.ventana.destroy()
        u.User().eliminarUsuario()


        #itinerarios

    def abrirBuscarItinCodigo(self):
        self.ventana.destroy()
        i.itinera().itinerarioPorCodigo()

    def abrirBuscarItinFecha(self):
        self.ventana.destroy()
        i.itinera().itinerarioPorFecha()
    def abrirAddItinerario(self):
        self.ventana.destroy()
        i.itinera().addItinerario()

    def abrirEliminarItinerario(self):
        self.ventana.destroy()
        i.itinera().deleteItinerario()

    def abrirModificarItinerario(self):
        self.ventana.destroy()
        i.itinera().modificarItinerario()
    
    def abririniciosesion(self):
        self.ventana.destroy()
        fl.App()