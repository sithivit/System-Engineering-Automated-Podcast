from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver service
service = Service('C:\\Users\\User\\PycharmProjects\\podcastAI\\System-Engineering-Automated-Podcast\\chrome\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Open the webpage
driver.get('https://app.podscribe.ai/series/2162?allEpisodes=1')
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.jss392 > div > a'))
    )
    links_elements = driver.find_elements(By.CSS_SELECTOR, 'div.jss392 > div > a')
    links = [element.get_attribute('href') for element in links_elements]
    for link in links:
        print(link)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()