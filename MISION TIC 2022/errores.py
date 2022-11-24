import os
os.system('cls')

#Metodo try, except
def ejemplo_1():
    try:
        a = int(input())
        suma = a / 0
        print("la suma es ", suma)
    except ValueError:
        print("Algo va mal")
    except TypeError:
        print("Algo no es correcto")
    except:
        print("Hasta luego..")

def ejemplo_2():
    try:
        a = int(input())
        suma = a / 1
        print("la suma es ", suma)

        if a == 9:
            #levantar errores
            raise NameError("Error fatal")

    except ValueError:
        #Tratar errores particulares
        print("Algo va mal")
    except NameError:
        #Mi propio error
        print("Ups")
    except:
        print("Hasta luego..")
    else:
        #Si try paso sin errores
        print("Exitoso")
    finally:
        #Se ejecuta siempre
        print("fin")

    

if __name__ == "__main__":
    ejemplo_2()