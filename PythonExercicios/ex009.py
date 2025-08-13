titulo = 'Tabuada'
n = float(input('Digite um número para ver sua tabuada: '))
print('{:=^20}'
      '\n{:.0f} x 1 = {:^20}'
      '\n{:.0f} x 2 = {:^20}'
      '\n{:.0f} x 3 = {:^20}'
      '\n{:.0f} x 4 = {:^20}'
      '\n{:.0f} x 5 = {:^20}'
      '\n{:.0f} x 6 = {:^20}'
      '\n{:.0f} x 7 = {:^20}'
      '\n{:.0f} x 8 = {:^20}'
      '\n{:.0f} x 9 = {:^20}'
      '\n{:.0f} x 10 ={:^20}'
      '\n{:=^20}'
      .format(titulo,n,
              n*1,n,
              n*2,n,
              n*3,n,
              n*4,n,
              n*5,n,
              n*6,n,
              n*7,n,
              n*8,n,
              n*9,n,
              n*10,
              'Final'))
