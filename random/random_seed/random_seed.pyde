""" 
Use random_seed() para fixar o gerador de números
aleatórios tando do Processing como do Python
retorna uma nova seed se chamado sem argumentos
"""

def setup():
    size(500, 500)
    random_seed(1)
    noLoop()
    
def draw():
    background(240, 250, 250)
    for _ in range(10):
        print(random_seed())
    
def random_seed(s=None):
    """
    Set a seed to both Processing and Python random number generators
    Set and return a random random seed if called without arguments
    """
    from random import seed    
    if s is None:
        s = int(random(100000))
    randomSeed(s) # Processing random seed setup
    seed(s) # Python random seed setup
    return "seed: {}".format(s)
