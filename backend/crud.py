from sqlalchemy.orm import Session
from models import Account
from schemas import AccountCreate, AccountUpdate


# CREATE
def create_account(db: Session, account):
    acc = Account(**account.dict())
    db.add(acc)
    db.commit()
    db.refresh(acc)
    return acc

# READ ALL
def get_accounts(db: Session):
    return db.query(Account).all()

# READ ONE
def get_account(db: Session, acc_id: int):
    return db.query(Account).filter(Account.id == acc_id).first()

# UPDATE
def update_account(db: Session, acc_id: int, data):
    acc = get_account(db, acc_id)
    if not acc:
        return None
    acc.name = data.name
    acc.email = data.email
    db.commit()
    db.refresh(acc)
    return acc

# DELETE
def delete_account(db: Session, acc_id: int):
    acc = get_account(db, acc_id)
    if not acc:
        return False
    db.delete(acc)
    db.commit()
    return True
