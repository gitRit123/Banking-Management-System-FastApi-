from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List


from database import SessionLocal, engine
import models, schemas, crud


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Banking Management System")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root ():
    return {"Message": "Welcome to Banking Management System API"}
# CREATE
@app.post("/accounts", response_model=schemas.AccountResponse)
def create_account(account: schemas.AccountCreate, db: Session = Depends(get_db)):
    return crud.create_account(db, account)

# READ ALL
@app.get("/accounts", response_model=List[schemas.AccountResponse])
def read_accounts(db: Session = Depends(get_db)):
    return crud.get_accounts(db)

# READ ONE
@app.get("/accounts/{acc_id}", response_model=schemas.AccountResponse)
def read_account(acc_id: int, db: Session = Depends(get_db)):
    acc = crud.get_account(db, acc_id)
    if not acc:
        raise HTTPException(status_code=404, detail="Account not found")
    return acc

# UPDATE
@app.put("/accounts/{acc_id}", response_model=schemas.AccountResponse)
def update_account(acc_id: int, data: schemas.AccountUpdate, db: Session = Depends(get_db)):
    acc = crud.update_account(db, acc_id, data)
    if not acc:
        raise HTTPException(status_code=404, detail="Account not found")
    return acc

# DELETE
@app.delete("/accounts/{acc_id}")
def delete_account(acc_id: int, db: Session = Depends(get_db)):
    success = crud.delete_account(db, acc_id)
    if not success:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"message": "Account deleted successfully"}
