from datetime import datetime, date, time
from typing import List, Optional
from pydantic import BaseModel

class AccionBase(BaseModel):
 id_accion : int
 descripcion : str
 informacionadicional : Optional[str] = None

 class Config:
    orm_mode = True

class ActividadBase(BaseModel):
    id_actividad :  Optional[int]
    descripcion : Optional[str]
    realizado : Optional[str]
    lista_id : Optional[int]

    class Config:
        orm_mode = True

class ActividadCreate(ActividadBase):
    id_actividad = 0

class CargoBase (BaseModel):
    id_cargo : int
    descripcion : str

    class Config:
        orm_mode = True

class CargoCreate (CargoBase):
    id_cargo = 0

class EmpresaBase(BaseModel):
    id_empresa : int
    razonsocial : str

    class Config:
        orm_mode = True   

class EmpresaCreate(EmpresaBase):
    id_empresa = 0


class Estado_tareaBase(BaseModel):
    id_estadotarea : int
    descripcion : str

    class Config:
        orm_mode = True

class historial_registroBase(BaseModel):
    id_historial : int
    usuario: str
    accion : str

    class Config:
        orm_mode = True

class historial_registroCreate(historial_registroBase):
    id_historial = 0
        
class historico_tareaBase(BaseModel):
    id_historicotarea : int
    fechacambio : datetime
    estadotarea_id : int
    usuario_id : int
    tarea_id : int

    class Config:
        orm_mode = True

class historico_tareaCreate(historico_tareaBase):
     id_historicotarea  = 0

class ListaBase(BaseModel):
    id_lista : int
    descripcion : str
    tarea_id : int

    class Config:
        orm_mode = True

class ListaCreate(ListaBase):
     id_lista = 0

class PerfilBase(BaseModel):
    id_perfil : int
    descripcion : str

    class Config:
        orm_mode = True

class PermisoBase(BaseModel):
    id_permiso : int
    accion_id : int
    perfil_id : int

    class Config:
        orm_mode = True

class ProcesoBase(BaseModel):
    id_proceso : int 
    descripcion : str
    modelo : str
    inicio : datetime
    termino : Optional[datetime]
    detalle : Optional[str]
    empresa_id : int

    class Config:
        orm_mode = True

class ProcesoCreate(ProcesoBase):
    id_proceso = 0

class TareaBase(BaseModel):
    id_tarea : int
    descripcion : str
    observaciones : Optional[str]
    inicio : Optional[datetime]
    termino : Optional[datetime]
    nivel : int
    usuario_id : int
    proceso_id : int
    inicioregistrado : Optional[datetime]
    terminoregistrado : Optional[datetime]
    estadotarea_id : int
    tareamadre : Optional[int]

    class Config:
        orm_mode = True

class TareaUpdate(TareaBase):
    descripcion : str
    observaciones : Optional[str]
    inicio : Optional[datetime]
    termino : Optional[datetime]
    nivel : Optional[int]
    usuario_id : Optional[int]
    proceso_id : Optional[int]
    inicioregistrado : Optional[datetime]
    terminoregistrado : Optional[datetime]
    estadotarea_id :  Optional[int]
    tareamadre : Optional[int]

class TareaCreate(TareaBase):
      id_tarea  = 0

class TokenRegistroBase(BaseModel):
    token : str
    vencimiento : datetime
    usuario_id : int
    id_token : int

    class Config:
        orm_mode = True

class TokenRegistroCreate(TokenRegistroBase):
    id_token = 0

class UsuarioBase (BaseModel):
    id_usuario : int
    nombreusuario : str
    contrasenna  : str
    nombre : str
    apellidos : str
    correo : Optional[str]
    perfil_id : int
    cargo_id : int
    empresa_id : int
    
    class Config:
        orm_mode = True

class UsuarioCreate(UsuarioBase):
    id_usuario = 0

class LoginTipo(BaseModel):
    idUsuario: int
    idPerfil: int
    nombreUsuario: str
    token : str

class accesoTipo(BaseModel):
    username : str
    password  : str

class HomeCustom(BaseModel):
    idUsuario: int