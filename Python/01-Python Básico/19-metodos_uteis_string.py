# string -> str
# existe varios métodos utilizáveis

curso = 'pYThoN'

# ----------------maiúscula, minúscula e titulo------------------------

# upper converte tudo para maiúsculo
print (curso.upper())
# PYTHON

# lower converte tudo para minúsculo
print (curso.lower())
# python

# title converte tudo para minúsculo exceto a primeira letra
print (curso.title())
# Python

# ------------------Eliminando espaços em branco------------------------

curso1 = "      Olá mundo!   "
# strip remove espaços em branco lado esquerdo e direito
print (curso1.strip()+ ".")
# "Olá mundo!."

# lstrip remove espaços em branco lado esquerdo 
print (curso1.lstrip()+ ".")
# "Olá mundo!   ."

# rstrip remove espaços em branco lado direito
print (curso1.rstrip()+ ".")
# "      Olá mundo!."

#--------------------- junção e centralização----------------------------
palavra = 'Javascript'
# center centraliza texto 
print (palavra.center(14,'#'))  #string ira ocupar 14 espaços, usado para fazer um menu bonito
# "##Javascript##"

# join junta ou uni texto 
print ("-".join(palavra))  #string ira juntar com traço a cada palavra
# "J-a-v-a-s-c-r-i-p-t"