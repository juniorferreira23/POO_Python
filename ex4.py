class Usuario:
    '''
        Herança e método especial super()
    '''
    
    def __init__(self, nome, cpf) -> None:
        self.nome = nome
        self.cpf = cpf
    
    def exibe_cpf(self):
        return self.cpf

# Passar paramêtro na classe é a forma de indicar herança
class Secretaria(Usuario):
    
    def __init__(self, id_secretaria, nome, cpf) -> None:
        # Uso do método super para receber o construtuor do método pai e seus atributos escolhidos
        super().__init__(nome, cpf)
        self.id_secretaria = id_secretaria
    
class Vendedor(Usuario):
    
    def __init__(self, id_vendedor, nome, cpf) -> None:
        super().__init__(nome, cpf)
        self.id_vendedor = id_vendedor
        
    def exibi_id_vendedor(self):
        print(self.id_vendedor)
    
s1 = Secretaria('2', 'Maria', '1234325345')
print(s1.exibe_cpf())
v1 = Vendedor('1', 'João', '3259235432')
print(v1.exibe_cpf())
v1.exibi_id_vendedor()

    

    