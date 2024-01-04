# Python-API-Angular

## Python 

> I will be using `Flask` is a popular Python web frameworks for building robust back-end systems

## API Python

```js
// check package installer for Python
pip --version

// check Phyton version
python -V

// check Flask version
flask --version
```

```js
// RUN BACK-END
// New-Item -ItemType File app.py
// app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return jsonify(message='Hello, World!')

if __name__ == '__main__':
    app.run(debug=True)
```

```js
python app.py
```

> This simple Flask app creates an API endpoint /api/hello that returns a JSON response with the message from server

```js
// RUN FRONT-END
// use angular 20
npm i -g @angular/cli

ng new --routing=false --style=css --standalone

ng version

cd AppProject/src/app

ng serve --open --port 4200
```

## Demo

![Python](https://raw.githubusercontent.com/leolanese/Python-API-Angular/main/app/src/assets/Python-API-Angular-Capture.jpg)
