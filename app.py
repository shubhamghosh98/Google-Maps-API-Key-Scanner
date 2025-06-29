from flask import Flask, render_template, request, redirect, url_for, session
import subprocess
import os
import re

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "default-fallback-secret")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        api_key = request.form.get("api_key", "").strip()
        if not re.match(r"^AIza[0-9A-Za-z-_]{35}$", api_key):
            session["output"] = ""
            session["error"] = "⚠️ Invalid API key format."
            return redirect(url_for("index"))

        try:
            result = subprocess.run(
                ['python3', 'maps_api_scanner.py', '--api-key', api_key],
                cwd=os.path.join(os.getcwd(), 'gmapsapiscanner'),
                capture_output=True,
                text=True,
                timeout=60
            )
            session['output'] = result.stdout or result.stderr
            session['error'] = None
        except subprocess.TimeoutExpired:
            session['output'] = ""
            session['error'] = "❌ Scan timed out. Please try again."
        except Exception as e:
            session['output'] = ""
            session['error'] = f"❌ Error: {str(e)}"
        return redirect(url_for("index"))

    output = session.pop("output", "")
    error = session.pop("error", None)
    return render_template("index.html", output=output, error=error)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
