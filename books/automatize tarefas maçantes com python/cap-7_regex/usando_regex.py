"""
1. Importe o módulo de regex usando import re.
2. Crie um objeto Regex usando a função re.compile(). (Lembre-se de usar
uma string pura.)
3. Passe a string que você quer pesquisar ao método search() do objeto Regex.
Isso fará um objeto Match ser retornado.
4. Chame o método group() do objeto Match para retornar uma string com o
texto correspondente.

"""
import re

phone_number_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phone_number_regex.search('My number is 415-555-4242.')

print('\nPhone number found: ' + mo.group())

# ______________________________________________________________________


# Agrupando com parênteses

obj_regex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo = obj_regex.search('My number is (415)-555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print(type(mo.groups()))
area_code, main_number = mo.groups()
print(area_code)
print(main_number)

#______________________________________________

# Usando o pipe |

obj_regex = re.compile(r'Batman|Tina Fey')

mo1 = obj_regex.search('Batman and Tina Fey.')
print(mo1.group())

mo2 = obj_regex.search('Tina Fey and Batman.')
print(mo2.group())

bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')

mo = bat_regex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

bat_regex2 = re.compile(r'Bat(m(a|e)n|mobile|copter|bat)')

mo = bat_regex2.search('Batmen não é um herói')
print(mo.group())
print(mo.group(1))
print(mo.group(2))
print(type(mo.group()))

# ponto de interrogação: zero ou uma ocorrência

# __________________________________________________

bat_regex = re.compile(r'Bat(wo)?man')
mo1 = bat_regex.search('The Adventures of Batman')
print(mo1.group())

mo2 = bat_regex.search('The Adventures of Batwoman')
print(mo2.group())

phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phone_regex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phone_regex.search('My number is 555-4242')
print(mo2.group())
#_____________________________________________________
# uso do asterísticos - zero ou mais

bat_regex = re.compile(r'Bat(wo)*man')
mo = bat_regex.search('The Adventures of Batman')
mo1 = bat_regex.search('The Adventures of Batwoman')
mo2 = bat_regex.search('The Adventures of Batwowowowowoman')
print(mo.group())
print(mo1.group())
print(mo2.group())

# Correspondendo a uma ou mais ocorrências usando o sinal de adição

bat_regex = re.compile(r'Bat(wo)+man')
mo1 = bat_regex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = bat_regex.search('The Adventures of Batwowowowowoman')
print(mo2.group())

#__________________________________________________________
# Correspondendo a repetições específicas usando chaves

risada_regex = re.compile(r'(Ha){3}')

##########################################

names_regex = re.compile(r'Agent \w+')

print(names_regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob'))