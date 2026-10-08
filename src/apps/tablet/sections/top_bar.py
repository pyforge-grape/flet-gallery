import flet as ft

from apps.common.i18n.translations import use_translation
from apps.common.stores.locale import use_locale_store
from features.top_bar_menu_items import MENU_ITEMS


@ft.component
def AppTopBar():
    localStore = use_locale_store()
    t = use_translation(localStore.locale)

    def change_selected_item(index: int):
        ft.context.page.navigate(MENU_ITEMS[index].path)

    return ft.AppBar(
        title="Flet Gallery",
        actions=[
            ft.PopupMenuButton(
                icon=ft.CircleAvatar(
                    content="User",
                    bgcolor=ft.Colors.PRIMARY,
                    color=ft.Colors.ON_PRIMARY,
                ),
                items=[
                    ft.PopupMenuItem(
                        content=t(item.content),
                        icon=item.icon,
                        on_click=lambda _, i=index: change_selected_item(i),
                    )
                    for index, item in enumerate(MENU_ITEMS)
                ],
            ),
        ],
    )
