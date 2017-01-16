'''
 Exemplo de animação 
 inspirado em conversa com o Regis "Grupy-SP" da Silva
'''

d, x, y = 5, 5, 5

def setup():
    ''' como o setup() do Arduino! Roda só no início'''

    size(600, 200)
    # frameRate(24) # opcional
    # noStroke()  # sem borda mata as linhas!!!
    stroke(255) # bordas/linhas brancas

def draw():    
    ''' equivalente ao loop() do Arduino é um loop infinito principal '''

    global x, y, d # pra poder alterar a posição e diâmetro do círculo
    background(0) # fundo preto (e limpa o frama da animação)
    # draw lines
    line(45, 100, 555, 100)
    for i in range(50,551,250):
        line(i,80,i,120)
    for i in range(50,610,50):
        line(i,90,i,110)
    # draw circle
    ellipse(x, y, d, d)
    # animate circle
    d = d + 1
    x += 1
    y += 0.6


