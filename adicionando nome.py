from random import random
from secrets import choice
from tkinter import N

print('########## adiconar nome na lista v.1 ###########\n')

minha_dic = {'joao', 'mateus', 'marcos'}


minha_dic.add(input('-adicionar nome: '))
    
    
print('\nnomes na lista:\n')

for todos in minha_dic:
    print(todos)

print('total de:', len(minha_dic),'pessoas')

if input('\n-achar nome: ') in minha_dic:
    print('\n#R:esta na lista\n')
else:
    print('\n# nao esta na lista #\n')

