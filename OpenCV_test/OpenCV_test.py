import cv2
import imageio

color_imagine = cv2.imread('yg.png')
print(color_imagine.shape)

# 读取单通道
gray_img = cv2.imread('yg.png', cv2.IMREAD_GRAYSCALE)
print(gray_img.shape)

# 把单通道图像保存后，再读取，仍然是3通道，相当于将单通道复制到3个通道保存
cv2.imwrite('grayscale_yg.png', gray_img)
reload_grayscale = cv2.imread('grayscale_yg.png')
print(reload_grayscale.shape)

# 指定jpg质量，范围从1~100，默认95，值越高画质越好，文件越大
cv2.imwrite('yg2.png', color_imagine, (cv2.IMWRITE_JPEG_QUALITY, 100))


def compose_gif():
    img_paths = ['yg.png', "grayscale_yg.png"]
    gif_images = []
    for path in img_paths:
        gif_images.append(imageio.imread(path))
    imageio.mimsave("yg.gif", gif_images, fps=10)
compose_gif()

# 二值图
for i in gray_img:
    for j in i:
        if j > 0:
            gray_img[i][j] = 1
        else:
            gray_img[i][j] = 0
cv2.imshow(gray_img)