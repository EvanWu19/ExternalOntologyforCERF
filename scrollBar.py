import flet as ft

def main(page: ft.Page):
    

    cl = ft.Column(
        spacing=10,
        height=200,
        width=float("inf"),
        scroll=ft.ScrollMode.ADAPTIVE,
    )
    for i in range(0, 100):
        cl.controls.append(ft.Text(f"Text line {i}", key=str(i)))


    page.add(cl)
    ft.Container(cl, border=ft.border.all(1))


ft.app(main)