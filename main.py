from flask import redirect, request, render_template, url_for, send_from_directory, Flask
from fibonacci_tools.fib_term import fast_double, fib_which_term, is_fib
from fibonacci_tools.combinations import solve, solve_all_combinations
from util import parse, parse_multiple, make_ordinal
import os

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/results", methods=["POST"])
def results():
    u_input = request.form.get("num")
    if not u_input:
        return redirect("/")
    u_input = int(u_input)
    fib_of_n = fast_double(u_input)
    n_is_fib = is_fib(u_input)
    which_fib = fib_which_term(u_input)
    if (n_is_fib):
        which_fib = make_ordinal(which_fib)
    sum_of_fib = parse_multiple(solve_all_combinations(u_input))
    return render_template("result.html", u_input = u_input, fib = fib_of_n, n_is_fib = n_is_fib,  which = which_fib, combinations=sum_of_fib)

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'LogoMark.svg')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)


