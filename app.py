from flask import Flask, render_template, request, redirect, url_for, flash
import random
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # برای نمایش پیام‌های flash

# مقدار کلید API سناتور پیامک خودت را اینجا بگذار
SENATOR_API_KEY = "1807093505:gKP98hHmnoGXTx0@SenatorApiBot"
# کد قالب پیامک (باید از پنل یا پشتیبانی بگیری)
TEMPLATE_CODE = "1000"

def send_sms_code(phone, code):
    url = f"https://api.fast-creat.ir/sms?apikey={SENATOR_API_KEY}&type=sms&code={code}&phone={phone}&template={TEMPLATE_CODE}"
    try:
        response = requests.get(url)
        return response.status_code == 200 and "success" in response.text.lower()
    except Exception as e:
        print("Error sending SMS:", e)
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mobile = request.form.get('mobile')
        if not mobile:
            flash("لطفا شماره موبایل را وارد کنید.")
            return render_template('index.html')

        # تولید کد 6 رقمی تصادفی
        code = str(random.randint(100000, 999999))
        
        # ارسال پیامک کد تایید
        success = send_sms_code(mobile, code)

        if success:
            # ذخیره کد و شماره موبایل در session یا دیتابیس (در این مثال ساده توی session)
            # برای سادگی اینجا فقط flash می‌کنیم و به صفحه پروفایل می‌رویم
            flash(f"کد تایید با موفقیت ارسال شد: {code} (برای تست)")
            return redirect(url_for('profile'))
        else:
            flash("ارسال پیامک با خطا مواجه شد. لطفا دوباره تلاش کنید.")
    return render_template('index.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        name = request.form.get('name')
        # اینجا می‌توانید اطلاعات پروفایل را ذخیره کنید
        flash("اطلاعات پروفایل با موفقیت ثبت شد.")
        return render_template('profile.html')

    return render_template('profile.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
