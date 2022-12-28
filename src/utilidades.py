import configparser
import ast

def fragmentar_texto(texto, longitud_fragmento):
    # Lista de fragmentos
    fragmentos = []
    # Rango de las posiciones iniciales de cada fragmento 
    rango_fragmentos = range(0, len(texto), longitud_fragmento)
    
    for i in rango_fragmentos:
        subcadena = texto[i:i+longitud_fragmento]
        fragmentos.append(subcadena)
        
    return fragmentos


def obtener_digitos_min_max(cantidad_digitos):
  minimo = 10 ** (cantidad_digitos - 1)
  maximo = (10 ** cantidad_digitos) - 1
  return minimo, maximo


def config_cantidad_digitos():
    # Carga la configuración del archivo config.ini
    config = configparser.ConfigParser()
    config.read('configs/config.ini')

    # Obtiene la cantidad de dígitos a utilizar para el descifrado
    cantidad_digitos = int(config['CIFRADO']['cantidad_digitos'])
    
    return cantidad_digitos


def config_longitud_fragmento():
    # Carga la configuración del archivo config.ini
    config = configparser.ConfigParser()
    config.read('configs/config.ini')

    # Obtiene la cantidad de dígitos a utilizar para el descifrado
    longitud_fragmento = int(config['CIFRADO']['longitud_fragmento'])
    
    return longitud_fragmento


def guardar_clave(clave):
    # Abre el archivo en modo de escritura
    archivo_clave = open("clave.txt", "w")
    archivo_clave.write(str(clave))
    archivo_clave.close()
        
def leer_clave():
    contenido = open("clave.txt", "r")
    lista_diccionarios = ast.literal_eval(str(contenido.read()))
    contenido.close()
    return  lista_diccionarios
