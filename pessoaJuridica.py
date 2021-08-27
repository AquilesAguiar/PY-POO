from pessoa import pessoa

class pessoaJuridica(pessoa):
	_cnpj = ""
	
	def __init__(self,nome,idade,endereco,telefone,cnpj):
		super().__init__(nome,idade,endereco,telefone)
		self._cnpj = cnpj