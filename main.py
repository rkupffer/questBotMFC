# automated form filler for mfc questionnaires (triplets, full ranking) using selenium
import random
import sys
import time
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver import ActionChains

# webdriver configurations
# initialization of class chromeOptions and set path to google chrome
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
options.add_argument("window-size=1000x1000")

# initialization of class Chrome and set questionnaire url
quest_file = open("link2questionnaire.txt", "r")
chrome = webdriver.Chrome(options=options)
chrome.get(url = quest_file.readline())

# questionnaire -----------------------------------------------------------------------------------------------------
chrome.find_element("name", "submitNext").click()

time.sleep(1)

def dragdrop(page, item, rank):
    start = chrome.find_element("id", "BT" + page + "_0" + item + "Tkn")
    end = chrome.find_element("id", "rankingBT" + page + "Tgt" + rank)
    rand_pause = random.uniform(0.5, 3)
    ActionChains(chrome).click_and_hold(start).pause(rand_pause).move_to_element(end).release().perform()


all_ranks = ["1", "2", "3"]
all_items = ["1", "2", "3"]
quest_pages = ["01", "02", "03", "04", "05", "06"]
p = 0

while p < len(quest_pages):
    time.sleep(0.5)
    sampled_rank = random.sample(all_ranks, 3)
    sampled_item = random.sample(all_items, 3)
    for i in range(len(all_items)):
        dragdrop(quest_pages[p], sampled_item[i], sampled_rank[i])
        rand_pause_between_items = random.uniform(0.5, 3)
        time.sleep(rand_pause_between_items)
    chrome.find_element("name", "submitNext").click()
    p += 1


chrome.close()
sys.exit()
