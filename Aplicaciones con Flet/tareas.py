import flet as ft

def main(page: ft.Page):
    page.title = "Tablero de notas Adhesivas"

    # Función para eliminar una nota
    def eliminar_nota(nota):
        grid.controls.remove(nota)
        page.update()

    def add_nota(e):
        new_nota = crear_nota("Nueva Nota")
        grid.controls.append(new_nota)
        page.update()
    
    # Crear una nota adhesiva con botón de eliminar
    def crear_nota(texto):
        note_content = ft.TextField(
            value=texto,
            multiline=True,
            color="black",  # Texto negro
        )

        nota = ft.Container(
            width=200,
            height=200,
            bgcolor="#F3AA6F",
            border_radius=10,
            padding=10,
            content=ft.Column([
                note_content,
                ft.IconButton(
                    icon=ft.Icons.DELETE,
                    icon_color="#8B0000",
                    tooltip="Eliminar nota",
                    on_click=lambda e: eliminar_nota(nota)
                )
            ])
        )
        return nota

    # Crear la cuadrícula para las notas
    grid = ft.GridView(
        expand=True,
        max_extent=220,
        horizontal=False,
        padding=20,          # Espacio interno
        spacing=10,          # Espacio entre columnas
        run_spacing=10,      # Espacio entre filas
        child_aspect_ratio=1 # Forma cuadrada
    )

    # Lista inicial de textos
    textos = [
        "Imprimir una nota nueva",
        "Arreglar el diseño de la página",
        "Terminar la aplicacion"
    ]

    # Añadir notas al grid
    for texto in textos:
        grid.controls.append(crear_nota(texto))
        

    # Fondo con margen y el grid dentro
    fondo = ft.Container(
        bgcolor="#E84A5F",
        expand=True,
        padding=20,  # Margen interno general
        content=ft.Column(
            controls=[
                ft.Row([
                    ft.Text("Notas Adhesivas", size=24, weight="bold", color="#FCE38A"),
                    ft.IconButton(
                        icon=ft.Icons.ADD,
                        on_click=add_nota,
                        icon_color="#FCE38A"
                    )
                    ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                grid
                ],
            alignment=ft.MainAxisAlignment.START
        )
    )

    # Agregar el fondo a la página
    page.add(fondo)

ft.app(target=main)
