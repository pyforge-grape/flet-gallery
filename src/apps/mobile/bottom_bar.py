import flet as ft

from apps.common.stores.locale import use_locale_store
from features.bottom_bar.items import BOTTOM_BAR_ITEMS
from features.i18n.translations import use_translation


@ft.component
def AppBottomBar():
    selected_index = next(
        (
            index
            for index, item in enumerate(BOTTOM_BAR_ITEMS)
            if ft.is_route_active(item.path)
        ),
        None,
    )

    localStore = use_locale_store()
    t = use_translation(localStore.locale)

    def change_selected_item(index: int):
        ft.context.page.navigate(BOTTOM_BAR_ITEMS[index].path)

    return ft.BottomAppBar(
        content=ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        ft.IconButton(
                            icon=item.icon,
                            selected_icon=item.selected_icon,
                            selected=selected_index == index,
                            on_click=lambda _, i=index: change_selected_item(i),
                        ),
                        ft.Text(t(item.label)),
                    ],
                    expand=True,
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
                for index, item in enumerate(BOTTOM_BAR_ITEMS)
            ],
        ),
    )
