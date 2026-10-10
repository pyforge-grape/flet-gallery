import flet as ft

from features.content.gallery.paths import GALLERY
from features.content.gallery.tablet.layout import GalleryLayout


def GalleryRoutes():
    return [
        ft.Route(
            path=GALLERY,
            component=GalleryLayout,
        ),
    ]
