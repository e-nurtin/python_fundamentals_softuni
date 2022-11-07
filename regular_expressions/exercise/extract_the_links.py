import re

# pattern = r"w{3}.[a-zA-Z0-9\-]+\.[a-z]+[\.a-z]*"
pattern = r"((w{3}\.[A-Za-z0-9\-]+\.)([a-z]+([\.][a-z]+)*))"
text = input()

while text:

    web_site = re.search(pattern, text)

    if web_site:
        print(web_site.group(0))

    text = input()
