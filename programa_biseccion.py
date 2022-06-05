
from contextlib import redirect_stderr
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols 
from sympy import lambdify
from sympy import sympify

logo = """
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | ____    ____ | || |  _________   | || |  _________   | || |     ____     | || |  ________    | || |     ____     | |
| ||_   \  /   _|| || | |_   ___  |  | || | |  _   _  |  | || |   .'    `.   | || | |_   ___ `.  | || |   .'    `.   | |
| |  |   \/   |  | || |   | |_  \_|  | || | |_/ | | \_|  | || |  /  .--.  \  | || |   | |   `. \ | || |  /  .--.  \  | |
| |  | |\  /| |  | || |   |  _|  _   | || |     | |      | || |  | |    | |  | || |   | |    | | | || |  | |    | |  | |
| | _| |_\/_| |_ | || |  _| |___/ |  | || |    _| |_     | || |  \  `--'  /  | || |  _| |___.' / | || |  \  `--'  /  | |
| ||_____||_____|| || | |_________|  | || |   |_____|    | || |   `.____.'   | || | |________.'  | || |   `.____.'   | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'                                                                                                                               
"""
logo2 = """
 .----------------.  .----------------.   .----------------.  .----------------.   
| .--------------. || .--------------. | | .--------------. || .--------------. |  
| |  ________    | || |  _________   | | | |   _____      | || |      __      | |  
| | |_   ___ `.  | || | |_   ___  |  | | | |  |_   _|     | || |     /  \     | |  
| |   | |   `. \ | || |   | |_  \_|  | | | |    | |       | || |    / /\ \    | |  
| |   | |    | | | || |   |  _|  _   | | | |    | |   _   | || |   / ____ \   | |  
| |  _| |___.' / | || |  _| |___/ |  | | | |   _| |__/ |  | || | _/ /    \ \_ | |  
| | |________.'  | || | |_________|  | | | |  |________|  | || ||____|  |____|| |  
| |              | || |              | | | |              | || |              | |  
| '--------------' || '--------------' | | '--------------' || '--------------' |  
 '----------------'  '----------------'   '----------------'  '----------------'                                                                               
"""
logo3 = """
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------.  
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |  
| |   ______     | || |     _____    | || |    _______   | || |  _________   | || |     ______   | || |     ______   | || |     _____    | || |     ____     | || | ____  _____  | |  
| |  |_   _ \    | || |    |_   _|   | || |   /  ___  |  | || | |_   ___  |  | || |   .' ___  |  | || |   .' ___  |  | || |    |_   _|   | || |   .'    `.   | || ||_   \|_   _| | |  
| |    | |_) |   | || |      | |     | || |  |  (__ \_|  | || |   | |_  \_|  | || |  / .'   \_|  | || |  / .'   \_|  | || |      | |     | || |  /  .--.  \  | || |  |   \ | |   | |  
| |    |  __'.   | || |      | |     | || |   '.___`-.   | || |   |  _|  _   | || |  | |         | || |  | |         | || |      | |     | || |  | |    | |  | || |  | |\ \| |   | |  
| |   _| |__) |  | || |     _| |_    | || |  |`\____) |  | || |  _| |___/ |  | || |  \ `.___.'\  | || |  \ `.___.'\  | || |     _| |_    | || |  \  `--'  /  | || | _| |_\   |_  | |  
| |  |_______/   | || |    |_____|   | || |  |_______.'  | || | |_________|  | || |   `._____.'  | || |   `._____.'  | || |    |_____|   | || |   `.____.'   | || ||_____|\____| | |  
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |  
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |  
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'                                                                                                                            
"""
print(f"{logo}\n{logo2}\n{logo3}")

print("")
x = symbols('x')
fn = sympify(input("Ingrese la funcion x : "))
f = lambdify(x,fn)
xpts = np.linspace(-10,10)
plt.plot(xpts,f(xpts))
plt.title("Grafica de la funcion")
plt.axhline(color="black")
plt.axvline(color="black")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True,which='both')
plt.ylim([-15,15])
plt.show()

a = float(input("valor inicial para a: "))
b = float(input("valor inicial para b: "))

crit = float(input("Margen de error permitido :"))

i= 0 # contador de interacioines
ea = 100 # valor inicial del error
x_anterior = 0 # guardado de valor de la x

if f(a) * f(b) < 0 :
    print ("")
    print ("{:^60}".format("Metodo de la biseccion"))
    #print("{:^10}{:^10}{:^10}{:^10}{:^10}".format("i","a", "b","xr","ea(%)"))
    print("Iteracion\t\tLimite inferior(a)\tLimite superior(b)\tPunto medio(xr)\tError Aproximado(ea))")

    while ea > crit:
        xr = (a+b)/2
        ea = abs((xr-x_anterior)/xr)

        if f(xr)* f(a) < 0:
            b = xr
        else:
            a = xr
        x_anterior=xr
        # print("{:^10} {:^10} {:^10} {:^10} {:^10}".format("i","a", "b","xr", round(ea * 100,4)))
        print(f"{i}\t\t\t{round(a,4)}\t\t\t{round(b,4)}\t\t\t{round(xr,4)}\t\t\t{round(ea * 100,4)}")

        i= i + 1

    print("")
    print("La Raiz esta en :",round(xr,4),"con un error de ",round (ea * 100,4),"%")

    xpts = np.linspace(-10,10)
    plt.plot(xpts,f(xpts))
    plt.title("Grafica de la funcion")
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.scatter(xr,0,c="red")
    plt.annotate(round(xr,9),xy=(xr,0.5))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True,which='both')
    plt.ylim([-15,15])
    plt.show()
else:
    print("")
    print("La funcion no tiene raiz en los intervalos de "+"x = "+ str(a)+"a x = " + str (b))
    print("Ingrese otros valores ")
    xpts = np.linspace(-10,10)
    plt.plot(xpts,f(xpts))
    plt.title("Grafica de la funcion")
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True,which='both')
    plt.ylim([-15,15])
    plt.show()
