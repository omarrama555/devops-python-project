from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # نقرأ اسم الجهاز أو الـ Pod للتأكد لاحقاً من توزيع الأحمال في كوبرنيتس
    hostname = os.environ.get('HOSTNAME', 'Localhost')
    return f"<h1>مرحباً بك في أول مشروع DevOps!</h1><p>الحاوية التي تعمل حالياً: {hostname}</p>"

if __name__ == '__main__':
    # تشغيل التطبيق على المنفذ 5000 ومتاح خارجياً
    app.run(host='0.0.0.0', port=5000)