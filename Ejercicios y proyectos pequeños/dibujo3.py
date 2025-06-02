#Importar librerias
import turtle
import colorsys as cs

#Configurar el entorno (la ventana que se ve en turtle)
turtle.setup(700, 700) #Tamaño de la ventana
turtle.speed(0) #Velocidad del pincel
turtle.tracer(10) #Cantidad de los traces visibles en el canvas
turtle.width(2) #Ancho del pincel
turtle.bgcolor("black") #Color de fondo del dibujo en turtle

#Vamos a repetir los trazos 25 veces
for i in range(25):
    for j in range(15):
        #Convertir los colores a formato rgb
        #Cambiar el color del trazo en cada iteracion
        turtle.color(cs.hsv_to_rgb(j/15, i/25, 1))
        '''
        i/15 -> Controla el matiz del color cambiandolo gradualmente
        j/25 -> Controla la saturación
        1 -> define el brillo que es constante
        '''
        
        
        #Movimientos del pincel
        #left y right son los ángulos
        turtle.right(90)
        #El circulo disminuye en cada iteración creando un efecto de espiral
        turtle.circle(200 - i*4, 90)
        turtle.left(90)
        turtle.circle(200 - i*4, 90)
        turtle.right(180)
        turtle.circle(30,24)
    
    
#Levantar el pincel
turtle.hideturtle()
turtle.done()