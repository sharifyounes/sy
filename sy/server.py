

from flask import Flask, render_template, url_for, redirect


from argparse import ArgumentParser


app = Flask(__name__, static_url_path="/static")


@app.route("/ping", methods=["GET"])
def ping():
    return "okay", 200


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

def _load_app(environment="dev"):
    app.config["environment"] = environment

    return app

@app.route("/favicon.ico")
def favicon():
    return redirect(url_for("static", filename="images/favicon.ico"))


if __name__ == "__main__":
    DEFAULT_PORT = 9002
    
    parser = ArgumentParser()
    parser.add_argument("--environment", "-env", required=True,
                        help="Specify environment. See diet/config/*.ini" )
    
    args = parser.parse_args()

    app = _load_app(environment=args.environment)

    port = int(app.config.get("PORT", DEFAULT_PORT))
    debug = (app.config["environment"] != "production")
    
    app.run(
        host="0.0.0.0",
        debug=debug,
        port=port
    )


