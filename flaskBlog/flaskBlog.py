from flask import Flask, render_template,url_for

app = Flask(__name__)
posts=[{
	'author' : 'Chandrika Sharma',	
	'title' : 'Blog 1',
	'content' : 'My first blog',
	'date_posted' : 'April 20, 2018'
},
{
	'author':'Aditya Sharma',	
	'title':'Cricket fever',
	'content':"Aditya's first blog",
	'date_posted' : 'April 20, 2018'
}
]

@app.route('/')
def hello():
    return render_template('/home.html',posts=posts)
@app.route('/about')
def about():
    return render_template('/about.html',title="About Page")

if __name__== '__main__':
   	app.run(debug=True)