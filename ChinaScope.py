"""
------------------------------------------------------------------------------------------------------------------------
Developers: qingtao.chen
Data: 2023.04.13
Version: 2.1
------------------------------------------------------------------------------------------------------------------------
"""

# TODO: traverse the document and click <structured> + review and pass respectively.

import os
import pyautogui
import keyboard
from time import sleep

print(
    "-----------------------------------------------------------------------------------------------------------------")
print("Developers: qingtao.chen \nData: 2023.04.06 \nVersion: 2.1")
print(
    "-----------------------------------------------------------------------------------------------------------------")

x_left = 120  # Document starting position
y_left = 455

# 从 position/position_01.txt read x and y value
with open('position/position_01.txt', 'r') as f:
    lines = f.readlines()
    x_01 = int(lines[0])
    y_01 = int(lines[1])

x_02 = x_01 - 32
y_02 = y_01

x_03 = x_01 + 45
y_03 = y_01 - 623

j = 1


def on_hotkey():
    print("Ctrl+Alt+A pressed. Exiting program...")  # 响应'ctrl+alt+a'，停止程序运行
    os._exit(0)


keyboard.add_hotkey('ctrl+alt+a', on_hotkey)  # 创建线程，检测'ctrl+alt+a'

#思路： 撤销审核——》 标准化——》确认审核

##前提参数
Y = 0
color_1 = (26, 171, 39)#   green button‘s RGB
color_11=(24, 176, 41)
color_2 =(241, 196, 15) # yellow button's RGB
color_3 =(254, 76, 85)#   red button's RGB
color_31 =(255, 75, 84)# Button Red RGB-External Quality Inspection
lc_x,lc_y=1689,109 # Standardized quality inspection location
w_x,w_y=1760,101
ij = 1
####

while Y < 4:   #Confirm the number of refresh pages----if judgment is not written, start from the second page
    if Y == 0:
        # pyautogui.click(414, 198, button='left')  # Click <Refresh on the left>
        print('page：1！！！！')
        sleep(2)
    else:
        pyautogui.click(219,1005,button='left')  # Click <Next Page Button>
        # print('page：',Y)
        sleep(2)
    for y_left in range(455, 980, 21):
        print("In progress", round((y_left-433)/22), "Processing of reports...")
        pyautogui.doubleClick(x_left, y_left)  # Double-click the document
        sleep(3.2)
        # if j == 1:
        pyautogui.click(1592, 197, button='left')  # Normalized data - first half
        sleep(1.5)
        pyautogui.click(1389, 829, button='left')  # save data
        pyautogui.click(1457, 829, button='left')  # Withdraw review
        sleep(0.4)
        pyautogui.press('1')#Keyboard input "1"
        sleep(1)
        pyautogui.click(1108, 605, button='left')  # Withdraw review - Confirm
        sleep(0.2)
        pyautogui.click(1441, 190, button='left')  # Click <Disclosure Data>
        sleep(0.3)
        pyautogui.click(1391, 824, button='left')  # Click <Structure>
        sleep(3)
        pyautogui.doubleClick(1358, 829, button='left')  # Click <Refresh>
        sleep(1.5)
        pyautogui.click(1422, 828, button='left')  # Confirm review
        sleep(0.25)
        # #  The moving mouse button is [Green RGB]
        # if pyautogui.pixel(lc_x,lc_y)==color_1:
        #     print("\033[0;32m pass！！！\033[1;43m\033[0m")
        #
        # elif  pyautogui.pixel(lc_x,lc_y)==color_2:
        #     print("\033[1;33m △△△△△Warning△△△△\033[0m")
        # #  The moving mouse button is [[yellow RGB]
        #
        # elif pyautogui.pixel(lc_x,lc_y) == color_3:
        #     print('Normalization failed', '\033[1;31;41m#########\033[0m')
        #
        # else:
        #     print("\033[1;47m Wrong button position  \033[0m")
# ####外部质检
#         if pyautogui.pixel(w_x, w_y) == color_1:
#             print("\033[0;32m outside：outside pass！！！\n\033[0m")
#
#         elif pyautogui.pixel(w_x, w_y) == color_2:
#             print("\033[1;33m outside：△△△△△warn△△△△\033[0m")
#         #  The moving mouse button is [[yellow RGB]
#         elif pyautogui.pixel(w_x, w_y) == color_31:
#             print('outside：fail', '\033[1;31;41m     #######\033[0m')
#         else:
#             print("\033[1;47m outside：Wrong button position  \033[0m")
#

    print('---------------page：', Y+1, "Processing completed-------------")
    j = j + 1  # for cycle——————used for counting
    Y +=1  #whil ecycle
    sleep(1)



print('The happy mission is over！！！！')
