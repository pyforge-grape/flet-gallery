import flet as ft


@ft.component
def DesktopLayout():
    return ft.Pagelet(
        content=ft.Text("Desktop Home"),
    )


@ft.component
def MobileLayout():
    return ft.Pagelet(
        content=ft.Text("Mobile Home"),
    )
