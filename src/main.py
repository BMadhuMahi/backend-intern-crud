from fastapi import FastAPI
from . import models, database
from .routers import auth, posts, likes, comments

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Blog API with Likes & Comments")

app.include_router(auth.router)
app.include_router(posts.router)
app.include_router(likes.router)
app.include_router(comments.router)
