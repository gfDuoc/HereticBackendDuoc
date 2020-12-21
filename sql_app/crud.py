from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from . import models, schemas
import datetime

#############################################################################
#accion [R]
def get_accion(db: Session, acccion_id: int):
    return db.query(models.Accion).filter(models.Accion.id_accion == acccion_id).first()

def get_acciones(db: Session, skip: int = 0 , limit : int = 100):
    return db.query(models.Accion).offset(skip).limit(limit).all()

#############################################################################
#Actividad [CRUD]
def get_actividad(db: Session, actividad_id: int):
    return db.query(models.Actividad).filter(models.Actividad.id_actividad == actividad_id).first()

def get_actividades(db: Session, skip: int = 0 , limit : int = 100, lista_id: int = 0):
    db_actividad = []
    if lista_id > 0:
        db_actividad =  db.query(models.Actividad).filter(models.Actividad.lista_id == lista_id).offset(skip).limit(limit).all()
    if lista_id < 1:
        db_actividad = db.query(models.Actividad).offset(skip).limit(limit).all()
    return db_actividad

def create_actividades(db: Session, actividad: schemas.ActividadCreate):
    last_id = db.query(func.max(models.Actividad.id_actividad)).scalar()
    if last_id is None:
        last_id = 0
    db_actividad = models.Actividad(**actividad.dict())
    db_actividad.id_actividad = (last_id+1)
    db.add(db_actividad)
    db.commit()
    db.refresh(db_actividad)
    return db_actividad

def update_actividades(db: Session, actividad: schemas.ActividadBase):
   db_actividad = db.query(models.Actividad).filter(models.Actividad.id_actividad == actividad.id_actividad).first()
   remplace = models.Actividad(**actividad.dict(exclude_unset=True))
   if remplace.descripcion is not None:
       db_actividad.descripcion = remplace.descripcion
   if remplace.realizado is not None:
       db_actividad.realizado = remplace.realizado
   if remplace.lista_id is not None:
       db_actividad = remplace.lista_id
   db.commit()
   return db_actividad

def delete_actividades(db:Session,actividad_id:int):
    db_actividad = db.query(models.Actividad).filter(models.Actividad.id_actividad == actividad_id).first()
    db_actividad = db.delete(db_actividad)
    db.commit()
    return db_actividad


#############################################################################
#Cargo [CRUD]
def get_cargo(db: Session, cargo_id: int):
    return db.query(models.Cargo).filter(models.Cargo.id_cargo == cargo_id).first()

def get_cargos(db: Session, skip: int = 0 , limit : int = 100):
    return db.query(models.Cargo).offset(skip).limit(limit).all()

def create_cargos(db: Session , cargo: schemas.CargoCreate):
    last_id = db.query(func.max(models.Cargo.id_cargo)).scalar()
    if last_id is None:
        last_id = 0
    db_cargo = models.Cargo(**cargo.dict())
    db_cargo.id_cargo = (last_id+1)
    db.add(db_cargo)
    db.commit()
    db.refresh(db_cargo)
    return db_cargo

def update_carg(db:Session , cargo:schemas.CargoBase):
    db_cargo =  db.query(models.Cargo).filter(models.Cargo.id_cargo == cargo.id_cargo).first()
    remplace =models.Cargo(**cargo.dict(exclude_unset=True))
    if remplace.descripcion is not None:
        db_cargo.descripcion =  remplace.descripcion
    db.commit()
    return db_cargo

def delete_cargos(db:Session, cargo_id: int):
     db_cargo =  db.query(models.Cargo).filter(models.Cargo.id_cargo == cargo_id).first()
     db_cargo = db.delete(db_cargo)
     db.commit()
     return db_cargo


#############################################################################
#Empresa [CRUD]
def get_empresa(db: Session, empresa_id: int):
    return db.query(models.Empresa).filter(models.Empresa.id_empresa == empresa_id).first()

def get_empresas(db: Session, skip: int = 0 , limit : int = 100):
    return db.query(models.Empresa).offset(skip).limit(limit).all()

