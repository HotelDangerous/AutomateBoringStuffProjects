# 2048.py - Uses selenium to navigate a Firefox browser to play 2048 simply by clicking the UP,
#           RIGHT, LEFT, AND DOWN keys in rotation until the game ends and a retry button appears.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Opens a Firefox window and navigates to the 2048 game
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

# Sending the UP, RIGHT, DOWN, LEFT keys to the until the retry button is displayed.
htmlElement = browser.find_element(By.TAG_NAME, 'html')
i = 0
while True:
    htmlElement.send_keys(Keys.UP)
    htmlElement.send_keys(Keys.RIGHT)
    htmlElement.send_keys(Keys.DOWN)
    htmlElement.send_keys(Keys.LEFT)
    i+=1

    #Every ten iterations check if the game has ended. If so, break the loop.
    if i == 10:
       i = 0
       if browser.find_element(By.CLASS_NAME, 'retry-button').is_displayed():  # check if retry is displayed.
           break

# Prints final score and then closes browser tab after 2 second wait.
final_score = browser.find_element(By.CLASS_NAME, 'score-container').text  # Getting final score
print(f'Final Score: {final_score}')
time.sleep(2)
browser.close()
