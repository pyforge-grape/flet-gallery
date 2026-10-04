import flet as ft

from apps.common.stores.providers import StoreProviders
from apps.tablet.router import AppRouter


@ft.component
def TabletApp():
    return StoreProviders(AppRouter())
