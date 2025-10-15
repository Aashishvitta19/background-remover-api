from flask import Flask, request, send_file
from rembg import remove
import io

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Background Removal API is running 🎯"}

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return {"error": "No image uploaded"}, 400

    input_image = request.files['image'].read()
    output_image = remove(input_image)

    return send_file(
        io.BytesIO(output_image),
        mimetype='image/png',
        as_attachment=True,
        download_name='no_bg.png'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # required for Render
