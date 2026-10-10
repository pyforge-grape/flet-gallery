import flet as ft

from features.content.profile.mobile.layout import ProfileLayout
from features.content.profile.paths import PROFILE


def ProfileRoutes():
    return [
        ft.Route(
            path=PROFILE,
            component=ProfileLayout,
        ),
    ]
