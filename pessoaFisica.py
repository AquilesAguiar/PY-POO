from pessoa import pessoa

class pessoaFisica(pessoa):
	__cpf = ""
	def __init__(self,nome,idade,endereco,telefone,cpf):
		super().__init__(nome,idade,endereco,telefone)
		self.__cpf = cpf
	
	def getCpf(self):
		return self.__cpf
