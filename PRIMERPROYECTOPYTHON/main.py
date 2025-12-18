#IMPORTAMOS FUNCIONES
from functions import *
#IMPORTAMOS TIEMPO PARA HACER PAUSAS
import time
#IMPORTAMOS OS PARA LIMPIAR PANTALLA
import os

# ============================================================
# Main Menu

def menu_principal():
    print("")
    print("========================================")
    print("         ACME RECIPE MANAGER           ")
    print("========================================")
    time.sleep(2)
    print("")
    print("\nNeed Quick Help?")
    print("1st: Register the necessary ingredients for your first recipe.")
    print("2nd: Create recipes and link ingredients with their respective quantities.")
    print("3rd: Generate your shopping list with your selected recipes.")
    print("")
    time.sleep(1)
    print("\n Menu Options: ")
    print("1. Ingredients Menu")
    print("2. Recipes Menu")
    print("3. Shopping List")
    print("0. Exit")
    return input("Select an option: ")

# Ingredients Menu
def menu_ingredientes():
    
    while True:
        print("")
        print("========================================")
        print("           INGREDIENTS MENU            ")
        print("========================================")
        time.sleep(1)
        print("")
        print("\nNeed Quick Help?")
        print("Register each ingredient so its information can be reused.")
        print("   Name: type the product exactly as you buy it.")
        print("   Base Unit: define the unit that sets the price. E.g., kg, g, l, ml, units.")
        print("   Unit Price: enter the price per purchase unit. E.g., if it's 1kg, enter the price for 1kg.")
        print("")
        print("\n Menu Options: ")
        print("1. Add new ingredient")
        print("2. View ingredients list")
        print("3. Update ingredient information")
        print("4. Delete ingredient")
        print("0. Back to Main Menu")
        
        opcion = input("Select an option: ")
        
        if opcion == "1":
            agregar_ingrediente()
        elif opcion == "2":
            mostrar_ingredientes()
        elif opcion == "3":
            actualizar_ingrediente()
        elif opcion == "4":
            eliminar_ingrediente()
        elif opcion == "0":
            break
        else:
            print("Invalid Option")

# Recipes Menu
def menu_recetas():
    
    while True:
        print("")
        print("========================================")
        print("             Recipes Menu              ")
        print("========================================")
        time.sleep(1)
        print("")
        print("\nQuick Help")
        print("Remember to enter the necessary ingredients before creating recipes.")
        print("Add the new recipes you need.")
        print("    Name: name of the dish. E.g., Chicken Skewers.")
        print("    Category: recipe type to filter. E.g., Appetizer, Main Course, Pasta, Soup, Salad, Drink, or Dessert.")
        print("    Portions: number of servings the recipe yields. E.g., 10.")
        print("    Description: brief detail for registration. E.g., Slow cook, olive oil.")
        print("You can view, edit and delete your recipes!")
        print("")
        print("\n Menu Options: ")
        print("1. Add new recipe")
        print("2. View recipes list")
        print("3. Update recipe information")
        print("4. Delete recipe")
        print("0. Back to Main Menu")
        
        opcion = input("Select an option: ")
        
        if opcion == "1":
            agregar_receta()
        elif opcion == "2":
            mostrar_recetas()
        elif opcion == "3":
            actualizar_receta()
        elif opcion == "4":
            eliminar_receta()
        elif opcion == "0":
            break
        else:
            print("Invalid Option")

#---------------------------------------------------------
# Main Program

#COMENZAMOS A LIMPIAR PANTALLA
os.system('cls' if os.name == 'nt' else 'clear')
print("")
print("========================================")
print("         WELCOME TO ACME INC           ")
print("========================================")
print("")
print("Starting system...")
print("")
time.sleep(2)

while True:
    print("")
    opcion = menu_principal()
    
    if opcion == "0":
        print("")
        print("\nShutting Down. Thank you for using the system.")
        break
    elif opcion == "1":
        menu_ingredientes()
    elif opcion == "2":
        menu_recetas()
    elif opcion == "3":
        generar_lista_compras()
    else:
        print("Invalid option")
