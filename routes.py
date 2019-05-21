from flask import Flask, url_for, render_template, flash, redirect
from config import Config
from forms import LoginForm

app = Flask(__name__)
app.config.from_object(Config)

#能够将函数绑定到对应的URL上
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : 'Jack'}
    posts = [
            {
                    'author': {'nickname' : 'John'},
                    'body' : 'Beautiful day!'
            },
            {
                    'author' : { 'nickname' : 'Fingal'},
                    'body' : 'The man in UCB'
            }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # 执行检验工作，通过后返回True
    if form.validate_on_submit():
        # flash会存储消息
        flash('Login requested for user {}, remeber_me = {}'.format(
			form.username.data, form.remeber_me.data
		))
        # 重定向
        return redirect(url_for('index'))
    return render_template('login.html', 
                title = 'Sign In',
                form = form)

if __name__ == '__main__':
        app.run(debug=True)
