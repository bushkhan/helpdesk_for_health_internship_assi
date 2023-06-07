from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

app = Flask(__name__, template_folder="templates")


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/chatbot", methods=["POST"])
def chatbot():
    condition = request.form["condition"]
    severity = request.form["severity"]
    
    def generate_chatbot_response(condition, severity):
        prompt = f"You selected:{condition} & severity:{severity}."

        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=256,
            temperature=0,
            top_p=1,
            stop=None,
            frequency_penalty=0,
            presence_penalty=5
        )

        chatbot_response = response.choices[0].text.strip()
        return chatbot_response

    bot_response = generate_chatbot_response(condition, severity)

    return render_template("chatbot.html", data1=condition,data2=severity, bot_response=bot_response)


if __name__ == "__main__":
    app.run(port=8000, debug=True)