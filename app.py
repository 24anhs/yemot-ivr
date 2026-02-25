from flask import Flask, request, Response

app = Flask(__name__)


@app.route('ivr:/', methods=['GET', 'POST'])
def ivr():
    hangup  = request.values.get('hangup', '')
    call_id = request.values.get('callId', '')
    id_num  = request.values.get('id_num', '').strip()

    if hangup == 'yes':
        return yemot_response('hangup=1')

    if id_num == '':
        return yemot_response(
            'read=t-שלום>אנא הזן מספר זהות בן 9 ספרות^id_num>>9>9>Digits'
        )

    if not id_num.isdigit() or len(id_num) != 9:
        return yemot_response(
            'read=t-מספר הזהות שהזנת אינו תקין>אנא נסה שנית^id_num>>9>9>Digits'
        )

    print(f"Call {call_id} - ID: {id_num}")
    digits_spaced = '>'.join(id_num)
    return yemot_response(
        f'id_list_message=t-תודה>מספר הזהות>{digits_spaced}>התקבל בהצלחה\n'
        'go_to_folder=ivr2:/'
    )


def yemot_response(text):
    return Response(text.strip(), content_type='text/plain; charset=utf-8')


@app.route('/', methods=['GET'])
def health():
    return 'OK', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
