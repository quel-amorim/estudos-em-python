from random import randint
roleta = randint(1 , 10)
print('Tabuada do número {}'.format(roleta))
for x in range(11):
    print(f' {roleta} x {x} = {roleta*x}')

print('-'*20)