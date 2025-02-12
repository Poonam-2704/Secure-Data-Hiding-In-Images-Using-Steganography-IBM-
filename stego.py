import cv2
import os

img = cv2.imread("C:\IBM\Stenography-main\Stenography-main\Treeimage.jpg")  
if img is None:
    print("Error: Image not found or cannot be opened. Please check the file path.")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

d = {}
c = {}
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

height, width, _ = img.shape
if len(msg) > height * width * 3:
    print("Error: Message too long for the selected image.")
    exit()

for i in range(len(msg)):
    row, col = divmod(n, width)
    img[row, col, z] = d[msg[i]]
    n += 1
    z = (z + 1) % 3

cv2.imwrite("C:\IBM\Stenography-main\Stenography-main\Treebranch.jpg", img)
os.system("start C:\IBM\Stenography-main\Stenography-main\Treebranch.jpg")

message = ""
n = 0
z = 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(len(msg)):
        row, col = divmod(n, width)
        message += c[img[row, col, z]]
        n += 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")
