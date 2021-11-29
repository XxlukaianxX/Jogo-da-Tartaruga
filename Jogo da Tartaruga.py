#Imports#
import turtle
from random import randrange


#Funções#

#Eventos de colisão#
#Tela 
def colisao_tela():
    #Coordenadas tartaruga
    x_tartaruga = tartaruga.xcor()
    y_tartaruga = tartaruga.ycor()

    if (x_tartaruga > 380):
        tartaruga.setpos(380, y_tartaruga)
        if (x_tartaruga > 380 and y_tartaruga > 353):
            tartaruga.setpos(380, 353)
        elif (x_tartaruga > 380 and y_tartaruga < -380):
            tartaruga.setpos(380, -380)

    elif (x_tartaruga < -380):
        tartaruga.setpos(-380, y_tartaruga)
        if (x_tartaruga < -380 and y_tartaruga > 353):
            tartaruga.setpos(-380, 353)
        elif (x_tartaruga < -380 and y_tartaruga < -380):
            tartaruga.setpos(-380, -380)

    elif (y_tartaruga > 353):
        tartaruga.setpos(x_tartaruga, 353)

    elif (y_tartaruga < -380):
        tartaruga.setpos(x_tartaruga, -380)
#Comida
def colisao_comida():
    global pontos
    global vidas
    global vidas_por_pontos

    #Coordenadas tartaruga
    x_tartaruga = tartaruga.xcor()
    y_tartaruga = tartaruga.ycor()
    #Coordenadas comida
    x_comida = comida.xcor()
    y_comida = comida.ycor()
        
    if (y_comida - 20 < y_tartaruga < y_comida + 20 and x_comida - 20 < x_tartaruga < x_comida + 20):
        Teclas_Off()
        pontos += 1
        vidas_por_pontos += 1
        if (vidas_por_pontos == 20):
            vidas += 1
            vidas_por_pontos = 0

        Comida()
        verificacao_dos_pontos()
        verificacao_das_vidas()
#Veneno
def colisao_veneno():
    global vidas

    #Coordenadas tartaruga
    x_tartaruga = tartaruga.xcor()
    y_tartaruga = tartaruga.ycor()
    #Coordenadas comida
    x_veneno = veneno.xcor()
    y_veneno = veneno.ycor()
        
    if (y_veneno - 20 < y_tartaruga < y_veneno + 20 and x_veneno - 20 < x_tartaruga < x_veneno + 20):
        Teclas_Off()
        vidas -= 1
        if (vidas == 0):
            Teclas_Off()
            restart()
        else:
            Veneno()

        verificacao_das_vidas()
#Verificação dos Pontos e Vidas
def verificacao_dos_pontos():
    #Animações Off
    janela.tracer(n = 2, delay = None)

    #Texto
    texto_pontos.clear()
    texto_pontos.write(f'Pontos: {pontos}', move = False, font = ('Arial', 20, 'bold'))

    #Animações On
    janela.tracer(n = 1, delay = None)
def verificacao_das_vidas():
    #Animações Off
    janela.tracer(n = 2, delay = None)

    #Texto
    texto_vidas.clear()
    texto_vidas.write(f'Vidas: {vidas}', move = False, font = ('Arial', 20, 'bold'))

    #Animações On
    janela.tracer(n = 1, delay = None)
#Verificação de eventos
def verificacao_eventos():
    colisao_tela()
    colisao_comida()
    colisao_veneno()

#Habilidades#
#Dash
def dash():
    global countdown_dash

    if (pontos >= 30 and countdown_dash == True):
        countdown_dash = False
        tartaruga.color('yellow')
        
        for d in range(20):
            tartaruga.forward(10)
            verificacao_eventos()

        tartaruga.color('white')
        janela.ontimer(Countdown_dash, 3000)
def Countdown_dash():
    global countdown_dash
    countdown_dash = True
