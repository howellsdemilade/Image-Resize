# Image Resizer

from PIL import Image

def resize_image(size1, size2):
    
    image = Image.open("C:/WORKS/Image_Resize/anime.jpg")
    print(f"Current Size : {image.size}")
        
    resized_image = image.resize((size1, size2))

    resized_image.save("anime" + str(size1) + ".jpg")

size1 = int(input("Enter Width: "))
size2 = int(input("Enter Length: "))
resize_image(size1, size2)
