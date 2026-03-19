import cv2
import numpy as np
print("Hello WORLD")
image = cv2.imread("test.jpg") # изображение с которым работаем и указываем полный путь если не в папке с проектом
print("Hello WORLD")
cv2.imshow("original", image) # создание окна и вывод на него объекта с подписью
cv2.waitKey(0) # ожидание нажатия любой кнопки
print("Hello WORLD")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #все цвета конвертируются в сервые оттенки
cv2.imshow("gray", gray_image)  # создание окна и вывод на него объекта с подписью
cv2.waitKey(0) # ожидание нажатия любой кнопки

blurred_image = cv2.GaussianBlur(image, (11, 11), 0) # размытие картинки, размытие по х и y, коэффициент размытия если
# 0 библиотека побирает автоматически
cv2.imshow("blurred", blurred_image) # создание окна и вывод на него объекта с подписью
cv2.waitKey(0) # ожидание нажатия любой кнопки

hsv_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV) # у размытого изображения меняем цветовую палитру, так лучше работает
cv2.imshow("hsv", hsv_image) # создание окна и вывод на него объекта с подписью
cv2.waitKey(0) # ожидание нажатия любой кнопки

# границы цвета можно найти в интернете или подобрать по палитре
hsv_min = np.array((36, 25, 25), np.uint8) # нижняя граница зеленого цвета
hsv_max = np.array((70, 255,255), np.uint8) # верхняя граница зеленого цвета
green_mask = cv2.inRange(hsv_image, hsv_min, hsv_max) # создали маску
cv2.imshow("mask", green_mask) # создание окна и вывод на него объекта с подписью
cv2.waitKey(0) # ожидание нажатия любой кнопки

# командой findContours находим контур, возвращаем контуры которые найдем и их иерархию, передаем копию объекта, алгоритм поиска,
# алгоритм апроксимации контура
contours, hierarchy = cv2.findContours(green_mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# отображаем найденные контуры, метсо рисования, сами конутры, -1 - без заливки, цвет по BRG, толщина конутра, тип линии, иерархия, не ниже уровня 1
cv2.drawContours(image, contours, -1, (255, 0, 0), 3, cv2.LINE_AA, hierarchy, 1)
cv2.imshow('contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()