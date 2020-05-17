question = ['name','quest','favorite color']
answer = ['lancelot','the holy grail','blue']
for q,a in zip(question,answer):
    print('What is your {0}? It is {1}.'.format(q,a))


for i,v in enumerate(['tic','tac','toe']):
    print(i,v)


knights = {'gallahad':'the pure','robin':'the brave'}
for k,v in knights.items():
    print(k,v)

print {x: x**2 for x in (2,4,6)}


basket = {'apple','orange','apple','orange','banana'}
print(basket)
