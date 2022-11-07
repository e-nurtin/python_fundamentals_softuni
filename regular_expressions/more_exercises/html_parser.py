import re

text = input()

title_pattern = r"<title>(.+)</title>"
content_pattern = r"<body>(.+)</body>"
remove_tags = re.compile(r"<[^>]*>")
remove_newline = r"\\n|\\t"
remove_spaces = r"[ ]+"
remove_whitespace = r"\b.+\b"

result_title = re.search(title_pattern, text)
result_content = re.search(content_pattern, text)

content = re.sub(remove_tags, " ", result_content[0])
title = re.sub(remove_tags, " ", result_title[0])

content = re.sub(remove_newline, "", content).strip()
title = re.sub(remove_newline, "", title).strip()

content = re.sub(remove_spaces, " ", content).strip()
title = re.sub(remove_spaces, " ", title).strip()

print(f"Title: {title}")
print(f"Content: {content}")
