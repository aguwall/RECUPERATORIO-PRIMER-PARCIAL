
# inicializar matriz
def inicializar_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any) -> list:
    matriz = []

    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    return matriz

COLUMNA = 0
JURADO_1 = 1
JURADO_2 = 2
JURADO_3 = 3

# Validar que los datos a ingresar sean correctos
def validar_nota(mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:
  

  numero = int(input(mensaje))
  while numero > maximo or numero < minimo:
      numero = int(input(mensaje_error))
  return numero

#1 Carga secuencial de votos y participantes.
def cargar_datos( matriz:list ) -> list:

  for fila in range(len(matriz)):
    matriz[fila][COLUMNA] = fila +1
    print(f"Participante N°: {fila +1}")
    matriz[fila][JURADO_1] = validar_nota("Ingrese la nota del jurado 1: ", "La nota tiene que estar entre 1 y 100. Escriba de nuevo la nota del jurado 1: ", 1, 100)
    matriz[fila][JURADO_2] = validar_nota("Ingrese la nota del jurado 2: ", "La nota tiene que estar entre 1 y 100. Escriba de nuevo la nota del jurado 2: ", 1, 100)
    matriz[fila][JURADO_3] = validar_nota("Ingrese la nota del jurado 3: ", "La nota tiene que estar entre 1 y 100. Escriba de nuevo la nota del jurado 3: ", 1, 100)
    print(f"\n")

# Calculamos la cantidad de votos totales de la matriz
def calcular_votos_totales(matriz:list) -> list:

  votos_totales = 0
  for fila in range(len(matriz)):
    votos_totales += sumar_votos_fila(matriz, fila)
  return votos_totales
    
# Calculamos la cantidad de votos por fila(participante)
def sumar_votos_fila(matriz:list, fila:int) -> int:
  
  votos_por_fila =  matriz[fila][JURADO_1] + matriz[fila][JURADO_2] + matriz[fila][JURADO_3]
  return votos_por_fila
  

# Calculamos el promedio de votos por participante
def calcular_promedio(matriz:list, fila:int) -> float:

  promedio = 0
  votos_totales = calcular_votos_totales(matriz)
  votos_por_fila = sumar_votos_fila(matriz, fila)
  if votos_totales > 0:
    promedio = votos_por_fila / (len(matriz[0]) -1)
    
  return round(promedio,2)


#2 MUESTRO LOS VOTOS

def mostrar_lista(fila:list) -> None:
 
  print(f"PARTICIPANTE N°: {fila[COLUMNA]}")
  print(f"NOTA DEL JURADO N° 1: {fila[JURADO_1]} votos")
  print(f"NOTA DEL JURADO N° 2: {fila[JURADO_2]} votos")
  print(f"NOTA DEL JURADO N° 3: {fila[JURADO_3]} votos")

#Muestro los resultados más el cálculo del promedio
def mostrar_resultados(matriz:list) -> list:

  for fila in range(len(matriz)):
    mostrar_lista(matriz[fila])
    print(f"PROMEDIO DE VOTOS: {calcular_promedio(matriz, fila)}")
    print("\n")



#3 ORDENO MATRIZ POR PROMEDIO.

def ordenar_matriz_desc(matriz:list) -> list:
 
  for i in range(len(matriz) - 1):
    for j in range(i+1,len(matriz)):
      if calcular_promedio(matriz,i) < calcular_promedio(matriz,j):
        auxiliar = matriz[i]
        matriz[i] = matriz[j]
        matriz[j] = auxiliar
  return matriz
 
def ordenar_matriz_asc(matriz:list) -> list:

  for i in range(len(matriz) - 1):
    for j in range(i+1,len(matriz)):
      if calcular_promedio(matriz, i) > calcular_promedio(matriz, j):
        auxiliar = matriz[i]
        matriz[i] = matriz[j]
        matriz[j] = auxiliar
  return matriz

#4 LOS 3 PARTICIPANTES CON PEOR PROMEDIO.

def mostrar_peores_promedios(matriz:list) -> list:

  respuesta = ordenar_matriz_asc(matriz)
  for fila in range(len(respuesta)-2): #Modifico matriz ordenada.
    print(f"PARTICIPANTE N°: {respuesta[fila][COLUMNA]}")
    print(f"NOTA DEL JURADO N° 1: {respuesta[fila][JURADO_1]}")
    print(f"NOTA DEL JURADO N° 2: {respuesta[fila][JURADO_2]}")
    print(f"NOTA DEL JURADO N° 3: {respuesta[fila][JURADO_3]}")
    print(f"PROMEDIO DE VOTOS: {calcular_promedio(respuesta, fila)}\n")
 

#5 MAYOR PROMEDIO
def mostrar_mayor_promedio(matriz:list) -> list:

  votos_totales =  calcular_votos_totales(matriz)
  promedio_de_notas_totales = votos_totales / 15 #-> 5 notas por jurado.


  for fila in range(len(matriz)):
    promedios = calcular_promedio(matriz, fila) #Me devuelve el promedio de cada participante por
    if promedios > promedio_de_notas_totales:
      print(f"PARTICIPANTE N°: {matriz[fila][COLUMNA]}")
      print(f"NOTA DEL JURADO N° 1: {matriz[fila][JURADO_1]}")
      print(f"NOTA DEL JURADO N° 2: {matriz[fila][JURADO_2]}")
      print(f"NOTA DEL JURADO N° 3: {matriz[fila][JURADO_3]}")
      print(f"PROMEDIO DE VOTOS: {calcular_promedio(matriz, fila)}\n")

#6 JURADO MALO
def mostrar_jurado_malo(matriz:list) -> list:
  
  calcular_jurado_malo(matriz)
      
def sumar_votos_por_columna(matriz:list, columna:int) -> int:
  
  suma_por_columna = 0
  for fila in range(len(matriz)):
    suma_por_columna += matriz[fila][columna]
  return suma_por_columna

def calcular_jurado_malo(matriz:list):
  
  promedio_jurado_1 = (sumar_votos_por_columna(matriz, JURADO_1) / 5)
  promedio_jurado_2 = (sumar_votos_por_columna(matriz, JURADO_2) / 5)
  promedio_jurado_3 = (sumar_votos_por_columna(matriz, JURADO_3) / 5)
       
  if promedio_jurado_1 < promedio_jurado_2 and promedio_jurado_1 < promedio_jurado_3:
    print(f"El jurado numero 1 es quien puso en promedio las notas mas bajas: {promedio_jurado_1}")
  elif promedio_jurado_2 < promedio_jurado_3:
    print(f"El jurado numero 2 es quien puso en promedio las notas mas bajas: {promedio_jurado_2}")
    
  else:
    print(f"El jurado numero 3 es quien puso en promedio las notas mas bajas: {promedio_jurado_3}")
   
#7 SUMATORIA.
def calcular_sumatoria(matriz:list) -> list:
 
  coincidencia = False
  numero_ingresado = validar_nota("Ingrese un número entre 3 y 300: ","El numero tiene que estar entre 3 y 300. Vuelva a ingresar un múmero: ", 3, 300)
  for fila in range(len(matriz)):
    if numero_ingresado == sumar_votos_fila(matriz, fila):
      mostrar_lista(matriz[fila])
      coincidencia = True
  if not coincidencia:
    print("No se encontraron coincidencias.")
    
#8 GANADOR.
def calcular_ganador(matriz:list) -> list:

  bandera = True
  ganador = 0
  fila_ganador = []

  for fila in range(len(matriz)):
    resultado = calcular_promedio(matriz, fila)
    if resultado > 0 and bandera == True:
      ganador = resultado
      bandera = False
      fila_ganador = matriz[fila]
    elif resultado > ganador:
      ganador = resultado
      fila_ganador = matriz[fila]
  mostrar_ganador(fila_ganador, ganador)


def mostrar_ganador(fila_ganador:list, ganador:int) -> list:
 
  print("EL GANADOR ES:")
  mostrar_lista(fila_ganador)
  print(f"PROMEDIO DE VOTOS: {ganador}\n")
  







