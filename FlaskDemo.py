from flask import Flask, render_template

app = Flask(__name__)


@app.route('/book/list')
def hello_world():
    books = [
        {
            "name": "三国演义",
            "author": "罗贯中",
            "price":100
        },
        {
            "name": "西游记",
            "author": "吴承恩",
            "price": 88
        },
        {
            "name": "红楼梦",
            "author": "曹雪芹",
            "price": 99
        },
        {
            "name": "水浒传",
            "author": "施耐庵",
            "price": 66
        }
    ]

    return render_template("index.html", books=books)


if __name__ == '__main__':
    app.run(debug=True)
