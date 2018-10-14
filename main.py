from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:root@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id =    db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body =  db.Column(db.String(1200))

    def __init__(self, name, body):
        self.name = name
        self.body = body


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        new_title = request.form['title']
        new_body = request.form['body']
        new_blog = Blog(new_title, new_body)
        db.session.add(new_blog)
        db.session.commit()

    blogs = Blog.query.all()
    # completed_tasks = Task.query.filter_by(completed=True).all()
    return render_template('blogs.html',title="Build a Blog!", 
        blogs=blogs)


@app.route('/blog', methods=['POST'])
def blog():

    blog_id = int(request.form['blog-id'])
    blog = Blog.query.get(blog_id)
    title = Blog.query.get('title')
    body = Blog.query.get('body')    

    # task.completed = True
    db.session.add(blog)
    db.session.commit()

    return redirect('/')

@app.route('/newpost', methods=['POST'])
def new_post():

    # task.completed = True
    db.session.add(blog)
    db.session.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run(port=5001)