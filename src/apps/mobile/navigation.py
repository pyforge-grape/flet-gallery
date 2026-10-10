import flet as ft

from apps.common.stores.locale import use_locale_store
from features.i18n.translations import use_translation
from features.navigation.items import NAVIGATION_ITEMS_MOBILE


@ft.component
def AppNavigation():
    selected_index = next(
        (
            index
            for index, item in enumerate(NAVIGATION_ITEMS_MOBILE)
            if ft.is_route_active(item.path)
        ),
        -1,
    )

    localStore = use_locale_store()
    t = use_translation(localStore.locale)

    async def change_selected_item(e):
        index = e.control.selected_index
        ft.context.page.navigate(NAVIGATION_ITEMS_MOBILE[index].path)
        await ft.context.page.close_drawer()

    return ft.NavigationDrawer(
        selected_index=selected_index,
        on_change=change_selected_item,
        controls=[
            ft.NavigationDrawerDestination(
                label=t(item.label),
                icon=item.icon,
                selected_icon=item.selected_icon,
            )
            for item in NAVIGATION_ITEMS_MOBILE
        ],
    )
