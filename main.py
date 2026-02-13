import flet as ft

def main(page: ft.Page):

    def clicou(e):
        page.add(
            ft.Text(f"Clicou no container:{e.control.content.value}")
        )

    def passou(e):
        page.add(
            ft.Text("Passou sobre o container")
        ),
        if(e.control.bgcolor =="lightblue"):
            e.control.bgcolor="green"
        else:
            e.control.bgcolor="lightblue"
       




    page.title = "Aula 6 - Container"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll= ft.ScrollMode.ADAPTIVE

    page.add(
        ft.Container(
            content=ft.Text("Container com Padding, margin e borda."),
            bgcolor="lightblue",
            padding=20,
            margin=15,
            border=ft.border.all(8, ft.Colors.BLACK),
            border_radius=10,
            width=200,
            height=200,
            on_click=clicou,
            on_hover=passou,
            image=ft.DecorationImage(
                src="images/flok.jpg",
                fit=ft.BoxFit.COVER
            )
        )
    )

ft.run(main)