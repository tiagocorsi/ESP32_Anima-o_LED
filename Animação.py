#Desenvolvido por: Tiago Henrique Corsi
#Data: 13/08/2022
#Sequencia de LEDs gerando uma animação

from machine import Pin
import machine, neopixel, time, random

#handler do botão
def button_handler(pin):
  global button_pressed
  button_pressed = pin

#definição botao
button1 = Pin(15, Pin.IN, Pin.PULL_UP)
button1.irq(trigger=Pin.IRQ_RISING, handler=button_handler)
button2 = Pin(14, Pin.IN, Pin.PULL_UP)
button2.irq(trigger=Pin.IRQ_RISING, handler=button_handler)
button3 = Pin(12, Pin.IN, Pin.PULL_UP)
button3.irq(trigger=Pin.IRQ_RISING, handler=button_handler)
button4 = Pin(13, Pin.IN, Pin.PULL_UP)
button4.irq(trigger=Pin.IRQ_RISING, handler=button_handler)

button_pressed = button1

#definição leds
ledButton1 = Pin(2, mode=Pin.OUT)
ledButton2 = Pin(18, mode=Pin.OUT)
ledButton3 = Pin(19, mode=Pin.OUT)
ledButton4 = Pin(21, mode=Pin.OUT)

ledButton1.off()
ledButton2.off()
ledButton3.off()
ledButton4.off()

#n = total leds / p = pino entrada fita led
n = 150
p = 4 
np = neopixel.NeoPixel(machine.Pin(p), n)


#botao1 - limpar
def clear():
  for i in range(n):
    np[i] = (0, 0, 0)
    np.write()
    
#botao2 - animação arco-iris
def sequencia_cores(pos):
  # Input a value 0 to 255 to get a color value.
  # The colours are a transition r - g - b - back to r.
  if pos < 0 or pos > 255:
    return (0, 0, 0)

  if pos < 85:
    return (255 - pos * 3, pos * 3, 0)

  if pos < 170:
    pos -= 85
    return (0, 255 - pos * 3, pos * 3)

  pos -= 170
  return (pos * 3, 0, 255 - pos * 3)

