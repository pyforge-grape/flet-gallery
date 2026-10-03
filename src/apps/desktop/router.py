import flet as ft

from apps.desktop.layout import AppLayout
from features.routes_desktop import FeatureRoutes


def AppRouter():
    return ft.Router(
        [
            ft.Route(
                component=AppLayout,
                outlet=True,
                children=FeatureRoutes(),
            ),
        ],
        manage_views=True,
    )
