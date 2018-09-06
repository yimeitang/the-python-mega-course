from flask import Flask

app=Flask(__name__)

@app.route('/')                                  #the decorator
def home():                                      #define what the homepage will do
    return "Website content goes here!"

if __name__=="__main__":
    app.run(debug=True)
