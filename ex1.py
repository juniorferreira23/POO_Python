class Usuario:
    '''
        Exemplificando Orientação a objeto 
        Construtor e Métodos de instância
    '''
    # Construtor - Abaixo temos o construtor que inicia aos atributos declarados e métodos
    def __init__(self, nome: str, idade: str) -> None:
        self.nome = nome
        self.idade = idade
        self.nome_usuario()
        self.idade_usuario()
    
    # Método - Métodos da classe
    def nome_usuario(self) -> None:
        print(self.nome)
        
    def idade_usuario(self) -> None:
        print(self.idade)
        

usuario1 = Usuario('junior', '25')
usuario2 = Usuario('elizeu', '24')
        
        
        
