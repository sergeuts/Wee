from bs4 import BeautifulSoup  # pip install beautifulsoup4
import requests  # pip install requests
from time import sleep
import csv
import pickle


# from app_projects_list.parsing import parse_files
# import app_projects_list.parsing as p

pickle_file_name = r"C:\it\Projects\WeeDeal\parse\pickle.txt"
result_file_name_csv = r"C:\it\Projects\WeeDeal\parse\result.csv"
# cb - common block in html profile
cb_begin = r'/html/body/div/div/div[3]/div/'
cb_txt = 'bs.html.body.div.div.div.find_next_sibling("div").div'
cb_txt = 'bs.html.body.div.div.div.find_next_sibling("div").find_next_sibling("div").div'
fields_xpath = {
    #'id': '',
    'name':     'div[1]/div/div/div[3]/div[1]/div[1]/h1',
    'location': 'div[1]/div/div/div[3]/div[2]/span',
    'pro user': 'div[1]/div/div/div[3]/div[1]/div[2]',
    'rating':   'div[1]/div/div/div[3]/div[3]/h3',
    #'industry': 'div[2]/div/div[2]/div[2]/div',
    #'startup_stage':    'div[2]/div/div[3]/div[2]/div',
    'site link':        'div[2]/div/div[4]/div[2]/div/a',
    #'why you are good': 'div[3]/div/div[2]/div[2]/div/div/p',
    #'description':      'div[3]/div/div[3]/div[2]/div/div/p',
    #'idea_stage':       'div[3]/div/div[4]/div[2]/div',
    #'your skills':      'div[3]/div/div[6]/div[2]/div',
    #'skills needed':    'div[3]/div/div[7]/div[2]/div/div/div',
    #'availability':     'div[3]/div/div[8]/div[2]/div',
    #'photo_url': 'div[1]/div/div/div[2]/div/div/div/span/img',
}
cb = ''
fields = {}
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'content_type': 'text/html; charset=UTF-8',
            'GET': 'https://www.starthawk.io/find-a-co-founder/ HTTP/2',
            'Host': 'https://www.starthawk.io/find-a-co-founder/',
            'accept-encoding': 'gzip, deflate, br'
            }


def init_fields():
    global fields
    fields = {k: get_field_cmd(v) for k, v in fields_xpath.items()}

    print(fields)


def get_soup_cmd(xp):
    if xp == '':
        return ''
    if xp[0] == r'/':
        xp = xp[1:]
    tag_list = xp.split(r'/')
    cmd_str = ''
    for i in tag_list:
        if i.endswith(']'):
            inx = i.rfind('[')
            # print('get_soup_cmd, line 7 (40)', xp, i) # debug
            n = int(i[inx + 1:-1])
            cur_cmd = i[:inx]
            cmd_str += '.' + cur_cmd
            # for j in range(1,n):
            #    cmd_str += '.find_next_sibling("' + cur_cmd + '")'
            cmd_str += ('.find_next_sibling("' + cur_cmd + '")') * (n - 1)
        else:
            cmd_str += '.' + i
    if cmd_str[0] == '.': cmd_str = cmd_str[1:]
    return cmd_str


def get_field(link):
    if link.startswith(cb_begin):
        link = link[len(cb_begin):]
    return eval('cb.' + get_soup_cmd(link) + '.text.strip()')


def get_field_cmd(link):
    #if not link.startswith(cb_begin):
    #    link = cb_txt + link
    return 'cb.' + get_soup_cmd(link) + '.text.strip()'


def get_html(url):
    #h = requests.get(url, headers, params=None)
    h = requests.get(url)
    # print(h)
    if not h.status_code == 200:
        print('--------------- Error loading html')
        return '--------------- Error loading html'
    return h.text[h.text.find('<html>'):-1]

def parse():
    # profile_file_name_html = r"C:\it\Projects\WeeDeal\parse\Lincoln's profile.html"
    # links_file_name_html = r"C:\it\Projects\WeeDeal\parse\Find a Co-founder Online _ App to Find Business Partners.html"
    #
    # html_file = open(links_file_name_html, 'r', encoding='UTF-8')
    # html = html_file.read()
    # html_file.close()

    link_list = r'https://www.starthawk.io/find-a-co-founder/page-'
    link_list_max_number = 10  # 714
    link_profile = r'https://www.starthawk.io/profile/'

    working = True
    current_page_number = 1
    result = []
    while working:
        current_page_link = link_list + str(current_page_number)
        html_links = get_html(current_page_link)
        if html_links == '':
            print(f'Page {current_page_link} not found')
            break
        bs = BeautifulSoup(html_links, 'html.parser')
        links = bs.find_all(attrs={"class": 'user-tile__first-name__link'})
        for li in links:
            profile_id = li.attrs['href'][9:]
            current_profile_link = link_profile + profile_id
            html_profile = get_html(current_profile_link)
            sleep(1)
            profile = parse_profile(id=profile_id, html=html_profile)
            result.append(profile)

        if current_page_number == link_list_max_number:
            working = False
        current_page_number += 1
    save_file_csv(result, result_file_name_csv)

    with open(pickle_file_name, 'wb') as file:
        pickle.dump(result, file)
##    with open('f_res', 'rb') as file: res1 = pickle.load(file)



