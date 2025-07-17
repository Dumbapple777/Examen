productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1],
}

#def stock_marca(marca):

def filtrarPorPrecio(precioMinimo,precioMaximo):

    diccionarioFiltrado = {}
    for clave in stock:
        if stock[clave][0] >= precioMinimo and stock[clave][0] <= precioMaximo:
            diccionarioFiltrado[clave] = stock[clave]
    return diccionarioFiltrado

while True:
    
    print("*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")
    print("")

    opcion = input("")

    match opcion:

        case "1":

            stockPorMarca = {}
            marcaIngresada = input("Ingrese marca a consultar: ")
    
            for clave in productos:
        
                if productos[clave][0] == marcaIngresada:
                    
                    stockPorMarca[clave] = productos[clave]
            
            print(stockPorMarca)

            stockTotal = {}
            numeroStock = 0
            stockdefinitivo = 0
            
            for clave in stock:
            
                if stock.keys() == stockPorMarca.keys():
                    
                    for clave in stock.values():

                        numeroStock = clave[1]
                        

            print(stockdefinitivo)
            

        case "2":

            while True:
                
                try:
                    
                    precioMinimo = int(input("Ingrese precio mínimo: ")) 
                    
                    if precioMinimo < 0:

                        print("Error: Número ingresado debe ser igual o mayor a 0")    
                    
                    else:
                        
                        break

                except ValueError:
                    
                    print("Debe ingresar valores enteros!!")
            
            while True:

                try:    
                
                    precioMaximo = int(input("Ingrese precio máximo: "))                 
                
                    if precioMaximo < 0:

                        print("Error: Número ingresado debe ser igual o mayor a 0")   

                    elif precioMaximo < precioMinimo:

                        print("Error: El precio máximo debe ser mayor a precio mínimo.") 
                    
                    else:
                        break

                except ValueError:
                    print("Debe ingresar valores enteros!!")
                    
            if precioMinimo >= 0 and precioMaximo >= 0:
                
                diccionarioFiltrado = filtrarPorPrecio(precioMinimo,precioMaximo)
                
                if len(diccionarioFiltrado) == 0:

                    print("No hay notebooks en ese rango de precios.")
                
                else:
                
                    print(f"Los notebooks entre los precios consultas son: ",diccionarioFiltrado)

        case "4":
            print("Programa finalizado.")
            break

    print("")
    
            



        

                 
            





                
                
                    
                
                    
            

                
                    