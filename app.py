from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
import base64
import os
from src.dog_face_cropper_service import DogFaceCropperService
from src.utils import eliminar_archivos_temporales

port = int(os.environ.get("PORT", 5000))

app = Flask(__name__)

dog_face_cropper_service = DogFaceCropperService()

@app.route('/')
@app.route('/index')
def index():
    return "Index Page"

@app.route('/dogfacecropper', methods=['POST'])
def dogfacecropper():
    fecha_busqueda = datetime.now()
    print('Inicio de recorte de imagen de mascota: {}'.format(fecha_busqueda))
    try:
        print(request.files)
        data = request.files.get('upload_file')
        
        if data == None:
            return jsonify('Got None')
        else:
            print("DATA",type(data))
            
            if data.filename == '':
                return jsonify('Debe ingresar una imagen.')

            if not os.path.exists('./temp_crop/'):
                os.mkdir('./temp_crop/')
            
            current_date = datetime.utcnow().strftime('%Y-%m-%d_%H%M%S.%f')[:-3]
            nombre_imagen_a_recortar = './temp_crop/image_{}.jpg'.format(current_date)
            nombre_imagen_recortada = './temp_crop/new_image_{}.jpg'.format(current_date)
            file = data
            file.save(nombre_imagen_a_recortar)
            dog_face_cropper_service.recortar_imagen_mascota(nombre_imagen_a_recortar, nombre_imagen_recortada)
            data = {}
            with open(nombre_imagen_recortada,'rb') as file:
                img = file.read()
            data['img'] = base64.encodebytes(img).decode('utf-8')
            respuesta = json.dumps(data)
            eliminar_archivos_temporales(nombre_imagen_a_recortar)
            eliminar_archivos_temporales(nombre_imagen_recortada)
    except Exception as e:
        print('Hubo un error en el recorte de imagen de mascota: {}'.format(datetime.now()))
        print('Hubo un error. {}'.format(e))
        eliminar_archivos_temporales(nombre_imagen_a_recortar)
        eliminar_archivos_temporales(nombre_imagen_recortada)
        return jsonify('Hubo un error. Volver a ingresar la imagen.')
    
    print('Fin de recorte de imagen de mascota: {}'.format(datetime.now()))
    return respuesta

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)