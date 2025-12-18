#IMPORTAMOS FUNCIONES NECESARIAS
from jasonHandler import readJson, saveData, saveCounter, readCounter
#IMPORTAMOS TIEMPO PARA HACER PAUSAS
import time

# ============================================================
# INGREDIENTES

def agregar_ingrediente():
    print("")
    print("========================================")
    print("            ADD INGREDIENT        ")
    print("========================================")
    time.sleep(1)
    print("")
    print("\nQuick Help?")
    print("Register each ingredient so its information can be reused.")
    print("     Name: type the product exactly as you buy it.")
    print("     Base Unit: define the base unit that determines the price. E.g., kg, g, l, ml, lb, units.")
    print("     Unit Price: enter the price per unit of purchase. E.g., if it's 1kg, then enter the price for 1kg.")
    print("")
    time.sleep(1)
    
    ingredientes = readJson('ingredients.json')
    
    #CONTADOR DE IDS UTILIZADOS EN RECETAS. EVITAMOS LA ELIMINACIÓN DE INGREDIENTES ASOCIADOS
    contador = readCounter('ingredients_counter.json')
    
    #VERIFICAMOS QUE EL CONTADOR DEL ID NO SE VUELVA A REPETIR SI HAY INGREDIENTES ELIMINADOS
    contador = contador + 1
    
    #PEDIMOS LOS DATOS DEL INGREDIENTE
    nombre = input('Name (Eg., Eggs): ')
    cantidad = float(input('Quantity (E.g., 5): '))
    unidad = input('Unit (E.g., kg, g, l, ml, units): ')
    precio = float(input('Price (E.g., 1.50): Q.'))
    
    #contador = contador + 1
    
    #AGREGAMOS EL INGREDIENTE A LA LISTA DE INGREDIENTES
    ingredientes.append({
        'id': contador,
        'nombre': nombre,
        'cantidad': cantidad,
        'unidad': unidad,
        'precio': precio
    })
    
    #SE GUARDA EL INGREDIENTE Y EL CONTADOR ACTUALIZADO
    saveData('ingredients.json', ingredientes)
    saveCounter('ingredients_counter.json', contador)
    print('Ingredient added correctly!')

def mostrar_ingredientes():
    print("")
    print("========================================")
    print("         LIST OF INGREDIENTS        ")
    print("========================================")
    time.sleep(1)
    print("")

    #LEEMOS LA LISTA DE INGREDIENTES
    ingredientes = readJson('ingredients.json')
    
    if len(ingredientes) == 0:
        print('There are no ingredients...')
        return
    
    #MOSTRAMOS LA LISTA DE INGREDIENTES SEGUN EL FORMATO
    print("ID INGREDIENT  |  UNIT-BASE  |  UNIT-PRICE")
    for ingrediente in ingredientes:
        print(f"{ingrediente['id']} | {ingrediente['nombre']} | {ingrediente['unidad']} | Q.{ingrediente['precio']}")

