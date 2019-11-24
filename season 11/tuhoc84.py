import random
adventure = {
    'name' : 'light',  
    'age' : 17,
    'strength' : 8,
    'defense' : 10,
    'HP' : 100,
    'backpack' : ['shield','bread loaf'],
    'gold' : 100,
    'level' : 2
}
adventure['gold'] + 50
adventure['backpack'].append('flight stone')
adventure['pocket'] = ['monstersdex','flashlight']
skill = {
    'skill1' : {
        'name' : 'tackle',        
        'minimum level' : 1,
        'damage' : 5,
        'hit rate' : 0.3        
    },
    'skill2' : {
        'name' : 'qick attack',        
        'minimum level' : 2,
        'damage' : 3,
        'hit rate' : 0.5        
    },
    'skill3' : {
        'name' : 'strong kick',        
        'minimum level' : 4,
        'damage' : 9,
        'hit rate' : 0.2        
    }
}
for i,a in enumerate(skill):
    print(i+1,skill[a])
c = random.randint(0,1)    
b = input('ban muon dung skill nao: ')
if int(b) == 1  and adventure['level'] > skill['skill1']['minimum level']:
    if c > skill['skill1']['hit rate']:
        print('shot!!','sat thuong ban gay ra la:',skill['skill1']['damage']) 
    else:
        print('skill cua ban da truot')     
if int(b) == 2  and adventure['level'] > skill['skill2']['minimum level']:
    if c > skill['skill2']['hit rate']:
        print('shot!!','sat thuong ban gay ra la:',skill['skill2']['damage']) 
    else:
        print('skill cua ban da truot')
if int(b) == 3 and adventure['level'] > skill['skill3']['minimum level']:
    if c > skill['skill3']['hit rate']:
        print('shot!!','sat thuong ban gay ra la:',skill['skill3']['damage']) 
    else:
        print('skill cua ban da truot')
else:
    pass
