#!/usr/bin/python3

from datetime import datetime
import sys

def create_blog_post(title=""):
    file_date = datetime.now().strftime("%Y-%m-%d")
    file_name = file_date + "---" + title.replace(" ", "-") + ".md"
    print(file_name)
    try:
        file = open("content/posts/" + file_name, "x")
    except FileExistsError:
        print("Post already exists. Delete old post first to create a new one")
        exit(1)
    content_date = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    content_slug = title.lower().replace(" ", "-")
    content = f"""---
    title: {title}
    date: \"{content_date}\"
    template: \"post\"
    draft: false
    slug: {content_slug}
    category: \"\"
    description: \"\"
    socialImage: \"\"
    ---""".replace("    ", "")
    file.write(content)
    file.close()
    print("Post sucesfully created!")

if __name__ == '__main__':
    if len(sys.argv):
        create_blog_post(sys.argv[1])
    else:
        create_blog_post()

    
