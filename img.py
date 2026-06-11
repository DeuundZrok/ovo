import cv2
from openfile import select_file
import time

def openimg():
    #open an iamge
    img_path=select_file()
    img=cv2.imread(img_path)
    cv2.imshow("image",img)
    key=cv2.waitKey(0)
    return img,key

def saveimg(img):
    filename=time.strftime("img_%Y%m%d_%H%M%S.jpg")
    cv2.imwrite(filename,img)
    print(f"已保存：{filename}")

if __name__ == "__main__":
    img,key=openimg()

    if key == 13:
        saveimg(img)

    cv2.destroyAllWindows()                   