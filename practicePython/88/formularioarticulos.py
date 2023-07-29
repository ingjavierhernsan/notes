import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import articulos

class FormularioArticulos:
    def __init__(self):
        self.articulo1=articulos.Articulos()

        self.ventana1=tk.Tk()
        self.ventana1.title("Mantenimiento de articulos")

        self.cuaderno1=ttk.Notebook(self.ventana1)

        self.carga_articulos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)

        self.ventana1.mainloop()

    def carga_articulos(self):
        self.pagina1=ttk.Frame(self.cuaderno1)

        self.cuaderno1.add(self.pagina1, text="Carga de articulos")

        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Articulo")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe1, text="Descripcion:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        self.descripcioncarga=tk.StringVar()

        self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe1, text="Precio:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)

        self.preciocarga=tk.StringVar()

        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def agregar(self):
        datos=(1, self.descripcioncarga.get(), self.preciocarga.get())
        
        self.articulo1.alta(datos)

        mb.showinfo("Informacion", "Los datos fueron cargados")

        self.descripcioncarga.set("")
        self.preciocarga.set("")

    def consulta_por_codigo(self):
        self.pagina2=ttk.Frame(self.cuaderno1)

        self.cuaderno1.add(self.pagina2, text="Consulta por codigo")

        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Articulo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe2, text="Codigo:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        self.codigo=tk.StringVar()

        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe2, text="Descripcion:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)

        self.descripcion=tk.StringVar()

        self.entrydescripcion=ttk.Entry(self.labelframe2, textvariable=self.descripcion, state="readonly")
        self.entrydescripcion.grid(column=1, row=2, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos=(self.codigo.get(),)
        respuesta=self.articulo1.consulta(datos)

        if len(respuesta)>0:
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:
            self.descripcion.set('')
            self.precio.set('')
            mb.showinfo("Informacion", "No existe un articulo con dicho codigo.")

    def listado_completo(self):
        self.pagina3=ttk.Frame(self.cuaderno1)
        
        self.cuaderno1.add(self.pagina3, text="Listado completo")

        self.labelframe3=ttk.LabelFrame(self.pagina2, text="Articulo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)

        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)

        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0, row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "codigo: "+str(fila[0])+"\nDescripcion: "+fila[1]+"\nPrecio: "+str(fila[2])+"\n\n")

aplicacion1=FormularioArticulos()