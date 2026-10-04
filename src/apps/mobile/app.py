import flet as ft

from apps.common.stores.providers import StoreProviders
from apps.mobile.router import AppRouter


@ft.component
def MobileApp():
    return StoreProviders(AppRouter())
