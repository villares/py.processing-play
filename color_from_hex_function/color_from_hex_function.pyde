
def setup():
    gr = color_hex('#00FF00')
    fill(gr)
    rect(0, 0, 50, 100)
    bl = color_hex('0000FF')
    fill(bl)
    rect(50, 0, 50, 100)
    
def color_hex(s):
    """
    No Processing tradicional (Java) podemos indicar cores com a notação hexadecimal  #AABBCC
    No modo Python é possivel usar essa notação entre aspas em fill(), stroke() e
    background(), mas não é possível fazer isso com a função color().
    Esta função permite usar cores a partir de um string com a notação hexa no modo Python
    """
    if s.startswith('#'):
        s = s[1:]
    return color(int(s[:2], 16), int(s[2:4], 16), int(s[4:6], 16))
