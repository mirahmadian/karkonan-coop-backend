from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# صفحه اصلی = فرم ورود شماره موبایل
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mobile = request.form.get("mobile")

        # بررسی ساده: شماره باید 11 رقم و با 0 شروع شود
        if mobile and mobile.isdigit() and mobile.startswith("0") and len(mobile) == 11:
            # اینجا در حالت واقعی کد تایید را ارسال می‌کنید
            return redirect(url_for("profile"))
        else:
            return render_template("index.html", error="شماره موبایل معتبر وارد کنید!")

    return render_template("index.html")


# صفحه تکمیل پروفایل
@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        name = request.form.get("name")
        family = request.form.get("family")
        national_code = request.form.get("national_code")

        # اینجا باید اطلاعات را ذخیره کنید در دیتابیس یا فایل یا هر روشی
        print(f"نام: {name}, نام خانوادگی: {family}, کدملی: {national_code}")

        return "اطلاعات با موفقیت ثبت شد."

    return render_template("profile.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