def actualizar_ingrediente():
    print("")
    print("========================================")
    print("          UPDATE INGREDIENT        ")
    print("========================================")
    time.sleep(1)
    print("")
    print("\nQuick Help")
    print("First, the ingredients are listed with their ID.")
    print("Enter the ID of the ingredient you wish to modify.")
    print("In each field, you can press Enter to keep the current value.")
    print("")
    time.sleep(1)
    
    #LEEMOS LA LISTA DE INGREDIENTES
    ingredientes = readJson('ingredients.json')
    
    if len(ingredientes) == 0:
        print('There are no ingredients...')
        return
    
    #MOSTRAMOS LA LISTA DE INGREDIENTES DISPONIBLES
    for ingrediente in ingredientes:
        print(f"{ingrediente['id']}. {ingrediente['nombre']}")
    
    #PEDIMOS EL ID DEL INGREDIENTE A MODIFICAR
    print("\nEnter the ID of the ingredient you wish to modify.")
    id_ing = int(input('\nID: '))
    
    #BUSCAMOS EL INGREDIENTE POR SU ID Y PERMITIMOS LA ACTUALIZACIÓN
    #SI EL USUARIO PRESIONA ENTER, SE MANTIENE EL VALOR ACTUAL
    #SI INGRESA UN NUEVO VALOR, SE ACTUALIZA
    for ingrediente in ingredientes:
        if ingrediente['id'] == id_ing:
            ingrediente['nombre'] = input(f"Name ({ingrediente['nombre']}): ") or ingrediente['nombre']
            nueva_cantidad = input(f"Quantity ({ingrediente['cantidad']}): ")
            
            if nueva_cantidad:
                ingrediente['cantidad'] = float(nueva_cantidad)
            
            ingrediente['unidad'] = input(f"Unit ({ingrediente['unidad']}): ") or ingrediente['unidad']
            nuevo_precio = input(f"Price ({ingrediente['precio']}): ")
            
            if nuevo_precio:
                ingrediente['precio'] = float(nuevo_precio)
            
            #GUARDAMOS LOS CAMBIOS
            saveData('ingredients.json', ingredientes)
            print('Updated successfully!')
            return
    
    print('Ingredient not found')

def eliminar_ingrediente():
    print("")
    print("========================================")
    print("          REMOVE INGREDIENT        ")
    print("========================================")
    time.sleep(1)
    print("")

    #RECORDAMOS LA RESTRICCIÓN DE ELIMINAR INGREDIENTES ASOCIADOS A RECETAS
    #UTILIZAMOS EL MISMO FORMATO DE BÚSQUEDA POR ID
    print("\nQuick Help")
    print("The system does not allow deleting ingredients that are associated with recipes.")
    print("If the ingredient is not associated, confirmation will be requested (y/n).")
    print("First, identify the ingredient by their ID (See table).")
    print("Then, Enter the ID of the ingredient you wish to remove.")
    print("")
    time.sleep(1)
    
    ingredientes = readJson('ingredients.json')

    #CONTADOR DE IDS UTILIZADOS EN RECETAS. EVITAMOS LA ELIMINACIÓN DE INGREDIENTES ASOCIADOS
    recetas = readJson('recipes.json')
    
    if len(ingredientes) == 0:
        print('There are no ingredients...')
        return
    
    #MOSTRAMOS LA LISTA DE INGREDIENTES DISPONIBLES
    for ingrediente in ingredientes:
        print(f"{ingrediente['id']}. {ingrediente['nombre']}")
    
    #PEDIMOS EL ID DEL INGREDIENTE A ELIMINAR
    print("\nEnter the ID of the ingredient you wish to remove.")
    id_ing = int(input('\nID: '))
    
    #INDICE Y VARIABLE PARA GUARDAR EL INGREDIENTE ENCONTRADO
    ingrediente_encontrado = None
    indice_ingrediente = -1
    
    #BUSCAMOS EL INGREDIENTE POR SU ID
    for i in range(len(ingredientes)):
        if ingredientes[i]['id'] == id_ing:
            ingrediente_encontrado = ingredientes[i]
            indice_ingrediente = i
            break
    
    if ingrediente_encontrado == None:
        print('Ingredient not found')
        return
    
    #VERIFICAMOS SI EL INGREDIENTE ESTÁ ASOCIADO A ALGUNA RECETA
    contador_asociaciones = 0
    
    #RECORREMOS LAS RECETAS Y SUS INGREDIENTES PARA CONTAR ASOCIACIONES
    for receta in recetas:
        for ing in receta['ingredientes']:
            if ing['nombre'] == ingrediente_encontrado['nombre']:
                contador_asociaciones = contador_asociaciones + 1
                break
    
    #VALIDAMOS EL CONTADOR DE ASOCIACIONES Y SI EXISTEN ASOCIACIONES, NO PERMITIMOS LA ELIMINACIÓN
    if contador_asociaciones > 0:
        print(f"\nCannot delete: the ingredient is associated with recipes.")
        print(f"Associations found: {contador_asociaciones}")
        return
    
    #PROCEDEMOS SI NO HAY ASOCIACIONES Y CONFIRMAMOS LA ELIMINACIÓN Y/N
    confirmacion = input(f"\nAre you sure you want to delete '{ingrediente_encontrado['nombre']}'? (y/n): ")
    
    if confirmacion.lower() == 'y':
        ingredientes.pop(indice_ingrediente)
        saveData('ingredients.json', ingredientes)
        print('Ingredient Removed successfully!')
    else:
        print('Operation canceled')

