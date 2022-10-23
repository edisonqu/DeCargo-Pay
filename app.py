from io import BytesIO

from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def pilImgToB64(img: Image):
    output = BytesIO()
    img.save(output, format='JPEG')
    img_b64 = base64.b64encode(output.getvalue())

    return img_b64.decode("ascii")




if __name__ == "__main__":
    app.run(debug=True)



