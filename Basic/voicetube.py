import selenium
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver 

def login():
    driver=webdriver.Chrome('./chromedriver')
    driver.get("https://tw.voicetube.com/")
    sleep(3)
    li=driver.find_elements_by_xpath('//*[@id="new_1"]/ul/li')
    hidden_text=[]
    for i in range(len(li)):
        link= driver.find_element_by_xpath("//*[@id='new_1']/ul/li["+str(i+1)+"]/div/div[2]/h5/a")
        action=ActionChains(driver)
        action.move_to_element(link).perform()
        caption=driver.find_elements_by_xpath("//*[@id='new_1']/ul/li["+str(i+1)+"]/div/div[2]/div")
        for j in range(len(caption)):
            if caption[j].get_attribute(name='class')=='tooltip fade top in':
                hidden_text.append(caption[j].text)
                #catch css property
                print('Color:',caption[j].value_of_css_property('color'))
                print('Size:',caption[j].value_of_css_property('font-size'))
    return hidden_text