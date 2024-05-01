from cuenta import Cuenta
from cuentaplus import CuentaPlus

def menu():
    """
    Resumido solo sera el menu donde conectare y creare las cuentas

    atte: ahdo/julio

    """ 
    usuario = cuentasOperacion()
    while True:
        opcion = int(input("=== menu() ===\n1.Inspeccionar credito\n2.Apostar\n3.Salir\n"))
        match(opcion):
            case 1:
                usuario.mostrardatos()
            case 2:
                print("usuario aposto") 
            case 3:
                print("adios")
                break


def preguntas():
    """
    aqui estan las preguntas que le hago al usuario
    """
    nombre  = input("cual es tu nombre? ")
    edad = inputNumero("cual es tu edad? ")
    credito = int(input("ingresa la cantidad de dinero que tienes: "))
    return nombre, edad, credito

def cuentasOperacion():
    """
    aqui es donde el usuario elige que tipo de usuario es
    """

    while True:
        option = inputNumero("=== usuario ===\n1. Usuario Ordinario\n2. Usuario +\n3. Salir\n")
        match(option):
            case 1:
                nombre, edad, credito = preguntas()
                usuario = Cuenta(nombre,edad,credito)
                return usuario
            case 2:
                nombre, edad, credito = preguntas()
                usuario = CuentaPlus(nombre,edad,credito,"20%")
                return usuario
            case 3:
                print("adios...")
                break
            case __:
                print("escoge una de las opciones que se te muestran en pantalla")

def inputNumero(mensaje):
    """
    aqui es la validacion de respuesta del usuario, en caso de que responda con
    un string o con cualquier cosa que no sea numero le retornara un error 
    """
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("ingresa un numero valido")