#Especial
def especial():
    global countdown_especial

    if (pontos >= 50 and countdown_especial == True):
        countdown_especial = False

        tartaruga.color('yellow')
        tartaruga.speed(15)
        tartaruga.pendown()
        verificacao_eventos()
        tartaruga.forward(50)
        verificacao_eventos()
        tartaruga.right(40)
        tartaruga.forward(50)
        verificacao_eventos()

        for e in range(2):
            tartaruga.left(80)
            tartaruga.forward(100)
            verificacao_eventos()
            tartaruga.right(80)
            tartaruga.forward(100)
            verificacao_eventos()

        tartaruga.left(80)
        tartaruga.forward(50)
        verificacao_eventos()
        tartaruga.right(40)
        
        tartaruga.color('white')
        tartaruga.speed(30)
        tartaruga.penup()
        tartaruga.clear()
        janela.ontimer(Countdown_especial, 10000)
def Countdown_especial():
    global countdown_especial
    countdown_especial = True

#Direção#
#Right
def direita():
    tartaruga.right(10)
#Left
def esquerda():
    tartaruga.left(10)
#Up
def cima():
    tartaruga.forward(8)
    verificacao_eventos()
#Down
def tras():
    tartaruga.backward(3)
    verificacao_eventos()

#Comida/Veneno#
#Comida
def Comida():
    x_comida = randrange(-367, 367)
    y_comida = randrange(-367, 340)

    comida.hideturtle()
    comida.setpos(x_comida, y_comida)
    comida.showturtle()

    #Teclas On
    Teclas_On()
#Veneno
def Veneno():
    x_veneno = randrange(-367, 367)
    y_veneno = randrange(-367, 340)

    veneno.hideturtle()
    veneno.setpos(x_veneno, y_veneno)
    veneno.showturtle()

    #Teclas On
    Teclas_On()
#Timer veneno
def Timer_veneno():
    global quantidade_por_vez_veneno
    global permissao_para_prosseguir_veneno

    if (permissao_para_prosseguir_veneno == True and quantidade_por_vez_veneno == 1):
        Veneno()
        janela.ontimer(Timer_veneno, 10000)
#Timer veneno True/False
def timer_veneno_true():
    global restart_timer_veneno
    global quantidade_por_vez_veneno

    if (permissao_para_prosseguir_veneno == True):
        quantidade_por_vez_veneno += 1
        restart_timer_veneno = True

        if (quantidade_por_vez_veneno == 2):
            quantidade_por_vez_veneno = 1
            Timer_veneno()

        elif (quantidade_por_vez_veneno == 1):
            janela.ontimer(Timer_veneno, 10000)
            
        else:
            quantidade_por_vez_veneno = 0
            janela.ontimer(timer_veneno_true, 10000)
    
    elif (restart_timer_veneno == False and permissao_para_prosseguir_veneno == False):
        quantidade_por_vez_veneno = 1
        janela.ontimer(timer_veneno_true, 10000)
def timer_veneno_false():
    global permissao_para_prosseguir_veneno
    global quantidade_por_vez_veneno

    quantidade_por_vez_veneno = 0
    permissao_para_prosseguir_veneno = False
    Timer_veneno()
#Jogar - Timer_veneno True
def jogar_timer_veneno_True():
    global jogar_timer_veneno
    global quantidade_por_vez_veneno

    jogar_timer_veneno = True
    quantidade_por_vez_veneno = 1
    timer_veneno_true()

#Atalhos#
#Restart
def restart():
    global restart_timer_veneno
    global iniciar_novamente
    global perdeu_e_jogar_novamente

    #Animações Off
    janela.tracer(n = 2, delay = None)

    #Ocultar objetos
    ocultar()
    #Pause
    pause.clear()
    janela.onclick(None)
    #Timer veneno
    timer_veneno_false()

    #Pontos/Vidas
    verificacao_das_vidas()

    #Você perdeu/Jogar novamente
    perdeu_e_jogar_novamente = turtle.Turtle()
    perdeu_e_jogar_novamente.penup()
    perdeu_e_jogar_novamente.hideturtle()
    perdeu_e_jogar_novamente.speed(0)
    perdeu_e_jogar_novamente.setpos(-170, 0)
    perdeu_e_jogar_novamente.color('red')
    perdeu_e_jogar_novamente.write('Você Perdeu!', move = False, font = ('Arial', 40, 'bold'))
    perdeu_e_jogar_novamente.setpos(-200, -30)
    perdeu_e_jogar_novamente.write('Pressione "Enter" para jogar novamente...', move = False, font = ('Arial', 15, 'bold'))

    #Teclas Off
    Teclas_Off()

    iniciar_novamente = True

    #Animações On
    janela.tracer(n = 1, delay = None)
