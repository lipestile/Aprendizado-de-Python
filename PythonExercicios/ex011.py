largura = float(input('Largura da Parede: '))
altura = float(input('Altura da Parede: '))
area = largura * altura
tinta = area / 2

print('Sua parede tem a dimensão de {} x {} e sua área é de {:.3}m²'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
