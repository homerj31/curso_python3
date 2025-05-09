import csv
def LeerPartidos():
    """Función que lee el fichero CSV y devuelve los datos del mismo en una 
    lista de diccionarios con los datos de la liga."""
    datos=[]
    keys=["fecha","equipo1","equipo2","final","mitad"]
    fichero = open("curso/u49/liga.csv")
    contenido = csv.reader(fichero)
    for row in list(contenido)[1:]:
        partido=dict(zip(keys,row))
        print (partido)
        datos.append(partido)
    fichero.close()
    return datos

def extraer_equipos(liga):
    return(tuple(set([partido["equipo1"] for partido in liga])))

if __name__ == '__main__':
    liga=LeerPartidos()
	#impClasificacion(liga)