def funcao_arco_iris():
    for j in range(255):
        for i in range(n):
          indice = (i * 128 // n) + j
          np[i] = sequencia_cores(indice & 255)
          if button_pressed != button2:
              break
        np.write()
        if button_pressed != button2:
            break

#botao3 - animação desenho formas
def icones(tempo_espera):
    red = (255,0,0)
    white = (255,255,255)
    yellow = (255,255,0)
    blue = (0,128,192)
    green = (0,255,0)
    violet = (128,0,255)
       
    data1 = [red,red,red,red,red,red,red,red,red,red,
            red,white,white,white,white,white,white,white,white,red,
            red,white,white,white,white,white,white,white,white,red,
            red,white,white,white,white,white,white,white,white,red,
            red,white,white,white,white,white,white,white,white,red,
            red,white,white,white,white,white,white,white,white,red,
            red,white,white,white,white,white,white,white,white,red,
            red,white,white,white,white,white,white,white,white,red,
            red,white,white,white,white,white,white,white,white,red,
            red,white,white,white,white,white,white,white,white,red,
            red,white,white,white,white,white,white,white,white,red,
            red,white,white,white,white,white,white,white,white,red,
            red,white,white,white,white,white,white,white,white,red,
            red,white,white,white,white,white,white,white,white,red,
            red,red,red,red,red,red,red,red,red,red]
    
    data2 = [white,white,white,white,white,white,white,white,white,white,
            white,blue,blue,blue,blue,blue,blue,blue,blue,white,
            white,blue,white,white,white,white,white,white,blue,white,
            white,blue,white,white,white,white,white,white,blue,white,
            white,blue,white,white,white,white,white,white,blue,white,
            white,blue,white,white,white,white,white,white,blue,white,
            white,blue,white,white,white,white,white,white,blue,white,
            white,blue,white,white,white,white,white,white,blue,white,
            white,blue,white,white,white,white,white,white,blue,white,
            white,blue,white,white,white,white,white,white,blue,white,
            white,blue,white,white,white,white,white,white,blue,white,
            white,blue,white,white,white,white,white,white,blue,white,
            white,blue,white,white,white,white,white,white,blue,white,
            white,blue,blue,blue,blue,blue,blue,blue,blue,white,
            white,white,white,white,white,white,white,white,white,white]
    
    data3 = [white,white,white,white,white,white,white,white,white,white,
            white,white,white,white,white,white,white,white,white,white,
            white,white,yellow,yellow,yellow,yellow,yellow,yellow,white,white,
            white,white,yellow,white,white,white,white,yellow,white,white,
            white,white,yellow,white,white,white,white,yellow,white,white,
            white,white,yellow,white,white,white,white,yellow,white,white,
            white,white,yellow,white,white,white,white,yellow,white,white,
            white,white,yellow,white,white,white,white,yellow,white,white,
            white,white,yellow,white,white,white,white,yellow,white,white,
            white,white,yellow,white,white,white,white,yellow,white,white,
            white,white,yellow,white,white,white,white,yellow,white,white,
            white,white,yellow,white,white,white,white,yellow,white,white,
            white,white,yellow,yellow,yellow,yellow,yellow,yellow,white,white,
            white,white,white,white,white,white,white,white,white,white,
            white,white,white,white,white,white,white,white,white,white]
    
    data4 = [white,white,white,white,white,white,white,white,white,white,
            white,white,white,white,white,white,white,white,white,white,
            white,white,white,white,white,white,white,white,white,white,
            white,white,white,green,green,green,green,white,white,white,
            white,white,white,green,white,white,green,white,white,white,
            white,white,white,green,white,white,green,white,white,white,
            white,white,white,green,white,white,green,white,white,white,
            white,white,white,green,white,white,green,white,white,white,
            white,white,white,green,white,white,green,white,white,white,
            white,white,white,green,white,white,green,white,white,white,
            white,white,white,green,white,white,green,white,white,white,
            white,white,white,green,green,green,green,white,white,white,
            white,white,white,white,white,white,white,white,white,white,
            white,white,white,white,white,white,white,white,white,white,
            white,white,white,white,white,white,white,white,white,white]
    
    data5 = [white,white,white,white,white,white,white,white,white,white,
            white,white,white,white,white,white,white,white,white,white,
            white,white,white,white,white,white,white,white,white,white,
            white,white,white,white,white,white,white,white,white,white,
            white,white,white,white,violet,violet,white,white,white,white,
            white,white,white,white,violet,violet,white,white,white,white,
            white,white,white,white,violet,violet,white,white,white,white,
            white,white,white,white,violet,violet,white,white,white,white,
            white,white,white,white,violet,violet,white,white,white,white,
            white,white,white,white,violet,violet,white,white,white,white,
            white,white,white,white,violet,violet,white,white,white,white,
            white,white,white,white,white,white,white,white,white,white,
            white,white,white,white,white,white,white,white,white,white,
            white,white,white,white,white,white,white,white,white,white,
            white,white,white,white,white,white,white,white,white,white]
    
    data6 = [red,red,red,red,red,red,red,red,red,red,
            red,blue,blue,blue,blue,blue,blue,blue,blue,red,
            red,blue,yellow,yellow,yellow,yellow,yellow,yellow,blue,red,
            red,blue,yellow,green,green,green,green,yellow,blue,red,
            red,blue,yellow,green,violet,violet,green,yellow,blue,red,
            red,blue,yellow,green,violet,violet,green,yellow,blue,red,
            red,blue,yellow,green,violet,violet,green,yellow,blue,red,
            red,blue,yellow,green,violet,violet,green,yellow,blue,red,
            red,blue,yellow,green,violet,violet,green,yellow,blue,red,
            red,blue,yellow,green,violet,violet,green,yellow,blue,red,
            red,blue,yellow,green,violet,violet,green,yellow,blue,red,
            red,blue,yellow,green,green,green,green,yellow,blue,red,
            red,blue,yellow,yellow,yellow,yellow,yellow,yellow,blue,red,
            red,blue,blue,blue,blue,blue,blue,blue,blue,red,
            red,red,red,red,red,red,red,red,red,red]
       
    for i in range(len(data1)):
        np[i] = data1[i]
    np.write()
    time.sleep_ms(tempo_espera)
    
    for i in range(len(data2)):
        np[i] = data2[i]
    np.write()
    time.sleep_ms(tempo_espera)
    
    for i in range(len(data3)):
        np[i] = data3[i]
    np.write()
    time.sleep_ms(tempo_espera)
    
    for i in range(len(data4)):
        np[i] = data4[i]
    np.write()
    time.sleep_ms(tempo_espera)
    
    for i in range(len(data5)):
        np[i] = data5[i]
    np.write()
    time.sleep_ms(tempo_espera)
    
    for i in range(len(data6)):
        np[i] = data6[i]
    np.write()
    time.sleep_ms(tempo_espera)
    
#botao4 - animação pontos coloridos
def rand(i):
    return random.randint(0,i-1)

def animacao():
    np[rand(150)] = (rand(255),rand(255),rand(255))
    np.write()


while True:   
    if button_pressed == button1:
        ledButton1.on()
        ledButton2.off()
        ledButton3.off()
        ledButton4.off()
        clear()    
    elif button_pressed == button2:
        ledButton1.off()
        ledButton2.on()
        ledButton3.off()
        ledButton4.off()
        funcao_arco_iris()
    elif button_pressed == button3:
        ledButton1.off()
        ledButton2.off()
        ledButton3.on()
        ledButton4.off()
        icones(250)
    elif button_pressed == button4:
        ledButton1.off()
        ledButton2.off()
        ledButton3.off()
        ledButton4.on()
        animacao()
    



