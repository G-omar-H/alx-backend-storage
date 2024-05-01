#!/usr/bin/env python3
""" Main file """

get_page = __import__('web').get_page



html_content = get_page('http://slowwly.robertomurray.co.uk')
print(html_content)
