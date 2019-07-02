from MyQR import myqr
import os
version, level, qr_name = myqr.run(
words="https://www.baidu.com",
version=1, #设置容错率为最高
level='H',
picture="123.gif", #将二维码和图片合成
colorized=True, #彩色二维码
contrast=1.0, #调节图片的对比度
brightness=1.0, #调节图片的亮度
save_name="3.gif",
save_dir=os.getcwd() #返回当前进程的工作目录
)