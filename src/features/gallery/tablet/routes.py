import flet as ft

from features.gallery.paths import GALLERY
from features.gallery.tablet.layout import GalleryLayout


def GalleryRoutes():
    return [
        ft.Route(
            path=GALLERY,
            component=GalleryLayout,
        ),
    ]
