import flet as ft

from apps.common.stores.providers import StoreProviders
from apps.desktop.router import AppRouter


@ft.component
def DesktopApp():
    return StoreProviders(AppRouter())
