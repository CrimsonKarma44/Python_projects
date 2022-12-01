'''
install and import pillow
open the image to reaize
print the current size
specify the new size to be resized to
save the image '''

from PIL import Image

image = Image.open('Image_Reizer/galaxy.jpg')


print(f"Current Size: {image.size}")

# 1366 x  768
x = int(input("Length: "))
y = int(input("Breath: "))
resized_image = image.resize((x, y))

resized_image.save("Image_Reizer/galaxy_new.jpg")