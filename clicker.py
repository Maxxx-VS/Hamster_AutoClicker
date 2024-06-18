import pyautogui
from time import sleep
import keyboard
from time import sleep
sleep_time = int(input('Сколько ожидания нужно? '))

for i in range(sleep_time, 0, -1):
    print(f'Начинаю работу через {i} секунды')
    sleep(1)

while True:
    width, height = pyautogui.size()
    pyautogui.click(width/2, height/2)
    if keyboard.is_pressed('esc'):
        print('Работа завершена!')
        break