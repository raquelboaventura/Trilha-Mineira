define s = Character(_("Sylvie"), color="#000000", image="side")
define m = Character(_("Me"), color="#050579")

image side sylvie = "images/sylvie_side.png"
default book = False

image ministerio_cultura = "gui/min-cult.png"
image pnab = "gui/pnab.png"

image mmbg = "gui/game_menu.png"

label splashscreen:
    scene black
    with Pause(1)

    $ renpy.movie_cutscene("gui/splash-l3.webm")
    
    scene black
    with Pause(1)

    show pnab with dissolve
    
    with Pause(2) 
    scene black
    show text "Bem-vindo ao jogo!" at truecenter with dissolve
    with Pause(3)
    scene black with dissolve
    return

label start:
    scene mmbg
    show sylvie_side at left
    s "Oi, eu sou a Sylvie! Minha imagem deve aparecer acima da caixa de texto."
    m "Olá, Sylvie! Eu não tenho imagem lateral."
    s "Se você está vendo minha imagem acima da caixa, está funcionando!"
    m "Fim do teste."

    menu:
        "Continuar":
            jump continue
        "Sair":
            return

    