import flet as ft


@ft.component
def App():
    return ft.View(
        controls=[
            ft.SafeArea(
                expand=True,
                content=ft.Pagelet(
                    content=ft.Text("Pagelet"),
                ),
            )
        ],
    )
