Peso = float (input('Digite seu peso em kg: '))
Altura = float (input('Digite sua altura em metros: '))
Idade = int (input('Digite sua idade: '))

imc = Peso / (Altura ** 2)
imc_arredondado = round(imc, 2)

f_string = f'Voce tem {Idade} anos, e seu IMC é de {imc_arredondado}'

print(f_string)