def save_file_csv(res, file_name):
    with open(file_name, 'w', encoding='utf8', newline='') as file:
        writer = csv.writer(file, delimiter='|')  # ;
        if not res:
            writer.writerow([])
            file.close()
            return
        for item in res:
            writer.writerow(item)
    file.close()

def parse_profile(id, html):
    #bs = BeautifulSoup(html, 'html.parser')
    #cb = eval(cb_txt)
    #f_values = {k: eval(v) for k, v in fields.items()}
    f_values = {}
    for k, v in fields.items():
        try:
            print(id, k, '-->', eval(v))
            f_values[k] = eval(v)
        except AttributeError:
            print(AttributeError)
    a = 1
    fields2 = [
        [['name'], 'class', 'heading heading--personal-details-first-name', '.h1.text.strip()'],
        [['location'], 'class', 'personal-details__location', '.span.text.strip()'],
        [['rating'], 'class', 'personal-details__points', '.h3.text.strip()'],
        [['why you are good', 'description'], 'class', 'text-area__static__value', ['join_str_p', '']],
        [['startup_stage', 'industry', 'availability'], 'class', 'select-dropdown__static__value', '.text.strip()'],
        [['website'], 'rel', 'noopener noreferrer', '.text.strip()'],
        [['your skills', 'skills needed'], 'class', 'multi-select__static', ['join_str_p', ', ']],
        #[['photo url'], 'alt', 'user'],
    ]
    rel = "noopener noreferrer"
    for field_names, attr, at_value, cmd in fields2:
        res = cb.find_all(attrs={attr: at_value})
        if not res:
            for field in field_names:
                f_values[field] = ''
        elif type(cmd) != list:
            if len(res) > len(field_names):
                res = res[-len(field_names):]
            elif len(res) < len(field_names):
                print(f'Недостаточно данных для заполнения полей {res=} {field_names=}')
            for i, fn in enumerate(field_names):
                try:
                    f_values[fn] = eval('res[i]' + cmd)
                except AttributeError:
                    print(AttributeError)
        elif type(cmd) == list and cmd[0] == 'join_str': # не используется
            for i_, fn_ in enumerate(res):
                res2 = fn_.find_all(attrs={cmd[1]: cmd[2]})
        elif type(cmd) == list and cmd[0] == 'join_str_p':
            for i, field in enumerate(field_names):
                res2 = []
                for s in res[i]:
                    try:
                        res2.append(s.text.strip())
                    except AttributeError:
                        print(AttributeError)
                f_values[field] = cmd[1].join(res2)
    f_values['id'] = id
    if f_values.get('pro user', None) is None:
        f_values['pro user'] = False
    else:
        f_values['pro user'] = True if f_values['pro user'] == 'Pro user' else False
    if 'photo_url' in fields and fields['photo_url']:
        tag = str(eval('cb.' + get_soup_cmd(fields['photo_url'])))
        find_url = tag.find('url(')
        if find_url > -1:
            url_start, url_end = find_url+4, tag.find(')', find_url)
            f_values['photo_url'] = tag[url_start:url_end]
    if f_values.get('rating', None) is None:
        f_values['rating'] = 0
    else:
        if f_values['rating'].startswith('Reputation points'):
            f_values['rating'] = int(f_values['rating'][18:])

    return f_values


def parse_files(files=[]):
    from os import listdir
    path = r"C:\it\Projects\WeeDeal\parse"
    if not files:
        files = [f for f in listdir(path) if len(f) == 30 and f.endswith('.html')]
    if not files:
        return []
    result = []

    for file in files:
        html_file = open(path + '\\' + file, 'r', encoding='UTF-8')
        html = html_file.read()
        html_file.close()

        global bs
        bs = BeautifulSoup(html, 'html.parser')
        global cb
        cb = bs.find_all(attrs={"class": 'profile profile--not-owner'})
        if len(cb) == 1:
            cb = cb[0]
        else:
            print('Ошибка len(cb) == ', len(cb))

        profile = parse_profile(file[:-5], html)
        result.append([*profile.values()])

    result2 = result.copy()
    result2.insert(0, [*profile.keys()])
    save_file_csv(result2, result_file_name_csv)

    with open(pickle_file_name, 'wb') as file:
        pickle.dump(result, file)


def reduce_time(t1, t2):
    m1, s1, m2, s2 = map(int, t1.split(':') + t2.split(':'))
    return f'{m1+m2}:{s1+s2}'


def get_youtube_pl():
    html_file = open(r"C:\it\Projects\WeeDeal\parse\Django уроки - YouTube.html", 'r', encoding='UTF-8')
    html = html_file.read()
    html_file.close()
    # from bs4 import BeautifulSoup
    bs = BeautifulSoup(html, 'html.parser')

    playlist = bs.find_all(attrs={'id': 'playlist', 'class': 'style-scope ytd-watch-flexy'})
    times = playlist[0].find_all(attrs={'id': 'text', 'class': 'style-scope ytd-thumbnail-overlay-time-status-renderer'})
    tt = [t.text.strip() for t in times]
    from functools import reduce


init_fields()
#parse_files(['ckzqjd7m40uku075577y6l1im.html', 'ckznqj4gm1f640710eaydnaj9.html'])
parse_files()
