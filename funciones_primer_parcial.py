import os
import json
from functools import reduce

def menu_de_opciones() -> str:

    """_summary_
    La funcion imprime el menu con las opciones, y le pide al usuario que ingrese una opcion 
    si esta opcion esta dentro del rango pedido se retorna

    Returns:
        _str_: retorna la opcion elegida 
    """
    
    print("""
    |-----------------------------------------|
    |           MENU DE OPCIONES              |
    |-----------------------------------------|
    | 1. Cargar Datos desde Archivo           |
    | 2. Listar Cantidad por Marca            |
    | 3. Listar Insumos por Marca             |
    | 4. Buscar Insumo por Caracteristica     |
    | 5. Listar Insumos Ordenados             |
    | 6. Realizar Compras                     |
    | 7. Guardar en Formato JSON              |
    | 8. Leer desde Formato JSON              |
    | 9. Actualizar Precios                   |
    | 10. Salir                               |
    |-----------------------------------------|
    """)


    while True:
        try:
            opcion = int(input("Ingrese Opcion 1-10: "))
            if opcion >= 1 and opcion <= 10:
                return str(opcion)
            else:
                print("Opcion ingresada fuera de rango")
        except ValueError:
            print("Debe ingresar valores numericos")

    





# 1
def cargar_datos_desde_archivo(lista:list) -> None:

    """_summary_
    La funcion valida que la lista recibida sea del tipo list y no este vacia
    Si la lista esta vacia , carga la lista con diccionarios desde el archivo csv
    No retorna nada
    """
    
    if type(lista) != list or len(lista) > 0:
        print("La lista esta llena")
    
    else:

        with open("Insumos.csv","r",encoding="utf-8") as file:
            file = file.readlines()
            file.pop(0)
            for linea in file:
                linea = linea.strip()
                valores = linea.split(",")
                insumos = {}
                insumos["id"] = int(valores[0])
                insumos["nombre"] = valores[1]
                insumos["marca"] = valores[2]
                insumos["precio"] = (valores[3].replace("$",""))
                insumos["caracteristicas"] = valores[4]
                lista.append(insumos)
    
    





# 2



def quitar_repetidos(lista:list) -> list:

    """_summary_
    La funcion valida que la lista sea del tipo list y la lista no este vacia 
    Se recorre la lista y si el elemento no esta en la lista , se suma a la nueva lista_sin_repe
    Retorna la nueva lista sin repetidos 
    Returns:
        _list_: _description_
    """
    lista_sin_repe = []
    if type(lista) == list or len(lista) > 0:
        for item in lista:
            if esta_en_lista(lista_sin_repe,item) == False:
                lista_sin_repe.append(item)
        
        return lista_sin_repe
    else:
        print("La lista esta vacia")



def esta_en_lista(lista:list,item:str) -> bool:

    """_summary_
    La funcion valida que la lista sea del tipo list y no este vacia , tambien se valida que el item sea del tipo str
    La funcion verifica si el elemento esta o no en la lista
    Returns:
        _bool_: retorna True si el elemento esta en la lista , retorna False si el elemento no esta en la lista
    """
    if len(lista) > 0 or type(lista) == list:
        if type(item) == str:

            esta = False

            for elemento in lista:
                if elemento == item:
                    esta = True
                    break
            return esta
        else:
            print("El item ingresado no es del tipo str")
    else:
        print("La lista esta vacia")


def marcas(lista_insumos:list) -> list:

    """_summary_
    La funcion valida que la lista no este vacia y sea del tipo list 
    La funcion recorre la lista y llena la nueva lista de marcas con las marcas de cada diccionario sin repetidos

    Returns:
        _list_: Retorna la lista de marcas sin repetidos
    """
    lista_marcas = []

    if len(lista_insumos) < 0 or type(lista_insumos) != list:
        print("La lista esta vacia o no es de tipo lista")

    else:
        for insumo in lista_insumos:
            lista_marcas.append(insumo["marca"])

        lista_marcas = quitar_repetidos(lista_marcas)

    return lista_marcas


