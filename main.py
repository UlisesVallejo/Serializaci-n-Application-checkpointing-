import pickle, os

# Funcion para limpiar la consola
def limpiar():
    os.system("cls")
    
# Funcion para pausar la consola
def pausar():
    os.system("PAUSE")

class Animal:
    def __init__(self, especie, sexo, raza, peso, tipo):
        self.especie = especie
        self.sexo = sexo
        self.raza = raza
        self.peso = peso
        self.tipo = tipo
        print('Se ha añadido un:',self.especie)
        
    def __str__(self):
        return 'Especie: {} Sexo: {} Raza: {} Peso: {} Tipo: {}'.format(self.especie, self.sexo, self.raza, self.peso, self.tipo)
            
        
class Bitacora:
    
    animales = []
    
    def añadir_animal(self, p):
        self.animales.append(p)
        self.guardar()
    
        
    def retaurar_bitacora(self):
        fichero = open('bitacora', 'ab+')
        fichero.seek(0)
        try:
            self.animales = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            print("Se han cargado {} animales".format(len(self.animales)))
        

    def ver_bitacora(self):
        if len(self.animales) == 0:
            print("La bítacora está vacío")
            return
        for p in self.animales:
            print(p)
        
           
    def guardar(self):
        fichero = open('bitacora', 'wb')
        pickle.dump(self.animales, fichero)
        fichero.close()
            
miBitacora = Bitacora()
        
while True:
    limpiar()
    print("----------- MENÚ BÍTACORA -------------")
    print("1)-Restaurar bítacora (cargar de bitacora.txt)")
    print("2)-Agregar Animal")
    print("3)-Ver Bítacora")
    print("0) Salir")
    opcion = input("Eliga una opcion: ")
    
    if opcion == "1":
        miBitacora.retaurar_bitacora()
        pausar()
    
    elif opcion == "2":
        limpiar()
        especie = input("Especie del animal: ")
        sexo = input("Sexo del animal: ")
        raza = input("Raza del animal: ")
        peso = input("Peso del animal: ")
        tipo = input("Aéreos / Acuáticos / Terrestres: ")
        miBitacora.añadir_animal(Animal(especie, sexo, raza, peso, tipo))  
        pausar()
        
    elif opcion == "3":
        limpiar()
        miBitacora.ver_bitacora()
        pausar()
    
    elif opcion == "0":
        break