from flask import Flask, render_template, request
from scipy.stats import binom

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    example_data = {}

    # Cek jika contoh data dipilih melalui query string
    example = request.args.get("example")
    if example == "1":
        example_data = {"n": 10, "p": 0.5, "k": 5}
    elif example == "2":
        example_data = {"n": 20, "p": 0.3, "k": 6}
    elif example == "3":
        example_data = {"n": 15, "p": 0.8, "k": 12}

    if request.method == "POST":
        # Ambil input dari form
        n = int(request.form["n"])
        p = float(request.form["p"])
        k = int(request.form["k"])

        # Hitung probabilitas menggunakan distribusi binomial
        prob = binom.pmf(k, n, p)
        result = f"Probabilitas {k} mahasiswa diterima adalah {prob:.4f}"

    return render_template("index.html", result=result, example_data=example_data)

if __name__ == "__main__":
    # Jalankan aplikasi pada host 127.0.0.1 dan port 2002
    app.run(host="127.0.0.1", port=8000, debug=True)

