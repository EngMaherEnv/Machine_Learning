# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 15:55:23 2021

@author: STC
"""

import requests

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename

download_file("https://cdn.artgrid.io/footage-hls/160266_720p.m3u8.mp4")

