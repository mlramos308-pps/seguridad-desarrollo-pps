# ------------------------------
# Script: mychar.py
# Descripción:  Función cadena_más_larga que recibe una lista de palabras y devuelve la palabra más larga y programa que solicita  al usuario 5 palabras y devuelva la más larga usando la función anterior
# Autor: Laura Ramos Granados
# Fecha: 3 de noviembre de 2025
# ------------------------------



def cadena_mas_larga(lista):
    """
    Función que devuelve la cadena más larga de una lista de cadenas
    """
    # Checa que se reciba una lista
    if not isinstance(lista, list):
        raise TypeError("Se espera recibir una lista de cadenas. Por favor, intentalo de nuevo")
    # Checa que los elementos dentro de la lista sean todos strings
    if not all (isinstance(cadena, str) for cadena in lista):
        raise ValueError("La lista debe contener solo cadenas de caracteres. Por favor, intentalo de nuevo")

    cadena_mas_larga=""  # En caso de que no haya cadenas se devuelve vacío
    longitud_maxima=0 
    # Recorre las cadenas en la lista
    for cadena in lista:
        cadena_limpia = cadena.strip() # cadena limpia --> sin los espacios al los lados
        if cadena_limpia == "":
            continue 
        if len(cadena_limpia) > longitud_maxima: # Comprueba cada vez el valor de la longitud de las cadenas con el mayor valor encontrado
            cadena_mas_larga = cadena_limpia 
            longitud_maxima = len(cadena_limpia) 
        elif len(cadena_limpia) == longitud_maxima: # Si encuenta una cadena de igual longitud ...
            if cadena_limpia.lower() < cadena_mas_larga.lower(): # compara si es  "menor" alfabéticamente 
                cadena_mas_larga = cadena_limpia     
    return cadena_mas_larga


def main(): 
    print("""
            ---------------------------------------------
                       La palabra más larga
            ---------------------------------------------
          A continuación introduce 5 palabras y te diré cuál es la palabra más larga:
        """)
    
    lista = []
    n = 0
    try:
        while n < 5:
            try: 
                cadena = input(f"Ingresa la palabra {n+1}: ").strip()
                if not cadena.isalpha():
                    raise ValueError("Entrada inválida. Escribe solo letras, sin números ni símbolos")
                lista.append(cadena)
                n += 1
            except ValueError as e:
                print(f"Error:{e}")
        resultado = cadena_mas_larga(lista)
        print(f"La palabra más larga es: {resultado}")
    except Exception as e:
        print(f"Error inesperado:  {e}")

if __name__ == "__main__":
    main()
