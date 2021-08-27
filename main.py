from pessoaFisica import pessoaFisica
from pessoaJuridica import pessoaJuridica

if __name__ == '__main__':
	AquilesF = pessoaFisica("Aquiles",19,"TRAVAZAP","27988155743","11680633213")
	AquilesJ = pessoaJuridica("Aquiles",19,"TRAVAZAP","27988155743","43223344558373")

	print(AquilesF.getCpf)
	print(AquilesJ.getCnpj)
	