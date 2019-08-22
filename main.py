import requests

print('######################')
print('#### CONSULTA CEP ####')
print('######################')
print()

cep_input = input('Digite o CEP para a consulta: ')

if len(cep_input) != 8:
	print('Quantidade de dígitos inválida!')
	exit()

request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

address_data = request.json()

if 'erro' not in address_data:
	print(request.json())
else:
	print('{}: CEP Inválido.'.format(cep_input))
	