def create_empresas(db: Session , empresa: schemas.EmpresaCreate):
    last_id = db.query(func.max(models.Empresa.id_empresa)).scalar()
    if last_id is None:
        last_id = 0
    db_empresa = models.Empresa(**empresa.dict())
    db_empresa.id_empresa = (last_id+1)
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

def update_empresas(db: Session , empresa: schemas.EmpresaBase):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id_empresa == empresa.id_empresa).first()
    remplace =  models.Empresa(**empresa.dict(exclude_unset=True))
    if remplace.razonsocial is not None:
        db_empresa.razonsocial = remplace.razonsocial
    db.commit()
    return db_empresa

def delete_empresas(db:Session, empresa_id:int):
    db_empresa = db.query(models.Empresa).filter(models.Empresa.id_empresa == empresa_id).first()
    db_empresa = db.delete(db_empresa)
    db.commit()
    return db_empresa

#############################################################################
#EstadoTarea [R]
def get_estadoTarea(db: Session, estadoTarea_id: int):
    return db.query(models.Estado_tarea).filter(models.Estado_tarea.id_estadotarea == estadoTarea_id).first()

def get_estadoTareas(db: Session, skip: int = 0 , limit : int = 100):
    return db.query(models.Estado_tarea).offset(skip).limit(limit).all()

#############################################################################
#HistorialRegistro[CR]
def get_historialRegistro(db:Session, historialRegistro_id: int):
    return db.query(models.historial_registro).filter(models.historial_registro.id_historial == historialRegistro_id).first()

def get_historialRegistros (db:Session, skip: int = 0, limit : int = 100):
    return db.query(models.historial_registro).offset(skip).limit(limit).all()

def create_historialRegistros(db:Session,historial: schemas.historial_registroCreate):
    last_id = db.query(func.max(models.historial_registro.id_historial)).scalar()
    if last_id is None:
        last_id = 0
    db_historial = models.historial_registro(**historial.dict())
    db_historial.id_historial = (last_id+1)
    db.add(db_historial)
    db.commit()
    db.refresh(db_historial)
    return db_historial

#############################################################################
#HistoricoTarea [CR]
def get_historicoTarea(db:Session, historicoTarea_id: int):
    return db.query(models.historico_tarea).filter(models.historico_tarea.id_historicotarea == historicoTarea_id).first()

def get_historicoTareas(db:Session,skip: int = 0, limit : int = 100):
    return db.query(models.historico_tarea).offset(skip).limit(limit).all()

def create_historicoTareas(db:Session, historico:schemas.historico_tareaCreate):
    last_id = db.query(func.max(models.historico_tarea.id_historicotarea)).scalar()
    if last_id is None:
        last_id = 0
    db_historico = models.historico_tarea(**historico.dict())
    db_historico.id_historicotarea = (last_id+1)
    db.add(db_historico)
    db.commit()
    db.refresh(db_historico)
    return db_historico

#############################################################################
#Lista[CRUD]
def get_lista(db:Session, lista_id: int):
    return db.query(models.Lista).filter(models.Lista.id_lista == lista_id).first()

def get_listas(db:Session,skip: int = 0, limit : int = 100, task: int = 0):
    db_lista  = []
    if task > 0:
     db_lista = db.query(models.Lista).filter(models.Lista.tarea_id == task).offset(skip).limit(limit).all()
    if task < 1:
     db_lista = db.query(models.Lista).offset(skip).limit(limit).all()
    return db_lista

def create_listas(db:Session, lista:schemas.ListaCreate):
    last_id = db.query(func.max(models.Lista.id_lista)).scalar()
    if last_id is None:
        last_id = 0
    db_lista = models.Lista(**lista.dict())
    db_lista.id_lista = (last_id+1)
    db.add(db_lista)
    db.commit()
    db.refresh(db_lista)
    return db_lista

def update_lista(db:Session,lista:schemas.ListaBase):
    db_lista = db.query(models.Lista).filter(models.Lista.id_lista == lista.id_lista).first()
    remplace = models.Lista(**lista.dict(exclude_unset=True))
    if remplace.descripcion is not None:
        db_lista.descripcion = remplace.descripcion
    if remplace.tarea_id is not None:
        db_lista.tarea_id = remplace.tarea_id
    db.commit()
    return db_lista

