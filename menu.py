
from funciones import *

def menu():
  matriz = []
  
  while(True):
    opcion = int(input("""
    Elija la opcion deseada:
    -----------------
                       
    1) Asignar notas a los cocineros.
    2) Mostrar notas de los cocineros.
    3) Mostrar notas de manera ascendente o descendente.
    4) Mostrar los peores promedios.
    5) Mostrar los mejores promedios.
    6) Nota jurado malo.
    7) Mostrar sumatoria.
    8) Ganador :D
    9) Salir
    
    Su opción elegida es: """))
    
    if opcion == 1:
      matriz = inicializar_matriz(5,4,0)
      cargar_datos(matriz)
    elif opcion == 2:
      if not matriz:
        print("No hay datos cargados, elija la opcion 1 para realizar la carga de datos.")
      else:
        mostrar_resultados(matriz)
    elif opcion == 3:
      if not matriz:
          print("Aun no se puede ordenar la matriz, esta vacia")
      else:
          orden = input("¿Quiere que se ordene de forma ascendente o descendente? (Ingrese 'desc' o 'asc'): ")
          if orden != "asc" and orden != "desc":
            print("Opcion incorrecta.")
          elif orden == "asc":           
            print("\n La matriz fue ordenada de manera ascendente, presione la opcion 2 para ver el resultado.")
            ordenar_matriz_asc(matriz)
            
          elif orden == "desc":
            print("\n La matriz fue ordenada de manera descendente, presione la opcion 2 para ver el resultado.")
            ordenar_matriz_desc(matriz)
          
    elif opcion == 4:
      if not matriz:        
        print("Aun no se pueden visualizar los 3 peores promedios.")
      else:
        print("Muestro los peores 3 participantes por su promedio.")
        mostrar_peores_promedios(matriz)
        
    elif opcion == 5:
      if not matriz:
        print("No se pueden ver los 3 mejores promedios ")
      else:
        print("Mostrado los participantes que superan el promedio general de notas.")
        mostrar_mayor_promedio(matriz)
        
    elif opcion == 6:
      if not matriz:
        print("El jurado aun no realizo la votacion por falta de carga de datos.")
      else:
        print("Mostrando al jurado que puso en promedio las peores notas.")
        mostrar_jurado_malo(matriz)
        
    elif opcion == 7:
      if not matriz:       
        print("Aun no hay coincidencia, no hay datos cargados.")
      else:        
        print("Muestro participantes cuyas notas sumadas coincidan con el numero ingresado.")
        calcular_sumatoria(matriz)
        
    elif opcion == 8:
      if not matriz:       
        print("Aún no hay un ganador porque el array esta vacio.")
      else:
        print("Muestro al ganador.")
        calcular_ganador(matriz)
        
    elif opcion == 9:
      print("Saliendo...")
      break
    else:      
      print("Debe elegir una opcion entre 1 y 9 - Vuelva a ingresar una opcion correcta: ")


menu()
      

