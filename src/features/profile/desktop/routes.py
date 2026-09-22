import flet as ft

from features.profile.desktop.layout import ProfileLayout
from features.profile.paths import PROFILE


def ProfileRoutes():
    return [
        ft.Route(
            path=PROFILE,
            component=ProfileLayout,
        ),
    ]
