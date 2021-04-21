## **Instrucciones para deploy en Azure** ##

#### **❗ Importante: ❗**

<a name="precondiciones"></a>
#### **Precondiciones:**

- Tener instalado Git o GitHub Desktop.
- Tener instalado Docker Hub (https://docs.docker.com/docker-for-windows/install/).

#### **Indice - Tabla de contenidos**

1. [Precondiciones](#precondiciones)
2. [Pasos deploy](#pasos-deploy)

    2.1. [Paso 1. Clonar repositorio](#paso-1-clonar-repositorio)
  
    2.2. [Paso 2. Crear contenedor Docker y subir a DockerHub](#paso-2-crear-contenedor-docker-y-subir-a-dockerhub)
  
    2.4. [Paso 3. Desplegar contenedor en Azure (Instancias de contenedor)](#paso-3-desplegar-contenedor-en-azure-instancias-de-contenedor)

<a name="pasos-deploy"></a>
#### **Pasos Deploy**

<a name="paso-1-clonar-repositorio"></a>
##### **Paso 1.** Clonar repositorio:

- Clonar repositorio: `git clone https://github.com/teamght/dog-face-cropper.git`.
- O descargarlo desde GitHub Desktop.

<a name="paso-2-crear-contenedor-docker-y-subir-a-dockerhub"></a>
##### **Paso 2.** Crear contenedor Docker y subir a DockerHub:

- Desde consola CMD ubicarse en la carpeta donde se ha clonado el respositorio.
- Iniciar sesión en Docker: `docker login`.
- Crear el contenedor: `docker build -t teamght/mascotas-face-cropper-app -f Dockerfile .`
- Iniciar el contenedor: `docker run -it -p 5000:5000 --name mascotas-face-cropper-app teamght/mascotas-face-cropper-app`
- Identificar el ID para subir a DockerHub: `docker ps -a`
- Confirmar cambios para subir a DockerHub: `docker commit 88b9ef6501a8 teamght/mascotas-face-cropper-app`. Para este ejemplo se usa el ID "88b9ef6501a8" y nombre de usuario "teamght".
- Subir contenedor a DockerHub: `docker push teamght/mascotas-face-cropper-app`. Para este ejemplo se usa el nombre de usuario "teamght".
- ❗ El proceso de subida puede tardar varios minutos dependiendo de la conexión a internet.

<a name="paso-3-desplegar-contenedor-en-azure-instancias-de-contenedor"></a>
##### **Paso 3.** Desplegar contenedor en Azure (Instancias de contenedor):

- En Azure ubicar el servicio Instancias de contenedor.
- Luego, dar click en el botón "Agregar".
- Completar el formulario de creación con: Nombre del contenedor, Origen de imagen, Imagen y Tamaño. Para este ejemplo se usó como Imagen "teamght/mascotas-face-cropper-app", donde "teamght" es el nombre del usuario donde se desplegó en DockerHub.
- ❗ El tamaño de la imagen pesa al rededor de 2.0GB. Por este motivo se debe modificar el valor por defecto de Azure y subirlo a 3.0GB.
![Imagen1](https://raw.githubusercontent.com/fcernafukuzaki/IATos/main/imagenes_tutorial/Imagen1.png)
- En la pestaña de Redes se debe habilitar el puerto 5000 como TCP.
![Imagen2](https://raw.githubusercontent.com/fcernafukuzaki/IATos/main/imagenes_tutorial/Imagen2.png)
- Finalmente, click en botón "Revisar y Crear" o "Crear". Y esperar que termine la creación.
- ❗ Para obtener el IP público del contenedor se debe dar click sobre el nombre del contenedor y dar click en "Información general". El IP se mostrará cuando la creación haya finalizado.
![Imagen3](https://raw.githubusercontent.com/fcernafukuzaki/IATos/main/imagenes_tutorial/Imagen3.png)
