from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/ivr', methods=['GET', 'POST'])
def ivr():
    call_id = request.values.get('callId', '')
    entry   = request.values.get('ApiEnter', '').strip()
    hangup  = request.values.get('hangup', '')

    # ימות שולחת hangup=yes בסוף שיחה – לא צריך לעשות כלום
    if hangup == 'yes':
        return yemot_response('hangup=1')

    # אם עוד לא הוזן כלום – בקש מספר זהות
    if entry == '':
        return yemot_response(
            "speak_text=שלום, אנא הזן מספר זהות בן 9 ספרות ולחץ כוכבית\n"
            "read_input=1\n"
            "max_digit=9\n"
            "min_digit=9\n"
            "tap_timeout=10"
        )

    # הוזן משהו – בדוק ולידציה
    if not entry.isdigit() or len(entry) != 9:
        return yemot_response(
            "speak_text=מספר הזהות שהזנת אינו תקין. אנא נסה שנית\n"
            "read_input=1\n"
            "max_digit=9\n"
            "min_digit=9\n"
            "tap_timeout=10"
        )

    # ת.ז תקינה!
    print(f"[CALL {call_id}] קיבלנו ת.ז: {entry}")

    digits_spaced = ' '.join(entry)
    return yemot_response(
        f"speak_text=תודה. מספר הזהות {digits_spaced} התקבל בהצלחה\n"
        "hangup=1"
    )


def yemot_response(text: str):
    return Response(text.strip(), content_type='text/plain; charset=utf-8')


@app.route('/', methods=['GET'])
def health():
    return "OK", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
קודים למימשוק עם ימות המשיח - Claude
