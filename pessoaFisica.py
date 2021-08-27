from pessoa import pessoa

class pessoaFisica(pessoa):
	_cpf = ""
	def __init__(self,nome,idade,endereco,telefone,cpf):
		super().__init__(nome,idade,endereco,telefone)
		self._cpf = cpf
