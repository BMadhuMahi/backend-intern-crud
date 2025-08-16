from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database, auth

router = APIRouter(prefix="/api/posts", tags=["Comments"])

@router.post("/{id}/comment", response_model=schemas.CommentOut)
def add_comment(id: int, comment: schemas.CommentCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    if not db.query(models.Post).filter(models.Post.id == id).first():
        raise HTTPException(status_code=404, detail="Post not found")
    new_comment = models.Comment(text=comment.text, user_id=current_user.id, post_id=id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

@router.get("/{id}/comments", response_model=List[schemas.CommentOut])
def get_comments(id: int, db: Session = Depends(database.get_db)):
    if not db.query(models.Post).filter(models.Post.id == id).first():
        raise HTTPException(status_code=404, detail="Post not found")
    return db.query(models.Comment).filter(models.Comment.post_id == id).all()
