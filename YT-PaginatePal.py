import json
import math

def generate_comment_html(comment):
    author = comment["author"]
    author_thumbnail = comment["author_thumbnail"]
    text = comment["text"]

    html = f'''
    <div class="comment">
        <img class="thumbnail" src="{author_thumbnail}" alt="{author}'s Thumbnail">
        <div class="comment-details">
            <span class="author">{author}</span>
            <p class="comment-text">{text}</p>
        </div>
    </div>
    '''
    return html

def generate_pagination(current_page, total_pages):
    prev_page = current_page - 1 if current_page > 1 else None
    next_page = current_page + 1 if current_page < total_pages else None

    pages = []
    for page in range(1, total_pages + 1):
        if page == current_page:
            pages.append(f'<a class="current" href="page{page}.html">{page}</a>')
        else:
            pages.append(f'<a href="page{page}.html">{page}</a>')

    prev_button = f'<a class="prev" href="page{prev_page}.html">Previous</a>' if prev_page is not None else ''
    next_button = f'<a class="next" href="page{next_page}.html">Next</a>' if next_page is not None else ''

    pagination = f'''
    <div class="pagination">
        {prev_button}
        {' '.join(pages)}
        {next_button}
    </div>
    '''

    return pagination

with open('test.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    comments = data["comments"]
    comments_per_page = 50
    total_pages = math.ceil(len(comments) / comments_per_page)

    for page_number in range(1, total_pages + 1):
        start_idx = (page_number - 1) * comments_per_page
        end_idx = min(start_idx + comments_per_page, len(comments))
        page_comments = comments[start_idx:end_idx]

        comments_html = ""
        for comment in page_comments:
            comments_html += generate_comment_html(comment)

        pagination = generate_pagination(page_number, total_pages)

        html_content = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    background-color: #333;
                    color: #fff;
                    font-family: Arial, sans-serif;
                }}
                .comment {{
                    display: flex;
                    margin-bottom: 20px;
                }}
                .thumbnail {{
                    width: 50px;
                    height: 50px;
                    border-radius: 50%;
                    margin-right: 10px;
                }}
                .comment-details {{
                    flex-grow: 1;
                }}
                .author {{
                    font-weight: bold;
                    margin-right: 5px;
                }}
                .comment-text {{
                    margin-top: 5px;
                }}
                .pagination {{
                    margin-top: 20px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }}
                .pagination a {{
                    color: #fff;
                    text-decoration: none;
                    padding: 5px 10px;
                    margin: 0 5px;
                    border: 1px solid #ccc;
                    border-radius: 3px;
                }}
                .pagination a.prev,
                .pagination a.next {{
                    background-color: #666;
                }}
                .pagination a.current {{
                    background-color: #444;
                    font-weight: bold;
                }}
                .pagination a:hover {{
                    background-color: #555;
                }}
            </style>
        </head>
        <body>
            {comments_html}
            {pagination}
        </body>
        </html>
        '''

        with open(f'page{page_number}.html', 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)
