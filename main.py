import time       
import csv      
import re         
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as CM

def main(url_maps): 
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")
    mobile_emulation = {
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(executable_path=CM().install(), options=options)
    driver.set_window_size(600, 700)    
    
    alamatURL = url_maps
    driver.get(alamatURL) 
    time.sleep(3)
    try:
        count = 0
        print(f"load all data..")
        while True:
            print(f"run infinite scrolling...{count}")
            count += 1
            last_review = driver.find_elements_by_css_selector('div[jsinstance="0"]')
            driver.execute_script('arguments[0].scrollIntoView(true);', last_review[count])
            time.sleep(0.8)
    except IndexError:
        print('finish load data')
 
    print('end scroll')
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    section = soup.find_all('div', {'jsinstance' : re.compile(r".*")})
    result = []
    re_nama_waktu = r'id="ml-reviews-page-user-review-name.\w*".jsan=".\w*.\w*,\d.\w*,\d.\w*".jstcache="\d*">\w* \w*<.div> <\w*.\w*="\w*" \w*="\d.\w*" jstcache="\d*">\d \w* \w*'
    re_rating = r'div aria-label="\w* \w*.\d'
    re_ulasan = f'<span class="\w*" jsan="\w.\w*" jstcache="\d*">[^<]*'
    for item in section:
        matches = re.search(re_nama_waktu, str(item), re.MULTILINE)
        matches_rating = re.search(re_rating, str(item), re.MULTILINE)
        matches_ulasan = re.search(re_ulasan, str(item), re.MULTILINE)
        if matches != None:
            raw = matches.group()
            raw_rating = matches_rating.group()
            raw_ulasan = matches_ulasan.group()

            nama = raw.split('>')[1].replace('</div', '')
            waktu = raw.split('>')[-1]
            rating = raw_rating.replace('div aria-label="Nilai dari ', '')
            ulasan = re.split(r'\d*">', raw_ulasan)[1]
            temp = {
                'nama': nama,
                'waktu': waktu,
                'rating': rating,
                'ulasan': ulasan
            }
            result.append(temp)
    # save to csv    
    keys = result[0].keys()
    with open(f'output.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(result)    
    print('finish')
    time.sleep(2)


if __name__ == '__main__':
    url_map = "https://www.google.com/maps/place/Pandawa+Beach/@-8.8448081,115.1865255,16z/data=!4m8!3m7!1s0x2dd25b7cd8ba1f31:0x41b8785dd055b2a4!8m2!3d-8.8452802!4d115.1870679!9m1!1b1!16s%2Fg%2F1ygbcghrt?entry=ttu"
    main(url_map)
