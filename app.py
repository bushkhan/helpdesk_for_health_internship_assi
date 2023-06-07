from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv
import pyttsx3

load_dotenv()

#load the key
openai.api_key = os.environ["OPENAI_API_KEY"]

app = Flask(__name__, template_folder="templates")

#flask create routes
@app.route('/')
def home():
    return render_template('index.html')


@app.route("/chatbot", methods=["POST"])
def chatbot():
    #get the values from form
    condition = request.form["condition"]
    severity = request.form["severity"]
    
    #method for calling api and getting the response
    def generate_chatbot_response(condition, severity):
        prompt = f"You selected:{condition} & severity:{severity}."

        response = openai.Completion.create(
            engine='text-davinci-003', #very powerful
            prompt=prompt,
            max_tokens=3000, #the maximum number of tokens to generate in the completion
            temperature=0, #higher value means the model will take more risks
            top_p=1, #alternative to sampling called nucleus sampling
            frequency_penalty=0.5, #number betn -2.0 and 2.0.
            presence_penalty=0  #number betn -2.0 and 2.0.
        )

        #responses
        chatbot_response = response.choices[0].text.strip()
        return chatbot_response

    bot_response = generate_chatbot_response(condition, severity)
    

    #passing thenvalues to next page
    return render_template("chatbot.html", data1=condition,data2=severity, bot_response=bot_response)


if __name__ == "__main__":
    app.run(port=8000, debug=True)