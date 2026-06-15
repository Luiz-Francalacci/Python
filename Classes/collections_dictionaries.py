paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'jp': 'Japão'}
print(paises)

paises2 = dict(br='Brasil', eua='Estados Unidos', jp="Japão")
print(paises2)

print(paises['br'])

print(paises.get('eua'))

paises['arg'] = "Argentina"
print(paises)

del paises['eua']
print(paises)
