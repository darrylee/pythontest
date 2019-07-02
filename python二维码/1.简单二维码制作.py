
import qrcode
img = qrcode.make("hello")
img.get_image().show()
img.save('1.png')

"""
qrcode.make(str):str为二维码包含的文字信息,也可以是网页链接
qrcode.show()：运行时展示二维码图案
qrcode.save(str):将二维码以str为名保存到本地目录（注意文件的扩展名）
"""