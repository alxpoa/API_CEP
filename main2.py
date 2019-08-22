import requests

print('######################')
print('#### CONSULTA CEP ####')
print('### Apenas números ###)')
print('######################')
print()

cep_input = input('Digite o CEP para a consulta: ')

if len(cep_input) != 8:
	print('Quantidade de dígitos inválida!')
	exit()

request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

address_data = request.json()

if 'erro' not in address_data:
	print('==> CEP LOCALIZADO! <==')

	print('CEP: {}'.format(address_data['cep']))
	print('Logradouro: {}'.format(address_data['logradouro']))
	print('Complemento: {}'.format(address_data['complemento']))
	print('Bairro: {}'.format(address_data['bairro']))
	print('Cidade: {}'.format(address_data['localidade']))
	print('Estado: {}'.format(address_data['uf']))

else:
	print('{}: CEP Inválido.'.format(cep_input))
