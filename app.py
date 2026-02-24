from flask import Flask, request

app = Flask(__name__)

# -------------------------
# Webhook ראשי - ימות קוראת לכאן
# -------------------------
@app.route('/ivr', methods=['GET', 'POST'])
def ivr():
    call_id  = request.values.get('callId', '')
    entry    = request.values.get('ApiEnter', '')   # מה המתקשר הקיש
    step     = request.values.get('step', '0')       # שלב בשיחה (אנחנו שולחים את זה בעצמנו)

    # ---- שלב 0: בקשת מספר זהות ----
    if step == '0' or entry == '':
        return yemot_response(
            "speak_text=שלום, אנא הזן מספר זהות בן 9 ספרות ולחץ כוכבית\n"
            "read_input=1\n"
            "max_digit=9\n"
            "min_digit=9\n"
            "block_asterisk=0\n"
            "tap_timeout=10\n"
            "go_to_page=ivr?step=1"
        )

    # ---- שלב 1: קיבלנו קלט - ניקח מ-ApiEnter ----
    if step == '1':
        id_number = entry.strip()

        # ולידציה: 9 ספרות בדיוק
        if not id_number.isdigit() or len(id_number) != 9:
            return yemot_response(
                "speak_text=מספר הזהות שהזנת אינו תקין. אנא נסה שנית\n"
                "read_input=1\n"
                "max_digit=9\n"
                "min_digit=9\n"
                "block_asterisk=0\n"
                "tap_timeout=10\n"
                "go_to_page=ivr?step=1"
            )

        # ---- כאן תוסיף לוגיקה עסקית לפי הצורך ----
        print(f"[CALL {call_id}] קיבלנו ת.ז: {id_number}")

        # אישור למתקשר
        return yemot_response(
            f"speak_text=תודה. מספר הזהות {' '.join(id_number)} התקבל בהצלחה\n"
            "hangup=1"
        )

    # fallback
    return yemot_response("hangup=1")


# -------------------------
# פונקציית עזר - מחזירה טקסט עם header נכון
# -------------------------
def yemot_response(text: str):
    from flask import Response
    return Response(text.strip(), content_type='text/plain; charset=utf-8')


# -------------------------
# Health check - Railway/Render דורשים זאת
# -------------------------
@app.route('/', methods=['GET'])
def health():
    return "OK", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
קודים למימשוק עם ימות המשיח - Claude
