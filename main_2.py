import time
from selenium import webdriver
from selenium.webdriver.common.by import By

google_forms_url = "<your forms URL>"

san_francisco_link = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A" \
                            "%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.88159201281336%2C%22east%22%3A-122" \
                            ".23248568896484%2C%22south%22%3A37.66883883415068%2C%22west%22%3A-122.63417331103516%7D" \
                            "%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22" \
                            "%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B" \
                            "%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22" \
                            "%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D" \
                            "%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C" \
                            "%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C" \
                            "%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"

# driver = webdriver.Firefox()
# driver.get(san_francisco_link)
#
# time.sleep(10)

# property_price = driver.find_elements(By.CLASS_NAME, "bqsBln")
# price_list = []
# for i in property_price:
#     price_list.append(i.text)


price_list = ['$2,750+ 1 bd', '$2,549+ 1 bd', '$2,688/mo', '$2,445+ 1 bd', '$2,988/mo', '$2,499/mo',
              '$2,994/mo', '$2,698/mo', '$2,499+ 1 bd', '$2,963+ 1 bd', '$2,849/mo', '$2,599+ 1 bd',
              '$2,800+/mo', '$2,858+ 1 bd', '$2,984+ 1 bd', '$2,600+ 1 bd', '$2,810+ 1 bd', '$2,399+ 1 bd',
              '$2,145+ 1 bd', '$2,895/mo', '$2,900+ 1 bd', '$2,810+/mo', '$2,495+ 1 bd', '$2,895/mo', '$2,995/mo',
              '$2,450/mo', '$2,099+ 1 bd', '$2,427+ 1 bd', '$2,800+ 1 bd', '$2,797+ 1 bd', '$2,595/mo', '$2,495+ 1 bd',
              '$2,195+ 1 bd', '$2,095+ 1 bd', '$2,737+ 1 bd', '$2,245+/mo', '$2,836+ 1 bd', '$2,865+ 1 bd',
              '$2,574+ 1 bd', '$3,000+/mo']

# offer_links = driver.find_elements(By.CLASS_NAME, "property-card-link")
# for offer in offer_links:
#     offer_links_list.append(offer.get_attribute("href"))
#
# print(offer_links_list)
property_link_list = ['https://www.zillow.com/b/parkmerced-san-francisco-ca-5XjKHx/', 'https://www.zillow.com/b/1177-market-at-trinity-place-san-francisco-ca-BNjvdD/', 'https://www.zillow.com/b/modera-rincon-hill-san-francisco-ca-9NJzvD/', 'https://www.zillow.com/b/840-van-ness-san-francisco-ca-5YCwMj/', 'https://www.zillow.com/b/vance-san-francisco-ca-9NKJBx/', 'https://www.zillow.com/b/1190-mission-at-trinity-place-san-francisco-ca-5XjVtb/', 'https://www.zillow.com/b/1190-mission-at-trinity-place-san-francisco-ca-5XjVtb/', 'https://www.zillow.com/b/chorus-san-francisco-ca-9NJvt7/', 'https://www.zillow.com/b/1188-mission-at-trinity-place-san-francisco-ca-5XjN4q/', 'https://www.zillow.com/b/the-landing-san-francisco-ca-9NK3gC/', 'https://www.zillow.com/b/crystal-tower-apartments-san-francisco-ca-5XjVtt/', 'https://www.zillow.com/b/33-8th-at-trinity-place-san-francisco-ca-9NJw4S/', 'https://www.zillow.com/b/loft-168-san-francisco-ca-9NK42M/', 'https://www.zillow.com/b/edgewater-san-francisco-ca-5XjVQc/', 'https://www.zillow.com/b/923-folsom-san-francisco-ca-5Yy6Np/', 'https://www.zillow.com/b/952-sutter-st.-san-francisco-ca-5XjxLz/', 'https://www.zillow.com/b/astella-san-francisco-ca-9NJxqH/', 'https://www.zillow.com/b/2133-stockton-street-apartments-san-francisco-ca-5Xhzkj/', 'https://www.zillow.com/b/750-o%27farrell-st-san-francisco-ca-5YXpvZ/', 'https://www.zillow.com/b/1755-van-ness-ave-san-francisco-ca-5Xk3VN/', 'https://www.zillow.com/b/2000-post-san-francisco-ca-5XjRNn/', 'https://www.zillow.com/b/northpoint-apartments-san-francisco-ca-5XjLPJ/', 'https://www.zillow.com/b/mt.-sutro-san-francisco-ca-5XjVRC/', 'https://www.zillow.com/b/24-franklin-san-francisco-ca-9NJqFL/', 'https://www.zillow.com/b/1395-golden-gate-ave-san-francisco-ca-9NKqZX/', 'https://www.zillow.com/b/845-sutter-san-francisco-ca-5XkKMm/', 'https://www.zillow.com/b/trinity-towers-apartments-san-francisco-ca-5XjPdR/', 'https://www.zillow.com/b/the-terraces-san-francisco-ca-5XjVSb/', 'https://www.zillow.com/b/cheshill-on-mission-san-francisco-ca-BKTtQD/', 'https://www.zillow.com/b/potrero-1010-san-francisco-ca-65fB7S/', 'https://www.zillow.com/b/50-golden-gate-ave.-san-francisco-ca-5j4CFB/', 'https://www.zillow.com/b/lofts-at-seven-san-francisco-ca-5XmsgS/', 'https://www.zillow.com/b/245-leavenworth-st.-san-francisco-ca-5YzSCr/', 'https://www.zillow.com/b/970-geary-st-san-francisco-ca-5YDJ2Y/', 'https://www.zillow.com/b/soma-square-san-francisco-ca-5Xj2Yr/', 'https://www.zillow.com/b/575-o%27farrell-st-san-francisco-ca-5j4D5y/', 'https://www.zillow.com/b/nob-hill-place-san-francisco-ca-5XkKgw/', 'https://www.zillow.com/b/l-seven-san-francisco-ca-9NJtD7/', 'https://www.zillow.com/b/bennett-lofts-san-francisco-ca-5Xrcx6/', 'https://www.zillow.com/b/grosvenor-atrium-san-francisco-ca-5XjKR5/']

