pt1 = input('ban muon nhap day so la:')
numbers = pt1.split(' ')
print(sum([int(i) for i in numbers if type(i)== int or i.isdigit()]))