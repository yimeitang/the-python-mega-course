from flask import Flask, render_template #render_template class let us render html and class

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')  # here the home。html needs to be under templates folder

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)
