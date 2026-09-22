import flet as ft

from apps.common.navigation.items import NAVIGATION_ITEMS


@ft.component
def AppNavigation():
    extended, set_extended = ft.use_state(True)

    selected_index = next(
        (
            index
            for index, item in enumerate(NAVIGATION_ITEMS)
            if ft.is_route_active(item.path)
        ),
        None,
    )

    def toggle_rail(e):
        set_extended(not extended)

    def change_selected_item(e):
        index = e.control.selected_index
        ft.context.page.navigate(NAVIGATION_ITEMS[index].path)

    return ft.NavigationRail(
        extended=extended,
        selected_index=selected_index,
        on_change=change_selected_item,
        leading=(
            ft.IconButton(
                icon=ft.Icons.CHEVRON_LEFT_SHARP,
                tooltip="Collapse",
                on_click=toggle_rail,
            )
            if extended
            else ft.IconButton(
                icon=ft.Icons.CHEVRON_RIGHT_SHARP,
                tooltip="Expand",
                on_click=toggle_rail,
            )
        ),
        destinations=[
            ft.NavigationRailDestination(
                label=item.label,
                icon=item.icon,
                selected_icon=item.selected_icon,
            )
            for item in NAVIGATION_ITEMS
        ],
    )