# ============================================================
# RECETAS

def agregar_receta():
    print("")
    print("========================================")
    print("               ADD RECIPE        ")
    print("========================================")
    time.sleep(1)
    print("")
    print("\nQuick Help")
    print("First, Create a recipe")
    print("    Name: dish or preparation name. E.g., Vanilla Cookies.")
    print("    Category: recipe type for filtering. E.g., Dessert, Appetizer, Main Course.")
    print("    Portions: number of servings the recipe yields. E.g., 10.")
    print("    Description: brief detail. E.g., Soft cookies, vanilla flavor.")
    print("Next, Select the ID from the available ingredients you need for the recipe.")
    print("     Enter a single ID per ingredient.")
    print("     Press enter and repeat until all the ingredients you need are added.")
    print("When you finish adding the ingredients press 0 and you will add the recipe!")
    time.sleep(1)

    #LEEMOS LA LISTA DE INGREDIENTES Y RECETAS
    ingredientes = readJson('ingredients.json')
    recetas = readJson('recipes.json')
    
    if len(ingredientes) == 0:
        print('Option not available, First add ingredients.')
        return
    
    #LEEMOS EL CONTADOR DE RECETAS PARA ASIGNAR EL ID CORRECTO
    contador_recetas = readCounter('recipes_counter.json')
    
    #PEDIMOS LOS DATOS DE LA RECETA
    nombre = input('Name (E.g., Vanilla Cookies): ')
    categoria = input('Category (Starters, Soups, Main Course, Salads, Dessert): ')
    porciones = int(input('Portions (E.g., 10): '))
    descripcion = input('Description (E.g., Soft cookies, vanilla flavor): ')
    
    #INICIALIZAMOS LA LISTA DE INGREDIENTES DE LA RECETA
    ingredientes_receta = []
    
    #PERMITIMOS AGREGAR VARIOS INGREDIENTES HASTA QUE EL USUARIO DECIDA TERMINAR
    #LE MOSTRAMOS LA LISTA DE INGREDIENTES DISPONIBLES
    while True:
        print('\nIngredients:')
        for ingrediente in ingredientes:
            print(f"{ingrediente['id']}. {ingrediente['nombre']} ({ingrediente['unidad']})")
        
        #PEDIMOS EL ID DE CADA INGREDIENTE HASTA QUE DECIDA TERMINAR CON 0
        print("Enter the ingredient ID from the list. Type 0 to finish adding:")
        id_ing = input('\nID: ')
        if id_ing == '0':
            break
        
        #ERROR POR MARCA DE 0
        try:
            id_ing = int(id_ing)
        except:
            print("Invalid ID. Please enter a valid number.")
            continue
        
        #BUSCAMOS EL INGREDIENTE POR SU ID
        id_ing = int(id_ing)
        ingrediente_encontrado = None
        
        for ingrediente in ingredientes:
            if ingrediente['id'] == id_ing:
                ingrediente_encontrado = ingrediente
                break

        #SI ENCONTRAMOS EL INGREDIENTE, PEDIMOS CANTIDAD, UNIDAD Y PRECIO
        if ingrediente_encontrado:
            cantidad = float(input(f'Quantity of {ingrediente_encontrado["nombre"]}: '))

            #PEDIMOS LA UNIDAD Y EL PRECIO, PERO SUGERIMOS EL PRECIO SEGÚN LA UNIDAD BASE
            unidad_usada = input(f'Unit ({ingrediente_encontrado["unidad"]}): ') or ingrediente_encontrado["unidad"]
            
            #CONVERSION DE UNIDADES SEGUN RUBRICA
            precio_sugerido = ingrediente_encontrado['precio']
            
            #KG A G
            if ingrediente_encontrado['unidad'] == 'kg' and unidad_usada == 'g':
                precio_sugerido = ingrediente_encontrado['precio'] / 1000
                print(f"Suggested price for g: Q.{precio_sugerido:.2f}")
            
            #LT A ML
            elif ingrediente_encontrado['unidad'] == 'l' and unidad_usada == 'ml':
                precio_sugerido = ingrediente_encontrado['precio'] / 1000
                print(f"Suggested price for ml: Q.{precio_sugerido:.2f}")
            
            #LB A OZ
            elif ingrediente_encontrado['unidad'] == 'lb' and unidad_usada == 'oz':
                precio_sugerido = ingrediente_encontrado['precio'] / 16
                print(f"Suggested price for oz: Q.{precio_sugerido:.2f}")
            
            #PEDIMOS EL PRECIO FINAL, PERMITIENDO USAR EL SUGERIDO SEGUN CALCULO
            precio_input = input(f'Unit price for {unidad_usada} (Enter to use suggested Q.{precio_sugerido:.2f}): ')
            
            if precio_input == '':
                precio_final = precio_sugerido
            else:
                precio_final = float(precio_input)
            
            #AGREGAMOS EL INGREDIENTE A LA LISTA DE INGREDIENTES DE LA RECETA
            ingredientes_receta.append({
                'id_ingrediente': ingrediente_encontrado['id'],
                'nombre': ingrediente_encontrado['nombre'],
                'cantidad': cantidad,
                'unidad': unidad_usada,
                'precio': precio_final
            })
    
    #CALCULAMOS EL COSTO TOTAL Y COSTO POR PORCIÓN DE LA RECETA
    costo_total = sum(ing['cantidad'] * ing['precio'] for ing in ingredientes_receta)
    costo_porcion = costo_total / porciones
    
    #VALIDAMOS EL ID DE LA RECETA USANDO EL CONTADOR LEÍDO
    #ELIMINAMOS LA POSIBILIDAD DE REPETIR IDS
    contador_recetas = contador_recetas + 1
    
    #AGREGAMOS LA RECETA A LA LISTA DE RECETAS
    recetas.append({
        'id': contador_recetas,
        'nombre': nombre,
        'categoria': categoria,
        'porciones': porciones,
        'descripcion': descripcion,
        'ingredientes': ingredientes_receta,
        'costo_total': costo_total,
        'costo_porcion': costo_porcion
    })
    
    #GUARDAMOS LA RECETA
    saveData('recipes.json', recetas)
   
   #ACTUALIZAMOS EL CONTADOR DE RECETAS PARA SU PRÓXIMO USO
    saveCounter('recipes_counter.json', contador_recetas)
    print(f'\nRecipe added successfully!')
    print(f'Total Cost: Q.{costo_total:.2f}')
    print(f'Cost per Portion: Q.{costo_porcion:.2f}')

