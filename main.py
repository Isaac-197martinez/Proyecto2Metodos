from secante import secante
from programa_biseccion import biseccion
# from replit import clear

logo = """

__________                                    __           ________  
\______   \_______  ____ ___.__. ____   _____/  |_  ____   \_____  \ 
 |     ___/\_  __ \/  _ <   |  |/ __ \_/ ___\   __\/  _ \   /  ____/ 
 |    |     |  | \(  <_> )___  \  ___/\  \___|  | (  <_> ) /       \ 
 |____|     |__|   \____// ____|\___  >\___  >__|  \____/  \_______ \
                         \/         \/     \/                      \/

"""

print(logo)

print("Desarrollo de programas para busqueda de raices por metodos numericos abiertos y cerrados\nRealizado por:\t\tIsaac Martinez\t\tManuel Vergara")

eleccion = 1

while eleccion != 0:
  eleccion = int(input("\n\nPresione 1 para elegir metodo abierto (Metodo de la secante), presione 2 para elegir metodo cerrado (Metodo de la Biseccion) o 0 para salir: "))
  if eleccion == 1:
    secante()

  elif eleccion == 2:
    biseccion()
# clear()

  
  
