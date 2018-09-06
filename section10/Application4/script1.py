from flask import Flask

app=Flask(__name__)

@app.route('/')                                  #the decorator, the content will be mapped here, you could also change this to @app.rout('/about/')
def home():                                      #define what the homepage will do
    return "Website content goes here!"

@app.route('/anotherpage/')
def about():
    return "This is another page"
    
if __name__=="__main__":
    app.run(debug=True)                          #run home() function

    
    
