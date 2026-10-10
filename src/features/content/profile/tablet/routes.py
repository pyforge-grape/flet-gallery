import flet as ft

from features.content.profile.paths import PROFILE
from features.content.profile.tablet.layout import ProfileLayout


def ProfileRoutes():
    return [
        ft.Route(
            path=PROFILE,
            component=ProfileLayout,
        ),
    ]
