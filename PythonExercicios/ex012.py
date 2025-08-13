preco = float(input('Digite o valor do produto: R$'))
desconto = (preco / 100)*5
print('O produto que custava {}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, preco-desconto))