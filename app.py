from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/ivr', methods=['GET', 'POST'])
def ivr():
    call_id = request.values.get('callId', '')
    entry = request.values.get('ApiEnter', '').strip()
    hangup = request.values.get('hangup', '')

    if hangup == 'yes':
        return yemot_response('hangup=1')

    if entry == '':
        return yemot_response(
            'speak_text=Please enter your 9 digit ID and press star\n'
            'read_input=1\n'
            'max_digit=9\n'
            'min_digit=9\n'
            'tap_timeout=10'
        )

    if not entry.isdigit() or len(entry) != 9:
        return yemot_response(
            'speak_text=Invalid ID number, please try again\n'
            'read_input=1\n'
            'max_digit=9\n'
            'min_digit=9\n'
            'tap_timeout=10'
        )

    print(f"Call {call_id} - ID received: {entry}")

    digits_spaced = ' '.join(entry)
    return yemot_response(
        f'speak_text=Thank you. ID number {digits_spaced} received successfully\n'
        'hangup=1'
    )


def yemot_response(text):
    return Response(text.strip(), content_type='text/plain; charset=utf-8')


@app.route('/', methods=['GET'])
def health():
    return 'OK', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
