

import random

n = []
for i in range (1,5):
    n.append(input('ALUNO {}: '.format(i)))

print('O aluno escolhido foi {}, PARABÉNS!'.format(random.choice(n)))


