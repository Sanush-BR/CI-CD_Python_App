import os
from flask import Flask, render_template

app = Flask(__name__)

# Hardcoded blog posts
posts = [
    {'title': 'Welcome to My Blog', 'content': 'This is my first blog post!'},
    {'title': 'Another Post', 'content': 'Here is another interesting article.'},
    {'title': 'Flask is Fun', 'content': 'Flask makes web development simple and quick.'}
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    # app.run(port=8080 , debug=True)
    port = int(os.environ.get("PORT",8085))
    app.run(host="0.0.0.0",port=port , debug=True)
