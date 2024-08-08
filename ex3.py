class Usuario:
    '''
        Método estático
    '''
    
    cargo = 'usuário'
    
    def __init__(self, idade: int) -> None:
        self.idade = idade
        
    def idade_usuario(self) -> None:
        return self.idade
    
    # Método Estático - essa configuração faz com que o método não seja nem de instância nem de classe, mas apenas está dentro da classe. Esse método não pode utilizar nem self e nem cls. Usado com o objetivo de ser um método auxiliar para informações 
    @staticmethod
    def e_adulto(idade) -> None:
        if type(idade) == int:
            if idade >= 18:
                print('Usuário maior de idade')
            elif idade >= 0:
                print('Usuário menor de idade')
            else:
                print('Erro na leitura da informação')
        else:
            print('Erro: tipo do dado')
            print('A função aceita apenas números inteiros')
            print(f'A idade informada -> ({idade}) não é um número inteiro, seu tipo é {type(idade)}')
        
          
usuario1 = Usuario(16)

Usuario.e_adulto(usuario1.idade_usuario())