def Enter():
    global iniciar_novamente
    global pontos
    global vidas
    global vidas_por_pontos
    global perdeu_e_jogar_novamente
    global restart_timer_veneno
    global permissao_para_prosseguir_veneno
    global quantidade_por_vez_veneno

    #Animações Off
    janela.tracer(n = 2, delay = None)

    if iniciar_novamente == True:
        iniciar_novamente = False

        #Teclas On
        Teclas_On()

        #Limpar a tela
        for i in range(2):
            perdeu_e_jogar_novamente.clear()

        #Desocultar objetos
        desocultar()
        #Pause
        Pause()
        janela.onclick(evento_clique_pause)
        #Timer veneno
        if (restart_timer_veneno == True):
            restart_timer_veneno = False
            quantidade_por_vez_veneno = 1
            janela.ontimer(timer_veneno_true, 10000)

        permissao_para_prosseguir_veneno = True

        #Restart Game
        tartaruga.home()
        tartaruga.setheading(90)

        pontos = 0
        vidas = 3
        vidas_por_pontos = 0

        Comida()
        Veneno()
        verificacao_dos_pontos()
        verificacao_das_vidas()
        verificacao_eventos()

    #Animações On
    janela.tracer(n = 1, delay = None)
#Teclas On/Off
def Teclas_On():
    janela.onkeypress(direita, "Right")
    janela.onkeypress(direita, "d")
    janela.onkeypress(esquerda, "Left")
    janela.onkeypress(esquerda, "a")
    janela.onkeypress(cima, "Up")
    janela.onkeypress(cima, "w")
    janela.onkeypress(tras, "Down")
    janela.onkeypress(tras, "s")
    janela.onkey(dash, 'q')
    janela.onkey(especial, 'e')
    janela.onkey(restart, 'f')
    janela.onkey(Enter, 'Return')
def Teclas_Off():
    janela.onkeypress(None, "Right")
    janela.onkeypress(None, "d")
    janela.onkeypress(None, "Left")
    janela.onkeypress(None, "a")
    janela.onkeypress(None, "Up")
    janela.onkeypress(None, "w")
    janela.onkeypress(None, "Down")
    janela.onkeypress(None, "s")
    janela.onkey(None, 'q')
    janela.onkey(None, 'e')
    janela.onkey(None, 'f')
#Ocultar/Desocultar os objetos
def ocultar():
    tartaruga.hideturtle()
    comida.hideturtle()
    veneno.hideturtle()
def desocultar():
    tartaruga.showturtle()
    comida.showturtle()
    veneno.showturtle()

#Elementos do Jogo#
#Bordas da tela
def Bordas():
    bordas.color('yellow')
    bordas.hideturtle()
    bordas.pensize(3)
    bordas.speed(0)
    bordas.penup()
    bordas.setpos(390, 396)
    bordas.setheading(270)
    bordas.pendown()

    for b in range(3):
        bordas.forward(787)
        bordas.right(90)
    bordas.pensize(73)
    bordas.forward(790)
#Pontos/Vidas iniciais
def pontos_e_vidas_iniciais():
    #Texto pontos
    texto_pontos.hideturtle()
    texto_pontos.penup()
    texto_pontos.speed(0)
    texto_pontos.setpos(-395, 363)
    texto_pontos.write(f'Pontos: {pontos}', move = False, font = ('Arial', 20, 'bold'))
    #Texto vidas
    texto_vidas.hideturtle()
    texto_vidas.penup()
    texto_vidas.speed(0)
    texto_vidas.setpos(-200, 363)
    texto_vidas.write(f'Vidas: {vidas}', move = False, font = ('Arial', 20, 'bold'))
#Pause
def Pause():
    #Texto pause
    pause.hideturtle()
    pause.penup()
    pause.speed(0)
    pause.setpos(310, 363)
    pause.write('Pause', move = False, font = ('Arial', 20, 'bold'))
