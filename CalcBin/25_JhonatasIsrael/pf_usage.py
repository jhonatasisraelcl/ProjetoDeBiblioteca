import pf_interpreter as pf

print('Impressão de toda a faixa representável:')
print('')
for i in range(255,127,-1): pf.interpreter(i)
for i in range(0,127,1): pf.interpreter(i)

print('')
print('Para importar a função use:')
print('		import pf_interpreter as pf')
print('')

import pf_interpreter as pf

print('Para avaliar apenas uma combinação use:')
print('		pf.interpreter(0b10110111)')
pf.interpreter(0b10110111)
print('')
print('ou')
print('		pf.interpreter(0xB7)')
pf.interpreter(0xB7)
print('')
print('ou')
print('		pf.interpreter(183)')
pf.interpreter(183)
print('')
