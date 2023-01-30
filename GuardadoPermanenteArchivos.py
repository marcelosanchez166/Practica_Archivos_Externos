import pickle


class persona:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print("Se ha creado la persona con nombre: ", self.name)

    """Metodo paradar formato a lo que se muestra """

    def __str__(self):
        return "{} {} {}".format(self.name, self.age, self.gender)


class ListaPersonas:
    personas = []

    def __init__(self):  # Constructor de la clase ListaPersonas
        ListaDePersonas = open("ficherodeGuardado", "ab+")
        # Posiciona el puntero en la posicion cero en el archivo que se crea
        ListaDePersonas.seek(0)
        try:  # Intenta mostrar el fichero pero al no tener info la primera ves dara error por eso se pone en un try
            # Carga los datos que se almacenaron con anterioridad en
            self.personas = pickle.load(ListaDePersonas)
            # binario en el ficherodeGuardado
            print("Se guardo {} Persona al fichero externo ".format(len(self.personas)))
        except:  # Mensaje que dara cuando muestre que el fichero esta vacio
            print("El fichero esta vacio ")
        finally:  # termina cerrando el fichero y elimina la varible en memoria ListaDePersonas
            ListaDePersonas.close()
            del(ListaDePersonas)

    def agregarPersonas(self, per):
        # Se agrega cada persona que se le pasa a la lista cuando se instancia el metodo
        self.personas.append(per)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for i in self.personas:  # Recorre la lista y la muestra
            print(i)

    def guardarPersonasEnFicheroExterno(self):
        # Escribe en el archivo
        ListaDePersonas = open("ficherodeGuardado", "wb")
        # hace el volcado de la info de la lista de la informacion que tiene la variable
        pickle.dump(self.personas, ListaDePersonas)
        # en memoria ListaDePersonas
        ListaDePersonas.close()  # Cierra la variable en memoria
        del(ListaDePersonas)  # Elimina la variable en memoria

    def mostrarInfoFicheroExterno(self):
        print("La informacion del fichero externo es la siguiente ")
        for n in self.personas:
            print(n)


milista = ListaPersonas()  # Instancia de la clase ListaPersonas
# Instancia y pasar parametros a la clase persona
person = persona("Juana", 28, "Femenina")
# Con el nombre de la instancia de milista de la clase ListaPersonas mando a llamar el metodo agregarPersonas
milista.agregarPersonas(person)
# y le paso los parametros de la instancia de la clase persona
milista.mostrarInfoFicheroExterno()
# milista.mostrarPersonas()#Mando a llamar el metodo Mostrar personas para que las muestre


# dump= permite hacer un volcado de datos al fichero binario externo
# load=Cargar los datos que se almacenaron con anterioridad en binario en un fichero externo