def evento_clique_pause(x, y):
    #Animações Off
    janela.tracer (n = 2, delay = None)

    if (309 < x < 389 and 370 < y < 392):
        #Menu
        background_color()
        jogar_e_sobre()
        #Evento de clique
        janela.onclick(evento_clique)
        #Teclas Off
        Teclas_Off()
        #Timer False
        timer_veneno_false()

    #Animações On
    janela.tracer (n = 1, delay = None)
#Tartaruga configurações iniciais
def tartaruga_inicial():
    tartaruga.color('white')
    tartaruga.shape('turtle')
    tartaruga.speed(30)
    tartaruga.home()
    tartaruga.setheading(90)
    tartaruga.shapesize(2)
    tartaruga.penup()
#Comida/Veneno configurações iniciais
def comida_e_veneno_iniciais():
    #Comida
    comida.hideturtle()
    comida.penup()
    comida.speed(0)
    comida.shape('circle')
    comida.color('red')
    comida.shapesize(1.5)
    Comida()
    #Veneno
    veneno.hideturtle()
    veneno.penup()
    veneno.speed(0)
    veneno.shape('circle')
    veneno.color('green')
    veneno.shapesize(1.5)
    Veneno()

#Tela inicial#
#Iniciar Jogo/Sobre
def jogar_e_sobre():
    #Texto - jogar
    jogar.hideturtle()
    jogar.penup()
    jogar.setpos(-55, 50)
    jogar.color('white')
    jogar.write('Jogar', move = False, font = ('Arial', 30, 'bold'))
    #Texto - sobre
    sobre.hideturtle()
    sobre.penup()
    sobre.setpos(-55, -10)
    sobre.color('white')
    sobre.write('Sobre', move = False, font = ('Arial', 30, 'bold'))
def texto_sobre():
    global regras_e_teclas

    regras_e_teclas = turtle.Turtle()
    regras_e_teclas.penup()
    regras_e_teclas.hideturtle()
    regras_e_teclas.color('white')
    regras_e_teclas.setpos(-50, 250)
    regras_e_teclas.write('Regras', move = False, font = ('Arial', 20, 'bold'))
    regras_e_teclas.setpos(-190, 205)
    regras_e_teclas.write('O jogo começa com 0 pontos e 3 vidas', move = False, font = ('Arial', 15, 'bold'))
    regras_e_teclas.setpos(-170, 175)
    regras_e_teclas.write('A cada 20 pontos, ganha uma vida', move = False, font = ('Arial', 15, 'bold'))
    regras_e_teclas.setpos(-300, 145)
    regras_e_teclas.write('30 pontos, é adquirido a habilidade "Dash" (countdown de 3s)', move = False, font = ('Arial', 15, 'bold'))
    regras_e_teclas.setpos(-300, 115)
    regras_e_teclas.write('50 pontos, é adquirido a habilidade "Thunder Z" (countdown de 10s)', move = False, font = ('Arial', 15, 'bold'))
    regras_e_teclas.setpos(-55, 50)
    regras_e_teclas.write('Teclado', move = False, font = ('Arial', 20, 'bold'))
    regras_e_teclas.setpos(-150, 10)
    regras_e_teclas.write('Frente: "Up" ou "w"', move = False, font = ('Arial', 15, 'bold'))
    regras_e_teclas.setpos(-150, -20)
    regras_e_teclas.write('Trás: "Down" ou "s"', move = False, font = ('Arial', 15, 'bold'))
    regras_e_teclas.setpos(-150, -50)
    regras_e_teclas.write('Direita: "Right" ou "d"', move = False, font = ('Arial', 15, 'bold'))
    regras_e_teclas.setpos(-150, -80)
    regras_e_teclas.write('Esquerda: "Left" ou "a"', move = False, font = ('Arial', 15, 'bold'))
    regras_e_teclas.setpos(-150, -110)
    regras_e_teclas.write('Dash: "q"', move = False, font = ('Arial', 15, 'bold'))
    regras_e_teclas.setpos(-150, -140)
    regras_e_teclas.write('Thunder Z: "e"', move = False, font = ('Arial', 15, 'bold'))
    regras_e_teclas.setpos(-150, -170)
    regras_e_teclas.write('Tela de reiniciar o jogo: "f"', move = False, font = ('Arial', 15, 'bold'))
    regras_e_teclas.setpos(-150, -200)
    regras_e_teclas.write('Iniciar outra partida: Enter', move = False, font = ('Arial', 15, 'bold'))
    regras_e_teclas.setpos(-110, -300)
    regras_e_teclas.write('Developed by lukaian', move = False, font = ('Arial', 15, 'bold'))
    regras_e_teclas.setpos(-392, 370)
    regras_e_teclas.write('Voltar', move = False, font = ('Arial', 17, 'bold'))
