import Bloque
import Cadena
import datetime

if __name__ == "__main__":
    try:
        print("Test of Bloque")
        bloque = Bloque.Bloque(datetime.datetime.now(),"abc","")
        print("\tData del Bloque: " + str(bloque.data))
        print("\tHash del Bloque: " + str(bloque.hash))
        print("\nTest of Cadena")
        print("\t\tNueva Cadena con data abc")
        cadena = Cadena.Cadena("abc")
        print(cadena)
        print("\n\t\tAgregando bloque \"123\" ")
        cadena.agregar_bloque("123")
        print(cadena)
        print("\t\tAgregando bloque \"Avion\" ")
        cadena.agregar_bloque("Avion")
        print(cadena)
        print("\n\t Verificando Integridad: Normal-> Deberia ser True")
        print(cadena.verificar_integridad())
        print("\n\t Verificando Integridad después de cambiar la cadena")
        cadena.chain[0] = Bloque.Bloque("12","abc","")
        print("\t\t Debería ser False")
        print(cadena.verificar_integridad())
        print("Fin de la verificación")

        print("Función crear_fork no implementada")
    except TypeError as identifier:
        print(identifier)