from flask import redirect, request, render_template, url_for, Flask
from fibonacci_tools.fib_term import fast_double, fib_which_term, is_fib
from fibonacci_tools.combinations import solve, solve_all_combinations
from util import parse, parse_multiple

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/term", methods=["POST"])
def term():
    u_input = request.form.get("num")
    if not u_input:
        return redirect("/")
    number = fast_double(int(u_input))
    message = f'Fib({u_input}) is:'
    return render_template("result.html", output = number, message=message)

@app.route("/sum", methods=["POST"])
def sum():
    u_input = request.form.get("num")
    if not u_input:
        return redirect("/")
   #  number = parse(solve(int(u_input)))
    number = parse_multiple(solve_all_combinations(int(u_input)))
    message = f'Combinations for {u_input}:'
    return render_template("result.html", output = number, message=message)


@app.route("/which", methods=["POST"])
def which():
    u_input = request.form.get("num")
    if not u_input:
        return redirect("/")
    number = fib_which_term(int(u_input))
    message = f'Position of {u_input}:'
    return render_template("result.html", output = number, message=message)


@app.route("/is_fib", methods=["POST"])
def is_fib_route():
    u_input = request.form.get("num")
    if not u_input:
        return redirect("/")
    result = is_fib(int(u_input))
    message = f"{u_input} is "
    if result:
        message += "a Fibonacci number"
    else:
        message += "not a Fibonacci number"
    return render_template("result.html", message = message, output="")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)


