import pyautogui
pyautogui.sleep(5)
lenght = 300

while lenght != 0:
    pyautogui.drag(lenght,0)
    pyautogui.drag(0,lenght)
    lenght -= 5
    pyautogui.drag(-lenght,0)
    pyautogui.drag(0,-lenght)
    lenght -= 5