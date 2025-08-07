from flask import Flask, render_template, request
import os
import cv2
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/cartoonized_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def apply_cartoon_style(input_path, output_path, style):
    img = cv2.imread(input_path)

    if style == "pencil":
        gray, sketch = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
        result = sketch
    elif style == "color":
        color = cv2.bilateralFilter(img, 9, 300, 300)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY, 9, 9)
        result = cv2.bitwise_and(color, color, mask=edges)
    elif style == "sketch":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        inv = 255 - gray
        blur = cv2.GaussianBlur(inv, (21, 21), 0)
        inv_blur = 255 - blur
        result = cv2.divide(gray, inv_blur, scale=256.0)
    else:
        result = img

    cv2.imwrite(output_path, result)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('media')
        style = request.form.get('style')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], 'input_' + filename)
            output_filename = 'output_' + style + '_' + filename
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)

            file.save(input_path)
            apply_cartoon_style(input_path, output_path, style)

            return render_template('index.html', output_path=output_filename)

    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
