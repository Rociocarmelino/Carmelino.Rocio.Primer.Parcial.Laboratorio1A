
from funciones_primer_parcial import *

insumos = []

bandera = False

bandera_datos_actualizados = True


while True:
    os.system("cls")

    match(menu_de_opciones()):
        case "1":
            if bandera == False:
                cargar_datos_desde_archivo(insumos)
                bandera = True
            else:
                print("Ya se cargaron los datos")
        case "2":
            if bandera:
                listar_cantidad_por_marca(insumos)
            else:
                print("Primero debe ingresar a la opcion 1")
        case "3":
            if bandera:
                listar_insumos_por_marca(insumos)
            else:
                print("Primero debe ingresar a la opcion 1")
        case "4":
            if bandera:
                buscar_insumo_por_caracteristica(insumos)
            else:
                print("Primero debe ingresar a la opcion 1")
        case "5":
            if bandera:
                listar_insumos_ordenados(insumos)
            else:
                print("Primero debe ingresar a la opcion 1")
        case "6":
            if bandera:
                realizar_compras(insumos)
            else:
                print("Primero debe ingresar a la opcion 1")
        case "7":
            if bandera:
                guardar_en_formato_json(insumos)
            else:
                print("Primero debe ingresar a la opcion 1")
        case "8":
            if bandera:
                leer_desde_formato_json(insumos)
            else:
                print("Primero debe ingresar a la opcion 1")
        case "9":
            if bandera and bandera_datos_actualizados:
                actualizar_precios(insumos)
                bandera_datos_actualizados = False

            else:
                print("Primero debe ingresar a la opcion 1")
        case "10":
            if bandera or bandera_datos_actualizados == False:
                agregar_producto(insumos)
        case "11":
            if bandera or bandera_datos_actualizados == False:
                guardar_datos_en_csv_o_json(insumos)
        case "12":
            if salir():
                break
    os.system("pause")



