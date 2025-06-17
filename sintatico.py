from lexico import lexer  # Importa o lexer para gerar os tokens

class Parser:
    def __init__(self, tokens):
        self.tokens = list(tokens)  # Converte o gerador de tokens para uma lista
        self.pos = 0                # Posição atual na lista de tokens

    def match(self, expected_type):
        # Verifica se o token atual é do tipo esperado e avança se for
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == expected_type:
            self.pos += 1
            return True
        return False

    def expect(self, expected_type):
        # Verifica se o próximo token é do tipo esperado, senão lança erro
        if not self.match(expected_type):
            atual = self.tokens[self.pos] if self.pos < len(self.tokens) else ('EOF', '', -1)
            raise SyntaxError(f"Linha {atual[2]}: Esperado {expected_type}, mas encontrou {atual[0]} ({atual[1]!r})")

    def parse(self):
        # Método principal para iniciar a análise do código
        while self.pos < len(self.tokens):
            tipo, valor, _ = self.tokens[self.pos]
            if tipo == 'KEYWORD' and valor == 'inicio':
                self.parse_inicio()       # Analisa o bloco 'inicio:'
            elif tipo == 'KEYWORD' and valor == 'mensagem':
                self.parse_mensagem()     # Analisa o bloco 'mensagem:'
            elif tipo == 'KEYWORD' and valor == 'fluxo':
                self.parse_fluxo()        # Analisa o bloco 'fluxo <nome>:'
            elif tipo == 'KEYWORD' and valor == 'fim':
                print("Fim do fluxo.")    # Finaliza o fluxo
                self.pos += 1
            else:
                print(f"Ignorando token inesperado: {tipo}, {valor}")  # Ignora tokens fora de contexto
                self.pos += 1

    def parse_inicio(self):
        """Analisa o bloco 'inicio:'"""
        print("Iniciando fluxo principal")
        self.expect('KEYWORD')  # Espera a palavra-chave 'inicio'
        self.expect('COLON')    # Espera os dois-pontos após 'inicio'

    def parse_mensagem(self):
        """Analisa bloco de mensagem e seus botões"""
        print("Detectado bloco de mensagem")
        self.expect('KEYWORD')  # Espera a palavra-chave 'mensagem'
        self.expect('COLON')    # Espera os dois-pontos após 'mensagem'
        if self.match('STRING'):  # Opcional: se houver string da mensagem, reconhece
            print("→ Texto da mensagem detectado.")
        # Continua analisando botões, se houver
        while self.pos < len(self.tokens):
            tipo, valor, _ = self.tokens[self.pos]
            if tipo == 'KEYWORD' and valor == 'botao':
                self.parse_botao()  # Analisa cada botão dentro do bloco de mensagem
            else:
                break  # Sai do loop se não houver mais botões

    def parse_botao(self):
        """Analisa um botão: botao NUM: "texto" -> identificador"""
        print("→ Botão detectado")
        self.expect('KEYWORD')  # 'botao'
        self.expect('NUMBER')   # número do botão
        self.expect('COLON')    # dois-pontos após o número
        self.expect('STRING')   # texto do botão
        self.expect('ARROW')    # seta (->) indicando o destino
        self.expect('IDENT')    # nome do fluxo de destino

    def parse_fluxo(self):
        """Analisa a definição de um fluxo nomeado"""
        print("Iniciando novo fluxo")
        self.expect('KEYWORD')  # 'fluxo'
        self.expect('IDENT')    # nome do fluxo
        self.expect('COLON')    # dois-pontos após o nome
