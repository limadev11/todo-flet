import flet as ft
import subprocess

def main(page: ft.Page):
    page.title = 'Doces da Vovó'
    page.window.width = 560
    page.window.height = 800
    page.window.center()
    page.bgcolor = ft.colors.WHITE


    
    img = ft.Container(
        content=ft.Image(
            src='logo.png',
            width=200,
            height=200,
            fit=ft.ImageFit.CONTAIN,
        ),
        alignment=ft.alignment.center,
        padding=40
    )


    login_input = ft.TextField(
    label="Digite seu E-mail",
    prefix_icon=ft.icons.EMAIL,
    width=300,
    height=50,
    text_style=ft.TextStyle(color=ft.colors.BROWN),
    bgcolor=ft.colors.WHITE,
    border_radius=8
)

    senha_input = ft.TextField(
        label='Digite sua senha',
        prefix_icon=ft.icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=300,
        height=50,
        text_style=ft.TextStyle(color=ft.colors.BROWN),
        bgcolor=ft.colors.WHITE, 
        border_radius=8,
        multiline=True
    )

    text_esqueceu = ft.TextButton(
        'Esqueceu sua senha? Clique aqui!',
    )
    
    text_cadastro = ft.TextButton(
        'Ainda não tem cadastro? Clique aqui!',
        on_click=ircadastro
    )
    
    
    def ircadastro(e):
        e:  page.go("/cadastro")
        
    def paginainicial(e):
        e:  page.go("/produto")


    botaoexecutar = ft.ElevatedButton(
        'Efetuar Login',
        bgcolor=ft.colors.BROWN,
        color=ft.colors.WHITE,
        width=200,
        on_click=paginainicial,
    )


    centerbotao = ft.Container(
        content=botaoexecutar, 
        alignment=ft.alignment.center,
        padding=10
    )
    centertexto = ft.Container(
        content=text_esqueceu, 
        alignment=ft.alignment.center,
        padding=10
    )
    centertexto2 = ft.Container(
        content=text_cadastro, 
        alignment=ft.alignment.center,
        padding=10
    )
    centerlogin = ft.Container(
        content=login_input, 
        alignment=ft.alignment.center,
        padding=3
    )
    centersenha = ft.Container(
        content=senha_input, 
        alignment=ft.alignment.center,
        padding=3
    )

    page.add(
        ft.Column(
            [
                img,
                centerlogin,
                centersenha,
                centerbotao,
                centertexto,
                centertexto2,
            ],
        )
    )

    page.update()

ft.app(target=main)
