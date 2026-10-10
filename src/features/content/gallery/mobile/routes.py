import flet as ft

from features.content.gallery.mobile.layout import GalleryLayout
from features.content.gallery.paths import GALLERY


def GalleryRoutes():
    return [
        ft.Route(
            path=GALLERY,
            component=GalleryLayout,
        ),
    ]
