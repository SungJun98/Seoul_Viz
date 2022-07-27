# -*- coding: utf-8 -*-
import argparse

from instagram_crawler import utils_mine, extract_mine # 이름 바꾸기 나중에!!


parser = argparse.ArgumentParser(description="Crawling Instgram Post")
parser.add_argument("--driver_path", 
                    help="selenium chrome driver path", 
                    required=True, type=str)

parser.add_argument("--id", 
                    help="instagramk id", 
                    required=True, type=str)

parser.add_argument("--password", 
                    help="instagram password", 
                    required=True, type=str)

parser.add_argument("--hash_tag", 
                    help="The hashtag want to extract.", 
                    required=True, type=str)

parser.add_argument("--extract_num", 
                    help="The number of posts want to extract.", 
                    default=50, type=int)


parser.add_argument("--mount",
                    help="changing part of CSS Selector",
                    require=True, type=str)
'''
parser.add_argument("--location_selector",
                    help="CSS selector about location data", 
                    required=True, type=str)

parser.add_argument("--date_selector",
                    help="CSS selector about date data", 
                    required=True, type=str)

parser.add_argument("--text_selector",
                    help="CSS selector about main text data", 
                    required=True, type=str)

parser.add_argument("--next_arrow_selector",
                    help="CSS selector about next arrow button", 
                    required=True, type=str)
'''

parser.add_argument("--save_path", 
                    help="path to save extracted data as csv", 
                    required=True, type=str)

parser.add_argument("--extract_file_name",
                    help="extract file name", 
                    default="extracted_main", type=str)

parser.add_argument("--extract_tag_file_name",
                    help="set extract tag file name", 
                    default="extracted_tag", type=str)


args = parser.parse_args()


'''
mount를 알아내는 방법에 대해 고민이 필요하다
방안 1.
인자로 받는게 아니라 로그인 후 첫 사진 클릭 한 후에
mount에 해당하는 걸 뽑아내면 되는거 아니야?!
근데 그 값을 어떻게 copy를 하느냐가 문제다.......

방안2.
로그인 후 첫 사진 클릭 하는 작업까지 원 스텝
mount에 해당하는 값 뽑아서 argument로 넣은 다음 crawling하는 과정 투 스텝
이렇게 py 파일을 나눠서 실행해볼까..?
'''
if __name__="__main__":
    utils_mine.open_web(args.driver_path)
    utils_mine.login(args.user_id, args.user_password)
    utils_mine.insta_search(args.driver, args.hash_tag)
    utils_mine.select_frist(args.driver)
    utils_mine.making_css_selector(args.mount)
    extract_mine.crawling_instgram(args.driver, args.extract_num, args.mount,
                          args.save_path, args.save_file_name, args.save_tag_file_name,)