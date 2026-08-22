import flet as ft

from app_layout import DesktopAppLayout, MobileAppLayout
from features.gallery.router import DesktopGalleryRoutes, MobileGalleryRoutes
from features.home.router import DesktopHomeRoutes, MobileHomeRoutes


def DesktopAppRouter():
    return ft.Router(
        [
            ft.Route(
                component=DesktopAppLayout,
                children=[
                    *DesktopGalleryRoutes(),
                    *DesktopHomeRoutes(),
                ],
            ),
        ],
    )


def MobileAppRouter():
    return ft.Router(
        [
            ft.Route(
                component=MobileAppLayout,
                children=[
                    *MobileGalleryRoutes(),
                    *MobileHomeRoutes(),
                ],
            ),
        ],
    )
