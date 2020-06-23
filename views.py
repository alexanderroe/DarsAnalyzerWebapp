import os
from flask import Flask, request, redirect, render_template
from werkzeug.utils import secure_filename

import dars_filter, dars_parser

app = Flask(__name__)

app.config['ALLOWED_EXTENSIONS'] = ['pdf']

def allowed_image(filename):
    file_extension = filename.rsplit('.', 1)[1].lower()
    extension_allowed = file_extension in app.config["ALLOWED_EXTENSIONS"]
    return '.' in filename and extension_allowed


def process(filename):
    return dars_filter.process_pdf(filename)


@app.route('/', methods=['GET', 'POST'])
def upload_image():

    if request.method == 'POST':

        if request.files:

            image = request.files['image']

            if image.filename == '':
                print('image must have nonempty filename') # show this on webpage
                return redirect(request.url)

            if not allowed_image(image.filename):
                print('extension not allowed') # show this on webpage
                return redirect(request.url)

            else:
                filename = secure_filename(image.filename)

            output = process(filename)

    if 'output' in locals():
        return render_template('index.html', output = output)

    else:
        return render_template('index.html')


# this allows running "python3 views.py" to start server
if __name__ == '__main__':
    app.run(debug=True)