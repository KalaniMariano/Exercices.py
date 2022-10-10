'''Create a tuple filled with the top 20 in the Brazilian 
Football Championship Table, in the order of placement. 
Then show:
A) Only the top 5 finishers.
B) The last 4 placed.
C) A list of teams in alphabetical order.
D) In ​​what position in the table is the Santos team.'''
championship_table = ('Palmeiras','Internacional','Corinthians','Flamengo','Fluminense','Athletico-PR','Atlético Mineiro','América-MG','Botafogo','Fortaleza','São Paulo','Bragantino','Goiás','Santos','Coritiba','Ceará','Cuiabá','Atlético Goianiense','Avaí','Juventude')
for table in range (0,20):
    print (f'{table+1}. {championship_table[table]}')
print('Top 5:')
for first in range (0,5):
    print (f'{first+1}. {championship_table[first]}')
print ('=-='*20)
print('Last 4: ')
for last in range (16,20):
    print (f'{last+1}. {championship_table[last]}')
print ('=-='*20)
sort = sorted(championship_table)
print ('In alphabetic order: ')
for alphabetical in range (0,20):
    print(f'{alphabetical+1}. {sort[alphabetical]}')
print ('=-='*20)
santos = championship_table.index('Santos')
print (f'The Santos team is in position {santos+1}')