from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def form():
    return render_template('template.html')


@app.route('/', methods=['POST'])
def num():
    text = int(request.form['number'])
    num_list = [str(num) for num in range(1, text + 1)]
    new_str = " ".join(num_list)
    return new_str

@app.route('/odd', methods=['POST'])
def odd():
    text = int(request.form['number'])
    num_list = [str(num) for num in range(1, text + 1) if num % 2 != 0]
    new_str = " ".join(num_list)
    return new_str



if __name__ == '__main__':
    app.run()