def mostrar_recetas():
    print("")
    print("========================================")
    print("            LIST OF RECIPES        ")
    print("========================================")
    time.sleep(1)
    print("")
    
    #LEEMOS LA LISTA DE RECETAS
    recetas = readJson('recipes.json')
    
    if len(recetas) == 0:
        print('There are no recipes...')
        return
    
    #PERMITIMOS FILTRAR POR CATEGORÍA
    print("Filter by Category")
    categoria = input("Category (Starters, Soups, Main Course, Salads, Dessert) or Enter for all: ")
    
    #MOSTRAMOS LA LISTA DE RECETAS SEGUN EL FORMATO
    for receta in recetas:
        if categoria == '' or receta['categoria'].lower() == categoria.lower():
            print(f"\n{receta['id']}. {receta['nombre']} ({receta['categoria']})")
            print(f"   Portions: {receta['porciones']}")
            print(f"   Cost: Q.{receta['costo_total']:.2f} - Portion: Q.{receta['costo_porcion']:.2f}")

#VISUALIZAR DETALLE DE RECETA
def ver_detalle_receta():
    print("")
    print("========================================")
    print("          RECIPE DETAIL        ")
    print("========================================")
    time.sleep(1)
    print("")
    
    #LEEMOS LA LISTA DE RECETAS
    recetas = readJson('recipes.json')
    
    if len(recetas) == 0:
        print('There are no recipes...')
        return
    
    #MOSTRAMOS LA LISTA DE RECETAS DISPONIBLES
    print("Available recipes:")
    for receta in recetas:
        print(f"{receta['id']}. {receta['nombre']}")
    
    #PEDIMOS EL ID DE LA RECETA A VISUALIZAR
    id_receta = int(input('\nEnter recipe ID: '))
    
    #BUSCAMOS LA RECETA POR SU ID
    receta_encontrada = None
    for receta in recetas:
        if receta['id'] == id_receta:
            receta_encontrada = receta
            break
    
    if receta_encontrada == None:
        print('Recipe not found')
        return
    
    #MOSTRAMOS EL RESUMEN DE LA RECETA
    print("\n" + "=" * 50)
    print("RECIPE SUMMARY")
    print("=" * 50)
    print(f"ID: {receta_encontrada['id']}")
    print(f"Name: {receta_encontrada['nombre']}")
    print(f"Category: {receta_encontrada['categoria']}")
    print(f"Portions: {receta_encontrada['porciones']}")
    print(f"Description: {receta_encontrada['descripcion']}")
    print(f"Total Cost: Q.{receta_encontrada['costo_total']:.2f}")
    print(f"Cost per Portion: Q.{receta_encontrada['costo_porcion']:.2f}")
    
    #MOSTRAMOS LISTA DE INGREGIENTES CON SUS DETALLES
    print("\n" + "=" * 50)
    print("INGREDIENTS")
    print("=" * 50)
    
    #LISTAMOS CADA INGREDIENTE CON SU CANTIDAD, PRECIO Y SUBTOTAL
    #UTILIZAMOS UN CONTADOR PARA ENUMERARLOS
    numero = 1
    for ing in receta_encontrada['ingredientes']:
        subtotal = ing['cantidad'] * ing['precio']
        print(f"\n{numero}. {ing['nombre']}")
        print(f"   ID Ingredient: {ing['id_ingrediente']}")
        print(f"   Quantity: {ing['cantidad']} {ing['unidad']}")
        print(f"   Unit Price: Q.{ing['precio']:.2f}")
        print(f"   Subtotal: Q.{subtotal:.2f}")
        numero = numero + 1
    
    print("\n" + "=" * 50)

