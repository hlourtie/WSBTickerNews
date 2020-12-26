from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=options)
for x in range(len(sys.argv)):
	if x == 0:
		continue
	driver.get('https://www.reddit.com/r/wallstreetbets/search?q='+sys.argv[x]+'&restrict_sr=1&sort=new')
	posts = driver.find_elements_by_xpath('//div[contains(@class,"scrollerItem")]')
	titles = []
	links = []
	flairs = []
	print("\nPosts for "+ sys.argv[x])
	for post in posts:
		titles.append(post.find_element_by_xpath('.//h3[contains(@class,"_eYtD2XCVieq6emjKBH3m")]').text)
		links.append(post.find_element_by_xpath('.//a[contains(@class,"SQnoC3ObvgnGjWt90zD9Z")]').get_attribute(name="href"))
		try:
			flairs.append(post.find_element_by_xpath('.//div[contains(@class,"_2X6EB3ZhEeXCh1eIVA64XM")]').text)
		except:
			flairs.append("No Flairs")
	if  len(titles) == 0 :
		print("No articles here")
	for i in range(len(titles)):
		print("----")
		print(titles[i])
		text = "The link: "
		target = links[i]
		print(f"\u001b]8;;{target}\u001b\\{text}\u001b]8;;\u001b\\" + target)
		print(flairs[i])
		print("----\n")
driver.quit()