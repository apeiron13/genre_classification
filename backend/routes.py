from flask import jsonify, request, send_from_directory
from app import *
import zipfile
import uuid
from Music import Music
from markupsafe import escape


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        musics = request.files.getlist('file')
        unique_id = uuid.uuid4()
        for music in musics:
            path = os.path.join(UPLOAD_FOLDER, str(unique_id) + "_" + music.filename)
            # path = os.path.join(UPLOAD_FOLDER, music.filename)
            music.save(path)
        msc = Music(unique_id, UPLOAD_FOLDER)
        msc.set_melspectrogram()
        gen = genre.predict_classes(msc.get_melspectrogram())
        msc.save_melspgram_by_genre(gen)

        return jsonify(names=msc.get_names(), genres=gen, paths=msc.get_list_img_path())


@app.route("/get_mel/<path:path>")
def get_file(path):
    return send_from_directory(UPLOAD_FOLDER, filename=path, as_attachment=True)
