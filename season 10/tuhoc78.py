tenphim = {
    'ba chang ngoc' : 'phat hanh nam 1973 tai An Do',
    'dien vien' : ['rancho','farham']
}
tenphim['dia chi'] = 'chua xac dinh'
for i,a in enumerate(tenphim):
    print(i+1,a,tenphim[a],sep = '-')
tenphim['dien vien'] = ['rancho','farham','dao dien']
tenphim['dien vien'].append('quay phim')
tenphim['dien vien'].pop(0)
print(tenphim['dien vien'][1])
for b,c in enumerate(tenphim['dien vien']):
    print(b+1,c)
for d,e in enumerate(tenphim):
    print(d+1,e,tenphim[e])    

