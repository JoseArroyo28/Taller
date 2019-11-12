class Persona:
    def __init__(self, nombre, apellido, color_cabello, color_ojos, altura, sexo,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.color_cabello=color_cabello
        self.color_ojos=color_ojos
        self.altura=altura
        self.sexo=sexo
        self.edad=edad
        
    def mostrar_info(self):
        print("nombre:  " + self.nombre)
        print("apellido:  " + self.apellido)
        print("color_cabello:  " + self.color_cabello)
        print("color_ojos:  " + self.color_ojos)
        print("altura:  " + self.altura)
        print("sexo:  " + self.sexo)
        print("edad:  " + self.edad)
        
    def mostrar_edad (self):
        edad=int (self.edad)
        edad=edad+10 
        print ("en 10 años"+ self.nombre+ "tendra" + str (edad))


nombre= input("ingrese nombre aqui: ")
apellido=input ("ingrese apellido aqui: ")
color_cabello=input ("ingrese color cabello aqui: ")
color_ojos=input ("ingrese color ojos aqui: ")
altura=input ("ingrese altura aqui: ")
sexo=input ("ingrese sexo aqui: ")
edad=input ("ingrese edad aqui: ")
Persona = Persona(nombre, apellido, color_cabello, color_ojos, altura, sexo,edad)
Persona.mostrar_info()