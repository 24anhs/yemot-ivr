# מערכת IVR - ימות המשיח | קליטת מספר זהות

## מה המערכת עושה?
- מקבלת שיחה נכנסת דרך ימות המשיח
- מבקשת מהמתקשר להזין מספר זהות בן 9 ספרות
- מוודאת שהמספר תקין (9 ספרות בדיוק)
- מאשרת קבלה או מבקשת הזנה מחדש

---

## העלאה ל-Railway (צעד אחר צעד)

### 1. GitHub
1. היכנס ל-github.com → New Repository
2. שם: `yemot-ivr`
3. העלה את כל הקבצים (app.py, requirements.txt, Procfile)

### 2. Railway
1. היכנס ל-railway.app עם חשבון GitHub
2. לחץ "New Project" → "Deploy from GitHub Repo"
3. בחר את `yemot-ivr`
4. Railway יבנה אוטומטית ויתן לך URL בסגנון:
   `https://yemot-ivr-production.up.railway.app`

### 3. הגדרה בימות המשיח
1. היכנס ללוח הבקרה של ימות המשיח
2. בחר את המרכזייה שלך
3. עבור לקמפיין/תפריט → הגדר Webhook URL:
   `https://YOUR-URL.railway.app/ivr`
4. שיטה: GET

---

## בדיקה מקומית (אופציונלי)

```bash
pip install flask gunicorn
python app.py
```
השרת יעלה על: http://localhost:5000/ivr

---

## הרחבות אפשריות
- שמירת ת.ז ל-Google Sheets / מסד נתונים
- בדיקת ת.ז מול רשימה מאושרת
- שליחת SMS אישור לאחר הזנה
