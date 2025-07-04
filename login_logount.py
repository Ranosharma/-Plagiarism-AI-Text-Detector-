@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("index"))
        else:
            return render_template_string(login_template, error="Invalid credentials")
    return render_template_string(login_template)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
