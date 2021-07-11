import os
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect

import Caption_It


app = Flask(__name__)
UPLOAD_FOLDER = "./static/"
# def caption():
#     return render_template("index.html")
@app.route('/')
def caption():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def imgCaption():
    if request.method == 'POST':
        f = request.files['userfile']
        path = "./static/{}".format(f.filename)
        f.save(path)

        caption = Caption_It.caption_this_image(path)
        #print(caption)

        result_dic = {
            'image': path,
            'caption': caption
        }

    return render_template("index.html",your_result=result_dic)



if __name__ == '__main__':
    app.run(debug=True)


