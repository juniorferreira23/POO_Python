Estudos do paradigma de programação orientado a objeto

Conceito: 
    Abstrair objetos do mundo real transformando-o em uma classe na códificação, buscando trazer as características conhecidas como atributos e suas ações conhecidas como métodos.

Caracteristicas:
    -Encapsulamento: Garantir a segurança da sua classe blindando-a para uso de acordo com a permissão. No python o encapsulamento é representado com o underline(_) antes do atributo

    -Herança: Classes pais podem herdar seus métodos para classes filhas. Na códificação é representado pelo chamado do método super()

    -Polimorfismo: 
        -Overwrite ou Sobreescrita: Sobre escreve os métodos os adaptando nas classes filhas
        -Overload ou Sobrecarga: Utilizar e rescrever apenas o payload ou carga do método herdado

Contrutor:
    É um método especial que recebe as configurações para a inicialização de uma estância da classe qual ela for iniciada.

    Geralmente em algumas linguagens o construtor possui o mesmo nome da classe, no Python temos como "def __init__(self, params):".
    Ps: os params, representa os paramêtros que pode receber para sua iniciação.

Atributos:
    Como mencionado anteriormente os atributos podem ser declarados antes do contrutor sendo uma variavel, podendo ser pública ou privada como informado no encapsulamento.

Métodos:
    São funções dentro das classes no qual recebem 'self' para terem um contexto e referênciarem a própria instância da classe.

    -Método de Classe: faz com que o interpretador considere esse método um método da classe e não para a instância. 
    Para usar basta colocar '@classmethod ' acima do método

    -Método Estático: Essa configuração faz com que o método não seja nem de instância nem de classe, mas apenas está dentro da classe. Esse método não pode utilizar nem self e nem cls. Usado com o objetivo de ser um método auxiliar para informações.
    Para usar basta colocar '@staticmethod' acima do método