class Usuario:
    '''
        Atributo e Método de Classe
    '''
    
    # Atributo de classe
    cargo = 'usuário'
    
    def __init__(self, altura: str) -> None:
        self.altura = altura
        
    def altura_usuario(self) -> None:
        # Uma outra maneira de printar a classe sem iniciar o método no construtor
        print(self.altura)
        
    @classmethod # Método de Classe - faz com que o interpretador considere esse método um método da classe e não para a instância
    def cargo_usuario(cls) -> None:
        print(cls.cargo)
        
# Instância da classe        
usuario1 = Usuario(altura='1.90')
usuario1.cargo_usuario()

# Tem acesso aos atributos da classe, mas não aos atributos da instância
Usuario.cargo_usuario()