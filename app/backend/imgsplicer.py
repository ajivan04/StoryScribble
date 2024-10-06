from PIL import Image
import os


def image_splicer(frames):
    imgs = []
    #have this var equal to how many frames the kid submitted

    for frame in range(1, frames+1):
        imgs.append(Image.open('./app/backend/temp/image' + str(frame) + '.jpg'))

    totalWidth = 0
    maxHeight=0
    for frame in imgs:
        #frame.show()
        totalWidth += frame.width
        if frame.height>maxHeight:
            maxHeight=frame.height

    newImage = Image.new('RGBA', (totalWidth, maxHeight))
    space = Image.new("RGB", (50, maxHeight), "black")

    widthSoFar=0
    for frame in imgs:
        newImage.paste(frame, (widthSoFar,0))
        widthSoFar+= frame.width
        newImage.paste(space, (widthSoFar,0))
        widthSoFar+= space.width

    newImage.show()
    image_url = './assets/combined_image.png'

    newImage.save(image_url)
    return image_url

