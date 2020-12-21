##form datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, CHAR, TIMESTAMP
from sqlalchemy.orm import relationship

from.database import Base

class Accion(Base):
 __tablename__  = "accion"
 id_accion = Column('id_accion',Integer, primary_key=True, nullable=False)
 descripcion = Column('descripcion', String, nullable=False)
 informacionadicional = Column('informacionadicional', String)

class Actividad(Base):
    __tablename__  ='actividad'
    id_actividad = Column('id_actividad',Integer, primary_key=True, nullable=False)
    descripcion = Column('descripcion', String , nullable=False)  
    realizado = Column('realizado', CHAR , nullable=False)
    lista_id = Column('lista_id',Integer, ForeignKey('lista.id_lista'), nullable=False)


class Cargo (Base):
    __tablename__  ='cargo'
    id_cargo = Column('id_cargo',Integer,  primary_key=True, nullable=False)
    descripcion = Column('descripcion', String,  nullable=False) 

class Empresa(Base):
    __tablename__ ='empresa'
    id_empresa = Column('id_empresa',Integer, primary_key=True, nullable=False)
    razonsocial = Column('razonsocial', String, nullable=False)

class Estado_tarea(Base):
    __tablename__ ='estado_tarea'
    id_estadotarea = Column('id_estadotarea',Integer, primary_key=True, nullable=False)
    descripcion = Column('descripcion', String, nullable=False)

class historial_registro(Base):
    __tablename__  ='historial_registro'
    id_historial = Column('id_historial',Integer, primary_key=True, nullable=False)
    usuario = Column('usuario', String, nullable=False)
    accion = Column('accion', String, nullable=False)

class historico_tarea(Base):
    __tablename__  = 'historico_tarea'
    id_historicotarea = Column('id_historicotarea',Integer, primary_key=True, nullable=False) 
    fechacambio = Column('fechacambio', DateTime, nullable=False) 
    estadotarea_id = Column('estadotarea_id',Integer, ForeignKey('estado_tarea.id_estadotarea'), nullable=False)
    usuario_id = Column('usuario_id',Integer, ForeignKey('usuario.id_usuario'), nullable=False)
    tarea_id = Column('tarea_id',Integer, ForeignKey('tarea.id_tarea'), nullable=False)

class Lista(Base):
    __tablename__  ='lista'
    id_lista =  Column('id_lista',Integer,  primary_key=True, nullable=False)
    descripcion = Column('descripcion', String,  nullable=False)
    tarea_id = Column('tarea_id',Integer, ForeignKey('tarea.id_tarea'),  nullable=False)

class Perfil(Base):
    __tablename__  ='perfil'
    id_perfil = Column('id_perfil',Integer,  primary_key=True, nullable=False)
    descripcion = Column('descripcion', String,  nullable=False)

class Permiso(Base):
    __tablename__  ='permiso'
    id_permiso = Column('id_permiso',Integer,primary_key=True, nullable=False,)
    accion_id = Column('accion_id',Integer, ForeignKey('accion.id_accion'),nullable=False)
    perfil_id = Column('perfil_id',Integer, ForeignKey('perfil.id_perfil'),nullable=False)

class Proceso(Base):
    __tablename__  ='proceso'
    id_proceso= Column('id_proceso',Integer,  primary_key=True, nullable=False)
    descripcion = Column('descripcion', String,  nullable=False)
    modelo = Column('modelo', CHAR(length=1),  nullable=False)
    inicio = Column('inicio', DateTime,  nullable=False)
    termino = Column('termino', DateTime)
    detalle = Column('detalle', String)
    empresa_id =Column('empresa_id',Integer, ForeignKey('empresa.id_empresa'),  nullable=False)

class Tarea(Base):
    __tablename__  = 'tarea'
    id_tarea = Column('id_tarea',Integer, primary_key=True, nullable=False)
    descripcion = Column('descripcion', String, nullable=False)
    observaciones = Column('observaciones', String)
    inicio = Column('inicio', DateTime) 
    termino = Column('termino', DateTime)
    nivel = Column('nivel',Integer, nullable=False)
    usuario_id = Column('usuario_id',Integer, ForeignKey('usuario.id_usuario'), nullable=False)
    proceso_id = Column('proceso_id',Integer, ForeignKey('proceso.id_proceso'), nullable=False)
    inicioregistrado = Column('inicioregistrado', DateTime)
    terminoregistrado =Column('terminoregistrado', DateTime)
    estadotarea_id = Column('estadotarea_id',Integer, ForeignKey('estado_tarea.id_estadotarea'), nullable=False)
    tareamadre = Column('tareamadre',Integer, ForeignKey('tarea.id_tarea'))

