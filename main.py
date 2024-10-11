from flask import Flask, render_template, request
import smtplib
import datetime

app = Flask(__name__)

MY_EMAIL = "ur email"
MY_PASSWORD = "ur password"


@app.route("/", methods=["POST", "GET"])
def home():
    year = datetime.date.today().year
    if request.method == "POST":
        data = request.form
        message = data["message"]
        email = data["email"]
        sent_email(email_from=email, message=message)
    return render_template("index.html", year=year)


def sent_email(email_from, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="email where u will receive the msg",
            msg=f"Subject: Message from personal website!\n\n"
                f"EMAIL: {email_from}\n"
                f"MESSAGE: {message}"
        )


if __name__ == "__main__" :
    app.run(debug=True)