def delete_lista(db:Session,lista_id:int):
    db_lista = db.query(models.Lista).filter(models.Lista.id_lista == lista_id).first()
    db_lista = db.delete(db_lista)
    db.commit()
    return db_lista

#############################################################################
#Perfil[R]
def get_perfil(db:Session, perfil_id: int):
    return db.query(models.Perfil).filter(models.Perfil.id_perfil == perfil_id).first()

def get_perfiles(db:Session, skip: int = 0 , limit : int = 100):
    return db.query(models.Perfil).offset(skip).limit(limit).all()

#############################################################################
#Permiso [R]
def get_permiso(db:Session, permiso_id: int):
    return db.query(models.Permiso).filter(models.Permiso.id_permiso == permiso_id).first()

def get_permisos(db:Session, skip: int = 0 , limit : int = 100):
    return db.query(models.Permiso).offset(skip).limit(limit).all()

#############################################################################
#Proceso [CRUD]
def get_proceso(db:Session, proceso_id: int):
    return db.query(models.Proceso).filter(models.Proceso.id_proceso == proceso_id).first()

def get_procesos(db:Session, skip: int = 0 , limit : int = 100):
    return db.query(models.Proceso).offset(skip).limit(limit).all()

def create_procesos(db:Session, proceso: schemas.ProcesoCreate):
    last_id = db.query(func.max(models.Proceso.id_proceso)).scalar()
    if last_id is None:
        last_id = 0
    db_proceso = models.Proceso(**proceso.dict())
    db_proceso.id_proceso = (last_id+1)
    db.add(db_proceso)
    db.commit()
    db.refresh(db_proceso)
    return db_proceso

def update_procesos(db:Session, proceso: schemas.ProcesoCreate):
    remplace  = models.Proceso(**proceso.dict(exclude_unset=True))
    db_proceso = db.query(models.Proceso).filter(models.Proceso.id_proceso == proceso.id_proceso).first()
    if remplace.descripcion is not None:
        db_proceso.descripcion = remplace.descripcion
    if remplace.modelo is not None:
        db_proceso.modelo = remplace.modelo
    if remplace.inicio is not None:
        db_proceso.inicio = remplace.inicio
    if remplace.termino is not None:
        db_proceso.termino = remplace.termino
    if remplace.detalle is not None:
        db_proceso.detalle = remplace.detalle
    if remplace.empresa_id is not None:
        db_proceso.empresa_id = remplace.empresa_id
    db.commit()
    return db_proceso
 
def delete_proceso(db: Session, proceso_id: int):
    db_proceso = db.query(models.Proceso).filter(models.Proceso.id_proceso == proceso_id).first()
    db_proceso = db.delete(db_proceso)
    db.commit()
    return db_proceso

#############################################################################
#Tarea [CRUD]
def get_tarea(db:Session, tarea_id: int):
    return db.query(models.Tarea).filter(models.Tarea.id_tarea == tarea_id).first()

def get_tareas(db:Session, skip: int = 0 , limit : int = 100, proceso_id: int = 0):
    db_tareas = []
    if proceso_id > 0:
        db_tareas = db.query(models.Tarea).filter(models.Tarea.proceso_id == proceso_id).offset(skip).limit(limit).all()
    if proceso_id < 1:
        db_tareas = db.query(models.Tarea).offset(skip).limit(limit).all()
    return db_tareas

def get_tareas_by_user(db:Session,user_id: int):
    return db.query(models.Tarea).filter(models.Tarea.usuario_id == user_id).all()

def create_tarea(db:Session, tarea: schemas.TareaCreate):
    last_id = db.query(func.max(models.Tarea.id_tarea)).scalar()
    db_tarea = models.Tarea(**tarea.dict())
    print(tarea.dict())
    if last_id is None:
        last_id = 0
    db_tarea.id_tarea = (last_id+1)
    if db_tarea.tareamadre == 0:
        db_tarea.tareamadre = None
    print(db_tarea.__dict__)
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)
    return db_tarea

