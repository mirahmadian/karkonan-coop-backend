from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mobile = request.form.get('mobile')
        print(f"شماره وارد شده: {mobile}")  # این لاگ در render در قسمت logs نمایش داده می‌شود
        return redirect(url_for('profile'))
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
