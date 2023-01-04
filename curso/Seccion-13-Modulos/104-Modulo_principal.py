#l primer archivo ejcutado es el principal y python lo llamaara __main__
#los demas archivos ejecutados despues de este tendran el nombre del archivo sin la extencion .py
print(__name__)

#punto de entrada oficial de toda plicacion python
if __name__ == "__main__":
    print("siuu")


#NOMENCLATURA DE MODULOS
#A ecepcion de archivos de nivel superior todos tiene que tener la ext .py o reconocida
#no pudeen tener palabras reservadas de python
#nombres instrucciones building como list/dict/def...
#esto mismo generara error con las carpetas
