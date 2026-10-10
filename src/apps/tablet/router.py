import flet as ft

from apps.tablet.layout import AppLayout
from features.routes.tablet import FeatureRoutes


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
