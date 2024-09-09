from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        text = request.form["userInput"]
        ans = ""
        for i in range(0,len(text)):
            if i%2 == 0:
                ans += text[i]
        ans1 = ""
        for i1 in range(0, len(text)):
            if i1 % 2 != 0:
                ans1 += text[i1]
        return render_template('answer.html', value=ans,value1 = ans1)  # Return the reversed text
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
