from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/ivr', methods=['GET', 'POST'])
def ivr():
    entry = request.values.get('ApiEnter', '').strip()
    hangup = request.values.get('hangup', '')
    call_id = request.values.get('callId', '')

    if hangup == 'yes':
        return yemot_response('hangup=1')

    if entry == '':
        return yemot_response(
            'read_input=1\n'
            'read_timeout=10\n'
            'read_max=9\n'
            'read_min=9\n'
            'speak_text=Please enter your 9 digit ID and press star'
        )

    if not entry.isdigit() or len(entry) != 9:
        return yemot_response(
            'read_input=1\n'
            'read_timeout=10\n'
            'read_max=9\n'
            'read_min=9\n'
            'speak_text=Invalid ID, please try again'
        )

    print(f"Call {call_id} - ID: {entry}")
    digits_spaced = ' '.join(entry)
    return yemot_response(
        f'speak_text=Thank you. ID {digits_spaced} received\n'
        'hangup=1'
    )


def yemot_response(text):
    return Response(text.strip(), content_type='text/plain; charset=utf-8')


@app.route('/', methods=['GET'])
def health():
    return 'OK', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
