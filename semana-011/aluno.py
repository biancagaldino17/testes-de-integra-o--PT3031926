class AlunoClass:

    def __init__(self, nome, sobrenome, nota):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nota = nota

    def mostrarAluno(self):
        return (
            'Aluno: '
            + self.nome
            + ' '
            + self.sobrenome
            + ' - Nota: '
            + str(self.nota)
        )

    def salvar(self, conexao, colecao):
        # Converte os atributos da instância do Aluno em dicionário
        mydict = self.__dict__
        # Insere na coleção MongoDB simulada via conexao[colecao]
        x = conexao[colecao].insert_one(mydict)
        # Retorna o status de confirmação da inserção (boolean)
        return x.acknowledged