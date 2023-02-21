from my-captionig-models.main import ImageProcessing
from deep_translator import GoogleTranslator
from flask import request
from deep_translator import GoogleTranslator
import base64
import os
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.route('/caption_image', methods = ['POST'])
def caption_image():    
    data = request.json
    imgstring =  data['base64Photo']
    imgdata = base64.b64decode(imgstring)
    filename = 'image.jpg'  

    with open(filename, 'wb') as f:
        f.write(imgdata)    
        
    text = ImageProcessing(filename)    
    text = ' '.join(text)
    print(text)
    
    to_translate = text
    translated = GoogleTranslator(source='auto', target='pt').translate(to_translate)
    print(translated)
        
    return (translated) 


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='0.0.0.0', port=8080, debug=True)
