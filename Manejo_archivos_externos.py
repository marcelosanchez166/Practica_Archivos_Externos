"""Los archivos externos se trabajan con el modulo io de la biblioteca estandar de python """

#Se usa para persistencia de datos
#Se pueden manejar de dos formas: archivos externos de texto plano o bianrio y base de datos

"""Fases necesarias para guardar informacion en archivos externos"""
#Creacion > Apertura > Manipulacion > Cierre 

from io import open#Metodo para abrir archivo externo

archivo=open("Archivo.txt", "w")#Se le pasan dos argumentos, el nombre del archivo y el modo en el que se abrira el archivo(lectura=r, 
#escritura=w, append=agregar info a un archivo que ya contiene informacion)
#Son esto ya se creo el archivo 
Frase="El manejo de archivos externos es genial pero confuso"
archivo.write(Frase)
archivo.close()



"""##############   Metodo para leer un archivo que ya contiene texto #########################"""

archivo=open("Archivo.txt","r")
texto=archivo.read()#tambien esta el metodo """readlines""" y lee la informacion del archivo linea a linea y la almacena en una lista
archivo.close()
print(texto)


"""####################### Metodo readlines ##################################"""

archivo=open("Archivo.txt","r")
lista=archivo.readlines()#metodo """readlines""" lee la informacion del archivo linea a linea y la almacena en una lista
archivo.close()
#for i in range(len(lista)):
print(lista)


"""########################### Metodo para agregar mas info a un archivo ###############################"""

archivo=open("Archivo.txt","a")# """a""" del metodo append
archivo.write("\n ya estoy entendiendo los archivos externos ")
archivo.close() 


"""##############################Metodo para poder elegir la posicion del puntero###################################"""


archivo=open("Archivo.txt","r")

archivo.seek(11)#Con el metodo seek le digo desde que caracter debe mostrar, por lo que mostrara desde el caracter 11

#TAmbien se puede hacer con el metodo read de la siguiente manera
print(archivo.read(11))#La diferencia es que read mostrar solo los primero 11 caracteres 

print(archivo.read())#En este caso despues de mostrar los primero 11 caracter en la parte de arriba con read, mostrara los caracteres 
#restantes 

"""con el siguiente podemos posicionar el puntero en medio del texto que tiene el archivo"""

archivo.seek(len(archivo.read())/2)#COn esto estaria mostrando solo la mitad ultima de lo que tiene el archivo de texto 
print(archivo.read())#y aca lo imprimo para que se muestre cuando ejecuto el progama


"""Con este metodo de esta forma podemos posicionar el puntero despues de la primera linea"""
archivo.seek(len(archivo.readlines()))#Mostraria el texto ignorando la primera linea



"""SE PUEDEN USAR DOS METODOS PARA LEER Y ESCRIBIR EN EL ARCHIVO """

archivo=open("Archivo.txt","r+")
lista_archivo=archivo.readlines()#Guarda lo que tienen el archivo en una lista en la variable lista_archivo

#Escribe esta linea en la posicion que se le indica de la lista que se creo del archivo
lista_archivo[1]="Se agrego esta linea entre la posicion 0 y 1 que se encontraba en el archivo por lo que esta pasaria a ser la posicion 1 \n"

archivo.seek(0)#Se posiciona en el principio de lo que tiene el archivo
archivo.writelines(lista_archivo)#el paramtero writeline recibe comovalor una lista por eso se le pasa la variable lista_archivo
print (lista_archivo)
archivo.close()#cierro el archivo para que no siga usando memoria