def actualizar_receta():
    print("")
    print("========================================")
    print("             UPDATE RECIPE        ")
    print("========================================")
    time.sleep(1)
    print("")
    
    #LEEMOS LA LISTA DE RECETAS
    recetas = readJson('recipes.json')
    
    if len(recetas) == 0:
        print('There are no recipes...')
        return
    
    #MOSTRAMOS LA LISTA DE RECETAS DISPONIBLES
    for receta in recetas:
        print(f"{receta['id']}. {receta['nombre']}")
    
    #PEDIMOS EL ID DE LA RECETA A MODIFICAR
    print("\nEnter the ID of the recipe you wish to modify.")
    id_receta = int(input('\nID: '))
    
    #BUSCAMOS LA RECETA POR SU ID Y PERMITIMOS LA ACTUALIZACIÓN
    #SI EL USUARIO PRESIONA ENTER, SE MANTIENE EL VALOR ACTUAL
    #SI INGRESA UN NUEVO VALOR, SE ACTUALIZA
    #UTILIZAMOS LA MISMA LÓGICA PARA ACTUALIZAR LAS PORCIONES Y EL COSTO POR PORCIÓN
    for receta in recetas:
        if receta['id'] == id_receta:
            receta['nombre'] = input(f"Name ({receta['nombre']}): ") or receta['nombre']
            receta['categoria'] = input(f"Category ({receta['categoria']}): ") or receta['categoria']
            nuevas_porciones = input(f"Portions ({receta['porciones']}): ")
            
            if nuevas_porciones:
                receta['porciones'] = int(nuevas_porciones)
                receta['costo_porcion'] = receta['costo_total'] / receta['porciones']
            
            receta['descripcion'] = input(f"Description ({receta['descripcion']}): ") or receta['descripcion']
            
            saveData('recipes.json', recetas)
            print('Updated successfully!')
            return
    
    print('Recipe not found')

