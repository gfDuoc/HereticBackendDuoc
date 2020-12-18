"""
to start de virtual env: env\Scripts\activate
 to start de app in cmd: uvicorn sql_app.main:app --reload
"""
from typing import List , Optional

from fastapi import Depends, FastAPI, HTTPException , Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

tags_metadata  = [
    {
        "name":"Acciones",
        "description":"acciones que pueden hacer los usuarios"
    },
    {        "name":"Actividades",
        "description":"..."
    },
        {        "name":"Cargo",
                 "description":" El cargo permite discriminar a los usuarios a nivel de empresa, esta información es meramente una formalidad ya que no afecta el funcionamiento del sistema."
    },
        {        "name":"Empresa",
                 "description":"..."
    },
        {        "name":"Estado tarea",
          "description":"..."
    },
        {        "name":"Historial Registro",
          "description":"..."
    },
        {        "name":"Historico Tarea",
         "description":"..."
    },
        {        "name":"Lista",
         "description":"..."
    },
        {        "name":"Perfil",
          "description":"..."
    },
        {        "name":"Permiso",
         "description":"El permiso es la sintesis de las acciones que puede realizar un perfil especifico."
    },
        {        "name":"Tarea",
         "description":"..."
    },
        {        "name":"TokenRegistro",
          "description":"..."
    },
        {        "name":"usuarios",
         "description":"..."
    },
]

app = FastAPI(
    title="process API",
    description="Heretek version to try save ours lives.",
    version="0.1",
    openapi_tags=tags_metadata,
)

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

##routas
#############################################################################
#accion [R]
@app.get("/acciones/", response_model=List[schemas.AccionBase], tags=["Acciones"])
def read_actions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    actions = crud.get_acciones(db, skip=skip, limit=limit)
   #return jsonable_encoder(actions)
    return actions

@app.get("/acciones/{action_id}",response_model=schemas.AccionBase,  tags=["Acciones"])
def read_action(action_id: int , db:Session = Depends(get_db)):
    db_action = crud.get_accion(db, acccion_id=action_id)
    if db_action is None:
        raise HTTPException(status_code=404, detail="Accion no encontrada")
    return db_action

#############################################################################
#Actividad [CRUD]
@app.post("/actividades/",response_model=schemas.ActividadCreate,tags=["Actividades"])
def create_activities(activity:schemas.ActividadCreate, db: Session= Depends(get_db)):
    db_activity = crud.create_actividades(db=db,actividad=activity)
    return db_activity

@app.get("/actividades/", response_model=List[schemas.ActividadBase], tags=["Actividades"])
def read_activities(skip: int= 0, limit: int = 100, db: Session = Depends(get_db)):
    activities = crud.get_actividades(db, skip=skip, limit=limit)
    return activities

@app.put("/actividades/{activity_id}",response_model=schemas.ActividadBase,tags=["Actividades"])
def update_activity(activity:schemas.ActividadBase,db:Session=Depends(get_db)):
    db_activity = crud.update_actividades(db=db,actividad=activity)
    return db_activity

@app.get("/actividades/{activity_id}",response_model=schemas.ActividadBase, tags=["Actividades"])
def read_activity(activity_id:int, db:Session = Depends(get_db)):
    db_activity = crud.get_actividad(db, actividad_id=activity_id)
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Actividad no encontrada")
    return db_activity

@app.delete("/actividades/{activity_id}",response_class=Response,responses={ 200: {"description": " successfully deleted"}, 404: {"description": "not found"}, }, tags=["Actividades"])
def delete_activity(activity_id:int, db:Session= Depends(get_db)):
    db_activity = crud.delete_actividades(db=db,actividad_id=activity_id)
    return Response(status_code=200)

#############################################################################
#Cargo [CRUD]
@app.post("/cargos/", response_model=schemas.CargoCreate, tags=["Cargo"])
def create_charge(charge: schemas.CargoCreate, db: Session = Depends(get_db)):
    db_charge = crud.create_cargos(db=db, cargo=charge )
    return db_charge

@app.get("/cargos/", response_model=List[schemas.CargoBase], tags=["Cargo"])
def read_charges(skip: int= 0, limit: int = 100, db: Session = Depends(get_db)):
    charges = crud.get_cargos(db, skip=skip, limit=limit)
    return charges

@app.put("/cargos/{charge_id}", response_model=schemas.CargoBase, tags=["Cargo"])
def update_charge(charge:schemas.CargoBase, db:Session= Depends(get_db)):
    db_charge = crud.update_carg(db=db,cargo=charge)
    return db_charge

