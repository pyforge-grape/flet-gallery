import flet as ft

from apps.mobile.layout import AppLayout
from features.routes_mobile import FeatureRoutes


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
