import flet as ft

def main(page: ft.Page):
    # Variável com a imagem certa
    imagem_correta = "tori"
    
    # Texto para feedback
    mensagem = ft.Text(
        f"Qual é o {imagem_correta}",
        text_align=ft.TextAlign.CENTER,
        size=20,
        height=50
    )

    # Função Jogar
    def jogar(e):
        imagem_selecionada = e.control.content.value
        if imagem_selecionada == imagem_correta:
            e.control.bgcolor = "#32a852"
            e.control.image.opacity = 0.3
            e.control.content.value = "😁👍"
            e.control.content.size = 40
            mensagem.value = "Parabéns! Você acertou pela 1° vez na vida!"
        else:
            e.control.bgcolor = "#ff0000"
            e.control.image.opacity = 0.3
            e.control.content.value = "😒"
            e.control.content.size = 40
            mensagem.value = f"Ops! Não é a {imagem_correta}. Tente de novo (se ainda conseguir né)."
        
        container_keira.on_click = None
        container_tori.on_click = None

        btn_jogar_novamente.visible = True

        page.update()
    
    # Função Jogar Novamente
    def jogar_novamente(e):
        btn_jogar_novamente.visible = False
        mensagem.value = f"Clique na {imagem_correta}"

        container_keira.image.opacity = 1.0
        container_keira.on_click = jogar
        container_keira.content.size = 0
        container_keira.content.value = "keira"

        container_tori.image.opacity = 1.0
        container_tori.on_click = jogar
        container_tori.content.size = 0
        container_tori.content.value = "tori"
        
        page.update()

    # Container KEIRA
    container_keira = ft.Container(
        content=ft.Text(
            "keira",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/keira.jpg",
            fit=ft.BoxFit.COVER
        ),
        width=120,
        height=120,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )
    # Container sla
    container_rapunzel = ft.Container(
        content=ft.Text(
            "rapunzel",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/rapunzel.jpg",
            fit=ft.BoxFit.COVER
        ),
        width=120,
        height=120,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    # Container TORI
    container_tori = ft.Container(
        content=ft.Text(
            "tori",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/tori.png",
            fit=ft.BoxFit.COVER
        ),
        width=120,
        height=120,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    # Botão "Jogar Novamente"
    btn_jogar_novamente = ft.Button(
        "Jogar Novamente",
        visible=False,
        on_click=jogar_novamente
    )

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Quem quis trocar de lugar no filme?",
                    size=24,
                    weight="bold"
                ),
                mensagem,
                ft.Row(
                    [
                        container_keira,
                        container_tori,
                        container_rapunzel
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                btn_jogar_novamente
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.run(main)