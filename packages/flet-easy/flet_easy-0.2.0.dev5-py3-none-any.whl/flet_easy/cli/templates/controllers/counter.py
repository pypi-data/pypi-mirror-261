import flet as ft


class CounterHook:
    def __init__(self):
        self.number = ft.Ref[ft.TextButton]()
        self.input = ft.Ref[ft.TextField]()
        self.alert = ft.Ref[ft.SnackBar]()

    def get_input(self):
        return (
            int(self.input.current.value)
            if self.input.current.value is not None and self.input.current.value != ""
            else 1
        )

    def is_number(self):
        if not self.input.current.value.isdigit():
            self.alert.current.content = ft.Text(
                "Enter number", text_align="center", color="#ffffff"
            )
            self.alert.current.bgcolor = "#ef233c"
            self.alert.current.open = True
            self.alert.current.update()
            return False
        return True

    def add(self, e):
        if self.is_number():
            self.number.current.text = str(
                int(self.number.current.text) + self.get_input()
            )
            self.number.current.update()

    def remove(self, e):
        if self.is_number():
            self.number.current.text = str(
                int(self.number.current.text) - self.get_input()
            )
            self.number.current.update()

    def reload(self, e):
        self.number.current.text = "0"
        self.input.current.value = "1"
        self.input.current.update()
        self.number.current.update()
