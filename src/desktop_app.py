import flet as ft

from desktop_app_router import DesktopAppRouter


@ft.component
def DesktopApp():
    return DesktopAppRouter()
