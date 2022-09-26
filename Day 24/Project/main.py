name = r'Day 24\Project\Input\Names\invited_names.txt'
text = r'Day 24\Project\Input\Letters\starting_letter.txt'

with open(text, 'r') as start:
    begin = start.read()
print(begin)

with open(name, 'r') as names:
    lines = names.readlines()
print(lines)

lines=[i.replace('\n','') for i in lines]
    
print(lines)

for i in lines:
    with open(f'Day 24\Project\Output\ReadyToSend\card_{i}.txt','w') as letters:
        letters.write(begin.replace('[name]',i) )

        

