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

---
### :100: <i>Thanks!</i>
#### Now, don't be an stranger. Let's stay in touch!

<a href="https://github.com/leolanese" target="_blank" rel="noopener noreferrer">
  <img src="https://scastiel.dev/api/image/leolanese?dark&removeLink" alt="leolanese’s GitHub image" width="600" height="314" />
</a>

##### :radio_button: Linkedin: <a href="https://www.linkedin.com/in/leolanese/" target="_blank">LeoLanese</a>
##### :radio_button: Twitter: <a href="https://twitter.com/LeoLanese" target="_blank">@LeoLanese</a>
##### :radio_button: Portfolio: <a href="https://www.leolanese.com" target="_blank">www.leolanese.com</a>
##### :radio_button: DEV.to: <a href="https://www.dev.to/leolanese" target="_blank">dev.to/leolanese</a>
##### :radio_button: Blog: <a href="https://www.leolanese.com/blog" target="_blank">leolanese.com/blog</a>
##### :radio_button: Questions / Suggestion / Recommendation: developer@leolanese.com

