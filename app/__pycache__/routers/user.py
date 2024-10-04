from fastapi import FastAPI,Response,status,HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session  
from .. import models, schema, utils
from ..database import get_db

router = APIRouter()






@router.post("/users", status_code=status.HTTP_201_CREATED,response_model=schema.UserOut)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):

    #hash the password - User.password

    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_User = models.User(**user.dict())
    db.add(new_User)
    db.commit()
    db.refresh(new_User)

    return new_User

@router.get('/users/{id}', response_model=schema.UserOut)
def get_user(id:int, db: Session = Depends(get_db),):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id}does not exist")

    return user   