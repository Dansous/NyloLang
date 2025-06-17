# Importa o analisador léxico e o analisador sintático dos módulos correspondentes
from lexico import lexer
from sintatico import Parser

# Função para testar o analisador léxico
def testar_lexer():
    print("Testando lexer...")  # Indica início do teste léxico
    codigo = 'mensagem: "Oi!"'  # Código de exemplo para teste
    tokens = list(lexer(codigo))  # Converte os tokens gerados em lista
    
    # Verifica se os tokens foram identificados corretamente
    assert tokens[0][0] == 'KEYWORD'  # Testa se primeiro token é uma palavra-chave
    assert tokens[1][0] == 'COLON'    # Testa se segundo token é dois pontos
    assert tokens[2][0] == 'STRING'   # Testa se terceiro token é uma string
    
    print("Lexer OK")  # Indica que o teste passou

# Função para testar o analisador sintático
def testar_parser():
    print("Testando parser...")  # Indica início do teste sintático
    codigo = '''                # Código mais complexo para teste
    inicio:
    mensagem:
        "Olá!"
        botao 1: "Ir" -> destino
    fim
    '''
    tokens = lexer(codigo)       # Gera tokens a partir do código
    parser = Parser(tokens)      # Cria instância do parser com os tokens
    parser.parse()               # Executa análise sintática
    print("Parser OK")          # Indica que o teste passou

# Ponto de entrada principal - executa os testes quando o script é rodado diretamente
if __name__ == "__main__":
    testar_lexer()  # Chama teste do analisador léxico
    testar_parser() # Chama teste do analisador sintático
