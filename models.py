from app.routes import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    # 哈希值存密码提高安全性
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default= datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
