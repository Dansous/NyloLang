import re

TOKEN_SPECIFICATION = [
    ('KEYWORD',    r'\b(mensagem|botao|fluxo|inicio|fim|ir_para)\b'),
    ('IDENT',      r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('STRING',     r'"([^"\\n]|\\.)*"'),
    ('NUMBER',     r'\d+'),
    ('COLON',      r':'),
    ('ARROW',      r'->'),
    ('NEWLINE',    r'\n'),
    ('COMMENT',    r'#.*'),
    ('WHITESPACE', r'[ \t]+'),
    ('MISMATCH',   r'.'),
]

def lexer(codigo):
    token_regex = '|'.join(f'(?P<{nome}>{regex})' for nome, regex in TOKEN_SPECIFICATION)
    linha = 1
    for match in re.finditer(token_regex, codigo):
        tipo = match.lastgroup
        valor = match.group()

        if tipo == 'NEWLINE':
            linha += 1
            continue
        elif tipo in ('WHITESPACE', 'COMMENT'):
            continue
        elif tipo == 'MISMATCH':
            raise RuntimeError(f"Linha {linha}: Caractere inv\u00e1lido {valor!r}")
        yield (tipo, valor, linha)