def update_tarea(db:Session,tarea:schemas.TareaUpdate):
    db_tarea = db.query(models.Tarea).filter(models.Tarea.id_tarea == tarea.id_tarea).first()
    remplace = models.Tarea(**tarea.dict(exclude_unset=True))
    if remplace.descripcion is not None:
         db_tarea.descripcion = remplace.descripcion
    if remplace.observaciones is not None:
        db_tarea.observaciones = remplace.observaciones
    if remplace.inicio is not None:
        db_tarea.inicio = remplace.inicio
    if remplace.termino is not None:
        db_tarea.termino = remplace.termino
    if remplace.nivel is not None:
        db_tarea.nivel = remplace.nivel
    if remplace.usuario_id is not None:
        db_tarea.user_id = remplace.usuario_id
    if remplace.proceso_id is not None:
        db_tarea.proceso_id = remplace.proceso_id
    if remplace.inicioregistrado is not None:
        db_tarea.inicioregistrado =  remplace.inicioregistrado
    if remplace.terminoregistrado is not None:
        db_tarea.terminoregistrado = remplace.terminoregistrado
    if remplace.estadotarea_id is not None:
        db_tarea.estadotarea_id = remplace.estadotarea_id
    if remplace.tareamadre is not None:
        db_tarea.tareamadre = remplace.tareamadre
    if remplace.estadotarea_id == 2:
        db_tarea.inicioregistrado =  datetime.datetime.now()
    if remplace.estadotarea_id == 3:
        db_tarea.terminoregistrado = datetime.datetime.now()
    db.commit()
    return db_tarea

def delete_tarea(db:Session, tarea_id: int):
    db_tarea= db.query(models.Tarea).filter(models.Tarea.id_tarea == tarea_id).first()
    db_tarea = db.delete(db_tarea)
    db.commit()
    return db_tarea

#############################################################################
#TokenRegistro [CR]
def get_token(db:Session, token_id: int):
    return db.query(models.TokenRegistro).filter(models.TokenRegistro.id_token == token_id).first()

def get_tokens(db:Session, skip: int = 0 , limit : int = 100):
    return db.query(models.TokenRegistro).offset(skip).limit(limit).all()

def create_tokens(db:Session, token:schemas.TokenRegistroCreate):
    last_id = db.query(func.max(models.TokenRegistro.id_token)).scalar()
    if last_id is None:
        last_id = 0
    db_token = models.TokenRegistro(**token.dict()) 
    db_token.id_token = (last_id+1)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token

#############################################################################
# usuarios [CRUD]
def get_usario(db: Session, user_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id_usuario == user_id).first()

def get_usario_by_name(db:Session, username):
    return db.query(models.Usuario).filter(models.Usuario.nombreusuario == username).first()

def get_usarios(db: Session, skip: int = 0 , limit : int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()

def create_usuarios(db: Session , user: schemas.UsuarioCreate):
    last_id = db.query(func.max(models.Usuario.id_usuario)).scalar()
    if last_id is None:
        last_id = 0
    db_user = models.Usuario(**user.dict())
    db_user.id_usuario = (last_id+1)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_usuarios(db: Session, user:schemas.UsuarioBase):
    db_user = db.query(models.Usuario).filter(models.Usuario.id_usuario == user.id_usuario).first()
    remplace = models.Usuario(**user.dict(exclude_unset=True))
    if remplace.nombreusuario is not None:
        db_user.nombreusuario = remplace.nombreusuario
    if remplace.contrasenna is not None:
        db_user.contrasenna = remplace.contrasenna
    if remplace.nombre is not None:
        db_user.nombre = remplace.nombre
    if remplace.apellidos is not None:
        db_user.apellidos = remplace.apellidos
    if remplace.correo is not None:
        db_user.correo = remplace.correo
    if remplace.perfil_id is not None:
        db_user.perfil_id = remplace.perfil_id
    if remplace.cargo_id is not None:
        db_user.cargo_id = remplace.cargo_id
    if remplace.empresa_id is not None:
        db_user.empresa_id = remplace.empresa_id
    db.commit()
    return db_user

def delete_usuarios(db: Session, user_id: int):
    db_user = db.query(models.Usuario).filter(models.Usuario.id_usuario == user_id).first()
    db_user = db.delete(db_user)
    db.commit()
    return db_user