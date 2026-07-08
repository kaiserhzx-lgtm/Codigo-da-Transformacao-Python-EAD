## --- Desafio Extra: Programa com Hora Atual ---

# Importamos a ferramenta de tempo do Python
from datetime import datetime

# Perguntamos o nome do usuário
nome = input("Por favor, digite o seu nome: ")

# Pegamos o horário do sistema e formatamos em Hora:Minuto:Segundo
hora_atual = datetime.now().strftime("%H:%M:%S")

# Exibimos a saudação e a hora atual
print("Oi, " + nome + "!")
print("Agora são exatamente: " + hora_atual)