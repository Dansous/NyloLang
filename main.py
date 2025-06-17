from lexico import lexer          # Importa o analisador léxico (tokenizador)
from sintatico import Parser      # Importa o analisador sintático (parser)

if __name__ == "__main__":        # Executa o bloco principal apenas se o script for rodado diretamente
    with open("codigo.nylo", "r") as f:  # Abre o arquivo com o código em linguagem própria (.nylo)
        codigo = f.read()               # Lê todo o conteúdo do arquivo

    tokens = lexer(codigo)             # Executa o lexer para transformar o código em uma sequência de tokens
    parser = Parser(tokens)            # Cria uma instância do parser com os tokens gerados
    parser.parse()                     # Inicia a análise sintática do código (interpretação/validação da estrutura)
