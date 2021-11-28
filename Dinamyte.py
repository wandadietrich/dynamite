import os

# Imprime mensaje de bienvenida.
def escribirMensajeDeBienvenida():
    os.system('cls')
    print("#" * 40)                                                            
    print("\n# Bienvenidos al gran juego \"DYNAMITE\" ;) #\n")
    print("Creado por Wanda Dietrich y Juliana Bandoni\n")    
    print("#" * 40)                                      
    
# gano: Checkea si el jugador 2 adivinó la palabra.    
# Datos de entrada:
#   palabra: palaba ingresada por el jugador 1.
#   letras: letras ingresadas por el jugador 2.     
# Dato de salida:
#   True si todas las letras de la palabra estan en la lista de letras ingresadas.
#   False de lo contrario.
def gano(palabra, letras):
    palabraEnCurso = palabraAdivinada(palabra,letras)
    resultado = palabraEnCurso == palabra
    return resultado
   
# perdió:checkea si la cantidad de letras erroneas ingresadas es mayor o igual a las oportunidades.
# Datos de entrada:
#   máximo: cantidad maxima de oportunidades.
#   palabra: palabra a adivinar, ingresada por el jugador 1.
#   letras: letras ingresadas por el jugador 2.
# Datos de salida:
#   True si el número de letras erroneas ingresadas es mayor o igual al número de oportunidades.
#   False de lo contrario.
def perdio(maximo,palabra,letras):
    cantidad = cantidadErrores(letras, palabra)
    resultado= cantidad>=maximo
    return resultado    
    
# terminoJuego:checkea si el juego terminó. Esto ocurre cuando el jugador 2 gana o pierde.
# Datos de entrada:
#   palabra: palabra a adivinar, ingresada por el jugador 1.
#   letras: letras ingresadas por el jugador 2
#   maximo: cantidad maxima de oportunidades.
# Datos de salida:
#   True si el jugador 2 ganó o perdió.
#   False si el jugador 2 no gana ni pierde.
def terminoJuego(palabra, letras, maximo): 
    return gano(palabra, letras) or perdio(maximo, palabra, letras)
    
# palabraAdivinada: checkea si las letra ingresadas se encuentran en la palabra a adivinar. Construye la palabra en proceso de adivinar.
# Datos de entrada:
#   palabra: palabra a adivinar, ingresada por el jugador 1.
#   letras: letras ingresadas por el jugador 2.
# Datos de salida:
#   Palabra a adivinar con las letras no adivinadas ocultas.
def palabraAdivinada(palabra,letras):
    resultado = ""
    for c in palabra:
        if c in letras:
            resultado= resultado + c
        else:
            resultado= resultado + " _ "            

    return resultado
 
# mostrar dinamita: imprime la dinamita.
# Datos de Entrada: 
#   cantErrores: número de veces que el jugador 2 ingeso una letra equivocada.
#   maximo: número de oportunidades. 
def mostrarDinamita(cantErrores, maximo):
    print("      ______________________________ ")
    print("     /                            / \ ")
    print("    |                            | ==", end = "")
    
    # imprimir mecha: la cual tiene un largo inicial igual al número de oportunidades y disminuye en 1 con cada letra ingresada incorrecta, hasta 0.
    for i in range(maximo, cantErrores, -1):
        print("==", end="")
    print("*")
    
    print("     \____________________________\_/ ")
  
# explosion: imprime una explosión.  
def explosion():
    print("                                 ____")
    print("                     __,-~~/~    `---.")
    print("                   _/_,---(      ,    )")
    print("               __ /        <    /   )  \___")
    print("- ------===;;;'====------------------===;;;===----- -  -")
    print("                  \/  ~\"~\"~\"~\"~\"~\~\"~)~\"/")
    print("                  (_ (   \  (     >    \)")
    print("                   \_( _ <         >_>'")
    print("                      ~ `-i' ::>|--\"")
    print("                          I;|.|.|")
    print("                         <|i::|i|`.")
    print("                        (` ^'\"`-' \")")
    
    
    
