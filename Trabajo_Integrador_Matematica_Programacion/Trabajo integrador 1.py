#Conversor de decimal a binario y de binario a decimal.
#Conversión de Números:
#Desarrollen un programa que convierta números decimales a binarios y, de forma opcional, también de binario a decimal.
#Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos.


import math


#Definicion de lista enlazada:
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato) #se crea el nuevo nodo (3)      // se crea el nuevo nodo (2)    // se crea el nuevo nodo (1)
        nuevo_nodo.siguiente = self.cabeza #el puntero -> None  // el puntero -> 3              // el puntero -> 2
        self.cabeza = nuevo_nodo #Cabeza(None) = 3              // cabeza(3) = 2                // cabeza(2) = 1

    def mostrar(self):
        actual = self.cabeza
        while (actual):
            print(actual.dato, end= "")
            actual = actual.siguiente

    def invertir_lista(self):
        actual = self.cabeza
        siguiente = actual.siguiente
        anterior = None
        while(actual):
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior
    
    def unir(self, otra_lista):
        if not self.cabeza:
            self.cabeza = otra_lista.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = otra_lista.cabeza


#Definicion de funciones:
#INGRESO DE NUMEROS, VALIDACION Y PASAJE A FLOAT:
def ingresar_numero():
    while True:
        valor = input("Ingresa un número entero o decimal: ")
        try:
            numero = float(valor)  # Intenta convertirlo a número (decimal o entero)
            return numero
        except ValueError:
            print("El valor ingresado no es válido. Por favor, intenta nuevamente.")

def ingresar_binario():
    
    while True:
        valor = input("Ingresa un número binario: ")
        # Contar cuántos puntos hay en el número
        if valor.count('.') > 1:  # Si hay más de un punto, no es válido
            print("El valor ingresado no es un número binario. Intenta nuevamente.")
            return ingresar_binario()
        # Verificar que todos los caracteres sean 0, 1 o .
        for caracter in valor:
            if caracter not in '01.': # Validar los caracteres
                print("El valor ingresado no es un número binario. Intenta nuevamente.")
                return ingresar_binario()
        return float(valor)


#FUNCIONES PARA CONVERTIR DE DECIMAL A BINARIO:
    #FUNCIONES PARA CONVERTIR DE DECIMAL A BINARIO CON LISTA ENLAZADA:
def conversor_entero_binario_LE(entero):
    #entero_aux = entero #Esto lo estaba usando por si necesitaba mostrar el numero dentro de esta funcion
    binario = ListaEnlazada()
    binario.insertar(",")
    while(entero>=2):
        aux = math.trunc(entero%2)
        binario.insertar(aux)
        entero = math.trunc(entero/2)
    binario.insertar(entero)
    return binario

def conversor_decimal_binario_LE(entero):
    decimal = entero - int(entero)
    #decimal_aux = decimal #Esto lo estaba usando por si necesitaba mostrar el numero dentro de esta funcion
    binario = ListaEnlazada()
    for i in range(2):
        aux = math.trunc(decimal*2)
        binario.insertar(aux)
        decimal = decimal*2
        decimal = decimal - int(decimal)
    return binario


    #FUNCIONES PARA CONVERTIR DE DECIMAL A BINARIO CON STRINGS:
def conversor_entero_binario_STR(entero):
    binario = ""
    entero = int(entero) #lo convierto en un entero porque no me interesa lo que esta despues de la coma en esta funcion.
    while(entero>=2):
        aux = math.trunc(entero%2)
        binario = binario + str(aux)
        entero = math.trunc(entero/2)
    binario = binario + str(entero)
    return binario[::-1] #Invierto el string con slicing para tener bien el resultado.

def conversor_decimal_binario_STR(entero):
    binario = "0."
    decimal = entero - int(entero)
    if (decimal!=0):
        cant_dig=0
        bandera=False
        while(not(bandera and cant_dig > 2)): #Quiero que itere siempre y cuando haya un 1 y como minimo 2 digitos, si hay 2 digitos pero no hay 1, que siga hasta que haya 1.
            aux = math.trunc(decimal*2)
            binario = binario + str(aux)
            decimal = decimal*2
            decimal = decimal - int(decimal)
            if '1' in binario:
                bandera = True
            cant_dig+=1
        return binario
    else:
        return binario

def sumatoria_entero_decimal(entero, decimal):
    entero = int(entero)
    decimal = float(decimal)
    binario = entero + decimal
    return binario


#FUNCIONES PARA CONVERTIR DE BINARIO A DECIMAL:
def conversor_binarioDec_decimal(binario): #Conversor de la parte decimal del binario al decimal
    cadena = str(binario)
    if "." in cadena:
        parte_decimal = cadena.split('.')[1]
        cantidad_digitos = len(parte_decimal)
        suma = 0
        potencia = 0
        for i in range(cantidad_digitos):
            potencia-=1
            aux=int(parte_decimal[i])
            suma+=aux*(2**potencia)
        return suma
    else:
        return 0

def conversor_binarioEnt_decimal(binario):
    binario = int(binario)
    cadena = str(binario)
    cantidad_digitos = len(cadena)
    suma = 0
    potencia = 0
    for cantidad_digitos in range(cantidad_digitos,0,-1):
        aux=int(cadena[cantidad_digitos-1])
        suma+=aux*(2**potencia)
        potencia+=1
    return suma

def sumatoria_decimal_entero(entero, decimal):
    numero = entero + decimal
    return numero



#Programa principal:

#PASAR DE DECIMAL A BINARIO:
#Para hacerlo con lista enlazada:
"""numero = ingresar_numero()
lista1 = conversor_entero_binario_LE(numero)
lista2 = conversor_decimal_binario_LE(numero)
lista1.unir(lista2)
lista1.mostrar()"""

#Para hacerlo con strings: #Tiene que tener un numero dps de la coma porque sino no anda.
numero = ingresar_numero()
binario = sumatoria_entero_decimal(conversor_entero_binario_STR(numero), conversor_decimal_binario_STR(numero))
print(f"El numero {numero} en binario es: {binario}") 


#PASAR DE BINARIO A DECIMAL:
numero = ingresar_binario()
decimal = sumatoria_decimal_entero(conversor_binarioEnt_decimal(numero), conversor_binarioDec_decimal(numero))
print(f"El numero {numero} en decimal es: {decimal}")