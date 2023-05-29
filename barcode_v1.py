import pyzbar.pyzbar as pyzbar
# pyzbar를 설치 후에 위 코드에 문제가 없는지 확인한다. 

import cv2
import matplotlib.pyplot as plt

# 이미지를 불러오기 
img = cv2.imread('img/bh_bar.jpg')

# 이미지를 확인해보기 
plt.imshow(img)

# 이미지를 흑백으로 변경한다. 원래는 RGR 3 채널이었는데 Gay로 1채널만 변경하게 된 것  
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray')

# decoded라는 변수를 만들고 pyzbar로 디코드한 값을 넣어준다.
decoded = pyzbar.decode(gray)

#한번 출력해본다. 
decoded 

# 배열안에 decoded의 object들이 들어있는것을 확인할 수 있다.   

# for d in decoded:
#     # byte 배열로 되어있기 때문에 utf-8로 디코드를 해줘야 링크로 변환이 된다. 
#     print(d.data.decode('utf-8'))
#     # qr코드라는 것이 나옴 
#     print(d.type)
    
#     cv2.rectangle(img, (d.rect[0],d.rect[1]),(d.rect[0]+d.rect[2],d.rect[1] + d.rect[3]), (0,0,255),2)
    
#     plt.imshow(img)