@app.get("/cargos/{charge_id}", response_model=schemas.CargoBase, tags=["Cargo"])
def read_charge(charge_id: int, db:Session = Depends(get_db)):
    db_charge = crud.get_cargo(db, cargo_id=charge_id)
    if db_charge is None:
            raise HTTPException(status_code=404, detail="Cargo no encontrado")
    return db_charge

@app.delete("/cargos/{charge_id}",response_class=Response,responses={ 200: {"description": " successfully deleted"}, 404: {"description": "not found"}, }, tags=["Cargo"])
def delete_company(charge_id: int, db:Session = Depends(get_db)):
    db_charge = crud.delete_cargos(db=db, cargo_id=charge_id)
    return Response(status_code=200)

#############################################################################
#Empresa [CRUD]
@app.post("/empresas/",response_model=schemas.EmpresaCreate,tags=["Empresa"])
def create_company(company:schemas.EmpresaCreate, db: Session= Depends(get_db)):
    #db_company = crud.
    db_company = crud.create_empresas(db= db , empresa= company)
    return  db_company

@app.get("/empresas/", response_model=List[schemas.EmpresaBase],tags=["Empresa"])
def read_companies(skip: int= 0, limit: int = 100, db: Session = Depends(get_db)):
    companies = crud.get_empresas(db, skip=skip, limit=limit)
    return companies

@app.put("/empresas/{company_id}", response_model=schemas.EmpresaBase,tags=["Empresa"])
def update_company(company:schemas.EmpresaCreate, db: Session= Depends(get_db)):
    db_company = crud.update_empresas(db=db, empresa=company )
    return db_company


@app.get("/empresas/{company_id}", response_model=schemas.EmpresaBase,tags=["Empresa"])
def read_company(company_id: int, db:Session = Depends(get_db)):
    db_company = crud.get_empresa(db,empresa_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="empresa no encontreada")
    return db_company

@app.delete("/empresas/{company_id}",response_class=Response,responses={ 200: {"description": " successfully deleted"}, 404: {"description": "not found"}, }, tags=["Empresa"])
def delete_company(company_id:int, db:Session = Depends(get_db)):
    db_company = crud.delete_empresas(db=db,empresa_id=company_id)
    return Response(status_code=200)
#############################################################################
#EstadoTarea [R]
@app.get("/estado_tareas/", response_model=List[schemas.Estado_tareaBase],tags=["Estado tarea"])
def read_status(skip: int= 0, limit: int = 100, db: Session = Depends(get_db)):
    status = crud.get_estadoTareas(db, skip=skip, limit=limit)
    return status

@app.get("/estado_tareas/{status_id}", response_model=schemas.Estado_tareaBase, tags=["Estado tarea"])
def read_state(state_id:int, db:Session = Depends(get_db)):
    db_state = crud.get_estadoTarea(db, estadoTarea_id=state_id)
    if db_state is None:
        raise HTTPException(status_code=404, detail="estado no encontrado")
    return db_state

#############################################################################
#HistorialRegistro[CR]
@app.post("/historial_registros", response_model=schemas.historial_registroCreate,tags=["Historial Registro"])
def create_records(record:schemas.historial_registroCreate, db:Session= Depends(get_db)):
    db_record = crud.create_historialRegistros(db=db, historial= record)
    return db_record

@app.get("/historial_registros/", response_model=List[schemas.historial_registroBase],tags=["Historial Registro"])
def read_records(skip: int= 0, limit: int = 100, db: Session = Depends(get_db)):
    records = crud.get_historialRegistros(db, skip=skip, limit=limit)
    return records

@app.get("/historial_registros/{history_id}",response_model=schemas.historial_registroBase,tags=["Historial Registro"])
def read_record(record_id:int, db:Session = Depends(get_db)):
    db_record = crud.get_historialRegistro(db, historialRegistro_id=record_id)
    if db_record is None:
        raise HTTPException(status_code=404,detail="registro no encontrado")
    return db_record

#############################################################################
#HistoricoTarea [CR]
@app.post("/historico_tareas/",response_model=schemas.historial_registroCreate,tags=["Historico Tarea"])
def create_history(history:schemas.historial_registroCreate,db:Session= Depends(get_db)):
    db_history = crud.create_historicoTareas(db=db, historico=history)
    return db_history

