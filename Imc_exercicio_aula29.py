nome = input("Informe seu nome \n")
altura = float(input("Informe sua altura \n"))
peso = float(input("Informe seu peso \n"))
imc = peso / (altura * altura)
print(nome,"tem:",altura)
print("Pesa:",peso,"e seu IMC é:",imc)