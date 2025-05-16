import flet as ft

def main(page: ft.Page):
    page.title = "Doces da Vovó"
    page.window.width = 560
    page.window.height = 800
    page.window.center()
    page.bgcolor = ft.Colors.WHITE

    def produto01(e):
        page.clean()
        img = ft.Container(
            content=ft.Image(src="logo.png", width=200, height=200,fit=ft.ImageFit.CONTAIN),
            alignment=ft.alignment.center,
            padding=40,
        )
        produto_container = ft.Container(
            content=ft.Column(
                [
                    ft.Image(src="alfajor.jpeg", width=100, height=100, fit=ft.ImageFit.COVER,border_radius=10),
                    ft.Text("Alfajor", size=20, color=ft.Colors.BROWN),
                    ft.Text("R$ 10,00", size=15, color=ft.Colors.BROWN),
                    ft.Text(
                        "Descrição: Delicioso biscoito recheado com doce de leite e coberto com chocolate, feito com todo o amor da Vovó Ana. "
                        "Cada mordida é um abraço aconchegante, um pedacinho de tradição.",
                        size=12,
                        color=ft.Colors.BROWN
                    ),
                    ft.TextButton("Adicionar ao carrinho", on_click=lambda e: print("Produto adicionado ao carrinho!")),
                ],
                horizontal_alignment=ft.alignment.center
            ),
            width=300,
            padding=20,
            border=ft.border.all(2, "#DAA06D"),
            border_radius=15,
            bgcolor="#EADDCA",
            alignment=ft.alignment.center
        )
        botao_voltar = ft.ElevatedButton(
            "Voltar",
            bgcolor=ft.Colors.BROWN,
            color=ft.Colors.WHITE,
            width=200,
            on_click=pagina_inicial,
        )
        
        centerproduto1 = ft.Container(
            content=produto_container,
            alignment=ft.alignment.center,
            padding=20
            )
        
        centerbotaovoltar = ft.Container(
            content=botao_voltar,
            alignment=ft.alignment.center,
            padding=20
        )
        
        page.add(ft.Column([img, centerproduto1,centerbotaovoltar], alignment=ft.alignment.center, horizontal_alignment=ft.alignment.center))
        page.update()

    def produto02(e):
        page.clean()
        img = ft.Container(
            content=ft.Image(src='logo.png', width=200, height=200, fit=ft.ImageFit.CONTAIN),
            alignment=ft.alignment.center,
            padding=40,
        )
        produto2 = ft.Container(
            content=ft.Column(
                [
                    ft.Image(src="boxdegustacao.jpg", width=100, height=100, fit=ft.ImageFit.COVER,border_radius=10),
                    ft.Text("Box Degustação", size=20, color=ft.Colors.BROWN),
                    ft.Text("R$ 40,00", size=15, color=ft.Colors.BROWN),
                    ft.Text(
                        "Descrição: Uma seleção de doces variados para você experimentar. Cada caixa traz um pedacinho do carinho da Vovó Ana.",
                        size=12,
                        color=ft.Colors.BROWN
                    ),
                    ft.TextButton("Adicionar ao carrinho", on_click=lambda e: page.go("/carrinho")),
                ],
                horizontal_alignment=ft.alignment.center
            ),
            width=300,
            padding=20,
            border=ft.border.all(2, "#DAA06D"),
            border_radius=15,
            bgcolor="#EADDCA",
            alignment=ft.alignment.center
        )
        
        botao_voltar = ft.ElevatedButton(
            "Voltar",
            bgcolor=ft.Colors.BROWN,
            color=ft.Colors.WHITE,
            width=200,
            on_click=pagina_inicial,
        )
            
        centerproduto2 = ft.Container(content=produto2, alignment=ft.alignment.center, padding=20)
        centerbotaovoltar = ft.Container(
            content=botao_voltar,
            alignment=ft.alignment.center,
            padding=20
        )
        page.add(ft.Column([img, centerproduto2,centerbotaovoltar], alignment=ft.alignment.center, horizontal_alignment=ft.alignment.center))
        page.update()

    def produto03(e):
        page.clean()
        img = ft.Container(
            content=ft.Image(src='logo.png', width=200, height=200, fit=ft.ImageFit.CONTAIN),
            alignment=ft.alignment.center,
            padding=40,
        )
        produto3 = ft.Container(
            content=ft.Column(
                [
                    ft.Image(src="tortaholandesa.avif", width=100, height=100, fit=ft.ImageFit.COVER,border_radius=10),
                    ft.Text("Torta Holandesa", size=20, color=ft.Colors.BROWN),
                    ft.Text("R$ 35,00", size=15, color=ft.Colors.BROWN),
                    ft.Text(
                        "Descrição: Torta de chocolate com recheio cremoso e cobertura de chantilly, perfeita para adoçar seu dia.",
                        size=12,
                        color=ft.Colors.BROWN
                    ),
                    ft.TextButton("Adicionar ao carrinho", on_click=lambda e: page.go("/carrinho")),
                ],
                horizontal_alignment=ft.alignment.center
            ),
            width=300,
            padding=20,
            border=ft.border.all(2, "#DAA06D"),
            border_radius=15,
            bgcolor="#EADDCA",
            alignment=ft.alignment.center
        )
        
        botao_voltar = ft.ElevatedButton(
            "Voltar",
            bgcolor=ft.Colors.BROWN,
            color=ft.Colors.WHITE,
            width=200,
            on_click=pagina_inicial,
        )
        centerproduto3 = ft.Container(content=produto3, alignment=ft.alignment.center, padding=20)
        centerbotaovoltar = ft.Container(
            content=botao_voltar,
            alignment=ft.alignment.center,
            padding=20
        )
        
        page.add(ft.Column([img, centerproduto3,centerbotaovoltar], alignment=ft.alignment.center, horizontal_alignment=ft.alignment.center))
        page.update()

    def produto04(e):
        page.clean()
        img = ft.Container(
            content=ft.Image(src='logo.png', width=200, height=200, fit=ft.ImageFit.CONTAIN),
            alignment=ft.alignment.center,
            padding=40,
        )
        produto4 = ft.Container(
            content=ft.Column(
                [
                    ft.Image(src="tortamorango.jpg", width=100, height=100, fit=ft.ImageFit.COVER,border_radius=10),
                    ft.Text("Torta de Morango", size=20, color=ft.Colors.BROWN),
                    ft.Text("R$ 45,00", size=15, color=ft.Colors.BROWN),
                    ft.Text(
                        "Descrição: Torta de morango com creme e cobertura de chantilly, perfeita para adoçar seu dia.",
                        size=12,
                        color=ft.Colors.BROWN
                    ),
                    ft.TextButton("Adicionar ao carrinho", on_click=lambda e: page.go("/carrinho")),
                ],
                horizontal_alignment=ft.alignment.center
            ),
            width=300,
            padding=20,
            border=ft.border.all(2, "#DAA06D"),
            border_radius=15,
            bgcolor="#EADDCA",
            alignment=ft.alignment.center
        )
        botao_voltar = ft.ElevatedButton(
            "Voltar",
            bgcolor=ft.Colors.BROWN,
            color=ft.Colors.WHITE,
            width=200,
            on_click=pagina_inicial,
        )
        centerbotaovoltar = ft.Container(
            content=botao_voltar,
            alignment=ft.alignment.center,
            padding=20
        )
        
        centerproduto4 = ft.Container(content=produto4, alignment=ft.alignment.center, padding=20)
        page.add(ft.Column([img, centerproduto4,centerbotaovoltar], alignment=ft.alignment.center, horizontal_alignment=ft.alignment.center))
        page.update()

    def pagina_inicial(e):
        page.clean()
        img = ft.Container(
            content=ft.Image(src="logo.png", width=200, height=200, fit=ft.ImageFit.CONTAIN),
            alignment=ft.alignment.center,
            padding=40,
        )
        produtos = [
            ("alfajor.jpeg", "Alfajor", produto01),
            ("boxdegustacao.jpg", "Box Degustação", produto02),
            ("tortaholandesa.avif", "Torta Holandesa", produto03),
            ("tortamorango.jpg", "Torta de Morango", produto04),
        ]
        colunas = [ft.Column() for _ in range(2)]
        for i, (imagem, nome, funcao_comprar) in enumerate(produtos):
            produto = ft.Container(
                content=ft.Column(
                    [
                        ft.Image(src=imagem, width=100, height=100, fit=ft.ImageFit.COVER,border_radius=10),
                        ft.Text(nome, size=16, weight=ft.FontWeight.BOLD),
                        ft.ElevatedButton(
                            "Comprar",
                            bgcolor=ft.Colors.BROWN,
                            color=ft.Colors.WHITE,
                            width=200,
                            on_click=funcao_comprar,
                        ),
                    ],
                    horizontal_alignment=ft.alignment.center
                ),
                width=250,
                padding=20,
                border=ft.border.all(2, "#DAA06D"),
                border_radius=15,
                bgcolor="#EADDCA",
                alignment=ft.alignment.center
            )
            colunas[i % 2].controls.append(produto)
        
        botao_voltar = ft.ElevatedButton(
            "Voltar",
            bgcolor=ft.Colors.BROWN,
            color=ft.Colors.WHITE,
            width=200,
            on_click=login
        )
        page.add(
            img,
            ft.Row(colunas, alignment=ft.alignment.center, spacing=20),
            ft.Container(content=botao_voltar, alignment=ft.alignment.center)
        )
        page.update()

    def ir_cadastro(e):
        page.clean()
        img = ft.Container(
            content=ft.Image(src='logo.png', width=200, height=200, fit=ft.ImageFit.CONTAIN),
            alignment=ft.alignment.center,
            padding=30
        )
        nome_input = ft.TextField(label="Digite seu nome", prefix_icon=ft.Icons.PERSON, width=300,bgcolor=ft.Colors.BROWN_200,border_radius=10,border_color=ft.Colors.BROWN)
        sobrenome_input = ft.TextField(label="Digite seu sobrenome", prefix_icon=ft.Icons.PERSON, width=300,bgcolor=ft.Colors.BROWN_200,border_radius=10,border_color=ft.Colors.BROWN)
        email_input = ft.TextField(label="Digite seu E-mail", prefix_icon=ft.Icons.EMAIL, width=300,bgcolor=ft.Colors.BROWN_200,border_radius=10,border_color=ft.Colors.BROWN)
        telefone_input = ft.TextField(label="Digite seu telefone", prefix_icon=ft.Icons.PHONE, width=300,bgcolor=ft.Colors.BROWN_200,border_radius=10,border_color=ft.Colors.BROWN)
        senha_input = ft.TextField(label="Digite sua senha", prefix_icon=ft.Icons.LOCK, password=True, can_reveal_password=True, width=300,bgcolor=ft.Colors.BROWN_200,border_radius=10,border_color=ft.Colors.BROWN)
        senhaconfirm_input = ft.TextField(label="Confirme sua senha", prefix_icon=ft.Icons.LOCK, password=True, can_reveal_password=True, width=300,bgcolor=ft.Colors.BROWN_200,border_radius=10,border_color=ft.Colors.BROWN)
        
        def voltar(e):
            login(e)
        
        botao_cadastrar = ft.ElevatedButton("Efetuar Cadastro", bgcolor=ft.Colors.BROWN, color=ft.Colors.WHITE, width=200)
        botao_voltar = ft.ElevatedButton("Voltar", bgcolor=ft.Colors.BROWN, color=ft.Colors.WHITE, width=200, on_click=voltar)
        
        page.add(
            ft.Column(
                controls=[
                    img,
                    ft.Container(content=nome_input, alignment=ft.alignment.center, padding=3),
                    ft.Container(content=sobrenome_input, alignment=ft.alignment.center, padding=3),
                    ft.Container(content=email_input, alignment=ft.alignment.center, padding=3),
                    ft.Container(content=telefone_input, alignment=ft.alignment.center, padding=3),
                    ft.Container(content=senha_input, alignment=ft.alignment.center, padding=3),
                    ft.Container(content=senhaconfirm_input, alignment=ft.alignment.center, padding=3),
                    ft.Container(content=botao_cadastrar, alignment=ft.alignment.center, padding=3),
                    ft.Container(content=botao_voltar, alignment=ft.alignment.center, padding=3),
                ],
                horizontal_alignment=ft.alignment.center
            )
        )
        page.update()

    # --- Função de Login ---
    def login(e=None):
        page.clean()
        img = ft.Container(
            content=ft.Image(src="logo.png", width=200, height=200, fit=ft.ImageFit.CONTAIN),
            alignment=ft.alignment.center,
            padding=40,
        )
        login_input = ft.TextField(label="Digite seu E-mail", prefix_icon=ft.Icons.EMAIL, width=300,bgcolor=ft.Colors.BROWN_200,border_radius=10,border_color=ft.Colors.BROWN)
        senha_input = ft.TextField(label="Digite sua senha", prefix_icon=ft.Icons.LOCK, password=True, can_reveal_password=True, width=300,bgcolor=ft.Colors.BROWN_200,border_radius=10,border_color=ft.Colors.BROWN)
        text_esqueceu = ft.TextButton("Esqueceu sua senha? Clique aqui!")
        text_cadastro = ft.TextButton("Ainda não tem cadastro? Clique aqui!", on_click=ir_cadastro)
        botao_executar = ft.ElevatedButton("Efetuar Login", bgcolor=ft.Colors.BROWN, color=ft.Colors.WHITE, width=200, on_click=pagina_inicial)
        
        layout = ft.Column(
            controls=[
                img,
                ft.Container(content=login_input, alignment=ft.alignment.center, padding=10,),
                ft.Container(content=senha_input, alignment=ft.alignment.center, padding=10),
                ft.Container(content=botao_executar, alignment=ft.alignment.center, padding=10),
                ft.Container(content=text_esqueceu, alignment=ft.alignment.center, padding=10),
                ft.Container(content=text_cadastro, alignment=ft.alignment.center, padding=10),
            ],
            alignment=ft.alignment.center
        )
        page.add(layout)
        page.update()

    # Exibe a página de Login ao iniciar
    login()

ft.app(target=main)
