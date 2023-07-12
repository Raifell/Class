count = []

with open('text.txt', 'r') as file:
    string = file.readlines()

result = '|'.join(string).replace('\n', '')
over = result.split('|')
over = over[::-1]

with open('result_text.txt', 'w') as file:
    for x in over:
        file.write(x + '\n')

print(over)
