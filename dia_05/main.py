import secrets
from string import ascii_letters, digits

simbolos = '!#$%&()*+><^~@-_çÇ`/|ªº¿'
alfabeto = ascii_letters + digits + simbolos
tamanho_senha = 16
while True:
    password = ''.join(secrets.choice(alfabeto) for _ in range(tamanho_senha))
    if (any(c.islower() for c in password) # tem alguma letra minúscula
            and any(c.isupper() for c in password) # tem alguma letra maiúscula
            and any(c in simbolos for c in password) # tem algum símbolo
            and sum(c.isdigit() for c in password) >= 3): # tem pelo menos 3 dígitos
        break 

print("Gerador de Senhas Aleatório")
print(f"Senha gerada:  {password}") 
    