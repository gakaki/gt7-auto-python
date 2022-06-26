working progress
GT7 Automation Python AFK (WIP)
Requirments
python env
windows 10 ( administrator privileges ) or macos ,linux not support ps remote play
python 3.9+ or Anaconda
Ps remote play
PyCharm or vscode if need development or code debug
Game Settings
Usage
pip install -r requirments.txt
python main.py
Arch
windows not support win32 input , using directx input ,so the pydxinput can help press key
Notice
pyautogui vk return can not use on ps remote play Please use pydirectxInput below code no usage on windows platform

pyautogui.press('{VK_RETURN}')
pyautogui.typewrite(["enter"])
pyautogui.moveTo(280,280)
pydirectinput.press('enter')
pydirectinput.press('{VK_RETURN}')
pyautogui.alert('This displays some text with an OK button.')