from flask import Flask, render_template, request, response
app = Flask(__name__, template_folder= "templates")
import openai


@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run()
   
   
@app.route('/get_response', methods=['POST'])
def get_response():
    condition = request.form['condition']
    severity = request.form['severity']
    
    # Add logic to process the condition and severity and generate a response
    
    return render_template('response.html', response=response)