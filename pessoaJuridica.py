from pessoa import pessoa

class pessoaJuridica(pessoa):
	__cnpj = ""
	
	def __init__(self,nome,idade,endereco,telefone,cnpj):
		super().__init__(nome,idade,endereco,telefone)
		self.__cnpj = cnpj

	def getCnpj(self):
		return self.__cnpj