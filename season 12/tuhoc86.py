from random import randint
man = 1
caichiakhoa = 0
vuotqua = 'ko the vuot ra pham vi ngoai map'
nhapnhanvat = input('ban muon nhan vat co ki hieu la gi? ')
nhanvat = {'ten': 'thuy kieu','balo' : {'thuốc tăng công': 'số lượng :1,dùng sẽ tăng 5 atk trong 1 lần đánh','thuốc tăng thủ' : 'số lượng: 1,dùng sẽ miễn nhiễm với 1 đòn tấn công '},'hp': 100,'atk': 20}
quaithu1 = {'ten': 'ga','hp' : 10,'atk' :5}
quaithu2 = {'ten' : 'cho','hp' : 15,'atk':10}
quaithu3 = {'ten' : 'lon','hp' : 20,'atk':5}
kichcomap = 10
if len(nhapnhanvat) > 1:
    print('neu nhan vat co nhieu ki tu se kho choi') 
else:
    print('luat choi : ban se nhap vai la mot nhan vat ten la: thuy kieu,W là kí hiệu bức tường,K là kí hiệu chìa khóa,D là kí hiệu cửa qua màn,M là kí hiệu quái vật ,X là sau khi bạn đã hoàn thành 1 việc gì đó')   
    print('Cốt truyện : Thúy Kiều - một người thiếu nữ tài sắc vẹn toàn, con gái đầu lòng trong gia đình trung lưu lương thiện, sống trong cảnh êm đềm chướng rủ màn che, bên cạnh cha mẹ và hai em là Thúy Vân và Vương Quan.')  
    print('Trong buổi du xuân, Thúy Kiều đã gặp gỡ Kim Trọng, giữa hai người đã chớm nở mối tình đẹp. Kim Trọng đến ở trọ cạnh nhà của Thúy Kiều, nhân việc trả chiếc thoa rơi, Kim Trọng đi gặp Kiều bày tỏ tâm tình, hai người đã chủ độn, tự do đính ước với nhau. Trong khi Kim Trọng về quê chịu tang cú, gia đình Kiều đã bị mắc oan, Kiều nhờ Vân trả nghĩa cho Kim Trọng, còn nàng thì bán mình chuộc cha. Thúy Kiều bị bọn buôn người là Mã Giám Sinh, Tú Bà, Sở Khanh lừa gạt, đẩy vào lầu xanh.')
    print('Sau đó nàng được Thúc Sinh, một khách làng chơi hào phóng cứu vớt khỏi cuộc đời kĩ nữ. Nhưng rồi Kiều bị vợ cả của Thúc Sinh là Hoạn Thư ghen tuông, đày đọa. Sau đó Kiều gặp Từ Hải, một người anh hùng đầu đội trời, chân đạp đất. Từ Hải lấy Kiều và giúp nàng báo ân báo oán. Do mắc lừa Hồ Tôn Hiến, Từ Hải bị giết, Thúy Kiều phải hầu đàn, hầu rượu Hồ Tôn Hiến rồi bị ép gả cho viên thổ quan. Đau đớn, tủi nhục Kiều đã trẫm mình xuống sông Tiền Đường. Nhưng nàng được sư Giác Duyên cứu lần thứ hai và sống nương nhờ cửa Phật.')
    print('. Sau nửa năm chịu tang chú ở Liêu Dương, Kim Trọng trở lại tìm Kiều. Hay tin gia đình Kiều bị tai biến và nàng phải bán mình chuộc cha, chàng đau đớn vô cùng. Tuy kết duyên với Thúy Vân nhưng Kim Trọng chẳng thể nào nguôi được nỗi nhớ Thúy Kiều. ')
    print('trong khi đó Kiều ngày ngày làm công cho nhà Phật , sau đó tình cờ Kiều nghe được là sư Giác Duyên là một tú bà được đưa ngầm vào nhà chùa để ăn miễn phí và tìm gái . Kiều nhanh trí đã bỏ trốn khỏi chùa , nàng lặn lội trong rừng sâu sau đó nàng gặp một lỗ đen siêu to,nó đã hút nàng vào một trò chơi . Đó chính là game này ...')
    print('CHÚNG TA HÃY CÙNG BẮT ĐẦU GAME :')
    loira = [0,0]
    toadonhanvat = [0,1]
    toadoquaithu1 = {'toa do quai thu':[2,randint(1,9)],'dau hieu quai thu':'M'}
    toadoquaithu2 = {'toa do quai thu':[4,randint(1,9)],'dau hieu quai thu':'M'}
    toadoquaithu3 = {'toa do quai thu':[6,randint(1,9)],'dau hieu quai thu':'M'}
    ngaunhien = randint(0,1)
    chiakhoa = {'toa do chia khoa' : [4,4],'dau hieu chia khoa' : 'K'}
    buctuong = {'toa do buc tuong' : [1,1],'dau hieu buc tuong' : 'W'}
    chiakhoa1 = {'toa do chia khoa' : [2,5],'dau hieu chia khoa' : 'K'}
    hopmau = {'toa do hop mau': [6,6],'dau hieu hop mau':'-'}
    def map():
        a = '-'        
        hinhtuong = [kichcomap*[a] for i in range(kichcomap)]
        hinhtuong[toadonhanvat[0]][toadonhanvat[1]] = nhapnhanvat
        hinhtuong[loira[0]][loira[1]] = "D"
        hinhtuong[chiakhoa['toa do chia khoa'][0]][chiakhoa['toa do chia khoa'][1]] = chiakhoa['dau hieu chia khoa']
        hinhtuong[buctuong['toa do buc tuong'][0]][buctuong['toa do buc tuong'][1]] = buctuong['dau hieu buc tuong']
        if man == 2:
            hinhtuong[chiakhoa1['toa do chia khoa'][0]][chiakhoa['toa do chia khoa'][1]+1] = chiakhoa1['dau hieu chia khoa']
        if man >= 3:    
            hinhtuong[toadoquaithu1['toa do quai thu'][0]][toadoquaithu1['toa do quai thu'][1]] = toadoquaithu1['dau hieu quai thu']
            hinhtuong[toadoquaithu2['toa do quai thu'][0]][toadoquaithu2['toa do quai thu'][1]] = toadoquaithu2['dau hieu quai thu']
            hinhtuong[toadoquaithu3['toa do quai thu'][0]][toadoquaithu3['toa do quai thu'][1]] = toadoquaithu3['dau hieu quai thu']
        if man == 4:
            hinhtuong[hopmau['toa do hop mau'][0]][hopmau['toa do hop mau'][1]] = hopmau['dau hieu hop mau']
        print('\n'.join(' '.join(row) for row in hinhtuong))
    def dichuyen():
        dichuyen = input("ban muon di huong nao(a,s,d,w): ")
        if dichuyen == 'w' and toadonhanvat[0] > 0:
            toadonhanvat[0] -= 1
        elif dichuyen == "a" and toadonhanvat[1] > 0:
            toadonhanvat[1] -= 1
        elif dichuyen == "s" and toadonhanvat[0] < kichcomap - 1:
            toadonhanvat[0] += 1
        elif dichuyen == "d" and toadonhanvat[1] < kichcomap - 1:
            toadonhanvat[1] += 1
        else:
            print(vuotqua)
    def cuocchienquaithu1():
        print('bận đã gặp quái vật!!!!!')
        print('thông tin nhân vật:',nhanvat)
        print('thông tin quái thú: ',quaithu1)
        hanhdong = input('bạn muốn chạy(r) hay đánh(c)')
        while quaithu1['hp'] > 0:
            if toadoquaithu1['toa do quai thu'][0] == toadonhanvat[0] and toadoquaithu1['toa do quai thu'][1] == toadonhanvat[1]:
                if hanhdong == 'r':
                    if ngaunhien == 0:
                        print('bạn chạy ko thành công và bạn sẽ bị quái vật tấn công 1 lần và bạn sẽ bị cuốn vào cuộc chiến!!!')
                        nhanvat['hp'] = nhanvat['hp'] - quaithu1['atk']
                        print('bạn còn',nhanvat['hp'],'máu')
                        hanhdong = 'c'
                    if ngaunhien == 1:
                        print('bạn đã chạy thàng công')
                        toadonhanvat[0] = toadonhanvat[0] + 1
                        break    
                elif hanhdong == 'c':
                    print('trận chiến sẽ diễn ra với lượt đánh đầu tiên là của bạn , sau đó sẽ đến lượt đánh của quái,sau khi 1 bên bị đánh chết(hp = 0) thì trận chiến sẽ kết thúc')
                    print('Cuộc chiến bắt đầu :')    
                    while toadoquaithu1['toa do quai thu'][0] == toadonhanvat[0] and toadoquaithu1['toa do quai thu'][1] == toadonhanvat[1]:
                        print('bạn tấn công !!! KI YA HAY YA !!! ƯA ỰA')
                        quaithu1['hp'] = quaithu1['hp'] - nhanvat['atk']
                        if quaithu1['hp'] <= 0:
                            print('quái thú đã chết')
                            print('quái thú còn số máu là:',0,'hp')
                            toadoquaithu1['dau hieu quai thu'] = 'X'
                            break
                        else:
                            print('đến lượt đánh của quái thú')
                            nhanvat['hp'] = quaithu1['atk'] - nhanvat['hp']
                        if nhanvat['hp'] < 0:
                            print('máu của bạn còn lại:',nhanvat['hp'])    
                        else:
                            print('bạn đã tèo r huhuhu')
                else:
                    print('Nếu bạn ko muốn đánh hoặc chạy thì máy sẽ mặc định là bạn sẽ bị tấn công!!! ')   
                    hanhdong = 'c'         
    def cuocchienquaithu2():
        print('bận đã gặp quái vật!!!!!')
        print('thông tin nhân vật:',nhanvat)
        print('thông tin quái thú: ',quaithu2)
        hanhdong = input('bạn muốn chạy(r) hay đánh(c)')
        while quaithu2['hp'] > 0:
            if toadoquaithu2['toa do quai thu'][0] == toadonhanvat[0] and toadoquaithu2['toa do quai thu'][1] == toadonhanvat[1]:
                if hanhdong == 'r':
                    if ngaunhien == 0:
                        print('bạn chạy ko thành công và bạn sẽ bị quái vật tấn công 1 lần và bạn sẽ bị cuốn vào cuộc chiến!!!')
                        nhanvat['hp'] = nhanvat['hp'] - quaithu2['atk']
                        print('bạn còn',nhanvat['hp'],'máu')
                        hanhdong = 'c'
                    if ngaunhien == 1:
                        print('bạn đã chạy thàng công')
                        toadonhanvat[0] = toadonhanvat[0] + 1
                        break   
                elif hanhdong == 'c':
                    print('trận chiến sẽ diễn ra với lượt đánh đầu tiên là của bạn , sau đó sẽ đến lượt đánh của quái,sau khi 1 bên bị đánh chết(hp = 0) thì trận chiến sẽ kết thúc')
                    print('Cuộc chiến bắt đầu :')    
                    while toadoquaithu2['toa do quai thu'][0] == toadonhanvat[0] and toadoquaithu2['toa do quai thu'][1] == toadonhanvat[1]:
                        print('bạn tấn công !!! KI YA HAY YA !!! ƯA ỰA')
                        quaithu2['hp'] = quaithu2['hp'] - nhanvat['atk']
                        if quaithu2['hp'] <= 0:
                            print('quái thú đã chết')
                            print('quái thú còn số máu là:',0,'hp')
                            toadoquaithu2['dau hieu quai thu'] = 'X'
                            break
                        else:
                            print('đến lượt đánh của quái thú')
                            nhanvat['hp'] = quaithu2['atk'] - nhanvat['hp']
                        if nhanvat['hp'] < 0:
                            print('máu của bạn còn lại:',nhanvat['hp'])    
                        else:
                            print('bạn đã tèo r huhuhu')
                else:
                    print('Nếu bạn ko muốn đánh hoặc chạy thì máy sẽ mặc định là bạn sẽ bị tấn công!!! ')   
                    hanhdong = 'c'                           
    def cuocchienquaithu3():
        print('bận đã gặp quái vật!!!!!')
        print('thông tin nhân vật:',nhanvat)
        print('thông tin quái thú: ',quaithu3)
        hanhdong = input('bạn muốn chạy(r) hay đánh(c)')
        while quaithu3['hp'] > 0:
            if toadoquaithu3['toa do quai thu'][0] == toadonhanvat[0] and toadoquaithu3['toa do quai thu'][1] == toadonhanvat[1]:
                if hanhdong == 'r':
                    if ngaunhien == 0:
                        print('bạn chạy ko thành công và bạn sẽ bị quái vật tấn công 1 lần và bạn sẽ bị cuốn vào cuộc chiến!!!')
                        nhanvat['hp'] = nhanvat['hp'] - quaithu3['atk']
                        print('bạn còn',nhanvat['hp'],'máu')
                        hanhdong = 'c'
                    if ngaunhien == 1:
                        print('bạn đã chạy thàng công')
                        toadonhanvat[0] = toadonhanvat[0] + 1
                        break   
                elif hanhdong == 'c':
                    print('trận chiến sẽ diễn ra với lượt đánh đầu tiên là của bạn , sau đó sẽ đến lượt đánh của quái,sau khi 1 bên bị đánh chết(hp = 0) thì trận chiến sẽ kết thúc')
                    print('Cuộc chiến bắt đầu :')    
                    while toadoquaithu3['toa do quai thu'][0] == toadonhanvat[0] and toadoquaithu3['toa do quai thu'][1] == toadonhanvat[1]:
                        print('bạn tấn công !!! KI YA HAY YA !!! ƯA ỰA')
                        quaithu3['hp'] = quaithu3['hp'] - nhanvat['atk']
                        if quaithu3['hp'] <= 0:
                            print('quái thú đã chết')
                            print('quái thú còn số máu là:',0,'hp')
                            toadoquaithu3['dau hieu quai thu'] = 'X'
                            break
                        else:
                            print('đến lượt đánh của quái thú')
                            nhanvat['hp'] = quaithu3['atk'] - nhanvat['hp']
                        if nhanvat['hp'] < 0:
                            print('máu của bạn còn lại:',nhanvat['hp'])    
                        else:
                            print('bạn đã tèo r huhuhu')
                else:
                    print('Nếu bạn ko muốn đánh hoặc chạy thì máy sẽ mặc định là bạn sẽ bị tấn công!!! ')   
                    hanhdong = 'c'                                      
    def buctuongcucsuc():
        if toadonhanvat[0] == buctuong['toa do buc tuong'][0] and toadonhanvat[1] == buctuong['toa do buc tuong'][1]:
            if ngaunhien == 0:
                toadonhanvat[0] =  buctuong['toa do buc tuong'][0] - 1
            if ngaunhien == 1:
                toadonhanvat[1] =  buctuong['toa do buc tuong'][1] - 1
            print('ban ko the di qua buc tuong va buc tuong se day lui ban ngau nhien ve 1 phia cua buc tuong')
    while man == 1:  
        map()
        dichuyen()
        buctuongcucsuc()
        if chiakhoa['toa do chia khoa'][0] == toadonhanvat[0] and chiakhoa['toa do chia khoa'][1] == toadonhanvat[1]:
            caichiakhoa += 1
            print('bạn đã nhặt được chìa khóa')   
            chiakhoa['dau hieu chia khoa'] =  'X'
            if vuotqua == 'ko the vuot ra pham vi ngoai map':
                caichiakhoa = 1
        if loira[0] == toadonhanvat[0] and loira[1] == toadonhanvat[1]:
            if caichiakhoa == 1:
                caichiakhoa = 0
                map()
                man += 1
                print('den man:',man)
            else:
                print('ban chua lay chia khoa')
    if man == 2:
        chiakhoa['dau hieu chia khoa'] = 'K'            
    while man == 2:
        map()
        dichuyen()
        buctuongcucsuc()
        if chiakhoa['toa do chia khoa'][0] == toadonhanvat[0] and chiakhoa['toa do chia khoa'][1] == toadonhanvat[1]:
            caichiakhoa += 1
            print('bạn đã nhặt được chìa khóa')
            chiakhoa['dau hieu chia khoa'] =  'X'
            if vuotqua == 'ko the vuot ra pham vi ngoai map':
                caichiakhoa = caichiakhoa
        if chiakhoa1['toa do chia khoa'][0] == toadonhanvat[0] and chiakhoa1['toa do chia khoa'][1] == toadonhanvat[1]:
            caichiakhoa += 1
            print('bạn đã nhặt được chìa khóa')
            chiakhoa1['dau hieu chia khoa'] =  'X'
            if vuotqua == 'ko the vuot ra pham vi ngoai map':
                caichiakhoa = caichiakhoa
        if loira[0] == toadonhanvat[0] and loira[1] == toadonhanvat[1]:
            if caichiakhoa >= 2:
                caichiakhoa = 0
                map()
                man += 1
                print('den man:',man)
            else:
                print('ban chua lay chia khoa')    
    if man == 3:
        chiakhoa['dau hieu chia khoa'] = 'K'  
        print('CẢNH BÁO!!!: Nếu bạn ko thấy chìa khóa trên bản đồ thì có thể chìa khóa đã bị quái vật nào đó trấn giữ !!!')   
    while man == 3:
        map()
        dichuyen()    
        buctuongcucsuc()
        if chiakhoa['toa do chia khoa'][0] == toadonhanvat[0] and chiakhoa['toa do chia khoa'][1] == toadonhanvat[1]:
            caichiakhoa += 1
            print('bạn đã nhặt được chìa khóa')   
            chiakhoa['dau hieu chia khoa'] =  'X'
            if vuotqua == 'ko the vuot ra pham vi ngoai map':
                caichiakhoa = 1
        if toadoquaithu1['toa do quai thu'][0] == toadonhanvat[0] and toadoquaithu1['toa do quai thu'][1] == toadonhanvat[1]:
            if toadoquaithu1['dau hieu quai thu'] == 'X':
                print('Bạn đã tiêu diệt quái thú R KK') 
            else:    
                cuocchienquaithu1()
        if toadoquaithu2['toa do quai thu'][0] == toadonhanvat[0] and toadoquaithu2['toa do quai thu'][1] == toadonhanvat[1]:
            if toadoquaithu2['dau hieu quai thu'] == 'X':
                print('Bạn đã tiêu diệt quái thú R KK') 
            else:    
                cuocchienquaithu2()
        if toadoquaithu3['toa do quai thu'][0] == toadonhanvat[0] and toadoquaithu3['toa do quai thu'][1] == toadonhanvat[1]:
            if toadoquaithu3['dau hieu quai thu'] == 'X':
                print('Bạn đã tiêu diệt quái thú R KK') 
            else:    
                cuocchienquaithu3()
        if loira[0] == toadonhanvat[0] and loira[1] == toadonhanvat[1]:
            if caichiakhoa >= 1:
                caichiakhoa = 0
                map()
                man += 1
                print('den man:',man)
            else:
                print('ban chua lay chia khoa') 
    while man == 4:  
        map()
        dichuyen()    
        buctuongcucsuc()
        if chiakhoa['toa do chia khoa'][0] == toadonhanvat[0] and chiakhoa['toa do chia khoa'][1] == toadonhanvat[1]:
            caichiakhoa += 1
            print('bạn đã nhặt được chìa khóa')   
            chiakhoa['dau hieu chia khoa'] =  'X'
            if vuotqua == 'ko the vuot ra pham vi ngoai map':
                caichiakhoa = 1
        if toadoquaithu1['toa do quai thu'][0] == toadonhanvat[0] and toadoquaithu1['toa do quai thu'][1] == toadonhanvat[1]:
            if toadoquaithu1['dau hieu quai thu'] == 'X':
                print('Bạn đã tiêu diệt quái thú R KK') 
            else:    
                cuocchienquaithu1()
        if toadoquaithu2['toa do quai thu'][0] == toadonhanvat[0] and toadoquaithu2['toa do quai thu'][1] == toadonhanvat[1]:
            if toadoquaithu2['dau hieu quai thu'] == 'X':
                print('Bạn đã tiêu diệt quái thú R KK') 
            else:    
                cuocchienquaithu2()
        if toadoquaithu3['toa do quai thu'][0] == toadonhanvat[0] and toadoquaithu3['toa do quai thu'][1] == toadonhanvat[1]:
            if toadoquaithu3['dau hieu quai thu'] == 'X':
                print('Bạn đã tiêu diệt quái thú R KK') 
            else:    
                cuocchienquaithu3()
        if hopmau['toa do hop mau'][0] == toadonhanvat[0] and hopmau['toa do hop mau'][1] == toadonhanvat[1]:
            print('YAHUUUU!!!! Bạn thật là may mắn bạn đã nhặt được hòm máu đuọc giấu trên bản đồ và hp của bạn sẽ được tăng 20 máu')
            nhanvat['hp'] = nhanvat['hp'] + 20
        if loira[0] == toadonhanvat[0] and loira[1] == toadonhanvat[1]:
            if caichiakhoa >= 1:
                caichiakhoa = 0
                map()
                man += 1
                print('den man:',man)
            else:
                print('ban chua lay chia khoa')         