# addresses = driver.find_elements(By.TAG_NAME, "address")
# for address in addresses:
#     addresses_list.append(address.text)
#
# print(addresses_list)
addresses_list = ['Parkmerced | 3711 19th Ave, San Francisco, CA', '1177 Market at Trinity Place | 1177 Market St, San Francisco, CA', 'Modera Rincon Hill, 390 1st St #109, San Francisco, CA 94105', '840 Van Ness | 840 Van Ness Ave, San Francisco, CA', 'Vance, 830 Eddy St #603, San Francisco, CA 94109', '1190 Mission at Trinity Place, 1190 Mission St APT 1824, San Francisco, CA 94103', '1190 Mission at Trinity Place, 1190 Mission St APT 1302, San Francisco, CA 94103', 'Chorus, 30 Otis St #429, San Francisco, CA 94103', '1188 Mission at Trinity Place | 1188 Mission St, San Francisco, CA', 'The Landing | 1395 22nd St, San Francisco, CA', 'Crystal Tower Apartments, 2140 Taylor St APT 101, San Francisco, CA 94133', '33 8th at Trinity Place | 33 8th St, San Francisco, CA', 'Loft 168, 168 Bluxome St, San Francisco, CA 94107', 'Edgewater | 355 Berry St, San Francisco, CA', '923 Folsom | 923 Folsom St, San Francisco, CA', '952 Sutter St. | 952 Sutter St, San Francisco, CA', 'Astella | 975 Bryant St, San Francisco, CA', '2133 Stockton Street Apartments | 2133 Stockton St, San Francisco, CA', "750 O'Farrell St | 750 Ofarrell St, San Francisco, CA", '1755 Van Ness Ave, 1755 Van Ness Ave #201, San Francisco, CA 94109', '2000 Post | 2000 Post St, San Francisco, CA', 'NorthPoint Apartments, 2211 Stockton St, San Francisco, CA 94133', 'Mt. Sutro | 480 Warren Dr, San Francisco, CA', '24 Franklin, 24 Franklin St #701, San Francisco, CA 94102', '1395 Golden Gate Ave, 1395 Golden Gate Ave APT 207, San Francisco, CA 94115', '845 Sutter, 845 Sutter St APT 409, San Francisco, CA 94109', 'Trinity Towers Apartments | 888 Ofarrell St, San Francisco, CA', 'The Terraces | 1330 Bush St, San Francisco, CA', 'ChesHill on Mission | 33 Seneca Ave, San Francisco, CA', 'Potrero 1010 | 1010 16th St, San Francisco, CA', '50 Golden Gate Ave., 50 Golden Gate Ave APT 100, San Francisco, CA 94102', 'Lofts at Seven | 277 Golden Gate Ave, San Francisco, CA', '245 Leavenworth St. | 245 Leavenworth St, San Francisco, CA', '970 Geary St | 970 Geary St, San Francisco, CA', 'SoMa Square | 1 Saint Francis Pl, San Francisco, CA', "575 O'Farrell St, 575 Ofarrell St, San Francisco, CA 94102", 'Nob Hill Place | 1155 Jones St, San Francisco, CA', 'L Seven | 1222 Harrison St, San Francisco, CA', 'Bennett Lofts | 530 Brannan St, San Francisco, CA', 'Grosvenor Atrium, 1690 Broadway, San Francisco, CA 94123']


# generate the form entries in Google Forms, change class names if different in your form
for i in range(5):
    driver = webdriver.Firefox()
    driver.get(google_forms_url)

    time.sleep(1)

    all_input_fields = driver.find_elements(By.CLASS_NAME, "zHQkBf")

    # send property address info
    property_address_field = all_input_fields[0]
    property_address_field.click()
    property_address_field.send_keys(addresses_list[i])
    time.sleep(0.2)

    # send property price per month
    property_price_field = all_input_fields[1]
    property_price_field.click()
    property_price_field.send_keys(price_list[i])
    time.sleep(0.5)

    # send property link
    property_link_field = all_input_fields[2]
    property_link_field.click()
    property_link_field.send_keys(property_link_list[i])
    time.sleep(0.5)

    # submit results
    submit_button = driver.find_element(By.CLASS_NAME, "Fxmcue")
    submit_button.click()
    time.sleep(0.5)
    driver.quit()

