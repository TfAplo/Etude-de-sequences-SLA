from fastapi import APIRouter

#fichier de définition des routes demandées par l'utilisateur

router = APIRouter()

@router.get("/")
def get_index():
    return {"message": "Hello from backend"}