class TokenRegistro(Base):
    __tablename__ ='token_registro'
    token = Column('token', String,  nullable=False)
    vencimiento = Column('vencimiento', TIMESTAMP,  nullable=False)
    usuario_id =  Column('usuario_id', Integer,  nullable=False)
    id_token = Column('id_token', Integer,primary_key=True , nullable=False)


class Usuario (Base):
 __tablename__ = 'usuario' 
 id_usuario = Column('id_usuario', Integer, primary_key=True, nullable=False) 
 nombreusuario = Column('nombreusuario', String, nullable=False)
 contrasenna  = Column('contrasenna', String, nullable=False)
 nombre = Column('nombre', String, nullable=False)
 apellidos = Column('apellidos', String, nullable=False)
 correo = Column('correo', String)
 perfil_id = Column('perfil_id', Integer, ForeignKey('perfil.id_perfil'), nullable=False)
 cargo_id = Column('cargo_id', Integer, ForeignKey('cargo.id_cargo'), nullable=False)
 empresa_id = Column('empresa_id', Integer, ForeignKey('empresa.id_empresa'), nullable=False)

"""
oracle_db = sqlalchemy.create_engine('oracle://ADMINPROCESS:Duoc2020@192.168.1.8:1521/XE')
 result = connection.execute("SELECT nombre FROM usuario")
 metadata = MetaData()
 user = Table('usuario',metadata, autoload=True, autoload_with=engine)
 Table('accion', MetaData(bind=None), Column('id_accion', NUMBER(asdecimal=False), table=<accion>, primary_key=True, nullable=False), Column('descripcion', VARCHAR(length=100), table=<accion>, nullable=False), Column('informacionadicional', VARCHAR(length=1000), table=<accion>), schema=None)
Table('actividad', MetaData(bind=None), Column('id_actividad', NUMBER(asdecimal=False), table=<actividad>, primary_key=True, nullable=False), Column('descripcion', VARCHAR(length=250), table=<actividad>, nullable=False), Column('realizado', CHAR(length=1), table=<actividad>, nullable=False), Column('lista_id', NUMBER(asdecimal=False), ForeignKey('lista.id_lista'), table=<actividad>, nullable=False), schema=None)
Table('cargo', MetaData(bind=None), Column('id_cargo', NUMBER(asdecimal=False), table=<cargo>, primary_key=True, nullable=False, comment='Identificador del cargo. El cargo permite discriminar a los usuarios a nivel de empresa, esta información es meramente una formalidad ya que no afecta el funcionamiento del sistema.'), Column('descripcion', VARCHAR(length=80), table=<cargo>, nullable=False, comment='Nombre público con el que será conocido el cargo.'), schema=None)
Table('empresa', MetaData(bind=None), Column('id_empresa', NUMBER(asdecimal=False), table=<empresa>, primary_key=True, nullable=False), Column('razonsocial', VARCHAR(length=100), table=<empresa>, nullable=False), schema=None)
Table('estado_tarea', MetaData(bind=None), Column('id_estadotarea', NUMBER(asdecimal=False), table=<estado_tarea>, primary_key=True, nullable=False), Column('descripcion', VARCHAR(length=50), table=<estado_tarea>, nullable=False), schema=None)
Table('historial_registro', MetaData(bind=None), Column('id_historial', NUMBER(asdecimal=False), table=<historial_registro>, primary_key=True, nullable=False), Column('usuario', VARCHAR(length=150), table=<historial_registro>, nullable=False), Column('accion', VARCHAR(length=500), table=<historial_registro>, nullable=False), schema=None)
Table('historico_tarea', MetaData(bind=None), Column('id_historicotarea', NUMBER(asdecimal=False), table=<historico_tarea>, primary_key=True, nullable=False), Column('fechacambio', DATE(), table=<historico_tarea>, nullable=False), Column('estadotarea_id', NUMBER(asdecimal=False), ForeignKey('estado_tarea.id_estadotarea'), table=<historico_tarea>, nullable=False), Column('usuario_id', NUMBER(asdecimal=False), ForeignKey('usuario.id_usuario'), table=<historico_tarea>, nullable=False), Column('tarea_id', NUMBER(asdecimal=False), ForeignKey('tarea.id_tarea'), table=<historico_tarea>, nullable=False), schema=None)
Table('lista', MetaData(bind=None), Column('id_lista', NUMBER(asdecimal=False), table=<lista>, primary_key=True, nullable=False), Column('descripcion', VARCHAR(length=50), table=<lista>, nullable=False), Column('tarea_id', NUMBER(asdecimal=False), ForeignKey('tarea.id_tarea'), table=<lista>, nullable=False), schema=None)
Table('perfil', MetaData(bind=None), Column('id_perfil', NUMBER(asdecimal=False), table=<perfil>, primary_key=True, nullable=False), Column('descripcion', VARCHAR(length=50), table=<perfil>, nullable=False), schema=None)
Table('permiso', MetaData(bind=None), Column('id_permiso', NUMBER(asdecimal=False), table=<permiso>, primary_key=True, nullable=False, comment='Identificador del permiso. El permiso es la sintesis de las acciones que puede realizar un perfil especifico. '), Column('accion_id', NUMBER(asdecimal=False), ForeignKey('accion.id_accion'), table=<permiso>, nullable=False), Column('perfil_id', NUMBER(asdecimal=False), ForeignKey('perfil.id_perfil'), table=<permiso>, nullable=False), schema=None)
Table('proceso', MetaData(bind=None), Column('id_proceso', NUMBER(asdecimal=False), table=<proceso>, primary_key=True, nullable=False), Column('descripcion', VARCHAR(length=100), table=<proceso>, nullable=False), Column('modelo', CHAR(length=1), table=<proceso>, nullable=False), Column('inicio', DATE(), table=<proceso>, nullable=False), Column('termino', DATE(), table=<proceso>), Column('detalle', VARCHAR(length=4000), table=<proceso>), Column('empresa_id', NUMBER(asdecimal=False), ForeignKey('empresa.id_empresa'), table=<proceso>, nullable=False), schema=None)
Table('tarea', MetaData(bind=None), Column('id_tarea', NUMBER(asdecimal=False), table=<tarea>, primary_key=True, nullable=False), Column('descripcion', VARCHAR(length=100), table=<tarea>, nullable=False), Column('observaciones', VARCHAR(length=4000), table=<tarea>), Column('inicio', DATE(), table=<tarea>), Column('termino', DATE(), table=<tarea>), Column('nivel', NUMBER(asdecimal=False), table=<tarea>, nullable=False), Column('usuario_id', NUMBER(asdecimal=False), ForeignKey('usuario.id_usuario'), table=<tarea>, nullable=False), Column('proceso_id', NUMBER(asdecimal=False), ForeignKey('proceso.id_proceso'), table=<tarea>, nullable=False), Column('inicioregistrado', DATE(), table=<tarea>), Column('terminoregistrado', DATE(), table=<tarea>), Column('estadotarea_id', NUMBER(asdecimal=False), ForeignKey('estado_tarea.id_estadotarea'), table=<tarea>, nullable=False), Column('tareamadre', NUMBER(asdecimal=False), ForeignKey('tarea.id_tarea'), table=<tarea>), schema=None)
Table('token_registro', MetaData(bind=None), Column('token', VARCHAR(length=500), table=<token_registro>, nullable=False, comment='reserva el token recibido'), Column('vencimiento', TIMESTAMP(), table=<token_registro>, nullable=False, comment='fecha de expiración del token'), Column('usuario_id', INTEGER(), table=<token_registro>, nullable=False, comment='ID usuario asociado'), Column('id_token', INTEGER(), table=<token_registro>, nullable=False), schema=None)
Table('usuario', MetaData(bind=None), Column('id_usuario', NUMBER(asdecimal=False), table=<usuario>, primary_key=True, nullable=False), Column('nombreusuario', VARCHAR(length=50), table=<usuario>, nullable=False), Column('contrasenna', VARCHAR(length=150), table=<usuario>, nullable=False), Column('nombre', VARCHAR(length=150), table=<usuario>, nullable=False), Column('apellidos', VARCHAR(length=150), table=<usuario>, nullable=False), Column('correo', VARCHAR(length=150), table=<usuario>), Column('perfil_id', NUMBER(asdecimal=False), ForeignKey('perfil.id_perfil'), table=<usuario>, nullable=False), Column('cargo_id', NUMBER(asdecimal=False), ForeignKey('cargo.id_cargo'), table=<usuario>, nullable=False), Column('empresa_id', NUMBER(asdecimal=False), ForeignKey('empresa.id_empresa'), table=<usuario>, nullable=False), schema=None)
"""