@app.get("/historico_tareas/", response_model=List[schemas.historico_tareaBase],tags=["Historico Tarea"])
def read_histories(skip: int= 0, limit: int = 100, db: Session = Depends(get_db)):
    histories = crud.get_historicoTareas(db, skip=skip, limit=limit)
    return  histories

@app.get("/historico_tareas/{history_id}",response_model=schemas.historico_tareaBase,tags=["Historico Tarea"])
def read_history(history_id:int,db:Session = Depends(get_db)):
    db_history = crud.get_historicoTarea(db,historicoTarea_id=history_id)
    if db_history is None:
        raise HTTPException(status_code=404, detail="historico no encontrado")
    return db_history

#############################################################################
#Lista[CRUD]
@app.post("/listas/",response_model=schemas.ListaCreate,tags=["Lista"])
def create_lists(listas:schemas.ListaCreate,db:Session=Depends(get_db)):
    db_lista = crud.create_listas(db=db,lista=listas)
    return db_lista


@app.get("/listas/", response_model=List[schemas.ListaBase],tags=["Lista"])
def read_lists(skip: int= 0, limit: int = 100, db: Session = Depends(get_db)):
    lists = crud.get_listas(db, skip=skip, limit=limit)
    return lists

@app.put("/listas/{list_id}",response_model=schemas.ListaBase,tags=["Lista"])
def update_lists(lista:schemas.ListaBase,db:Session=Depends(get_db)):
    db_lista = crud.update_lista(db=db,lista=lista)
    return db_lista

@app.get("/listas/{list_id}", response_model=schemas.ListaBase,tags=["Lista"])
def read_list(list_id:int , db: Session = Depends(get_db)):
    db_list = crud.get_lista(db, lista_id=list_id)
    if db_list is None:
        raise HTTPException(status_code=404,detail="no se encuentra la lista")
    return db_list

@app.delete("/listas/{list_id}",response_class=Response,responses={ 200: {"description": " successfully deleted"}, 404: {"description": "not found"}, },tags=["Lista"])
def delete_list(list_id:int , db: Session = Depends(get_db)):
    db_delete = crud.delete_lista(db=db,lista_id=list_id)
    return Response(status_code=200)

#############################################################################
#Perfil[R]
@app.get("/perfiles/", response_model=List[schemas.PerfilBase],tags=["Perfil"])
def read_profiles(skip: int= 0, limit: int = 100, db: Session = Depends(get_db)):
    profiles = crud.get_perfiles(db, skip=skip, limit=limit)
    return profiles

@app.get("/perfiles/{profile_id}", response_model=schemas.PerfilBase,tags=["Perfil"])
def read_profile(profile_id:int, db:Session = Depends(get_db)):
     db_profile = crud.get_perfil(db, perfil_id=profile_id)
     if db_profile is None:
         raise HTTPException(status_code=404,detail="no se encuentra el perfil")
     return db_profile

#############################################################################
#Permiso [R]
@app.get("/permisos/", response_model=List[schemas.PermisoBase],tags=["Permiso"])
def read_permits(skip: int= 0, limit: int = 100, db: Session = Depends(get_db)):
    permits = crud.get_permisos(db, skip=skip, limit=limit)
    return permits

@app.get("/permisos/{permit_id}", response_model=schemas.PermisoBase,tags=["Permiso"])
def read_permit(permit_id:int,db:Session = Depends(get_db)):
    db_permit = crud.get_permiso(db,permiso_id=permit_id)
    if db_permit is None:
        raise HTTPException(status_code=404, detail="permiso no encontrado")
    return db_permit

#############################################################################
#Proceso [CRUD]
@app.post("/procesos/",response_model=schemas.ProcesoCreate,tags=["Proceso"])
def create_processes(processes:schemas.ProcesoCreate, db:Session=Depends(get_db)):
    db_processs = crud.create_procesos(db=db,proceso=processes)
    return db_processs

@app.get("/procesos/", response_model=List[schemas.ProcesoBase],tags=["Proceso"])
def read_processes(skip: int= 0, limit: int = 100, db: Session = Depends(get_db)):
    process = crud.get_procesos(db, skip=skip, limit=limit)
    return process

@app.put("/procesos/{process_id}",response_model=schemas.ProcesoBase,tags=["Proceso"])
def update_processes(processes:schemas.ProcesoBase,db:Session=Depends(get_db)):
    db_process = crud.update_procesos(db=db,proceso=processes)
    return db_process

