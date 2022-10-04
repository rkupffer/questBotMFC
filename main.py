# automated form filler for mfc questionnaires (triplets, full ranking) using selenium
import random
import sys
import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver import ActionChains

# webdriver configurations
# initialization of class chromeOptions and set path to google chrome
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
options.add_argument("window-size=700x700")

# initialization of class Chrome and set questionnaire url
quest_file = open("link2questionnaire.txt", "r")
chrome = webdriver.Chrome(options=options)
chrome.get(url = quest_file.readline())

# create sample of n = X bot responses ------------------------------------------------------------------------------
r = 0
while r < 10:
    # questionnaire -------------------------------------------------------------------------------------------------
    time.sleep(1)
    chrome.find_element("name", "submitNext").click()

    time.sleep(1)

    def dragdrop(page, item, rank):
        start = chrome.find_element("id", "BT" + page + "_0" + item + "Tkn")
        end = chrome.find_element("id", "rankingBT" + page + "Tgt" + rank)
        rand_pause = random.uniform(0.5, 6)
        ActionChains(chrome).click_and_hold(start).pause(rand_pause).move_to_element(end).release().perform()


    all_ranks = ["1", "2", "3"]
    all_items = ["1", "2", "3"]
    quest_pages = ["02", "01", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
                   "18", "19", "20", "21"]
    p = 0
    while p < len(quest_pages):
        for page in quest_pages:
            try:
                sampled_rank = random.sample(all_ranks, 3)
                sampled_item = random.sample(all_items, 3)
                for i in range(len(all_items)):
                    dragdrop(page, sampled_item[i], sampled_rank[i])
                    rand_pause_between_items = random.uniform(0.5, 6)
                    time.sleep(rand_pause_between_items)
                chrome.find_element("name", "submitNext").click()
            except selenium.common.exceptions.NoSuchElementException:
                pass
        p += 1

    chrome.close()
    sys.exit()

r += 1

