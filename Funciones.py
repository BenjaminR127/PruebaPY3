import json

#se me cerro el programa y se me perdio todo

def agregarCategoria(CategoriaID:int,Nombre:str,):
    with open(biblioteca.json, mode ="r" ) as nuevaCategoriaJson:
        nuevaCategoriaJson= json.load(biblioteca.json)
        
    nuevaCategoriaJson = {}
    nuevaCategoriaJson.append = input('Ingrese su nueva categoria')
    CategoriaID = +1
               
            

            

     




def editarCategoria(CategoriaID:int,Nombre:str,):
    with open(biblioteca.json, mode="w") as archivoJson:
        leerJson = json.load(archivoJson)
        input()



def eliminarCategoria(CategoriaID:int,Nombre:str):
    with open("biblioteca.json", mode="w") as IDeliminar:
        leerJson = json.dump(IDeliminar)
    for i in (leerJson["Categoria"]):

        IDeliminar : input("Ingrese el ID de la  categoria a eliminar :")
        IDeliminar.pop
        
        print("Categoria eliminada con exito")


 

def mostrar_menu():
        print('1.-Mantenedor de categorias')
        print('2.- Reportes')
        print('3.- Salir')

    opcion = int((input('Ingrese una opcion'))
            if opcion ==1:
            menu_mantenedor_categorias
            else:
            break
    




def menu_mantenedor_categorias():
    while opcion != 5:
        print('1- Agregar Categoria')
        print('2- Editar Categoria')
        print('3- Eliminar Categoria')
        print('4- Mostrar categorias')
        print('5- Volver')

        opcion = int(input('Seleccione una opcion'))
        if opcion == 1:
             agregarCategoria()
        elif opcion == 2:
             editarCategoria()
        elif opcion == 3:
             eliminarCategoria()
        elif opcion == 4:
             mostrarCategoria()
        elif opcion == 5:
             print('Usted Esta saliendo')
             break