@app.get("/procesos/{process_id}",response_model=schemas.ProcesoBase, tags=["Proceso"])
def read_process(process_id:int, db:Session = Depends(get_db)):
    db_process = crud.get_proceso(db,proceso_id=process_id) 
    if db_process is None:
        raise HTTPException(status_code=404, detail="proceso no encontrado")
    return db_process

@app.delete("/procesos/{process_id}",response_class=Response,responses={ 200: {"description": " successfully deleted"}, 404: {"description": "not found"}, },tags=["Proceso"])
def delete_process(process_id:int, db:Session = Depends(get_db)):
      db_process = crud.delete_proceso(db,proceso_id=process_id) 
      return Response(status_code=200)

#############################################################################
#Tarea [CRUD]
@app.post("/tareas/",response_model=schemas.TareaCreate,tags=["Tarea"])
def create_tasks(tasks:schemas.TareaCreate,db:Session = Depends(get_db)):
   db_task = crud.create_tarea(db=db,tarea=tasks)
   return db_task

@app.get("/tareas/", response_model=List[schemas.TareaBase],tags=["Tarea"])
def read_tasks(skip: int= 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_tareas(db, skip=skip, limit=limit)
    return tasks

@app.put("/tareas/{tasks_id}",response_model=schemas.TareaBase,tags=["Tarea"])
def update_tasks(tasks:schemas.TareaBase,db:Session = Depends(get_db)):
    db_task = crud.update_tarea(db=db, tarea=tasks)
    return db_task

@app.get("/tareas/{tasks_id}",response_model=schemas.TareaBase,tags=["Tarea"])
def read_task(task_id:int, db:Session = Depends(get_db)):
    db_task = crud.get_tarea(db, tarea_id=task_id)
    if db_task is None:
         raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return db_task

@app.delete("/tareas/{tasks_id}",response_class=Response,responses={ 200: {"description": " successfully deleted"}, 404: {"description": "not found"}, },tags=["Tarea"])
def delete_task(task_id:int, db:Session = Depends(get_db)):
       db_task = crud.delete_tarea(db, tarea_id=task_id)
       return Response(status_code=200)

#############################################################################
#TokenRegistro [CR]
@app.post("/tokens",response_model=schemas.TokenRegistroCreate,deprecated=True, tags=["TokenRegistro"])
def create_tokens(tokens:schemas.TokenRegistroCreate,db:Session=Depends(get_db)):
    db_tokens = crud.create_tokens(db=db, token=tokens)
    return db_tokens

@app.get("/tokens",response_model=List[schemas.TokenRegistroBase], deprecated=True, tags=["TokenRegistro"])
def read_tokens(skip: int= 0, limit: int = 100, db: Session = Depends(get_db)):
    tokens = crud.get_tokens(db, skip=skip, limit=limit)
    return tokens

@app.get("/tokens/{id_token}",response_model=schemas.TokenRegistroBase,deprecated=True, tags=["TokenRegistro"])
def read_token(id_token:int,db:Session= Depends(get_db)):
    db_token = crud.get_token(db, token_id=id_token)
    if db_token is None: 
        raise HTTPException(status_code=404, detail="token no encontrado")
    return db_token

#############################################################################
# usuarios [CRUD]
@app.post("/usuarios/",response_model=schemas.UsuarioCreate,tags=["usuarios"])
def create_users(users:schemas.UsuarioCreate,db: Session= Depends(get_db)):
    db_user = crud.create_usuarios(db=db,user=users)
    return db_user

@app.get("/usuarios/", response_model=List[schemas.UsuarioBase],tags=["usuarios"])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_usarios(db, skip=skip, limit=limit)
    #return jsonable_encoder(users)
    return (users)

@app.put("/usuarios/{user_id}",response_model=schemas.UsuarioBase,tags=["usuarios"])
def update_users(user:schemas.UsuarioBase,db:Session=Depends(get_db)):
    db_user = crud.update_usuarios(db=db,user=user)
    return db_user

@app.get("/usuarios/{user_id}", response_model=schemas.UsuarioBase,tags=["usuarios"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_usario(db,user_id = user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="usuario no encontrado")
    return db_user

@app.delete("/usuarios/{user_id}",response_class=Response,responses={ 200: {"description": " successfully deleted"}, 404: {"description": "not found"}, },tags=["usuarios"])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_usuarios(db,user_id = user_id)
    return Response(status_code=200)

