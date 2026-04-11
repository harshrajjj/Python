from typing import List, Optional
from pydantic import BaseModel  

class Comment(BaseModel):
    id: int
    content: str    
    replies: Optional[List['Comment']] = None

class Post(BaseModel):
    id: int
    title: str
    content: str
    comments: List[Comment]
Comment.model_rebuild()# Resolve forward references
post = Post(
    id=1,
    title="My First Post",
    content="This is my first post!",
    comments=[
        Comment(id=1, content="Great post!"),
        Comment(
            id=2,
            content="Thanks for sharing!",
            replies=[
                Comment(id=3, content="I agree!"),
                Comment(id=4, content="Me too!")
            ]
        )
        ]
)

print(post)
print(post.comments)
print(post.comments[1].replies)