#coding=utf-8

#导入图片处理模块PIL的类Image
from PIL import Image

#将图片转为字符画所需的字符
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#得到对应每个像素点的字符
def getstr(r,g,b,alpha=256):
    if alpha==0:
        return ' '
    lens=len(ascii_char)

    #根据公式将rgb值转换为灰度值
    gray=int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit=257.0/lens
    char=ascii_char[int(gray/unit)]#得到灰度值对应的字符

    return char

if __name__ == '__main__':
    picture_name=raw_input('please input picture name---->')
    size=raw_input('please input size you want like 30x30 or enter to default---->')
    a=size.split('x')
    width=int(a[0]) if size else 40
    height=int(a[1]) if size else 40

    #用Image模块打开图片
    im=Image.open(picture_name)
    #将图片尺寸调整为指定像素
    im=im.resize((width,height),Image.NEAREST)

    txt=''

    #将每个像素对应的字符加入字符串txt
    for i in range(width):
        for j in range(height):
            txt+=getstr(*im.getpixel((j,i)))
        #当一列结束时插入换行符
        txt+='\n'

    print txt
    #将字符串写入文件output.txt
    with open('output.txt','w') as e:
        e.write(txt)
        e.close()
