import flet as ft
import os

os.system('cls')

#Interfaz donde se ponen los elementos 
def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_800
    page.title ="Aplicacion con Flet"
    texto = ft.Text("Mi primera app con Flet")
    page.add(texto)
    texto2 = ft.Text("Haciendo la aplicación")
    

#Funcion target main
ft.app(target=main)
    
