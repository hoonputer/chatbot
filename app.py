from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# OpenAI API 키 설정
openai.api_key = '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'

@app.route('/')
def home():
    return 'Hello, this is your chatbot server.'

@app.route('/chat', methods=['POST'])
def chat():
    # 요청에서 메시지 추출
    data = request.json
    user_message = data['message']

    # OpenAI API를 사용하여 챗봇 응답 생성
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    )

    # OpenAI API 응답에서 챗봇 메시지 추출
    bot_response = response.choices[0].message['content']

    # 챗봇 응답을 사용자에게 전송
    return jsonify({
        "response": bot_response
    })

if __name__ == '__main__':
    app.run(debug=True)