#Eventos de clique
def evento_clique(x, y):
    global jogar_timer_veneno
    global permissao_para_prosseguir_veneno
    
    #Animações Off
    janela.tracer(n = 2, delay = None)

    #Evento - Jogar
    if (-58 < x < 55 and 49 < y < 90):
        #Evento de clique "Pause"
        janela.onclick(evento_clique_pause)
        #Limpar/Desocultar
        jogar.clear()
        sobre.clear()
        background_inicial.clear()
        desocultar()
        #Teclas On
        Teclas_On()
        #Timer veneno
        permissao_para_prosseguir_veneno = True
        
        if (jogar_timer_veneno == True):
            jogar_timer_veneno = False
            janela.ontimer(jogar_timer_veneno_True, 10000)

    #Evento - Sobre
    elif (-58 < x < 59 and -3 < y < 29):
        #Evento de clique "Voltar"
        janela.onclick(evento_clique_voltar)
        #Limpar
        jogar.clear()
        sobre.clear()
        #Regras/Teclas
        texto_sobre()
        
    #Animações On
    janela.tracer(n = 1, delay = None)
def evento_clique_voltar(x, y):
    global regras_e_teclas

    #Animações Off
    janela.tracer (n = 2, delay = None)

    if (-394 < x < -324 and 374 < y < 394):
        janela.onclick(None)

        for i in range(16):
            regras_e_teclas.clear()

        jogar_e_sobre()
        janela.onclick(evento_clique)

    #Animações On
    janela.tracer (n = 1, delay = None)
#Background color
def background_color():
    #Ocultar os objetos
    ocultar()

    #Background
    background_inicial.hideturtle()
    background_inicial.penup()
    background_inicial.setpos(400,400)
    background_inicial.setheading(270)
    background_inicial.pendown()
    background_inicial.begin_fill()
    for i in range(4):
        background_inicial.forward(800)
        background_inicial.right(90)
    background_inicial.end_fill()


#Main#

#Configurações da janela
janela = turtle.Screen()
janela.setup(800, 800)
janela.bgcolor('medium slate blue')
janela.title('Jogo da Tartaruga')

#Animações Off ---
janela.tracer(n = 2, delay = None)

#Bordas da tela
bordas = turtle.Turtle()
Bordas()

#Pontos/Vidas
pontos = 0
vidas = 3
vidas_por_pontos = 0
#Texto pontos/vidas
texto_pontos = turtle.Turtle()
texto_vidas = turtle.Turtle()
pontos_e_vidas_iniciais()
#Pause
pause = turtle.Turtle()
Pause()

#Tartaruga
tartaruga = turtle.Turtle()
tartaruga_inicial()

#Comida/Veneno
comida = turtle.Turtle()
veneno = turtle.Turtle()
comida_e_veneno_iniciais()

#Tela inicial#
#Background color
background_inicial = turtle.Turtle()
background_color()
#Iniciar jogo/Sobre o jogo
jogar = turtle.Turtle()
sobre = turtle.Turtle()
#Texto jogar/Sobre
jogar_e_sobre()
#Evento de clique
janela.onclick(evento_clique)

#Animações On ---
janela.tracer(n = 1, delay = None)

#Eventos#
janela.listen()
#Teclas
Teclas_Off()
#Variáveis - Habilidades
countdown_dash = True
countdown_especial = True
#Variáveis - Restart 
iniciar_novamente = False
#Variáveis - Timer veneno
jogar_timer_veneno = True
restart_timer_veneno = True


#Loop para manter a janela aberta#
janela.mainloop()