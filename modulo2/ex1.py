class Escola:
    def __init__(self, nome, cnpj):
        self.__nome =nome
        self.__cnpj = cnpj

    def Puxardados(self):
        print(f'Puxando dados...\n')
        print(f'O nome da Escola é {self.__nome} e seu cnpj é {self.__cnpj}')

class Pessoa:
    def __init__(self, nome:str, idade:int,):
        self.__nome = nome
        self.__idade = idade
   
    def get_nome(self):
        print('pegando nome')
        return self.__nome
    
    def set_nome(self, novo_nome:str):
        if isinstance(novo_nome, str) and novo_nome:
            self._nome = novo_nome
        else: 
            print('Erro! O novo nome deve ser uma string não vazia')
  
    def get_idade(self):
        print('pegando idade')
        return self.__idade
    
    
    def set_idade(self, nova_idade:int):
        if isinstance(nova_idade, str) and nova_idade:
            self._idade= nova_idade
        else: 
            print('Erro! O nova idade deve ser um inteiro não vazia')

class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade, matricula)
        self.matricula = matricula

    
    
a1 = Estudante('isis', '20', '1356879') 
dicionario_pessoa:dict[str, list[Pessoa]] = {'nome':[], 'idade':[], 'matricula':[]}
dicionario_pessoa["estudandes"].append(a1)


for estudante in dicionario_pessoa.values():
    for Pessoa in Estudante:
        Pessoa.exibir()
    
    