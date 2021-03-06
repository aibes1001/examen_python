import random

def encontrar_menores(diccionario,letra):
    """Dado un diccionario de palabras, y una letra, esta función devuelve la lista de palabras que empiezan por una letra que alfabéticamente está antes que la indicada.
    Args:
      diccionario
      letra
    Returns:
      resultado: ej. ['AUNQUE','ABINAR']
    """
    #L'error indicava que només detectava una paraula en la llista, mentre que l'assert esperava 2. S'ha solucionat posant la llista
    # resultado = [] abans dels bucles
    resultado=[]
    for clave in diccionario:
        for palabra in diccionario[clave]:
            if palabra[0] < letra:
                
                resultado.append(palabra)
    return resultado



def add_client(clients_list,nif,name,address,phone,email):
    """Dado un diccionario de clientes y datos de un nuevo cliente, esta función inserta estos datos como un nuevo cliente.
    Args:
      diccionario
      nif
      name 
      address
      phone
      email
    """
    #L'error es trobaja que el test esperava que retornara un diccionari com a valor amb el nom, adreça  ..., pero conforme estava configurada la funció
    # introduïa un diccionari amb la clau del DNI (de nou) i dins el diccionari amb nom, adreça ....
    #S'ha corregit deixant només la clau amb el diccionari nom, adreça...
    clients_list[nif] = {
        'name': name,
        'address': address,
        'phone': phone,
        'email': email
        
    }
    print(clients_list)

def repartir_cartas(cartas_iniciales,repeticiones):
    """Dada una baraja de cartas iniciales y un número de repeticiones, esta función selecciona 5 cartas aleatorias de esta baraja y las mete en un diccionario llamado combinaciones. El proceso se repite tantas veces como repeticiones se indiquen.
    Args:
      cartas_iniciales
      repeticiones
    Returns:
      combinaciones: ej. {'repeticion1': ['contable', 'alguacil', 'asesino', 'cardenal', 'obispo']}
    """    
    combinaciones={}
    for i in range(1,repeticiones+1):
        cartas_aleatorias = cartas_iniciales 
        combinaciones["repeticion"+str(i)]=[]
        for j in range(0,5):
            carta=random.choice(cartas_aleatorias)
            combinaciones["repeticion"+str(i)].append(carta)
            cartas_aleatorias.remove(carta)

    return combinaciones

    
