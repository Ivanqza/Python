countries = input().split(', ')
capitals = input().split(', ')

together = {country: capital for country, capital in zip(countries, capitals)}
print('\n'.join([f'{country} -> {capital}' for country, capital in together.items()]))