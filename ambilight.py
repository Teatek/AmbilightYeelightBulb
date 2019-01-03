from yeelight import Bulb
from PIL import Image
import pyautogui, time, cv2, math

# tableaux pour enregistrer les couleurs des pixels
tabx=[0]*60
taby=[0]*60
tabz=[0]*60

# initialisation de l'ampoule et allumage
bulb = Bulb("192.168.0.16")
bulb.turn_on()
count = 0

while (count == 0):
    
    # variables 
    x=0
    y=0
    z=0
    tabCount = 0
    
    # screenshot de l'écran
    picture = pyautogui.screenshot()
    picture.save('screenshot.png')

    # rescale de l'image et sauvegarde
    img = cv2.imread('screenshot.png')
    res = cv2.resize(img, dsize=(10, 6), interpolation=cv2.INTER_AREA)
    status = cv2.imwrite('screenshot.png', res)
    print("Sauvegarde de l'image rescale")

    for i in range(0,10) :
        for j in range(0,6) :
            image = Image.open('screenshot.png')
            rgb_im = image.convert('RGB')
            string = str(rgb_im.getpixel((i, j)))
            string = string.replace('(','')  
            string = string.replace(')','')  
            #print(string)
            couleurs = string.split(",")

            for i in range(0,3):
                couleurs[i] = couleurs[i].replace(' ','')  
                #print(couleurs[i])
            tabx[tabCount] = couleurs[0]
            taby[tabCount] = couleurs[1]
            tabz[tabCount] = couleurs[2]
            tabCount+=1
            #print(tabx)
            #print(taby)
            #print(tabz)

    for i in range (0,60):
        x += int(tabx[i])
        #print("x : ", x)
        y += int(taby[i])
        #print("y : ", y)
        z += int(tabz[i])
        #print("z : ", z)
    x = x/60
    y = y/60
    z = z/60
    x = math.floor(x)
    y = math.floor(y)
    z = math.floor(z)

    print(x, y, z)
    if(x != 0 and y != 0 and z != 0):
        # change la couleur de l'ampoule en fonction du resultat
        bulb.set_rgb(x, y, z)

        # reset des valeurs de variables
    for i in range (0,60):
        tabx[i] = 0
        taby[i] = 0
        tabz[i] = 0
        
    time.sleep(1)
    count = 0
    
