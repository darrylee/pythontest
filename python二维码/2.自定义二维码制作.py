
from PIL import Image
import qrcode
# 创建QRCode对象，设置相关参数
qr = qrcode.QRCode(version=5,
error_correction=qrcode.constants.ERROR_CORRECT_H,
box_size=8,
border=4)
# 添加二维码数据
qr.add_data("http://www.baidu.com")
# 生成二维码图片
qr.make(fit=True)
# 设置二维码图片的填充色和背景色
img = qr.make_image()  #fill_color="black", back_color="white"
img = img.convert("RGBA")
# 打开logo文件
icon = Image.open("baidu.png")
# 计算logo的尺寸
img_w,img_h = img.size
factor = 4
size_w = int(img_w / factor)
size_h = int(img_h / factor)
# 比较并重新设置logo文件的尺寸
icon_w,icon_h=icon.size
if icon_w>size_w:
    icon_w=size_w
if icon_h>size_h:
    icon_h=size_h
icon=icon.resize((icon_w,icon_h),Image.ANTIALIAS) #重新设定大小，设定ANTIALIAS，即抗锯齿
# 计算logo的位置，并复制到二维码图像中
w=int((img_w-icon_w)/2)
h=int((img_h-icon_h)/2)
icon = icon.convert("RGBA")
img.paste(icon,(w,h),icon) #图片重新合成
# 保存二维码
img.save('2.png')

"""
qr=qrcode.QRCode()  //这是我们创建的一个对象
version：值为1~40的整数，控制二维码的大小（最小值是1，是个21×21的矩阵）
error_correction：控制二维码的错误纠正功能。可取值下列4个常量：
ERROR_CORRECT_X：X=L时，大约7%或更少的错误能被纠正。 
X=M（默认）时，大约15%或更少的错误能被纠正。
X=Q时，25 %以下的错误会被纠正 。
X=H时，大约30%或更少的错误能被纠正
box_size：控制二维码中每个小格子包含的像素数。
border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4）
"""