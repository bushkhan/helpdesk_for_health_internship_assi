# from flask import Flask, render_template, request


# app = Flask(__name__, template_folder= "templates")
# import openai


# @app.route('/')
# def home():
#    return render_template('index.html')
# if __name__ == '__main__':
#    app.run()
   
# @app.route('/get_response', methods=['POST'])
# def get_response():
#     condition = request.form['condition']
#     severity = request.form['severity']
    
#     # Add your logic to process the condition and severity and generate a response
    
#     # Example response based on condition and severity
#     response = f"You selected {condition} with severity {severity}."
    
#     return response

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

# print(openai.api_key)


#SETUP FOR FLASK
app = Flask(__name__, template_folder= "templates")


#DEFINE THE HOME PAGE ROUTE
@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run()
   

#DEFINE THE CHATBOT ROUTE
@app.route("/chatbot",methods=["POST"])
def chatbot():
    pass
