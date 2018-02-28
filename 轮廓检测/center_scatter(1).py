import matplotlib.pyplot as plt
import numpy as np
import argparse
import imutils
import cv2
count=3
#**********************注:这里涉及到的x,y都是以左下角为(0,0)点***********************#
class Car:
             """Class to represent a car
             """
             position=[[0,0],[0,0],[0,0],[0,0]];
             def center(self,args):
                          image = cv2.imread(args)
                          gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                          #blurred = cv2.GaussianBlur(gray, (5, 5), 0)
                          thresh = cv2.threshold(gray, 96, 255, cv2.THRESH_TRUNC)[1]
                          # find contours in the thresholded image
                          cnts = cv2.findContours(thresh.copy(), cv2.RETR_LIST,
                                  cv2.CHAIN_APPROX_NONE )
                          cnts = cnts[0] if imutils.is_cv2() else cnts[1]
                          # loop over the contours
                          list=[0,0,0,0];
                          # compute the center of the contour
                          M = cv2.moments(cnts[0])
                          cX = int(M["m10"] / M["m00"])
                          cY = int(M["m01"] / M["m00"])
                          # draw the contour and center of the shape on the image
                          cv2.drawContours(image, [cnts[0]], -1, (255, 255, 0), 2)
                          cv2.circle(image, (cX, cY), 7, (255, 0, 0), -1)
                          cv2.putText(image, "center", (cX - 20, cY - 20),
                                  cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                          key=self.position.index([0,0])
                          # show the image
                          #print(cX,cY)
                          if M['m00']!=0:
                                   self.position[key][0]=cX
                                   self.position[key][1]=cY
                          #s[c]=str(cY)
                          cv2.imshow("Image", image)
                          cv2.imshow("gray", gray)
                          k = cv2.waitKey(0)
                          if k == 27:  # wait for ESC key to exitcv2.destroyAllWindows
                                  cv2.destroyAllWindows
             def scatter(self):
                          for row in range(count):#count的值是可变的在上面定义过（在这里只设置为了3）
                                       X = self.position[row][0]
                                       Y = 500-self.position[row][1]
                                       print(X,Y)
                                       print(row)
                                       T = np.arctan2(Y,X) # for color value
                                       plt.scatter(X, Y, s=75, c=T, alpha=.5)#s是size大小，c是指颜色，alpha是透明度50%
                                       plt.xlim(0, 100)#取值范围
                                       plt.xticks(())  # ignore xticks
                                       plt.ylim(-0, 1000)
                                       plt.yticks(())  # ignore yticks
                                       #设置x，y轴坐标轴范围
                                       plt.xlim((0, 1000))
                                       plt.ylim((0, 100))
                                       #设置x，y轴刻度
                                       plt.xticks(np.linspace(0, 1000, 10))
                                       plt.yticks(np.linspace(0, 500, 5))
                                       #设置x，y轴标签
                                       plt.xlabel('X axis')
                                       plt.ylabel('Y axis')
                          plt.show()

car_test=Car()
args_1="1.png"
args_2="2.png"
args_3="3.png"
car_test.center(args_1)#该函数只确定一幅图的质心，args是同一路径下图片的名
car_test.center(args_2)
car_test.center(args_3)
car_test.scatter()#该函数显示该对象所有的位置（路径）

