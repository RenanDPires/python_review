text = input('Anything\n')
VOWELS = 'AEIOU'


# For Loop
for letter in text:
    if letter.upper() in VOWELS:
        print(letter,': is a vowel',sep=' ', end='\n')
    else:
        print('Not a vowel')

for num in range(0,4,2): #(start, end+1, steps)
    print(num)

# For Loop and Continue usage
for num in range(0,100,3):
    if num % 2 == 0:
        continue # Used to skip this iteration
    print (num, end='\n')

# While Loop and Break usage
while True:
    opcao = (int(input('[1] -> SACAR\n[2] -> EXTRATO\n[3] -> SAIR\n')))
    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Imprimindo extrato...')
    elif opcao == 3:
        print('Saindo...')
        break # Used to break WHILE LOOP
    else: 
        print('Digite uma das três opções informadas\n')


