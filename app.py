from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/ivr', methods=['GET', 'POST'])
def ivr():
    entry = request.values.get('id_num', '').strip()
    hangup = request.values.get('hangup', '')
    call_id = request.values.get('callId', '')

    if hangup == 'yes':
        return yemot_response('hangup=1')

    if entry == '':
        return yemot_response(
            'read=id_num,;t Please enter your 9 digit ID and press star,9,9,10'
        )

    if not entry.isdigit() or len(entry) != 9:
        return yemot_response(
            'read=id_num,;t Invalid ID number please try again,9,9,10'
        )

    print(f"Call {call_id} - ID: {entry}")
    digits_spaced = ' '.join(entry)
    return yemot_response(
        f'speak_text=Thank you. ID {digits_spaced} received\nhangup=1'
    )


def yemot_response(text):
    return Response(text.strip(), content_type='text/plain; charset=utf-8')


@app.route('/', methods=['GET'])
def health():
    return 'OK', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
