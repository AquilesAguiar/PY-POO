class pessoa():
	_nome = ""
	_idade = 0
	_endereco = ""
	_telefone = ""

	def __init__(self,nome,idade,endereco,telefone):
		self._nome = nome
		self._idade = idade
		self._endereco = endereco
		self._telefone = telefone