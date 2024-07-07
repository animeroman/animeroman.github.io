from flask import Flask, render_template

app = Flask(__name__, template_folder='.')

@app.route('/anime-watching')
def anime_watching():
    return render_template('anime-watching.html')

if __name__ == '__main__':
    app.run(debug=True)
