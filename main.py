import time

t0 = time.perf_counter()
import flet as ft
flet_import_ms = (time.perf_counter() - t0) * 1000


def main(page: ft.Page):
    page.title = "Hello World"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Text(
            f"Hello, World! {flet_import_ms}ms",
            size=32,
            weight=ft.FontWeight.BOLD,
        )
    )


if __name__ == "__main__":
    ft.run(main)
