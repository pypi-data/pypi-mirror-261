import flet as ft
import flet_easy as fs
from components import Counter

counter = fs.AddPagesy(
    route_prefix="/counter",
)


# We add a second page
@counter.page(route="/test/{id}", title="Counter")
def counter_page(data: fs.Datasy, id: str):
    page = data.page
    view = data.view

    def show_drawer(e):
        view.drawer.open = True
        page.update()

    return ft.View(
        route="/counter",
        controls=[
            Counter(page=page, id=id, width=250),
            ft.FilledButton("Show_drawer", on_click=show_drawer),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        drawer=view.drawer,
    )
