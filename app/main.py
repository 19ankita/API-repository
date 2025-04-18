from fastapi import FastAPI, Response, status, HTTPException
from fastapi import Body 

from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI() #instance of FastAPI


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    
    
my_posts = [{"title": "title of post 1",
             "content": "content of post 1",
             "id": 1},
            
            {"title": "favourite food",
             "content": "I like pizza",
             "id": 2}]    

##Find a speific post in the list of posts
def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i        

#decorator
@app.get("/") #get() method is used to get the root directory when a client sends a request to the server
async def root():
    return {"message": "Hello Ankita Sarkar!!!!!!!!!!"}

@app.get("/posts", status_code=status.HTTP_201_CREATED)
def get_posts():
    return {"data": my_posts}

## How to extract the data from the body of a payload?
# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#     print(payload) #payload is the data that is sent in the request body
#     # Body(...) indicates that the payload is required
#     return {"new_post": f"title: {payload['title']}  content: {payload['content']}"}

## How to extract the data from the body of a payload?
# @app.post("/posts")
# def create_posts(post: Post):
#     print(post) 
#     print(post.title)
#     print(post.published)
#     print(post.rating)
#     print(post.dict()) #convert the pydantic model to a dictionary
#     return {"data": post}

#Adding an unique number to the posts
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(1, 100000)
    my_posts.append(post_dict)
    return {"data": post_dict} 

##grab the latest post
@app.get("/posts/latest", status_code=status.HTTP_201_CREATED)
def latest_post():
    post = my_posts[len(my_posts) -1]
    return {"detail": post}

# #Retrive only one post 
# @app.get("/posts/{id}")
# def get_posts(id: int, response: Response):
#     print(type(id))
#     #post = find_post(int(id))
#     post = find_post(id)
#     if not post:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {"message": f"post with id {id} is not found"}
#     return {"data": post}
#     #return {"One post": f"Here is the post {id}"}

@app.get("/posts/{id}")
def get_posts(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} not found")
    return {"data": post}
    

#delete a post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)    
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    my_posts.pop(index)
    #return {"message": f"post {id} is deleted successfully"}
    return Response(status_code=status.HTTP_204_NO_CONTENT)

##updating the post
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} does not exist")
    
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data": post_dict}