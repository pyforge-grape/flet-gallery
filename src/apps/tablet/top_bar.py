import flet as ft

from apps.common.top_bar.menu_items import MENU_ITEMS


@ft.component
def AppTopBar():
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
                        content=item.content,
                        icon=item.icon,
                        on_click=lambda _, i=index: change_selected_item(i),
                    )
                    for index, item in enumerate(MENU_ITEMS)
                ],
            ),
        ],
    )
