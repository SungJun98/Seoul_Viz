# -*- coding: utf-8 -*-
import time, re
from selenium import webdriver
import random, os
import pandas as pd

def make_radom_sleep_time(start, end):
    return random.randrange(start=start, stop=end+1)

def open_web(driver_path, url='https://www.instagram.com'):
    driver = webdriver.Chrome(driver_path)
    driver.get(url)
    time.sleep(10)




def login(user_id, user_password):
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

    # Save the log of Log-in
    try:
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
    except:
        pass


def insta_search(driver, hash_tag):
    try:
       hash_tag_url = url = 'https://www.instagram.com/explore/tags/' + hash_tag
       driver.get(hash_tag_url)
       time.sleep(10)
   except:
       pass

def select_first(driver):
    first = driver.find_element_by_css_selector('div._aagw')
    first.click()
    time.sleep(5)



def making_css_selector(mount):
    loc_sel = '#mount_0_0_' + mount + ' > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div.pi61vmqs.od1n8kyl.h6an9nv3.j4yusqav.djyw54ux.c9k30104.rxghi256.jhx0qe0y.mbxd2wpa.hb7lyos6.rfyvs5rk.sspdcydq.n34oi56o.c3wyshyw.im6prb7w.kzdz7bm1.k01ojvdi.alxbew3a.t78t6opn > div > article > div > div._aata > div > div > div._aasx > div._aat8 > div > div > a > div > time'
    date_sel = '#mount_0_0_' + mount + ' > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div.pi61vmqs.od1n8kyl.h6an9nv3.j4yusqav.djyw54ux.c9k30104.rxghi256.jhx0qe0y.mbxd2wpa.hb7lyos6.rfyvs5rk.sspdcydq.n34oi56o.c3wyshyw.im6prb7w.kzdz7bm1.k01ojvdi.alxbew3a.t78t6opn > div > article > div > div._aata > div > div > div._aasx > div._aat8 > div > div > a > div > time'
    main_sel = '#mount_0_0_' + mount + ' > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div.pi61vmqs.od1n8kyl.h6an9nv3.j4yusqav.djyw54ux.c9k30104.rxghi256.jhx0qe0y.mbxd2wpa.hb7lyos6.rfyvs5rk.sspdcydq.n34oi56o.c3wyshyw.im6prb7w.kzdz7bm1.k01ojvdi.alxbew3a.t78t6opn > div > article > div > div._aata > div > div > div._aasx > div._aat6 > ul > div > li > div > div > div._a9zr > div._a9zs'
    next_arrow_sel = '#mount_0_0' + mount + ' > div > div:nth-child(1) > div > div:nth-child(4) > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div._a3gq._ab-1 > div > div > div._aaqg._aaqh > button > div'
    
    return loc_sel=loc_sel, date_sel=date_sel, main_sel=main_sel, next_arrow_sel=next_arrow_sel
    
    


def save_extract_data_to_csv_file(location_infos, location_hrefs, 
                                  date_times, date_titles, main_texts, save_path, save_file_name):
    os.chdir(save_path)
    try:
        insta_info_df = pd.DataFrame(
            {"location_info": location_infos, "location_href": location_hrefs,
             "date_time": date_times, "date_title": date_titles, "main_text": main_texts,})
        insta_info_df.to_csv("{}.csv".format(save_file_name), index=True)
    except:
        print("Fail to save extract data to csv file")


def save_extract_tag_data_to_csv_file(instagram_tags, save_path, save_file_name_tag):
    
    os.chdir(save_path)
    try:
        insta_tag_df = pd.DataFrame({"tag": instagram_tags})
        insta_tag_df.to_csv("{}.csv".format(save_file_name_tag), index=True)
    except:
        print("Fail to save extract tag data to csv file")