# -*- coding: utf-8 -*-
import time, re
from instgram_crawler import utils_mine # 이름 나중에 바꾸기!!



    


# Crawling Location Data
def get_location_data(driver, loc_sel):
    try:
        location_object = driver.find_element_by_css_selector(loc_sel)
        location_info = location_object.text
        location_href = location_object.get_attribute("href")
    except:
        location_info = None
        location_href = None

    return location_info, location_href


# Crawling Date Date
def get_date_info(driver, date_sel):
    try:
        date_object = driver.find_element_by_css_selector(date_sel)
        date_time = date_object.get_attribute("datetime")
        date_title = date_object.get_attribute("title")
    except:
        date_time = None
        date_title = None

    return date_time, date_title


# Crawling Main Text Data
def get_main_text(driver, instagram_tags, main_sel):
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


# CLick next arrow for next post
def click_next_arrow_button(driver, next_arrow_sel):
    try:
        right= driver.find_element_by_css_selector(next_arrow_sel)
        right.click()
        time.sleep(5.0)
    except:
        pass
    
    
    
def crawling_instgram(driver, extract_num, mount,
                      save_path,save_file_name, save_tag_file_name,):
    location_infos, location_hrefs = [], []
    date_times, date_titles = [], []
    main_texts, instagram_tags = [], []


    count_extract_num = 0

    loc_sel, date_sel, main_sel, next_arrow_sel = utils_mine.making_css_selector(mount)

    while True:
        if count_extract_num > extract_num:
            break

        time.sleep(utils_mine.make_radom_sleep_time(start=5, end=9))

        location_info, location_href = get_location_data(driver, loc_sel)

        date_time, date_title = get_date_info(driver, date_sel)

        main_text, instagram_tags = get_main_text(driver, instagram_tags, main_sel)

        count_extract_num += 1

        location_infos.append(location_info)
        location_hrefs.append(location_href)
        date_times.append(date_time)
        date_titles.append(date_title)
        main_texts.append(main_text)

        time.sleep(utils_mine.make_radom_sleep_time(start=5, end=8))

        click_next_arrow_button(driver, next_arrow_sel)

    utils_mine.save_extract_data_to_csv_file(location_infos=location_infos, location_hrefs=location_hrefs,
                                             date_times=date_times, date_titles=date_titles, main_texts=main_texts,
                                             save_path=save_path, save_file_name=save_file_name)

    utils_mine.save_extract_tag_data_to_csv_file(instagram_tags=instagram_tags,
                                                 save_path=save_path, save_file_name_tag=save_tag_file_name)

    driver.close()

