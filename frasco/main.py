from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def starter():
    return '''
    <form action="/forward/" method="post">
        <button name="forwardBtn" type="submit">Forward</button>
    </form>

    '''


@app.route("/forward/",methods=["GET", "POST"])
def move_forward():
    print("cu")
    return ("sex")


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)