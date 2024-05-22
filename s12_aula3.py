# calculadora_de_frete-
#feito por : david
valor = float(input('qual o valor do pedido'))
fidelidade = str(input('voce é membro?(s/n)'))
taxa = 0

if valor < 10:
    taxa +=5
if valor >=10 and valor <20:
    taxa += 3
if valor>=20:
    taxa = 0
elif fidelidade =='s':
    taxa = taxa - 2

print('revisao do pedido:\nvalor do pedido:R$',valor,'\ntaxa de entrega:',taxa,'\nvalor total:R$',taxa + valor)