def eliminar_receta():
    print("")
    print("========================================")
    print("             REMOVE RECIPE        ")
    print("========================================")
    time.sleep(1)
    print("")

    #LEEMOS LA LISTA DE RECETAS 
    recetas = readJson('recipes.json')
    
    if len(recetas) == 0:
        print('There are no recipes...')
        return
    
    #MOSTRAMOS LA LISTA DE RECETAS DISPONIBLES
    for receta in recetas:
        print(f"{receta['id']}. {receta['nombre']}")
    
    #PEDIMOS EL ID DE LA RECETA A ELIMINAR
    print("\nEnter the ID of the recipe you wish to remove.")
    id_receta = int(input('\nID: '))
    
    #BUSCAMOS LA RECETA POR SU ID
    for i in range(len(recetas)):
        if recetas[i]['id'] == id_receta:

            #CONFIRMAMOS LA ELIMINACIÓN
            confirmacion = input(f"Are you sure you want to delete '{recetas[i]['nombre']}'? (y/n): ")
            
            if confirmacion.lower() == 'y':
                recetas.pop(i)
                saveData('recipes.json', recetas)
                print('Recipe Removed successfully!')
            else:
                print('Operation canceled')
            return
    
    print('Recipe not found')

# ============================================================
#SHOPPING LIST

def generar_lista_compras():
    print("")
    print("========================================")
    print("             SHOPPING LIST        ")
    print("========================================")
    time.sleep(1)
    print("")

    #LEEMOS LA LISTA DE RECETAS
    recetas = readJson('recipes.json')
    
    if len(recetas) == 0:
        print('There are no recipes...')
        return
    
    #MOSTRAMOS LA LISTA DE RECETAS DISPONIBLES
    print("Available recipes:")
    for receta in recetas:
        print(f"{receta['id']}. {receta['nombre']}")
    
    #PEDIMOS AL USUARIO QUE SELECCIONE VARIAS RECETAS POR SU ID
    print('\nSelect the recipes you want to include in the shopping list.')
    print('Enter the IDs separated by commas (e.g., 1,3,4):')
    ids = input('\nIDs: ')
    lista_ids = [int(x) for x in ids.split(',')]
    
    #CONSOLIDAMOS LOS INGREDIENTES NECESARIOS DE LAS RECETAS SELECCIONADAS
    consolidado = {}
    
    #RECORREMOS LAS RECETAS SELECCIONADAS
    #Y SUMAMOS LAS CANTIDADES DE CADA INGREDIENTE
    for id_receta in lista_ids:
        for receta in recetas:
            if receta['id'] == id_receta:
                for ingrediente in receta['ingredientes']:
                    nombre = ingrediente['nombre']
                    if nombre in consolidado:
                        consolidado[nombre]['cantidad'] += ingrediente['cantidad']
                    else:
                        consolidado[nombre] = {
                            'cantidad': ingrediente['cantidad'],
                            'unidad': ingrediente['unidad'],
                            'precio': ingrediente['precio']
                        }
    
    #MOSTRAMOS LA LISTA CONSOLIDADA DE INGREDIENTES
    #Y EL COSTO TOTAL ESTIMADO
    print('\n===== INGREDIENTS NEEDED =====')
    costo_total = 0
    
    for nombre, info in consolidado.items():
        costo = info['cantidad'] * info['precio']
        costo_total += costo
        print(f"{nombre}: {info['cantidad']} {info['unidad']} - Q.{costo:.2f}")
    
    print(f"\nTOTAL COST: Q.{costo_total:.2f}")