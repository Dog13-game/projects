from flask import Flask, session, request, render_template

app = Flask(__name__)
app.secret_key = "секретний_ключ"

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = session.get("result", 0)

    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        op = request.form["operation"]

        try:
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                result = num1 / num2 
            session["result"] = result
        except ZeroDivisionError:
            result = "На нуль не ділиться"
            session["result"] = result

    return render_template("calculator.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
