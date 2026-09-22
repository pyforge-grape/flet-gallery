import flet as ft

from features.gallery.desktop.layout import GalleryLayout
from features.gallery.paths import GALLERY


def GalleryRoutes():
    return [
        ft.Route(
            path=GALLERY,
            component=GalleryLayout,
        ),
    ]
