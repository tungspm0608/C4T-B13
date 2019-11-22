a = {'name' : 'HUY',
    'role' : 'waiter',
    'hour' : 12,
    'salary per hours($)' : 0.8}                        
b = {'name' : 'TUNG',
    'role' : 'cook',
    'hour' : 24,
    'salary per hours($)' : 1.5}                                        
c = {'name' : 'MDUC',
    'role' : 'manager',
    'hour' : 20,
    'salary per hours($)' : 2}
luongthang = {
    'luong thang HUY' : 0.8*12,
    'luong thang TUNG' : 1.5*12,
    'luong thang MDUC' : 2*12
}
for i in enumerate(luongthang):
    print(i)