import flet as ft

from features.profile.paths import PROFILE
from features.profile.tablet.layout import ProfileLayout


def ProfileRoutes():
    return [
        ft.Route(
            path=PROFILE,
            component=ProfileLayout,
        ),
    ]
