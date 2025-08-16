from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, database, auth

router = APIRouter(prefix="/api/posts", tags=["Likes"])

@router.post("/{id}/like")
def like_post(id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(auth.get_current_user)):
    if not db.query(models.Post).filter(models.Post.id == id).first():
        raise HTTPException(status_code=404, detail="Post not found")
    if db.query(models.Like).filter(models.Like.user_id == current_user.id, models.Like.post_id == id).first():
        raise HTTPException(status_code=400, detail="Already liked this post")
    like = models.Like(user_id=current_user.id, post_id=id)
    db.add(like)
    db.commit()
    return {"message": "Post liked"}