# felicitacionesGanaste: imprime fuegos artificiales de éxito.  
def felicitacionesGanaste():
    print("                                   .''.")
    print("       .''.      .        *''*    :_\/_:     .")
    print("      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.")
    print("  .''.: /\ :    /)\   ':'* /\ *  : '..'.  -=:o:=-")
    print(" :_\/_:'.:::.  | ' *''*    * '.\'/.'_\(/_ '.':'.'")
    print(" : /\ : :::::  =  *_\/_*     -= o =- /)\     '  *")
    print("  '..'  ':::' === * /\ *     .'/.\'.  ' ._____")
    print("      *        |   *..*         :       |.   |' .---\"|")
    print("        *      |     _           .--'|  ||   | _|    |")
    print("        *      |  .-'|       __  |   |  |    ||      |")
    print("     .-----.   |  |' |  ||  |  | |   |  |    ||      |")
    print(" ___'       ' /\"\ |  '-.\"\".    '-'   '-.'    '`      |____")
    print("jgs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("  &                    ~-~-~-~-~-~-~-~-~-~   /|")
    print(" ejm97    )      ~-~-~-~-~-~-~-~  /|~       /_|\\")
    print("        _-H-__  -~-~-~-~-~-~     /_|\    -~======-~")
    print("~-\XXXXXXXXXX/~     ~-~-~-~     /__|_\ ~-~-~-~")
    print("~-~-~-~-~-~    ~-~~-~-~-~-~    ========  ~-~-~-~")
    print("      ~-~~-~-~-~-~-~-~-~-~-~-~-~ ~-~~-~-~-~-~")
    print("                        ~-~~-~-~-~-~    ")
 
 
# letraEstaONo: checkea si la letra ingresada esta en la palabra a adivinar y lo muestra por mensaje. 
# Datos de Entrada:
#   letra_ingresada: letra que ingresa el jugador 2.
#   palabra: palabra a adivinar.
def letraEstaONo(letra_ingresada,palabra):
    if letra_ingresada in palabra:
       print("¡Felicitaciones! Encontraste una letra.")
    
    else:
        print("¡Uh! Te equivocaste.") 
        
# cantErrores: cuenta la cantidad de veces que el jugador 2 ingresa una letra erronea.       
# Dato de entrada: 
#   letras: letras ingresadas por el jugador 2.
#   palabra: palabra a adivinar, ingresada por el jugador 1.
# Datos de salida:
#   cantidad de letras erroneas ingresadas.    
def cantidadErrores(letras, palabra):
    cantidad=0
    for l in letras:
        if not (l in palabra):
            cantidad= cantidad+1
    return cantidad

# número de oportunidades que tiene el jugador 2 para adivinar la palabra.
oportunidades = 7

# imprime el mensaje de bienvenida.
escribirMensajeDeBienvenida()

# palabra a adivinar.
palabra = input(" Jugador 1, ingrese la palabra a adivinar y presione enter: ").upper()

# limpia la pantalla para ocultar la palabra ingresada por el jugador 1.
os.system('cls')

# imprime un encabezado de pantalla.
print("GRAN JUEGO DYNAMITE")

# lista en donde se guardan las letras ingresadas por el jugador 2.
letras_ingresadas=[]

# ciclo primcipal.
while not terminoJuego(palabra, letras_ingresadas, oportunidades):

    # letra ingresada por el jugador 2.
    letra_ingresada= input("Jugador 2, ingrese la letra: ").upper()
    
    # limpiar la pantalla.
    os.system('cls')
    
    # chekea si la letra ingresada por el jugador 2 se encuentra en la palabra a adivinar.
    letraEstaONo(letra_ingresada,palabra)
    
    # agrega la letra ingresada a la lista de letras ingresadas.
    letras_ingresadas.append(letra_ingresada)
    
    # imprime la lista de letras ingresadas.
    print(f"Letras ingresadas: {letras_ingresadas}")
    
    # imprime la palabra en proceso de construcción, con guiones (letras ocultas) y letras (adivinadas).
    print("Palabra: "+palabraAdivinada(palabra,letras_ingresadas))
    
    # actualizar dinamita. Si perdió,  mostrar explosión. Si ganó, mostrar fuegos artificiales, sino, mostrar dinamita.
    cantErrores = cantidadErrores(letras_ingresadas, palabra)
    if(perdio(oportunidades, palabra, letras_ingresadas)):
        explosion()
    elif gano(palabra, letras_ingresadas):
        felicitacionesGanaste()
    else:
        mostrarDinamita(cantErrores, oportunidades)
        
#mensaje final.
print("Termino el juego")
if gano(palabra, letras_ingresadas):
    print ("Has ganado jugador 2, FELICITACIONES!!")
else:
    print ("Has perdido jugador 2")    