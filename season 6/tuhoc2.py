while True:
    import datetime
    x = datetime.datetime.now().hour
    print(x)
    y = datetime.datetime.now().minute
    print(y)
    if x == 21 and y == 59:
        print('thuc day di')    
        import pyglet
        music = pyglet.resource.media("sample.mp3")
        music.play()
        pyglet.app.run()

        break
    else:
        print('chua den gio')


 


