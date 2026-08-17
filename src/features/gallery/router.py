import flet as ft

from features.gallery.layout import DesktopLayout, MobileLayout

PATH = "/gallery"


def DesktopGalleryRoutes():
    return [
        ft.Route(
            path=PATH.removeprefix("/"),
            component=DesktopLayout,
        ),
    ]


def MobileGalleryRoutes():
    return [
        ft.Route(
            path=PATH.removeprefix("/"),
            component=MobileLayout,
        ),
    ]


def ToGallery():
    ft.context.page.navigate(PATH)
