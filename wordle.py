import random
from time import sleep

def choose_secret(filename):
    """Dado un nombre de fichero, esta función devuelve una palabra aleatoria de este fichero transformada a mayúsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayúsculas. Ej. "CREMA"
    """
    file = open(filename, mode="rt", encoding="utf-8")

    palabras = file.readlines()
    palabra = palabras[random.randint(0,len(palabras)-1)].upper()
    print(palabra)
    return palabra

    
def compare_words(word, secret):
    """Dadas dos palabras en mayúsculas (word y secret), esta función calcula las posiciones de las letras de word que aparecen en la misma posición en secret, y las posiciones de las letras de word que aparecen en secret pero en una posición distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posición en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras están en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """
    print("LONGITUDS")
    print(len(word))
    print(len(secret))
    same_position = []
    same_letter = []

    for i in range(len(word)):
      if word[i] == secret[i]:
        same_position.append(i)
    
    for i in range(len(word)):
      for j in range(len(secret)):
        if word[i] == secret[j] and same_position.count(i) == 0:
          same_letter.append(i)
    

    return same_position, same_letter


def print_word(word, same_position, same_letter):
    """Dada una palabra, una lista same_position y otra lista same_letter, esta función creará un string donde aparezcan en mayúsculas las letras de la palabra que ocupen las posiciones de same_position, en minúsculas las letras de la palabra que ocupen las posiciones de same_letter y un guión (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """
    transformed = ""
    
    for i in range(len(word)):
      if same_position.count(i) == 1:
        transformed += word[i].upper()
      elif same_letter.count(i) == 1:
        transformed += word[i].lower()
      else:
        transformed += "-"
    
    return transformed


    
def choose_secret_advanced(filename):
    """Dado un nombre de fichero, esta función filtra solo las palabras de 5 letras que no tienen acentos (á,é,í,ó,ú). De estas palabras, la función devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayúsculas
    """

    file = open(filename, mode="rt", encoding="utf-8")

    palabras = file.readlines()
    
    palabras_sin_acento = []

    for palabra in palabras:
        if palabra.count("á") == 0 and palabra.count("é") == 0 and palabra.count("í") == 0 and palabra.count("ó") == 0 and palabra.count("ú") == 0:
          palabras_sin_acento.append(palabra)
    
    selected = []

    while len(selected) < 15:
      p = palabras_sin_acento[random.randint(0,len(palabras_sin_acento)-1)]
      if selected.count(p) == 0:
        selected.append(p)

    secret = selected[random.randint(0,len(selected)-1)].upper()
    return secret, selected

 
def check_valid_word(selected):
    """Dada una lista de palabras, esta función pregunta al usuario que introduzca una palabra hasta que introduzca una que esté en la lista. Esta palabra es la que devolverá la función.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que está en la lista.
    """
    print(selected)
    word = ""

    esta = False
    while esta == False:
      word = input("Introduce una nueva palabra: ")

      for i in selected:
        if selected == word:
          esta = True
          break

    return word


if __name__ == "__main__":
    secret, selected =choose_secret_advanced("palabras_extended.txt")
    word = check_valid_word(selected)
    print("FINAL " + word)
    """print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
    for repeticiones in range(0,6):
        word = input("Introduce una nueva palabra: ")
        same_position, same_letter = compare_words(word, secret)
        print(same_position)
        print(same_letter)
        resultado=print_word(word, same_position, same_letter)
        print(resultado)
        if word == secret:
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)   
    """
    
