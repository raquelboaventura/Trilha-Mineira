define s = Character(_("Aline"), color="#f75f00", image="side")
define m = Character(_("Me"), color="#050579")

# Definição correta da imagem lateral (Side Image)
# Nome da imagem é 'side aline feliz'
image side aline feliz = "images/aline feliz.png" 

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

    # CORREÇÃO: Chamando a imagem pelo seu nome completo e tag.
    # O nome é 'aline feliz', e a tag é 'side'.
    show side aline feliz at left 
    
    s "Oi, eu sou a Aline! Minha imagem deve aparecer acima da caixa de texto."
    m "Olá! Eu não tenho imagem lateral."
    
    # Exemplo: Ocultando a Side Image no final da fala
    hide side aline feliz

    s "Se você viu minha imagem acima da caixa, está funcionando!"
    m "Fim do teste."

    menu:
        "Continuar":
            jump continue
        "Sair":
            return
