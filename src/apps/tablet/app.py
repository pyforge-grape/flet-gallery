import flet as ft

from apps.tablet.router import AppRouter


@ft.component
def TabletApp():
    return AppRouter()
