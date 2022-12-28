import random
from src.utilidades import fragmentar_texto,obtener_digitos_min_max,config_cantidad_digitos


def generar_tuplas_letra_codigo(fragmento):
    # Diccionario para almacenar los códigos asignados a cada letra del fragmento
    dicc_letra_codigo = {}
    # Lista para almacenar las parejas (letra, código) de la clave
    tuplas_letra_codigo = []
    
    for letra in fragmento:
        # Si la letra no tiene un código asignado, genera uno aleatorio
        if letra not in dicc_letra_codigo:
            # Obtenemos los las cotas para saber dentro de que rango obtener el codigo aleatorio
            minimo, maximo = obtener_digitos_min_max(config_cantidad_digitos())
            # numero de N cifras aleatorio
            dicc_letra_codigo[letra] = random.randint(minimo, maximo)
            
        # Agrega la pareja (letra, código) a la clave del fragmento
        tuplas_letra_codigo.append((letra, dicc_letra_codigo[letra]))
    
    return tuplas_letra_codigo

def cifrar_fragmento(tuplas_letra_codigo):
    # Lista de codigos
    codigos = []
    
    for letra, numero in tuplas_letra_codigo:
        codigos.append(str(numero))
   
    return "".join(codigos)


def generar_dicc_cogido_letra(tuplas_letra_codigo):
    dicc_codigo_letra = {}
    for letra,codigo in tuplas_letra_codigo:
        dicc_codigo_letra[codigo] = letra
    return dicc_codigo_letra  
        


"""
Cifra el texto proporcionado en fragmentos de longitud especificada y devuelve el texto cifrado y las claves de cifrado.
Args:
    texto[str]: El texto a cifrar.
    longitud_fragmento[int]: La longitud de los fragmentos de texto a cifrar.
Returns:
    Una tupla con el texto cifrado y las claves de cifrado.
        type: Tuple[str, List[Dicc[int,str]]:
"""
def cifrar(texto, longitud_fragmento): 
    # Variables para almacenar el texto cifrado y la clave
    texto_cifrado = ""
    clave = []
    
    # Divide el texto en fragmentos
    fragmentos = fragmentar_texto(texto, longitud_fragmento)
    
    # Itera sobre los fragmentos
    for fragmento in fragmentos:
        
        # Genera la lista de pares (letra,clave) para este fragmento
        tuplas_letra_codigo = generar_tuplas_letra_codigo(fragmento)
        
        # Cifra el fragmento
        fragmento_cifrado = cifrar_fragmento(tuplas_letra_codigo)
        
        # Actualiza el texto cifrado y la clave
        texto_cifrado += fragmento_cifrado
        clave.append(generar_dicc_cogido_letra(tuplas_letra_codigo))
    # Devuelve el texto cifrado y la clave
    return texto_cifrado, clave    
