import flet_easy as fs
import flet as ft
from views import index, counter
from core.config import ConfigApp

app = fs.FletEasy(route_init="/home")

app.add_pages(
    [
        index,
        counter,
    ]
)
ConfigApp(app)

# We run the application
app.run(view=ft.AppView.WEB_BROWSER)
