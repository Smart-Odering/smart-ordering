# pip install flask_cors
# pip install flask
# pip install
from flask import Flask, request, json, jsonify
from flask_cors import CORS
# import speech_recognition as sr

app = Flask(__name__)
CORS(app)

@app.route("/stt", methods=['GET'])
def stt():
    # params = request.get_json()
    # print("받은 Json 데이터 ", params)
    # recogResult = None
    # try:
    #     r = sr.Recognizer()

    #     with sr.Microphone() as source:
    #         print('음성을 입력하세요.')
    #         audio = r.listen(source)
    #     try:
    #         recogResult = r.recognize_google(audio, language='ko-KR')
    #         print('음성변환 : ' + recogResult)
    #     except sr.UnknownValueError:
    #         print('오디오를 이해할 수 없습니다.')
    #     except sr.RequestError as e:
    #         print(f'에러가 발생하였습니다. 에러원인 : {e}')

    # except KeyboardInterrupt:
    #     pass

    # response = recogResult
    response = {
        "result":"success"
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3001)