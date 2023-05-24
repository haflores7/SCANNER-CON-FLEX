import ply.lex as lex

# Definición de tokens
tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'ID',
)

# Expresiones regulares para los tokens
t_SELECT = r'(?i)select'
t_FROM = r'(?i)from'
t_WHERE = r'(?i)where'

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.value = t.value.split() 
    return t

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores
def t_error(t):
    print(f'Carácter no válido: {t.value[0]}')
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

# Ejemplo de ejecucion
data = '''
    Select name FroM table2 WHEre a2 
    
'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
