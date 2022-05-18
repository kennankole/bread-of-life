from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("project.config.Config")
    db.init_app(app)
    with app.app_context():
        from project.routes import home 
        app.register_blueprint(home)
        
    return app



# app.config.from_object("project.config.Config")
# db = SQLAlchemy(app)


# @app.route("/")
# def hello_world():
#     return jsonify(hello="World")


# @app.route("/static/<path:filename>")
# def staticfiles(filename):
#     return send_from_directory(app.config["STATIC_FOLDER"], filename)


# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['MEDIA_FOLDER'], filename))
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <form action="" method=post enctype=multipart/form-data>
#     <p><input type=file name=file><input type=submit value=Upload>
#     </form>
#     '''


# @app.route('/media/<path:filename>')
# def mediafiles(filename):
#     return send_from_directory(app.config['MEDIA_FOLDER'], filename)
