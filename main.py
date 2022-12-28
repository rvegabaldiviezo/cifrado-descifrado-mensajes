import argparse
from src.cifrado import cifrar
from src.descifrado import descifrar
from  src.utilidades import config_longitud_fragmento,leer_clave,guardar_clave

def main():
    # Crea un analizador de argumentos
    parser = argparse.ArgumentParser(description='Cifra y descifra mensajes utilizando una clave aleatoria')
    # Agrega los argumentos necesarios
    parser.add_argument("-c", "--cifrar", action="store_true", help="Cifra el mensaje especificado")
    parser.add_argument("-d", "--descifrar", action="store_true", help="Descifra el mensaje especificado")
    parser.add_argument("mensaje", type=str, help="Mensaje a cifrar o descifrar")
    
    # Parsea los argumentos
    args = parser.parse_args()
    
    # Determina si se debe cifrar o descifrar el mensaje
    cifrar_mensaje = args.cifrar
    descifrar_mensaje = args.descifrar
    
    # Mensaje recibido y longitud de Fragmento
    mensaje = args.mensaje
    longitud_fragmento = config_longitud_fragmento()

    # Si solo se debe cifrar el mensaje, muestra solo el resultado del cifrado
    if cifrar_mensaje and mensaje:
        texto_cifrado, clave = cifrar(mensaje, longitud_fragmento)
        guardar_clave(clave)
        print(f"\nTexto cifrado: \n{texto_cifrado}")
    # Si solo se debe descifrar el mensaje, muestra solo el resultado del descifrado
    elif descifrar_mensaje and mensaje:
        texto_descifrado = descifrar(mensaje, leer_clave(), longitud_fragmento)
        print(f"\nTexto descifrado: \n{texto_descifrado}")
    # Si se debe cifrar y descifrar el mensaje, muestra ambos resultados
    elif mensaje:
        texto_cifrado, clave = cifrar(mensaje, longitud_fragmento)
        guardar_clave(clave)
        texto_descifrado = descifrar(texto_cifrado, clave, longitud_fragmento)
        print(f"\nTexto cifrado: \n{texto_cifrado}")
        print(f"\nTexto descifrado: \n{texto_descifrado}")
    # En cualquier otro caso mostramos como debe usar el programa
    else:
        print(f"Error, se debe pasar como parametros algunas de las siguientes opciones:")
        print(f"py main.py mensaje:  cifra y descifra el mensaje")
        print(f"py main.py -c mensaje:  solo cifra el mensaje y muestra por consola el texto cifrado")
        print(f"py main.py -p mensaje:  solo descifra el mensaje y monstra por consola el texto original")

if __name__ == "__main__":
    main()
    