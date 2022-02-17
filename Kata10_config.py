"""
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
def main():
    try:
        open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except PermissionError as PerError:
        print("Se necesitan mas permisos para acceder al archivo: ",PerError)
    except (BlockingIOError, TimeoutError):         #Solo agrupar cuando sea necesario
        print("Filesystem under heavy load, can't complete reading configuration file")


def main():
    try:
        open("config.txt")
    except OSError as err:
        if err.errno == 2:
             print("Couldn't find the config.txt file!")
        elif err.errno == 13: #permisionError
            print("Found config.txt but couldn't read it")
"""

#generando nuestro propia excepcion


def travelJupiter(Weight, crewNumber, Maxspeed):
    try:
        Weight = Weight + (crewNumber * 75) #sumando peso de tripulación
        if Maxspeed > 1500:
            raise RuntimeError(f"La nave no puede ir a una velocidad mayor de 1500 km/s, velocidad actual {Maxspeed}")
        elif crewNumber > 12:
            raise RuntimeError(f"el numero Maximo de miembros es de 12 , Tripulacion actual : {crewNumber}")
        elif Weight < 1200:
            raise RuntimeError(f"La nave no puede tener un peso menor a 1200 kilos, peso actual {Weight}")
    except TypeError:
        raise TypeError("todos los parametros que pueden ser recibidos deben ser enteros")
    return f"""La tripulacion esta lista ,
            La nave tiene un peso adecuado de {Weight},
            Una triuplacion autosuficiente de {crewNumber},
            y una velocidad adecuada de {Maxspeed} km/s
            """

if __name__ == '__main__':
  # main()
  #print(travelJupiter(100,12,1300))
  #print(travelJupiter(1200,13,1000))
  #print(travelJupiter(1200,12,"hola"))
  #print(travelJupiter(1200,12,2500))
  print(travelJupiter(1200,12,1300))
