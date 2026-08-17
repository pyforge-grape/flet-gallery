import flet as ft

from app_router import DesktopAppRouter, MobileAppRouter


@ft.component
def DesktopApp():
    return DesktopAppRouter()


@ft.component
def MobileApp():
    return MobileAppRouter()
