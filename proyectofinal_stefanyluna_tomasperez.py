from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash

# Inicialización de bases de datos
bd_sql = SQLAlchemy()
bd_mongo = PyMongo()

# Modelos SQL
class UsuarioSQL(bd_sql.Model):
    id_usuario = bd_sql.Column(bd_sql.Integer, primary_key=True)
    nombre_usuario = bd_sql.Column(bd_sql.String(50), nullable=False, unique=True)
    clave = bd_sql.Column(bd_sql.String(128), nullable=False)
    rol = bd_sql.Column(bd_sql.String(20), nullable=False)  # 'Admin', 'Doctor', 'Técnico'

class PacienteSQL(bd_sql.Model):
    id = bd_sql.Column(bd_sql.String(50), primary_key=True)
    nombre = bd_sql.Column(bd_sql.String(50), nullable=False)
    edad = bd_sql.Column(bd_sql.Integer, nullable=False)
    genero = bd_sql.Column(bd_sql.String(10), nullable=False)

class DiagnosticoSQL(bd_sql.Model):
    id = bd_sql.Column(bd_sql.Integer, primary_key=True)
    id_paciente = bd_sql.Column(bd_sql.String(50), bd_sql.ForeignKey('paciente_sql.id'), nullable=False)
    tipo_imagen = bd_sql.Column(bd_sql.String(20), nullable=False)  # MRI, CT, Rayos X
    probabilidad_resultado = bd_sql.Column(bd_sql.Float, nullable=False)  # % de probabilidad
    fecha_imagen = bd_sql.Column(bd_sql.Date, nullable=False)
    fecha_diagnostico = bd_sql.Column(bd_sql.Date, nullable=False)
    revision_estado = bd_sql.Column(bd_sql.Boolean, default=False)  # Sí/No

# Modelo para MongoDB
class ImagenMongo(bd_mongo.Document):
    id_imagen = bd_mongo.StringField(required=True)
    id_paciente = bd_mongo.StringField(required=True)
    tipo_imagen = bd_mongo.StringField(required=True)  # MRI, CT, Rayos X
    fecha_imagen = bd_mongo.DateField(required=True)
    analisis_resultado = bd_mongo.FloatField(required=True)  # % de análisis
    notas_tecnico = bd_mongo.StringField(required=True)  # Notas del técnico
    zona_estudio = bd_mongo.StringField(required=True)  # Abdomen, cabeza, extremidades
    revision_estado = bd_mongo.BooleanField(default=False)  # Estado de revisión

class ReporteMongo(bd_mongo.Document):
    id_imagen = bd_mongo.StringField(required=True)
    id_paciente = bd_mongo.StringField(required=True)
    fecha = bd_mongo.DateField(required=True)
    tipo_imagen = bd_mongo.StringField(required=True)  # MRI, CT, Rayos X
    parte_cuerpo = bd_mongo.StringField(required=True)  # Cerebro, abdomen, etc.
    ruta_imagen = bd_mongo.StringField(required=True)  # Ruta de la imagen
    analisis_resultado = bd_mongo.DictField(required=True)  # Análisis
    notas_tecnicas = bd_mongo.ListField(mongo.DictField())  # Notas técnicas

# Operaciones CRUD para Usuarios
def agregar_usuario(datos):
    usuario_nuevo = UsuarioSQL(
        nombre_usuario=datos['nombre_usuario'],
        clave=generate_password_hash(datos['clave']),
        rol=datos['rol']
    )
    bd_sql.session.add(usuario_nuevo)
    bd_sql.session.commit()

def obtener_usuario_por_id(id_usuario):
    return UsuarioSQL.query.get(id_usuario)

def modificar_usuario(id_usuario, datos):
    usuario = UsuarioSQL.query.get(id_usuario)
    if usuario:
        usuario.nombre_usuario = datos.get('nombre_usuario', usuario.nombre_usuario)
        usuario.clave = generate_password_hash(datos.get('clave', usuario.clave))
        usuario.rol = datos.get('rol', usuario.rol)
        bd_sql.session.commit()
        return usuario
    return None

def borrar_usuario(id_usuario):
    usuario = UsuarioSQL.query.get(id_usuario)
    if usuario:
        bd_sql.session.delete(usuario)
        bd_sql.session.commit()

