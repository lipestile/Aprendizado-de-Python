n1 = float(input("Primeira nota do aluno: "))
n2 = float(input("Segunda nota do aluno: "))
media = (n1 + n2)/2
print('A media aritimética de {} e {} corresponde a {:.1f}'.format(n1, n2, media))
## outra forma
print('A média aritimética de {} e {} corresponde a {:.1f}'.format(n1, n2, (n1+n2)/2))