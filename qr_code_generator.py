import qrcode

route = input('Write the name for QR: ')
path_web = input('Write your name of domain [Example= example.com]: ')

path_follow = 'https://' + path_web
filename = route + '.png'

image = qrcode.make(path_follow)
image.save(filename)