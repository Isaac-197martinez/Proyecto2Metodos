def secante():
  import matplotlib.pyplot as plt


  logo1= """

 __       __            __                    __          
/  \     /  |          /  |                  /  |         
$$  \   /$$ | ______  _$$ |_    ______   ____$$ | ______  
$$$  \ /$$$ |/      \/ $$   |  /      \ /    $$ |/      \ 
$$$$  /$$$$ /$$$$$$  $$$$$$/  /$$$$$$  /$$$$$$$ /$$$$$$  |
$$ $$ $$/$$ $$    $$ | $$ | __$$ |  $$ $$ |  $$ $$ |  $$ |
$$ |$$$/ $$ $$$$$$$$/  $$ |/  $$ \__$$ $$ \__$$ $$ \__$$ |
$$ | $/  $$ $$       | $$  $$/$$    $$/$$    $$ $$    $$/ 
$$/      $$/ $$$$$$$/   $$$$/  $$$$$$/  $$$$$$$/ $$$$$$/                                            
"""

  logo2= """
       __                 __                
      /  |               /  |               
  ____$$ | ______        $$ | ______        
 /    $$ |/      \       $$ |/      \       
/$$$$$$$ /$$$$$$  |      $$ |$$$$$$  |      
$$ |  $$ $$    $$ |      $$ |/    $$ |      
$$ \__$$ $$$$$$$$/       $$ /$$$$$$$ |      
$$    $$ $$       |      $$ $$    $$ |      
 $$$$$$$/ $$$$$$$/       $$/ $$$$$$$/       
            
"""
  logo3= """


  ______                                        __              
 /      \                                      /  |             
/$$$$$$  | ______   _______  ______  _______  _$$ |_    ______  
$$ \__$$/ /      \ /       |/      \/       \/ $$   |  /      \ 
$$      \/$$$$$$  /$$$$$$$/ $$$$$$  $$$$$$$  $$$$$$/  /$$$$$$  |
 $$$$$$  $$    $$ $$ |      /    $$ $$ |  $$ | $$ | __$$    $$ |
/  \__$$ $$$$$$$$/$$ \_____/$$$$$$$ $$ |  $$ | $$ |/  $$$$$$$$/ 
$$    $$/$$       $$       $$    $$ $$ |  $$ | $$  $$/$$       |
 $$$$$$/  $$$$$$$/ $$$$$$$/ $$$$$$$/$$/   $$/   $$$$/  $$$$$$$/ 
                                                                                                                     


"""

  print(f"{logo1}\n{logo2}\n{logo3}")
  print("Funcion de prueba: (x**3) + (2*x) - 5")
  
  function_usr = input("Ingrese la formula a evaluar: ")

  def evaluar_f_usr(x):
    return eval(function_usr)

#En esta variable se genera una lista con valores del -10 al 10.
#Todos estos valores serán los que tomara x.

  x = range(-20, 20)
  plt.figure(facecolor= "#83C5BE")
  ax = plt.axes()
  ax.set_facecolor('#006D77') 

#Con el método plot especificamos que función graficaremos.
#El primer argumento es la variable con los valores de x.
#El segundo argumento le pasamos todos estos valares a la función con ayuda de un bucle.
  plt.plot(x, [evaluar_f_usr(i) for i in x], "#E29578")

#Titulos
  plt.title("Metodo de la secante", color = "#006D77")
  plt.xlabel("Eje x", color = "#006D77")
  plt.ylabel("Eje y", color = "#006D77")

#Establecemos el color de los ejes.
  plt.axhline(0, color="#EDF6F9")
  plt.axvline(0, color="#EDF6F9")
  plt.grid(color= "#83C5BE")

#Especificamos los limites de los ejes.
  plt.xlim(-5, 10)
  plt.ylim(-5, 10)
  plt.xticks( range(-5,10,1), color = "#006D77" )
  plt.yticks( range(-5, 10,1), color = "#006D77")

# Mostramos el gráfico.
  plt.show(block=False)

  valor_usr = int(input("Ingrese el punto a evaluar: "))
  error_tolerable = float(input("Ingrese el margen de error esperado: "))

  valor_raiz=0
  errur = 100
  iteracion = 1

  print("Iteracion\tXi\t\t\tXi-1\t\tf(Xi)\t\tf(Xi-1)\t\tXr\t\tError Aproximado")

#iteracion 1
  x= valor_usr
  f_equis=evaluar_f_usr(x)
  x_menos_uno = valor_usr-1
  x=x_menos_uno
  f_equis_menos_uno = evaluar_f_usr(x)
  x_erre = valor_usr - (f_equis * (x_menos_uno - valor_usr))/(f_equis_menos_uno - f_equis)
  print(f"{iteracion}\t\t\t{valor_usr}\t\t\t{x_menos_uno}\t\t\t{ round(f_equis, 4)}\t\t\t{round(f_equis_menos_uno, 4)}\t\t\t{round(x_erre,4)}\t\t---")
  x= valor_raiz
  while evaluar_f_usr(x) != 0 and errur >error_tolerable:
    erre_anterior = x_erre
    x_menos_uno = valor_usr
    valor_usr = x_erre
    x= valor_usr
    f_equis=evaluar_f_usr(x)
    x_menos_uno = valor_usr-1
    x=x_menos_uno
    f_equis_menos_uno = evaluar_f_usr(x)

    x_erre = valor_usr - (f_equis * (x_menos_uno - 
  valor_usr))/(f_equis_menos_uno - f_equis)

    errur = ((x_erre - erre_anterior)/x_erre)*100
    if errur<0:
      errur *= -1
    valor_raiz = x_erre
    x = valor_raiz
    iteracion += 1
    print(f"{iteracion}\t\t\t{round(valor_usr,4)}\t\t{round(x_menos_uno,4)}\t\t{round(f_equis, 4)}\t\t{round(f_equis_menos_uno, 4)}\t\t{round(x_erre,4)}\t\t{round(errur,4)}")

  valor_raiz=round(valor_raiz,4)
  r = valor_raiz
  x=[valor_raiz]
  y=[0]
  plt.plot(x, y, marker="o", markersize=8, markeredgecolor="white", markerfacecolor="#E29578")
  plt.text(r, 0.6, f"Raiz encontrada: {r}", color ="white")
  plt.show(block=False)
  print(f"Raiz encontrada: {valor_raiz}")
  print(f"Error presente: {round(errur,4)}")
  print(f"Iteraciones requeridas: {iteracion}")
