import flet as ft

from apps.mobile.router import AppRouter


@ft.component
def MobileApp():
    return AppRouter()
