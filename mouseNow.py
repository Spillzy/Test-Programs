#! python3
# Displays the mouse cursor's current position.
# Doesn't display properly in the Interactive Window.  Have to run with F5 

import pyautogui, time 

print('Press reset in the interactive window to quit')
try:
    while True:
        # Get and print the mouse coordinates.
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end = '')
        #time.sleep(.1)
        print('\b' * len(positionStr), end = '', flush = True)
except KeyboardInterrupt:
    print('\Done.')

