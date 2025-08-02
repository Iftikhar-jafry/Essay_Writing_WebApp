from flask import Flask , render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Writing_Essay.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Writing_Essay(db.Model):
    sno= db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    content=db.Column(db.String(2000), nullable=False)
    date=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self)->str:
        return f'{self.sno} {self.title}'

@app.route('/delete/<int:sno>')
def delete(sno):
    row_to_delete=Writing_Essay.query.filter_by(sno=sno).first()
    db.session.delete(row_to_delete)
    db.session.commit()
    return redirect(url_for('read'))

@app.route('/update/<int:sno>')
def update(sno):
    row=Writing_Essay.query.get_or_404(sno)
    return render_template("index.html", row=row)

@app.route('/read')
def read():
    all_data=Writing_Essay.query.all()
    return render_template('read.html',all_data=all_data)

@app.route('/', methods=["GET","POST"])
def index():
    if request.method=='POST':
        sno=request.form.get('sno')
        title=request.form["title"]
        content=request.form["content"]
        if sno:
            row=Writing_Essay.query.get_or_404(sno)
            row.title=title
            row.content=content
            db.session.commit()
        else:
            row=Writing_Essay(title=title,content=content)
            db.session.add(row)
            db.session.commit()
    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True , port=8000)