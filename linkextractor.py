#!/usr/bin/env python

import requests
import json

def extract_links(lmt=8):
    apikey = "LIVDSRZULELA"
    search_term = "excited"
    r = requests.get("https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))
    links = []
    xx = 0
    if r.status_code == 200:
        top_8gifs = json.loads(r.content)
        for x in range (10000):
            for x in range(len(top_8gifs['results'])):
                links.append({
                    "text": top_8gifs['results'][x]['id'],
                    "href": top_8gifs['results'][x]['media'][0]['webm']['preview']
            })
    return links

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\nUsage:\n\t{} <URL>\n".format(sys.argv[0]))
        sys.exit(1)
    for link in extract_links(sys.argv[-1]):
        print("[{}]({})".format(link["text"], link["href"]))