# Operaciones CRUD para Pacientes
def agregar_paciente(datos):
    paciente_nuevo = PacienteSQL(
        id=datos['id'],
        nombre=datos['nombre'],
        edad=datos['edad'],
        genero=datos['genero']
    )
    bd_sql.session.add(paciente_nuevo)
    bd_sql.session.commit()

def obtener_paciente_por_id(id_paciente):
    return PacienteSQL.query.get(id_paciente)

def modificar_paciente(id_paciente, datos):
    paciente = PacienteSQL.query.get(id_paciente)
    if paciente:
        paciente.nombre = datos.get('nombre', paciente.nombre)
        paciente.edad = datos.get('edad', paciente.edad)
        paciente.genero = datos.get('genero', paciente.genero)
        bd_sql.session.commit()
        return paciente
    return None

def borrar_paciente(id_paciente):
    paciente = PacienteSQL.query.get(id_paciente)
    if paciente:
        bd_sql.session.delete(paciente)
        bd_sql.session.commit()

# Operaciones CRUD para Diagnósticos
def agregar_diagnostico(datos):
    nuevo_diagnostico = DiagnosticoSQL(
        id_paciente=datos['id_paciente'],
        tipo_imagen=datos['tipo_imagen'],
        probabilidad_resultado=datos['probabilidad_resultado'],
        fecha_imagen=datos['fecha_imagen'],
        fecha_diagnostico=datos['fecha_diagnostico'],
        revision_estado=datos.get('revision_estado', False)
    )
    bd_sql.session.add(nuevo_diagnostico)
    bd_sql.session.commit()

def obtener_diagnostico_por_id(id_diagnostico):
    return DiagnosticoSQL.query.get(id_diagnostico)

def modificar_diagnostico(id_diagnostico, datos):
    diagnostico = DiagnosticoSQL.query.get(id_diagnostico)
    if diagnostico:
        diagnostico.tipo_imagen = datos.get('tipo_imagen', diagnostico.tipo_imagen)
        diagnostico.probabilidad_resultado = datos.get('probabilidad_resultado', diagnostico.probabilidad_resultado)
        diagnostico.fecha_imagen = datos.get('fecha_imagen', diagnostico.fecha_imagen)
        diagnostico.fecha_diagnostico = datos.get('fecha_diagnostico', diagnostico.fecha_diagnostico)
        diagnostico.revision_estado = datos.get('revision_estado', diagnostico.revision_estado)
        bd_sql.session.commit()
        return diagnostico
    return None

def borrar_diagnostico(id_diagnostico):
    diagnostico = DiagnosticoSQL.query.get(id_diagnostico)
    if diagnostico:
        bd_sql.session.delete(diagnostico)
        bd_sql.session.commit()

# Operaciones CRUD para Imágenes
def guardar_imagen(datos):
    imagen_nueva = ImagenMongo(
        id_imagen=datos['id_imagen'],
        id_paciente=datos['id_paciente'],
        tipo_imagen=datos['tipo_imagen'],
        fecha_imagen=datos['fecha_imagen'],
        analisis_resultado=datos['analisis_resultado'],
        notas_tecnico=datos['notas_tecnico'],
        zona_estudio=datos['zona_estudio'],
        revision_estado=datos.get('revision_estado', False)
    )
    bd_mongo.db.imagenes.insert_one(imagen_nueva.to_dict())

    # Registro en SQL
    agregar_diagnostico(datos)

def obtener_imagen_por_id(id_imagen):
    return bd_mongo.db.imagenes.find_one({"id_imagen": id_imagen})

def modificar_imagen(id_imagen, datos):
    imagen = bd_mongo.db.imagenes.find_one({"id_imagen": id_imagen})
    if imagen:
        bd_mongo.db.imagenes.update_one(
            {"id_imagen": id_imagen},
            {"$set": {
                "revision_estado": datos.get('revision_estado', imagen['revision_estado']),
                "notas_tecnico": datos.get('notas_tecnico', imagen['notas_tecnico'])
            }}
        )

def borrar_imagen(id_imagen):
    imagen = bd_mongo.db.imagenes.find_one({"id_imagen": id_imagen})
    if imagen:
        bd_mongo.db.imagenes.delete_one({"id_imagen": id_imagen})
        borrar_diagnostico(imagen['id_paciente'])  # Sincronización con SQL