def listar_cantidad_por_marca(lista_insumos:list) -> None:

    """_summary_
    La funcion valida que la lista no este vacia y sea del tipo list 
    Recorre la lista e imprime las marcas con la cantidad de insumos de cada una
    No retorna nada
    """

    lista_marcas = marcas(lista_insumos)
    
    if len(lista_marcas) < 0 or type(lista_marcas) != list:
        print("La lista esta vacia o no es de tipo lista")

    else:
        print("|-----------------------------------------------------------------|")
        print("|     LISTA DE MARCAS CON SU RESPECTIVA CANTIDAD DE INSUMOS       |")
        print("|-----------------------------------------------------------------|")
        print("|           MARCA                              CANTIDAD           |")
        print("|-----------------------------------------------------------------|")
        
        for marca in lista_marcas:
            cantidad = len(list(filter(lambda insumo: insumo["marca"] == marca,lista_insumos)))
            print(f"|         {marca:25s}               {cantidad:2d}              |")
    







# 3

def listar_insumos_por_marca(lista_insumos:list) -> None:
    
    """_summary_
    La funcion valida que la lista no este vacia y sea del tipo list 
    Recorre la lista e imprime de cada marca el nombre de cada insumo con su precio 
    No retorna nada
    """
    lista_marcas = marcas(lista_insumos)
    
    if len(lista_marcas) < 0 or type(lista_marcas) != list:
        print("La lista esta vacia o no es de tipo lista")
    
    else:
    
        for marca in lista_marcas:
            print("|--------------------------------------------------|")
            print(f"|           MARCA:       {marca:25s} |")
            print("|--------------------------------------------------|")
            print("|       NOMBRE                      PRECIO         |")
            print("|--------------------------------------------------|")
            lista = list(filter(lambda insumo: insumo["marca"] == marca,lista_insumos))
            for insumo in lista:
                print(f"   {insumo['nombre']:30s}   {insumo['precio']}")








# 4

def buscar_insumo_por_caracteristica(lista_insumos:list) -> None:

    """_summary_
    La funcion valida que la lista no este vacia y sea del tipo list y que la caracteristica ingresada sea del tipo str
    Filtra todos los insumos que coincidan con la caracteristica ingresada y le pasa la lista filtrada de esos insumos a la funcion
    mostrar_insumos_coincidencias
    No retorna nada
    """

    caracteristica = input("Ingrese una caracteristica: ")
    if type(caracteristica) == str:

        caracteristica = caracteristica.capitalize()

        lista_coincidencia = list(filter(lambda insumo: caracteristica in insumo["caracteristicas"],lista_insumos))

        if len(lista_coincidencia) > 0 and type(lista_coincidencia) == list:
            mostrar_insumos_coincidencias(lista_coincidencia,caracteristica)
        else:
            print("Esa caracteristica no esta en la lista")

   




