import flet as ft

from apps.desktop.router import AppRouter


@ft.component
def DesktopApp():
    return AppRouter()
