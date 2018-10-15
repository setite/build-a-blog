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

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/', methods=['POST', 'GET'])
def index():

    blogs = Blog.query.all()
    # completed_tasks = Task.query.filter_by(completed=True).all()
    return render_template('blogs.html',title="Build a Blog!", 
        blogs=blogs)


@app.route('/blog/')
def blog():

    blog_id = request.args.get('id')
    # blog_id = Blog.query.get(blog.id)
    blog = Blog.query.get(blog_id)
    title = blog.title
    body = blog.body
    return render_template('blog_entry.html', title=title, body=body)
    
    # new_blog = Blog(new_title, new_body)
    # return render_template('single_entry.html', title="Blog Entry", entry=entry)   

    # task.completed = True
    # db.session.add(blog)
    # db.session.commit()

    # return redirect('/')

@app.route('/newpost/', methods=['GET', 'POST'])
def new_post():
    
    if request.method == 'POST':
        new_title = request.form['title']
        new_body = request.form['body']
        new_blog = Blog(new_title, new_body)
 
        db.session.add(new_blog)
        db.session.commit()
       
        url = "/blog?id=" + str(new_blog.id)
        return redirect(url)
        # return render_template('blog_entry.html', title=blog.title, body=blog.body)

    else:
        return render_template('newpost.html', title="Build a Blog!")

if __name__ == '__main__':
    app.run(debug=True)
