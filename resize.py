import os
from PIL import Image

def keepAspectResizeSimple(image,id):#imageオブジェクトを渡すこと
    name=id+".jpg"
    size=(980,1080)
    # 画像の読み込み
    # サイズを幅と高さにアンパック
    width, height = size
    # 矩形と画像の幅・高さの比率の小さい方を拡大率とする
    ratio = min(width / image.width, height / image.height)
    # 画像の幅と高さに拡大率を掛けてリサイズ後の画像サイズを算出
    resize_size = (round(ratio * image.width), round(ratio * image.height))
    # リサイズ後の画像サイズにリサイズ
    resized_image = image.resize(resize_size)
    #resized_image.save("./debug/"+id+"_resize.jpg")
    resized_image.save("./download/resize/"+name)
    return resized_image
if __name__ == '__main__':
    pass