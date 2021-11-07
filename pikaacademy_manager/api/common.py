from logging import getLogger
import werkzeug
import dropbox
import tempfile
from datetime import datetime
from config import ACCESS_TOKEN_DROPBOX
from flask_restplus import Namespace, Resource, reqparse
from werkzeug.utils import secure_filename
logger = getLogger(__name__)

api = Namespace("common")

file_upload_parameter = reqparse.RequestParser()
file_upload_parameter.add_argument('folder', type=str, location='args')
file_upload_parameter.add_argument(
  'file', type=werkzeug.datastructures.FileStorage, location='files', required=True
)

@api.route("/file-upload")
class FileUpload(Resource):

    @api.doc()
    @api.expect(file_upload_parameter, validate=True)
    def post(self):
        args = file_upload_parameter.parse_args()
        file = args['file']
        folder =args['folder'] if args['folder'] else '/Apps/Edumall-default'
        upload_filename = secure_filename(file.filename)
        file_format = upload_filename.split('.')
        upload_file_path = tempfile.NamedTemporaryFile().name
        file.save(upload_file_path)
        file_to = f"{folder}/{str(int(round(datetime.now().timestamp())))}.{file_format[len(file_format) - 1]}"
        url = None
        with open(upload_file_path, 'rb') as f:
            data = f.read()
        try:
            dbx = dropbox.Dropbox(ACCESS_TOKEN_DROPBOX)
            res = dbx.files_upload(f=data, path=file_to, mode=dropbox.files.WriteMode.overwrite)
            shared_link_metadata = dbx.sharing_create_shared_link_with_settings(file_to)
            url = shared_link_metadata.url
            url = url.replace("dl=0", "raw=1")
        except Exception as e:
            res = f"Error = {e}"
            logger.exception(res)
        return url
