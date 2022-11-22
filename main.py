from fastapi import FastAPI, Depends
from database import engine, Base, SessionLocal
from sqlalchemy.orm import Session
import schemas 
import models 

Base.metadata.create_all(engine)

app = FastAPI()

async def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get('/')
async def getAllItems(session: Session=Depends(get_session)):
    obj = session.query(models.ItemModelTable).all()
    return obj

@app.get('/get/{ids}')
async def getItemDetail(ids:int, session: Session=Depends(get_session)):
    obj = session.query(models.ItemModelTable).get(ids)
    return obj

@app.post('/create')
async def createItem(item:schemas.Item, session: Session=Depends(get_session)):
    newItem = models.ItemModelTable(task=item.task)
    session.add(newItem)
    session.commit()
    session.refresh(newItem)
    return newItem

@app.put('/update/{ids}')
async def updateItem(ids:int, item:schemas.Item, session: Session=Depends(get_session)):
    obj = session.query(models.ItemModelTable).get(ids)
    obj.task = item.task
    session.commit()
    return obj

@app.delete('/delete/{ids}')
async def deleteItem(ids:int, session: Session=Depends(get_session)):
    obj = session.query(models.ItemModelTable).get(ids)
    session.delete(obj)
    session.commit()
    session.close()
    return {'Success':'Item has been deleted...'}



