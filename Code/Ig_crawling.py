#-*- coding: utf-8 -*-
import time, re
from selenium import webdriver
from bs4 import BeautifulSoup
import random, os
import pandas as pd

user_id="lsj9862" ; user_password="Slanjdi2553@"

driver = webdriver.Chrome(r'C:\Users\SungJunLim\Desktop\Lim\UOS\Side-Project\Seoul_Viz\Instagram_Crawler\chromedriver.exe')

url = 'https://www.instagram.com'

driver.get(url)
time.sleep(10)

################################################################################
# 로그인
################################################################################
try:
    input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
    input_id.clear()
    input_id.send_keys(user_id)
    
    input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
    input_pw.clear()
    input_pw.send_keys(user_password)
    
    input_pw.submit()
    time.sleep(5)
    
except:
    print("instagram login fail")

# 로그인 정보 저장
try:
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
except:
    pass
################################################################################


################################################################################
# 키워드 검색
################################################################################
def insta_search(word):
    url = 'https://www.instagram.com/explore/tags/' + word
    return url 

url = insta_search('서울핫플')
driver.get(url)
time.sleep(40)

def select_first(drive):
    first = driver.find_element_by_css_selector('div._aagw')
    first.click()
    time.sleep(5)

select_first(driver)
################################################################################

def making_css_selector(mount):
    loc_sel = '#mount_0_0_' + mount + ' > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div.pi61vmqs.od1n8kyl.h6an9nv3.j4yusqav.djyw54ux.c9k30104.rxghi256.jhx0qe0y.mbxd2wpa.hb7lyos6.rfyvs5rk.sspdcydq.n34oi56o.c3wyshyw.im6prb7w.kzdz7bm1.k01ojvdi.alxbew3a.t78t6opn > div > article > div > div._aata > div > div > div._aasx > div._aat8 > div > div > a > div > time'
    date_sel = '#mount_0_0_' + mount + ' > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div.pi61vmqs.od1n8kyl.h6an9nv3.j4yusqav.djyw54ux.c9k30104.rxghi256.jhx0qe0y.mbxd2wpa.hb7lyos6.rfyvs5rk.sspdcydq.n34oi56o.c3wyshyw.im6prb7w.kzdz7bm1.k01ojvdi.alxbew3a.t78t6opn > div > article > div > div._aata > div > div > div._aasx > div._aat8 > div > div > a > div > time'
    main_sel = '#mount_0_0_' + mount + ' > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div.pi61vmqs.od1n8kyl.h6an9nv3.j4yusqav.djyw54ux.c9k30104.rxghi256.jhx0qe0y.mbxd2wpa.hb7lyos6.rfyvs5rk.sspdcydq.n34oi56o.c3wyshyw.im6prb7w.kzdz7bm1.k01ojvdi.alxbew3a.t78t6opn > div > article > div > div._aata > div > div > div._aasx > div._aat6 > ul > div > li > div > div > div._a9zr > div._a9zs'
    next_arrow_sel = '#mount_0_0_' + mount + ' > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div._a3gq._ab-1 > div > div > div._aaqg._aaqh > button > div'
    return loc_sel, date_sel, main_sel, next_arrow_sel

loc_sel, date_sel, main_sel, next_arrow_sel = making_css_selector('Sm')

# 위치 정보
def get_location_data(driver):
    try:
        location_object = driver.find_element_by_css_selector(loc_sel)
        location_info = location_object.text
        location_href = location_object.get_attribute("href")
    except:
        location_info = None
        location_href = None

    return location_info, location_href


# 날짜 정보
def get_date_info(driver):
    try:
        date_object = driver.find_element_by_css_selector(date_sel)
        date_time = date_object.get_attribute("datetime")
        date_title = date_object.get_attribute("title")
    except:
        date_time = None
        date_title = None

    return date_time, date_title



# 본문 및 해시태그
def get_main_text(driver, instagram_tags):
    try:
        main_text_object = driver.find_element_by_css_selector(main_sel)
        main_text = main_text_object.text
    except:
        main_text = None

    try:
        data = driver.find_element_by_css_selector(main_sel)
        tag_raw = data.text
        tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)
        tag = ''.join(tags).replace("#", " ")

        tag_data = tag.split()

        for tag_one in tag_data:
            instagram_tags.append(tag_one)
    except:
        pass

    return main_text, instagram_tags



# 다음버튼 클릭
def click_next_arrow_button(driver):
    try:
        right= driver.find_element_by_css_selector(next_arrow_sel)
        right.click()
        time.sleep(5.0)
    except:
        pass



def save_extract_data_to_csv_file(location_infos, location_hrefs, 
                                  date_times, date_titles, main_texts, save_file_name):
    try:
        insta_info_df = pd.DataFrame(
            {"location_info": location_infos, "location_href": location_hrefs,
             "date_time": date_times, "daste_title": date_titles, "main_text": main_texts,})
        insta_info_df.to_csv("{}.csv".format(save_file_name), index=True)
    except:
        print("Fail to save extract data to csv file")


def save_extract_tag_data_to_csv_file(instagram_tags, save_file_name_tag):
    try:
        insta_tag_df = pd.DataFrame({"tag": instagram_tags})
        insta_tag_df.to_csv("{}.csv".format(save_file_name_tag), index=True)
    except:
        print("Fail to save extract tag data to csv file")


def make_radom_sleep_time(start, end):
    return random.randrange(start=start, stop=end+1)


################################################################################
# Crawling 실행
################################################################################
location_infos, location_hrefs = [], []
date_times, date_titles = [], []
main_texts, instagram_tags = [], []

driver_path = r'C:\Users\SungJunLim\Desktop\Lim\UOS\Side-Project\Seoul_Viz\Instagram_Crawler\chromedriver.exe'
save_file_name = r"C:\Users\SungJunLim\Desktop\Lim\UOS\Side-Project\Seoul_Viz\crawled_data\instagram\extracted_main"
save_tag_file_name = r"C:\Users\SungJunLim\Desktop\Lim\UOS\Side-Project\Seoul_Viz\crawled_data\instagram\extracted_tag"


count_extract_num = 0
wish_num = 200

while True:
    if count_extract_num > wish_num:
        break

    time.sleep(make_radom_sleep_time(start=5, end=9))

    location_info, location_href = get_location_data(driver=driver)

    date_time, date_title = get_date_info(driver=driver)

    main_text, instagram_tags = get_main_text(driver=driver, instagram_tags=instagram_tags)

    count_extract_num += 1

    location_infos.append(location_info)
    location_hrefs.append(location_href)
    date_times.append(date_time)
    date_titles.append(date_title)
    main_texts.append(main_text)

    time.sleep(make_radom_sleep_time(start=5, end=8))

    click_next_arrow_button(driver=driver)

save_extract_data_to_csv_file(location_infos=location_infos, location_hrefs=location_hrefs,
                             date_times=date_times, date_titles=date_titles,
                             main_texts=main_texts, save_file_name=save_file_name)

save_extract_tag_data_to_csv_file(instagram_tags=instagram_tags, save_file_name_tag=save_tag_file_name)

driver.close()
driver.quit()

