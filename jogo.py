import random
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print("🪽 jogo de adivinhação   🪽") 
print("🪽  Bianca               🪽")
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&")

numeroSecreto= random.randrange(0,100)
totalTentativas = 0 
pontos = 100

print(" Qual níveis de dificuldade! ")
print("(1)- Facíl (2)- Médio (3)- Difícil ")

nivel = int(input("Escolha um nível"))

if nivel == 1:
    print("20 tentativas? ")
    totalTentativas = 20
elif nivel == 2:
    print("10 tentativas")
    totalTentativas = 10
elif nivel == 3:
    print("5 tentativas")
    totalTentativas = 5        


