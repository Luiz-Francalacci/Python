idade = 19

if idade < 18:
    print("Você é menor de idade")
elif idade == 18:
    print("Você tem 18 anos")
else:
    print("Você é maior de 18")

if idade > 18 and idade < 65:
    print("Você é um adulto")
elif not idade > 10:
    print("Você é uma criança")