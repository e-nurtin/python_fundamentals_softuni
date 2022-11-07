title = input()
article_content = input()

print(f"<h1>\n    {title}\n</h1>")
print(f"<article>\n    {article_content}\n</article>")

comments = input()
while comments != "end of comments":
    print(f"<div>\n    {comments}\n</div>")
    comments = input()
