#Instalar libreria yagmail

#PERMITE ENVIAR CORREOS
#pip install yagmail[all]
#py -m pip install yagmail[all] --user

#LIBRERIA PARA TRANSFORMAR TXT A PDF
#pip install aspose-words

#pip install jinja2
#REEMPLAZA EL CONTENIDO DINAMICO, O LAS VARIABLES DEL TEMPLATE

#pip install pdfkit
#PERMITE GENERAR EL DOCUMENTO PDF A PARTIR DE UN TEMPLATE HTML

#apt-get install wkhtmltopdf
#FUNCIONA EN CONJUNTO CON PDFKIT PARA LOGRAR LA GENERACION DEL PDF

#--------------------------------------------------------------------------------------------------------------------------------------------

import yagmail
from fpdf import FPDF


def correollamar(nroVenta, nombre, apellido, pasajeroId, codVuelo, origen, destino, fechaVuelo, horaVuelo, valorTramo, corr):

    #direccion de correo el cual enviara correos
    email = 'vdapcorreoprueba@gmail.com'
    #Clave de aplicacion para el dispositivo
    passwordcorreo = 'qniyvvmkhumfhwyd'
    #Asignacion de cliente de yagmail
    yag = yagmail.SMTP(user=email, password=passwordcorreo)
    #Destinatarios de para el envio de correo, dentro de los corchetes van los correos que sera enviado el correo
    destinatarios = [f'{corr}']

    #--------------------------------------------------------------------------------------------------------------------------------------------

    #INFORMACION QUE VA DENTRO DEL CORREO
    #Asunto del correo
    asunto = '¡Realizaste tu check in con éxito!'
    #Mensaje
    mensaje = '<h2>¡Tu check-in está listo!</h2>'
    #Mensaje
    mensajeDos = f'<FONT SIZE=4; FACE="Arial Narrow">Hola {nombre} {apellido}, gracias por preferir Aerolínea VDAP, el siguiente correo contiene adjunta tu tarjeta de embarque.<br>Recuerda que debes llevarla impresa o de forma digital.</FONT>'
    #Mensaje
    mensajeTres = '<FONT SIZE=4; FACE="Arial Narrow">Por favor no responder el asunto de este correo, no va a ser respondido ya que es un bot automatico.</FONT>'
    #Imagen
    mensajeImagen = '<img src="https://imagenes.20minutos.es/files/image_990_v3/uploads/imagenes/2022/03/01/istock-955952680.jpeg" alt="" />'

    #--------------------------------------------------------------------------------------------------------------------------------------------

    #Variables en donde se adjunta los archivos para el cliente (Debe estar en la misma carpeta con el archivo .py)
    archivopdf = 'ClientePDF.pdf'

    #--------------------------------------------------------------------------------------------------------------------------------------------





    #--------------------------------------------------------------------------------------------------------------------------------------------
    
    #Se llama a la funcion FPDF
    pdf = FPDF()
    #Se agrega una pagina al pdf
    pdf.add_page()
    #Se instancia la clase pdf, primero es el tipo de fuente, la siguiente puede ser si quiere negrita o italy, ultimo el tamano
    pdf.set_font("arial", "", 10)


    #Se importa una imagen al pdf, este es el logo que esta el parte superior derecha
    pdf.image('https://i.imgur.com/2BvzpK9.png', w=50, h=25, x=148, y=12, )
    #Texto debajo del logo VDAP
    pdf.multi_cell(w=0, h=61, txt=f"VDAP Aerolinea. Sucursal Chile. Porvenir", align="R")
    #Texto sobre la introduccion al texto
    pdf.multi_cell(w=0, h=-13, txt=f"Este documento contiene el detalle y condiciones del servicio que adquiriste.\nINFORMACION DE TU PASAJE", align="L")

    #Color gris: r= 151 , g = 152, b = 152
    #Color Celeste de las casillas de la informacion
    pdf.set_fill_color(r=160,g=245,b=245)
    #Color Celeste sobre el borde casillas de la informacion
    pdf.set_draw_color(r=160,g=245,b=245)

    #Espacio para cada casilla
    pdf.cell(w=0, h=25, ln=1)
    #Informacion dentro de la casilla
    pdf.multi_cell(w=35, h=10, txt=f"Número de venta", align="L", border=1, fill=1)
    #Informacion escrita por el usuario
    pdf.multi_cell(w=85, h=-9, txt=f"  {nroVenta}", align="C", border=0, fill=0)

    #Espacio para cada casilla
    pdf.cell(w=0, h=10, ln=1)
    #Informacion dentro de la casilla
    pdf.multi_cell(w=40, h=10, txt=f"Nombre del Pasajero", align="L", border=1, fill=1)
    #Informacion escrita por el usuario
    pdf.multi_cell(w=110, h=-9, txt=f"  {nombre} {apellido}", align="C", border=0, fill=0)

    #Espacio para cada casilla
    pdf.cell(w=0, h=10, ln=1)
    #Informacion dentro de la casilla
    pdf.multi_cell(w=47, h=10, txt=f"Documento de identificacion", align="L", border=1, fill=1)
    #Informacion escrita por el usuario
    pdf.multi_cell(w=110, h=-9, txt=f"  {pasajeroId}", align="C", border=0, fill=0)

    #Espacio para cada casilla
    pdf.cell(w=0, h=10, ln=1)
    #Informacion dentro de la casilla
    pdf.multi_cell(w=47, h=10, txt=f"Código de Vuelo", align="L", border=1, fill=1)
    #Informacion escrita por el usuario
    pdf.multi_cell(w=110, h=-9, txt=f"  {codVuelo}", align="C", border=0, fill=0)

    #Espacio para cada casilla
    pdf.cell(w=0, h=10, ln=1)
    pdf.multi_cell(w=47, h=10, txt=f"Origen", align="L", border=1, fill=1)
    #Informacion escrita por el usuario
    pdf.multi_cell(w=110, h=-9, txt=f"  {origen}", align="C", border=0, fill=0)

    #Espacio para cada casilla
    pdf.cell(w=0, h=35, txt=f"ITINERARIO", ln=1)

    #
    pdf.cell(w=0, h=-10, ln=1)
    #Informacion dentro de la casilla
    pdf.multi_cell(w=45, h=10, txt=f"Destino", align="L", border=1, fill=1)
    #Informacion escrita por el usuario
    pdf.multi_cell(w=105, h=-9, txt=f"  {destino}", align="C", border=0, fill=0)

    #Espacio para cada casilla
    pdf.cell(w=0, h=10, ln=1)
    #Informacion dentro de la casilla
    pdf.multi_cell(w=40, h=10, txt=f"Fecha de Vuelo", align="L", border=1, fill=1)
    #Informacion escrita por el usuario
    pdf.multi_cell(w=105, h=-9, txt=f"  {fechaVuelo}", align="C", border=0, fill=0)

    #Espacio para cada casilla
    pdf.cell(w=0, h=10, ln=1)
    #Informacion dentro de la casilla
    pdf.multi_cell(w=47, h=10, txt=f"Hora de vuelo", align="L", border=1, fill=1)
    #Informacion escrita por el usuario
    pdf.multi_cell(w=110, h=-9, txt=f"  {horaVuelo}", align="C", border=0, fill=0)

    #Espacio para cada casilla
    pdf.cell(w=0, h=10, ln=1)
    #Informacion dentro de la casilla
    pdf.multi_cell(w=47, h=10, txt=f"Valor", align="L", border=1, fill=1)
    #Informacion escrita por el usuario
    pdf.multi_cell(w=110, h=-9, txt=f"{valorTramo}", align="C", border=0, fill=0)

    #Espacio para cada casilla
    pdf.cell(w=0, h=10, ln=1)
    #Informacion dentro de la casilla
    pdf.multi_cell(w=40, h=10, txt=f"Email de Contacto", align="L", border=1, fill=1)
    #Informacion escrita por el usuario
    pdf.multi_cell(w=140, h=-9, txt=f"{corr}", align="C", border=0, fill=0)

    #Espacio para cada casilla
    pdf.cell(w=0, h=60, ln=1)
    #Informacion de footer del pdf
    pdf.multi_cell(w=190, h=10, txt=f"AEROLINEA VDAP. PORVENIR. 2022 ", align="C", border=1, fill=1)

    #Imagen del logo en el footer
    pdf.image('https://i.imgur.com/2BvzpK9.png', w=50, h=25, x=79, y=257, )

    #Salida del PDF para poder enviarlo al correo
    pdf.output("ClientePDF.pdf")

    #--------------------------------------------------------------------------------------------------------------------------------------------

    #Llamada para enviar el correo
    yag.send(destinatarios, asunto, [mensaje, mensajeDos, mensajeTres, mensajeImagen], attachments=[archivopdf])

    #---------------------------------------------------------------
    #Desde el terminal debe ingresar a la carpeta donde se encuentra el archivo .py
    #cd C:\Users\Matia\OneDrive\Escritorio\yang
    #Luego ejecutar py correoenvio.py