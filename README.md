## GT7 (Sony PS5 Race Game) Automation Python AFK 

###### Current project get Jetbrain Pycharm ide powerfuly support 

<img src="https://www.jetbrains.com/shop/static/images/jetbrains-logo-inv.svg" height="100">   

<img src="https://resources.jetbrains.com/storage/products/company/brand/logos/PyCharm_icon.svg?_gl=1*4auk5d*_ga*MTMxMDA0NDgwNS4xNjU1NDY1NTM2*_ga_9J976DJZ68*MTY1NTQ2NTUzNS4xLjEuMTY1NTQ2NTkyNC4w&_ga=2.91672986.163686740.1656229826-1310044805.1655465536" height="100">   



### ChangeLog
2022.07.17 update for 1.18 tokyo express pp550 race

2022.06.26 update for 1.17 reward bug

2022.06.01 update for 1.15 tokyo express pp550 race

2022.05.23 update for 1.13 race x and america dyna race

#### Usage

    pip install -r requirments.txt
    
    # in ps remote play cursor to cafe than
    
    python main.py
    
    
    windows 10 ( administrator privileges ) or macos,linux not support ps remote play, use the chiaki
    python 3.9+ or Anaconda
    Ps remote play or  chiaki
    PyCharm or vscode if need development or code debug


   1.18 version the 1.17 extra menus reward is no effect,Please not use
    
   1.17 version unlimited engine swap and unlimited get reward is recommend for earn the cr and cars.


    >>> reward117
    
    [GT7 1.17] AFK Unlimited draw 4-star ticket & 6-star Engine ticket Earn Money Gran Turismo 7 PS4 PS5
    https://www.youtube.com/watch?v=Zl5lBkCIViE
    
    every 1hour cr [45, 2975]
    every day   cr [1080, 71400]
    every month cr [32400, 2142000]
    
    >>> clubman_tokyo [using the specifi car]
    every 1hour cr [63, 88]
    every day   cr [1512, 2112]
    every month cr [45360, 63360]
    
    >>> pan_america_1st_round [dead in 1.17 verison]
    every 1hour cr [62, 84]
    every day   cr [1488, 2016]
    every month cr [44640, 60480]
    
    >>> dyna
    every 1hour cr [37, 74]
    every day   cr [888, 1776]
    every month cr [26640, 53280]
    
    >>> x
    every 1hour cr [19, 28]
    every day   cr [456, 672]
    every month cr [13680, 20160]

![img](https://i0.hdslb.com/bfs/article/d588eb255ba3c4f39ea867c128d808bb5149ccad.png@942w_531h_progressive.webp)



![img](https://i0.hdslb.com/bfs/article/be8f5332b5e04bd72d263c3be855ddfaba36f075.png@942w_531h_progressive.webp)

![img](https://i0.hdslb.com/bfs/article/52457dd472c6f5d5cc3b2f801d7f9282ec06f8ce.png@942w_531h_progressive.webp)

![img](https://i0.hdslb.com/bfs/article/9e93f5490159c4615559b53538a76a61a4325504.png@942w_531h_progressive.webp)

![img](https://i0.hdslb.com/bfs/article/5de9155e723d3b935e8df8c58389d0e6840fe5d2.png@942w_531h_progressive.webp)



### Arch

use airtest for image search and pyautogui pixel match to detect game ui

windows not support win32 input , using directx input ,so the pydxinput can help press key

    pyautogui vk return can not use on ps remote play Please use pydirectxInput below code no usage on windows platform
    pyautogui.press('{VK_RETURN}')
    pyautogui.typewrite(["enter"])
    pyautogui.moveTo(280,280)
    pydirectinput.press('enter')
    pydirectinput.press('{VK_RETURN}')
    pyautogui.alert('This displays some text with an OK button.')



   

