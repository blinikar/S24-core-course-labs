from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def template():
    msk_time = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=3))
    ).strftime('%d.%m.%y %H:%M:%S')

    print(f"datetime rendered is {msk_time}")

    return render_template(
        'index.html',
        time=msk_time
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
