# import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import datetime

"get price from amazon more easily using selenium:"
# chrome_driver_path = Service("C:/Users/Barnaby's Pc/Development/chromedriver.exe")
# driver = webdriver.Chrome(service=chrome_driver_path)
#
# driver.get("https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/ref=sr_1_1?keywords=ps5&qid=1666169"
#            "340&qu=eyJxc2MiOiI0LjM5IiwicXNhIjoiNi4xNyIsInFzcCI6IjYuMDkifQ%3D%3D&sprefix=ps%2Caps%2C52&sr=8-1")
# price = driver.find_element(By.XPATH, "//*[@id='corePrice_feature_div']/div/span").text    # went to outer span...
# # ...right-click on the line and go to 'Copy' -> 'Copy XPath' and change double quotes to single quotes.
# # 'https://selenium-python.readthedocs.io/locating-elements.html#'
# print(price)
#
# # driver.close()    # closes active tab
# driver.quit()    # closes whole browser
"#################################################"
"----------------------------------------------------------------------------------------------------------------------"
"get python.org events list into a dictionary:"
# chrome_driver_path = Service("C:/Users/Barnaby's Pc/Development/chromedriver.exe")
# driver = webdriver.Chrome(service=chrome_driver_path)
#
#
# driver.maximize_window()    # # # # # AS SOME VALUES DONT SHOW UNLESS MAXIMISED SCREEN # # # # #
#
#
# driver.get("https://www.python.org/")
# events = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')
#
# events_dict = {}
# counter = 0
#
# for event in events:    # COULD ALL BE COMPRESSED INTO ONE LINE USING RANGE FOR 'COUNTER'?
#     event_name = event.find_element(By.CSS_SELECTOR, 'li a').text
#     date = event.find_element(By.CSS_SELECTOR, ".event-widget time").text
#     events_dict[counter] = {"time": f"{date}", "name": f"{event_name}"}
#     counter += 1
#
# print(events_dict)
# driver.quit()
"############################################"
"----------------------------------------------------------------------------------------------------------------------"

chrome_driver_path = Service("C:/Users/Barnaby's Pc/Development/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)
driver.maximize_window()
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, 'cookie')
counter = 0
game_prices = []

shop = driver.find_element(By.ID, 'store')  # gets all items in shop
upgrade = shop.find_elements(By.CSS_SELECTOR, 'div')  # gets all elements in upgrade
for item in upgrade[1:len(upgrade) - 1]:
    name = item.find_element(By.CSS_SELECTOR, 'b').text.split()[0]
    game_prices.append(f"buy{name}")

for n in range(1000000000):
    cookie.click()
    microsecond = datetime.datetime.now().microsecond
    if microsecond <= 12000:
        counter += 1
        if counter % 5 == 0 and counter > 0:
            for item in reversed(game_prices):
                try:
                    button = shop.find_element(By.ID, f"{item}")
                    # button.click()
                except NoSuchElementException or StaleElementReferenceException:
                    pass
                except NoSuchElementException and StaleElementReferenceException:
                    pass
                # If anything breaks it is due to below 'else':
                else:
                    try:
                        available = int(button.find_element(By.CLASS_NAME, 'amount').text)
                    except NoSuchElementException or StaleElementReferenceException:
                        available = 0
                    except NoSuchElementException and StaleElementReferenceException:
                        available = 0
                    if available < 15:
                        try:
                            button.click()
                        except NoSuchElementException or StaleElementReferenceException:
                            pass
                        except NoSuchElementException and StaleElementReferenceException:
                            pass
        if counter >= 300:
            break

driver.quit()
with open("score_tracker.txt", "a") as data:
    file = data.write(f"Score in 5 minutes is: {driver.find_element(By.ID, 'money').text} "
                      f"with {driver.find_element(By.ID, 'cps').text} cookies per second!\n")
