from src.utilidades import fragmentar_texto,config_cantidad_digitos

def descifrar(texto_cifrado, clave, longitud_fragmento):
    # Variables para almacenar el texto descifrado
    texto_descifrado = ""
    
    # Divide el texto cifrado en fragmentos, tenienfo en cuenta que por cada caracter del fragmento existen n digitos de cifrado
    nro_digitos = config_cantidad_digitos() 
    fragmentos_cifrados = fragmentar_texto(texto_cifrado, longitud_fragmento*nro_digitos)
    
    # Itera sobre los fragmentos cifrados
    for pos_dicc,fragmento_cifrado in enumerate(fragmentos_cifrados):
        
        # Diccionario de codigos y letras
        dicc_codigo_letra = clave[pos_dicc]
        
        # Cada Fragmento tiene que dividirse en la cantidad de digitos indicados en configuracion
        codigos_fragmento_cifrado = fragmentar_texto(fragmento_cifrado, nro_digitos)
        
        # Descifra el fragmento
        fragmento_descifrado = ""
        
        for codigo in codigos_fragmento_cifrado:
            letra = dicc_codigo_letra[int(codigo)]
            fragmento_descifrado += letra
            
        # Actualiza el texto descifrado
        texto_descifrado += fragmento_descifrado

    return texto_descifrado