# Proyecto: Cifrado y Descifrado de texto

Este proyecto consiste en una aplicación en python que permite cifrar y descifrar mensajes utilizando una clave aleatoria.

## Resumen

- Este proyecto consiste en una aplicación de consola que permite cifrar y descifrar mensajes de texto.

- Los mensajes se dividen en fragmentos de N letras y se asigna un número aleatorio de M cifras a cada una de las letras. Donde N y M estan definidos en el archivo de configuracion /configs/config.ini .

- El texto cifrado se compone de los números generados y el texto descifrado se obtiene a partir de la clave, que es una lista de diccionarios que asocia cada codigo y letra con su respectivo fragmento.

La aplicación ofrece la posibilidad de cifrar y descifrar mensajes de forma individual o ambas a la vez. En ambos casos imprime por pantalla el resultado, solo guarda en un archivo de texto (clave.txt) la clave que obtuvimos al cifrar un texto.

## Requisitos

Para utilizar esta aplicación es necesario tener instalado Python 3.x .

Puedes instalar todos los módulos necesarios ejecutando el siguiente comando en tu terminal:

```bash
pip install -r requirements.txt
```

## Instalación

Para utilizar este proyecto, clona este repositorio en tu equipo con el siguiente comando:

```bash
git clone https://github.com/rvegabaldiviezo/cifrado-descifrado-mensajes.git
```

## Uso

Para utilizar este proyecto, abre una terminal en la raíz del proyecto y utiliza el siguiente comando:

```bash
py main.py [opciones] [mensaje]
```

Donde [opciones] es alguna de las siguiente:

- -c: cifra el mensaje.
- -d: descifra el mensaje.
  
Si no se especifica ninguna opción, se realizará tanto el cifrado como el descifrado del mensaje.

## Ejemplos

- **Caso 1**: cifra el mensaje. Ademas guarda en el archivo **clave.txt** la clave generada.

```bash
$ py main.py -c "Hola soy un programador"

Texto cifrado:
20766479204498921764341991798286967193286908131185946716669551886506375630513756901773679244
```

- **Caso 2**: descifra el texto cifrado. Usa la clave del archivo **clave.txt**.

```bash
$ py main.py -d "20766479204498921764341991798286967193286908131185946716669551886506375630513756901773679244"

Texto descifrado:
Hola soy un programador
```

- **Caso 3**: Si no se especifica ninguna opción, se realizará tanto el cifrado como el descifrado del mensaje.

```bash
$ py main.py "Hola soy un programador"

Texto cifrado:
27876695715899481384524241938294639634573894676118708942496796952074305921303059146878585679

Texto descifrado:
Hola soy un programador
```

