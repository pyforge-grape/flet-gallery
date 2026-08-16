import flet as ft

from mobile_app_router import MobileAppRouter


@ft.component
def MobileApp():
    return MobileAppRouter()
