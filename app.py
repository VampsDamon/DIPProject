from flask import Flask, request, render_template, send_file
from PIL import Image, ImageEnhance
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    contrast_value = float(request.form['contrast'])
    image = Image.open(file.stream)
    
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(contrast_value)
    
    img_io = io.BytesIO()
    enhanced_image.save(img_io, 'JPEG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
