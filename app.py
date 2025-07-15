from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# صفحه اصلی یا صفحه ورود (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# اگر صفحه ورود جدا دارید (مثال)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # دریافت شماره موبایل یا اطلاعات فرم
        mobile = request.form.get('mobile')
        # اینجا می‌توانید منطق ارسال کد تایید یا اعتبارسنجی را اضافه کنید
        
        # فعلا فقط هدایت به صفحه پروفایل (یا هر مسیر دیگر)
        return redirect(url_for('profile'))
    return render_template('login.html')

# صفحه پروفایل (profile.html)
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        # دریافت داده های فرم پروفایل
        name = request.form.get('name')
        # ذخیره یا پردازش اطلاعات
        
        return "اطلاعات پروفایل ذخیره شد."
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
