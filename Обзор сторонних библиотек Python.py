import numpy as np
import random
from PIL import Image, ImageFilter, ImageDraw, ImageFont


print(arr)


arr = arr * 3 + 10
print(arr)



arr = np.random.randint(1, 51, size=15)


print(f'Сумма всех элементов массива: {np.sum(arr)}')


print(f'Среднее значение всех элементов массива: {np.mean(arr)}')


print(f'Минимальное значение элементов массива: {np.min(arr)}')
print(f'Максимальное значение элементов массива: {np.max(arr)}')



arr = np.arange(10, 50, 5)


print(arr[2])


arr[4] = 99
print(arr)



arr = np.random.randint(0, 101, size=20)


print(arr[arr > 50])


arr[arr < 20] = 0
print(arr)



img = Image.open('./img.webp')
print("Исходный размер:", img.size)


new_size = (img.width // 2, img.height // 2)
resized_img = img.resize(new_size)


resized_img.save('resized_image.jpg', format='JPEG')



grayscale_img = img.convert('L')


blur_img = img.filter(ImageFilter.BLUR)


blur_img.save('blurred_image.png', format='PNG')



img.save('new_image.jpg', format='JPEG')



draw = ImageDraw.Draw(img)
font = ImageFont.truetype('arial.ttf', size=40)
draw.text((15, 15), "Hello, Pillow!", fill='red', font=font)


img.save('text_image.jpg', format='JPEG')