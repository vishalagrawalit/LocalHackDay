import requests


data = {}


#param = {'/?username': 'harkirat155',
#         'api_key': '63b3040dd99d6820d23626e658843d9042ca638a'}


resp = requests.get('https://clist.by/').content

print(resp)

#if resp.status_code != 200:
    # This means something went wrong.
    #    raise ApiError('GET /api/v1/contest {}'.format(resp.status_code))
#    print('error')


#with open("data_file.json", "w") as write_file:
#    json.dump(resp, write_file)


def get_next_target(resp):
    start_link = resp.find('<div class="row contest')
    if start_link == -1:
        return None, 0
    start_quote = resp.find('::before', start_link) + 8
    end_quote = resp.find('::after', start_quote + 1)
    scontest = resp[start_quote + 1:end_quote]
    return scontest, end_quote


def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_contest(resp):
    contest = []
    while True:
        scontest, endpos = get_next_target(resp)
        if scontest:
            contest.append(scontest)
            resp = resp[endpos:]
        else:
            break
    return contest


def crawl_web(seed, max_depth):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled


