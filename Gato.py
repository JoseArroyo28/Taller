class Gato:
    def __init__(self, nombre, raza, color, peso,  sexo,edad,vidas):
        self.nombre=nombre
        self.raza=raza
        self.color=color
        self.peso=peso
        self.sexo=sexo
        self.edad=edad
        self.vidas = vidas
    def mostrar_info(self):
        print("nombre:  " + self.nombre)
        print("Raza:  " + self.raza)
        print("Color:  " + self.color)
        print("Peso:  " + self.peso)
        print("sexo:  " + self.sexo)
        print("edad:  " + self.edad) 
        print("vidas:  " + self.vidas) 
    def mostrar_cmurio(self):
        vidas =int(self.vidas)
        vidas = vidas-1
        print ("El gato se murio de "+ self.vidas+ " vidas le quedan: " + str (vidas))
      
nombre= input("ingrese nombre aqui: ")
raza=input ("ingrese la raza aqui: ")
color=input ("ingrese color aqui: ")
peso=input ("ingrese peso aqui: ")
sexo=input ("ingrese sexo aqui: ")
edad=input ("ingrese edad aqui: ")
vidas=input ("ingrese vidas aqui: ")

Gato = Gato(nombre, raza, color, peso, sexo,edad,vidas)
Gato.mostrar_info()
Gato.mostrar_cmurio()
        
        