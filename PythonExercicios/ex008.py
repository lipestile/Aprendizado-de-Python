metro = float(input('Digite um valor em metros: '))
print('A medida de {}m corresponde a \n{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'
      .format(metro,
    metro/1000,
    metro/100,
    metro/10,
    metro*10,
    metro*100,
    metro*1000))