#----------------------------------
# Proyecto: Tres en raya en Python
# Autor: Tavo
# Fecha: 23/01/2023
#----------------------------------

# Mostrar el juego para el inicio y cada jugada realizada
def imprimir_juego(matriz):
   for i in range(len(matriz)):
      # Las barras (|) no se deben imprimir junto a las coordenadas
      if i>4 and i!=8 and i!= 12:
         print("|", end="")
      else:
         print(" ", end="")
      print(matriz[i], end="") # El arreglo contiene los elementos a mostrar
      # Para los saltos de línea y ordenar el juego
      if i%4==3:
         if i!=3:
            print("|", end="")
         print("\n")

# Actualizar el arreglo que contiene los datos a mostrar en pantalla con las jugadas ingresadas
def dibujarCaracter(j,arr,c):
   # Para cada jugador, se recibe la jugada realizada y se actualiza el arreglo con los caracteres a mostrar
   # Por ejemplo: A1 -> (65-64)+4*1 = 5 -> indice para "X"
   if j == 1:
      arr[(ord(c[0])-64)+4*(int(c[1]))] = 'X' # ord(s) retorna el valor ASCII del caracter s
   else:
      arr[(ord(c[0])-64)+4*(int(c[1]))] = 'O' # ord(s) retorna el valor ASCII del caracter s

# Función para cada turno
def turnos(turno, matriz, jugadas_prohibidas):
   coordenadas_posibles = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
   # Asignar valores para cada jugador
   if turno%2==0:
      jugador = 1
      simbolo = "X"
   else:
      jugador = 2
      simbolo = "O"
   # Mensaje e ndicación para los jugadores
   if(turno>1):
      print(f"Turno del jugador {jugador} [{simbolo}]:")
      print("Ingrese coordenadas de la casilla (ej: D4):")
      # Recibir la casilla y actualizar el arreglo con los datos a mostrar
      caracter = input()
      while caracter not in coordenadas_posibles or caracter in jugadas_prohibidas:
         if caracter in jugadas_prohibidas:
            print("Casilla ya ocupada, ingrese otra (ej: D4):")
         else:
            print("Coordenadas ingresadas de forma incorrecta")
            print("Ingrese coordenadas de la casilla (ej: D4):")
         caracter = input()
      coordenadas_posibles.remove(caracter)
      jugadas_prohibidas.append(caracter)
      print(jugadas_prohibidas)
      dibujarCaracter(jugador, matriz, caracter)

# Crear los arreglos de 3 coordenadas de cada jugador para verificar un tres en raya.
def arreglos_de_tres(arr):
   arreglos = []
   arr_aux = []
   
   # Tres casos para el número de jugadas de un jugador: 3, 4 o 5
   if len(arr)==3: # Un único arreglo de 3 coordenadas tras 3 jugadas
      arreglos.append(arr)
   elif len(arr)==4: # Cuatro arreglos de 3 coordenadas tras 4 jugadas
      for i in range(4):
         arr_aux = []
         for j in range(4):
            arr_aux.append(arr[j])
         arr_aux.pop(i)
         arreglos.append(arr_aux)
   else: # Varios más arreglos de 3 coordenadas tras 5 jugadas
      for i in range(5):
         for j in range(4):
            arr_aux = []
            for k in range(5):
               arr_aux.append(arr[k])
            arr_aux.pop(i)
            arr_aux.pop(j)
            arreglos.append(arr_aux)
   #print(arreglos)
   return arreglos

# Función para verificar si hay tres en raya
def verificar_endgame(arr):
   # Arreglos que contiene todas las posibilidades para el tres en raya
   combinacionesGanadorasPosibles = [[5,6,7],[9,10,11],[13,14,15],[5,9,13],[6,10,14],[7,11,15],[5,10,15],[7,10,13]]
   gameOver = 0
   j1 = []
   j2 = []
   arrtresj1 = []
   arrtresj2 = []

   # Se van agregando las coordenadas de las jugadas de cada jugador a un arreglo
   for i in range(len(arr)):
      if arr[i]=='X':
         j1.append(i)
      if arr[i]=='O':
         j2.append(i)

   # Llamado a funciones a partir de una tercera jugada de un jugador para verificar el tres en raya
   if len(j1)>2:
      arrtresj1 = arreglos_de_tres(j1)
   if len(j2)>2:
      arrtresj2 = arreglos_de_tres(j2)

   # Verificar si alguno de los arreglos de las coordenadas es una combinación ganadora
   for j in range(len(arrtresj1)):
      if arrtresj1[j] in combinacionesGanadorasPosibles:
         gameOver = 1
   for k in range(len(arrtresj2)):
      if arrtresj2[k] in combinacionesGanadorasPosibles:
         gameOver = 2
   #print(gameOver)
   return gameOver

# Función principal
if __name__ == '__main__':
#def jugar():
   # Arreglo con los caracteres a mostrar
   juego = [" ","A","B","C",1,"_","_","_",2,"_","_","_",3,"_","_","_"]
   
   print("--------------------")
   print("---   TA-TE-TI   ---")
   print("------¡A jugar!-----")
   print("--------------------")
   imprimir_juego(juego)
   maxTurnos = 10
   win = 0
   jugadas_prohibidas = []
   # Rutina para cada turno
   while maxTurnos>1 and win==0: # Finaliza si se terminaron los turnos o hubo 3 en raya
      turnos(maxTurnos,juego, jugadas_prohibidas)
      maxTurnos-=1
      imprimir_juego(juego)
      if maxTurnos<6: # Lógicamente, solo se verificará el tres en raya desde la jugada 5
         win = verificar_endgame(juego)

   print("----------------------")
   if maxTurnos == 1 or win!=0:
      print("Game over")
      if win != 0:
         print("¡TA-TE-TI!")
         print(f"Gana el jugador {win}")
      else:
         print("¡Empate!")
   print("----------------------")