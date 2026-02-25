from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/ivr', methods=['GET', 'POST'])
def ivr():
    hangup = request.values.get('hangup', '')
    call_id = request.values.get('callId', '')
    id_num = request.values.get('id_num', '').strip()

    if hangup == 'yes':
        return yemot_response('hangup=1')

    if id_num == '':
        return yemot_response(
            'read=t-Please enter your 9 digit ID and press star=id_num,,9,9,Digits'
        )

    if not id_num.isdigit() or len(id_num) != 9:
        return yemot_response(
            'read=t-Invalid ID number please try again=id_num,,9,9,Digits'
        )

    print(f"Call {call_id} - ID: {id_num}")
    digits_spaced = ' '.join(id_num)
    return yemot_response(
        f'id_list_message=t-Thank you. ID {digits_spaced} received\nhangup=1'
    )


def yemot_response(text):
    return Response(text.strip(), content_type='text/plain; charset=utf-8')


@app.route('/', methods=['GET'])
def health():
    return 'OK', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
