import requests

data = []
indata = []

url = "https://clist.by"

resp = requests.get(url).content

#print(resp)

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


#def crawl_page(seed, max_depth):
#    tocrawl = [seed]
#    crawled = []
#    while tocrawl:
#        page = tocrawl.pop()
#        if page not in crawled:
#            union(tocrawl, get_all_contest(get_page(resp)))
#            crawled.append(page)
#    return crawled

print(get_all_contest(resp))
