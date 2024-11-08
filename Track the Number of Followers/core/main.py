from PlaywrightDriver import PlaywrightDriver
from core import FollowersTracker
import GoogleFormsSubmitter
import time as t

def run_scraper():
    driver = PlaywrightDriver(cookies_file='cookies.json')
    context = driver.initialize_driver()

    tracker = FollowersTracker(
        context,
        r'input files/accounts.xlsx',
        r'input files/pages.xlsx',
        r'input files/Newstellers.xlsx',
        r'input files/Youtube.xlsx',
        r'input files/Instagram.xlsx',
        r'input files/X.xlsx'  
    )

    followers_data = tracker.scrap_info()
    print("Followers Data:", followers_data)

    form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSeK_A8x_7ipnICGwK3k3MdTq3vGhXwfu9BhSz37Bgz27T1llw/formResponse'
    
    form_fields = {
        'Business Infographics': 'entry.627780398',
        'Nicolas Boucher Online': 'entry.1247179473',
        'AI Finance Club': 'entry.1150066733',
        'Nicolas Boucher Personal Account': 'entry.269674828',
        'AI + Finance by Nicolas Boucher Newsteller': 'entry.508828894',
        'Nicolas Boucher Online Videos | YouTube Subscribers': 'entry.114799247',
        'Nicolas Boucher Online Videos | YouTube Total Views': 'entry.1433952907',
        'Instagram Total Followers': 'entry.147129590',
        'X Total Number of Followers': 'entry.121881511',  
        'X Followers Last 30 Days': 'entry.1810313943',   
        'X Followers Last 30 Days Percentage': 'entry.1647920330'  
    }

    mapped_data = {
        'Business Infographics': followers_data[0],
        'Nicolas Boucher Online': followers_data[1],
        'AI Finance Club': followers_data[2],
        'Nicolas Boucher Personal Account': followers_data[3],
        'AI + Finance by Nicolas Boucher Newsteller': followers_data[4],
        'Nicolas Boucher Online Videos | YouTube Subscribers': followers_data[5]['subscribers'],
        'Nicolas Boucher Online Videos | YouTube Total Views': followers_data[5]['views'],
        'Instagram Total Followers': followers_data[6],
        'X Total Number of Followers': followers_data[7].get('followers', 'Not Found'),  
        'X Followers Last 30 Days': followers_data[7].get('last_30_days_growth', 'Not Found'),  
        'X Followers Last 30 Days Percentage': followers_data[7].get('Growth Percentage', 'Not Found')  
    }


    form_submitter = GoogleFormsSubmitter.GoogleFormsSubmitter(form_url, form_fields)
    form_submitter.submit_data(mapped_data)

    driver.close(context)

while True:
    run_scraper()
    t.sleep(60 * 60 * 6)