def mostrar_insumos_coincidencias(lista:list,caracteristica:str) -> None:

    """_summary_
    La funcion valida que la lista no este vacia y sea del tipo list 
    Recorre la lista y le pasa cada insumo  que coincidan con la caracteristica ingresada a la funcion mostrar_insumo_coincidencia
    No retorna nada
    """

    if len(lista) < 0 or type(lista) != list:
        print("La lista esta vacia o no es de tipo lista")
    
    else:
        print("|---------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print(f"|                       LISTA DE INSUMOS QUE COINCIDEN CON LA CARACTERISTICA INGRESADA:  {caracteristica}                                                     |")
        print("|---------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print("|  ID              NOMBRE                      MARCA             PRECIO                              CARACTERISTICA                                       |")
        print("|---------------------------------------------------------------------------------------------------------------------------------------------------------|")
        for coincidencia in lista:
            mostrar_insumo_coincidencia(coincidencia)




def mostrar_insumo_coincidencia(insumo:dict) -> None:

    """_summary_
    La funcion valida que lo recibido sea del tipo dict y muestra de cada diccionario sus respectivos valores
    No retorna nada
    """

    if type(insumo) == dict:
        print(f"   {insumo['id']:2d}      {insumo['nombre']:<30s}    {insumo['marca']:<20s} {insumo['precio']}        {insumo['caracteristicas']:<60s} ")
    else:
        print("No es de tipo diccionario")








# 5

def listar_insumos_ordenados(lista_insumos:list) -> None:

    """_summary_
    La funcion valida que la lista no este vacia y sea del tipo list 
    Recorre la lista cortando cada caracteristica por su separador (~) y
    de todas las caracteristicas de cada insumo deja solo la primera , despues
    ordena la lista por marcas de manera ascendente , 
    si las marcas son iguales , ordena los precios de manera descendente
    Le pasa la lista ordenada a la funcion mostrar_insumos para que la muestre
    No retorna nada
    """

    if len(lista_insumos) < 0 or type(lista_insumos) != list:
        print("La lista esta vacia o no es de tipo lista")

    else:
        for insumo in lista_insumos:
            if insumo["caracteristicas"]:
                caracteristicas = insumo["caracteristicas"].split("~")
                insumo["caracteristicas"] = caracteristicas[0]

        tam = len(lista_insumos)

        for i in range(tam - 1):
            for j in range(i + 1,tam):
                if ((lista_insumos[i]["marca"] == lista_insumos[j]["marca"]) and (lista_insumos[i]["precio"] < lista_insumos[j]["precio"])) or (lista_insumos[i]["marca"] > lista_insumos[j]["marca"]): # lo que esta en el if se llama criterio de ordenamiento
                    aux = lista_insumos[i]
                    lista_insumos[i] = lista_insumos[j]
                    lista_insumos[j] = aux

        mostrar_insumos(lista_insumos)





def mostrar_insumos(lista:list) -> None:

    """_summary_
    La funcion valida que la lista no este vacia y sea del tipo list 
    Recorre cada elemento de la lista y se lo pasa a la funcion mostrar_insumo
    No retorna nada
    """

    if len(lista) < 0 or type(lista) != list:
        print("La lista esta vacia o no es de tipo lista")

    else:
        print("|----------------------------------------------------------------------------------------------------------------------------------------|")
        print("|                                               LISTA DE INSUMOS ORDENADOS                                                               |")
        print("|----------------------------------------------------------------------------------------------------------------------------------------|")
        print("|  ID              NOMBRE                                 MARCA                         PRECIO                CARACTERISTICA             |")
        print("|----------------------------------------------------------------------------------------------------------------------------------------|")
        for insumo in lista:
            mostrar_insumo(insumo)




def mostrar_insumo(insumo:dict) -> None:

    """_summary_
    La funcion valida que lo recibido sea del tipo dict y muestra de cada diccionario sus respectivos valores
    No retorna nada
    """

    if type(insumo) == dict:
        print(f"   {insumo['id']:2d}      {insumo['nombre']:<40s}    {insumo['marca']:<30s}   {insumo['precio']}            {insumo['caracteristicas']:<40s} ")
    else:
        print("No es de tipo diccionario")










# 6

def capitalizar_palabras(cadena:str) ->str:

    """_summary_
    La funcion valida que la cadena recibida sea del tipo str , corta cada palabra por un espacio 
    , pasa la primer letra de cada palabra a mayuscula y las incluye en una lista nueva
    Con el metodo join , pasa esa lista a str nuevamente
  
    Returns:
        _str_: Retorna la cadena capitalizada
    """

    if type(cadena) == str:

        palabras_capitalizadas = []
        cadena = cadena.split()

        for palabra in cadena:
            palabra = palabra.capitalize()
            palabras_capitalizadas.append(palabra)

        cadena_capitalizada = " ".join(palabras_capitalizadas)   

        return cadena_capitalizada
    else:
        print("La cadena ingresada no es string")





def realizar_compras(lista_insumos:list) -> None:

    """_summary_
    La funcion valida que la lista no este vacia y sea del tipo list 
    Primero : le pide al usuario una marca y verifica que esa marca ingresada coincida con alguna marca de los insumos 
    y llena una lista con esos insumos
    Segundo : muestra cada uno de esos productos de la lista nueva con su respectivo precio
    Tercero : le pide al usuario que eliga uno de esos productos y la cantidad que quiere de ese producto
    Cuarto : hace el calculo del subtotal multiplicando el precio del producto elegido por la cantidad elegida
    Quinto : si el usuario no desea seguir comprando , se calcula el total de la compra , sumando los subtotales
    Por ultimo : crea una factura.txt con los datos: .Producto elegido
                                                    .Cantidad elegida
                                                    .Subtotal
                                                    .Total de la compra
    No retorna nada
    """

    
    suma = 0

    compras = []

    seguir = "s"

    if len(lista_insumos) < 0 or type(lista_insumos) != list:
        print("La lista esta vacia o no es de tipo lista")

    else:


        while seguir.lower() == "s":

            encontrado = False

            bandera = False

            lista_de_productos = []

            os.system("cls")

            marca_ingresada = input("Ingrese una marca: ")
            marca_ingresada = validar_marca(marca_ingresada)

            
            for insumo in lista_insumos:
                if insumo["marca"] == marca_ingresada:
                    lista_de_productos.append(insumo)
                    bandera = True
                    break
                    
            
            if bandera:
                print("|--------------------------------------------------|")
                print(f"|           MARCA:       {marca_ingresada:25s} |")
                print("|--------------------------------------------------|")
                print("|       NOMBRE                      PRECIO         |")
                print("|--------------------------------------------------|")
                        
                for producto in lista_de_productos:    
                    print(f"   {producto['nombre']:30s}   {producto['precio']}")
            
                
                producto = input("Ingrese un producto: ") 

                producto = producto.capitalize()

                while True:
                    try:
                        cantidad = int(input("Ingrese cantidad que quiere comprar: "))
                        if cantidad > 0: 
                            break
                        else:
                            print("Ingrese una cantidad")
                    except ValueError:
                        print("Ingreso algo que no es numero")

                for item in lista_de_productos:
                    if item["nombre"] == producto:
                        encontrado = True
                        subtotal = float(item["precio"]) * cantidad
                        compras.append({"producto": producto, "cantidad": cantidad, "subtotal": subtotal})

                if not encontrado:
                    os.system("cls")
                    print("Ese producto no esta en la lista")
            else:
                print("No se encontraron productos de la marca ingresada")    
                
            
            seguir = input("Desea seguir comprando ? S/N: ")
            
        subtotal_lista = []
        for compra in compras:
            subtotal_lista.append(float(compra["subtotal"]))
        total_compra = reduce(lambda x,y: x + y ,subtotal_lista)
       

        with open("Factura.txt", "w") as archivo:
            archivo.write("Factura de Compra\n")
            archivo.write("-----------------\n\n")
            for item in compras:
                archivo.write(f"Producto: {item['producto']}\n")
                archivo.write(f"Cantidad: {item['cantidad']}\n")
                archivo.write(f"Subtotal: ${item['subtotal']}\n")
                archivo.write("-----------------\n")
            archivo.write(f"Total de la compra: ${total_compra}\n")

        print("Compra realizada exitosamente. Se generó la factura en el archivo factura.txt.")


            

            

def validar_marca(marca_ingresada:str) -> str:

    """_summary_
    La funcion valida que la marca ingresada sea del tipo str 
    Valida que si la marca es cualquiera de las indicadas haga una logica para que coincida con la marca del insumo

    Returns:
        _str_: Retorna la marca ingresada
    """

    if type(marca_ingresada) != str:
        print("La cadena ingresada no es string")

    else:

    
        if marca_ingresada == "purina one":
            marca_ingresada = capitalizar_palabras(marca_ingresada)
            marca_ingresada = marca_ingresada.split()
            for i in range(len(marca_ingresada)):
                marca_ingresada[1] = marca_ingresada[1].upper()
            cadena = " ".join(marca_ingresada)
            marca_ingresada = cadena
            

        elif marca_ingresada == "wellness core":
            marca_ingresada = capitalizar_palabras(marca_ingresada)
            marca_ingresada = marca_ingresada.split()
            for i in range(len(marca_ingresada)):
                marca_ingresada[1] = marca_ingresada[1].upper()
            cadena = " ".join(marca_ingresada)
            marca_ingresada = cadena
            
        elif marca_ingresada == "gopetclub":
            marca_ingresada = marca_ingresada.replace('g', 'G').replace('p', 'P').replace('c', 'C')
            
        elif marca_ingresada == "petfusion":
            marca_ingresada = marca_ingresada.replace('p', 'P').replace('f', 'F')
            
        elif marca_ingresada == "amazonbasics":
            marca_ingresada = marca_ingresada.replace('a', 'A', 1).replace('b', 'B')
            
        elif marca_ingresada.islower():
            marca_ingresada = capitalizar_palabras(marca_ingresada)
                
        return marca_ingresada





# 7

def guardar_en_formato_json(lista_insumos:list) -> None:

    """_summary_
    La funcion valida que la lista no este vacia y sea del tipo list 
    Filtra todos los insumos que contengan en su nombre la palabra "Alimento"
    y guarda esos insumos en un archivo json
    No retorna nada
    """

    if len(lista_insumos) < 0 or type(lista_insumos) != list:
        print("La lista esta vacia o no es de tipo lista")

    else:
        productos_que_contienen_la_palabra_alimento = list(filter(lambda insumo: "Alimento" in insumo["nombre"],lista_insumos))

        with open("Alimento.json", "w") as file:
            json.dump(productos_que_contienen_la_palabra_alimento, file,indent = 2)




# 8

def leer_desde_formato_json(lista_insumos:list) -> None:

    """_summary_
    La funcion valida que la lista no este vacia y sea del tipo list 
    Lee el archivo json y se lo pasa a la funcion mostrar_insumos_desde_json 
    No retorna nada
    """

    if len(lista_insumos) < 0 or type(lista_insumos) != list:
        print("La lista esta vacia o no es de tipo lista")

    else:

        with open("Alimento.json","r") as file:  
            productos = json.load(file)
        
        mostrar_insumos_desde_json(productos)




def mostrar_insumos_desde_json(lista:list) -> None:

    """_summary_
    La funcion valida que la lista no este vacia y sea del tipo list 
    Recorre la lista y le pasa cada insumo a la funcion mostrar_insumo_coincidencia para que los muestre
    No retorna nada 
    """

    if len(lista) < 0 or type(lista) != list:
        print("La lista esta vacia o no es de tipo lista")

    else:
        print("|---------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print(f"|                                                    LISTA DE INSUMOS                                                                                     |")
        print("|---------------------------------------------------------------------------------------------------------------------------------------------------------|")
        print("|  ID              NOMBRE                      MARCA             PRECIO                              CARACTERISTICA                                       |")
        print("|---------------------------------------------------------------------------------------------------------------------------------------------------------|")
        for insumo in lista:
            mostrar_insumo_coincidencia(insumo)






# 9



def actualizar_precios(lista_insumos) -> None:

    """_summary_
    La funcion valida que la lista no este vacia y sea del tipo list 
    Recorre la lista de insumos y con la funcion map se obtiene una nueva lista de los precios de
    cada insumo con el aumento del 8.4 %
    Recorre la lista de los precios actualizados y con la funcion map se obtiene una nueva lista de 
    diccionarios de los insumos con sus precios actualizados 
    Por ultimo genera un nuevo archivo csv con los insumos actualizados 
    No retorna nada
    """

    if len(lista_insumos) < 0 or type(lista_insumos) != list:
        print("La lista esta vacia o no es de tipo lista")

    else:

        precios_actualizados = list(map(lambda x: float(x["precio"]) * 1.084,lista_insumos))

        productos_actualizados = list(map(lambda x, y: {**x, "precio": y}, lista_insumos, precios_actualizados))

        with open("Insumos.csv", "w",encoding="utf-8") as file:
            file.write("id,nombre,marca,precio,caracteristicas\n")
            for producto in productos_actualizados:
                linea = f"{producto['id']},{producto['nombre']},{producto['marca']},{producto['precio']},{producto['caracteristicas']}\n"
                file.write(linea)




# 10

def salir() -> bool:

    """_summary_
    La funcion le pide al usuario que ingrese S (si quiere seguir en el programa) O N (si no quiere continuar con el programa) 

    Returns:
        _bool_: En caso de ingresar S - Retorna True , En caso de ingresar N - Retorna False
    """
    respuesta = input("¿Desea salir? (S/N) ")
    if respuesta.lower() == "s":
        return True
    else:
        return False  