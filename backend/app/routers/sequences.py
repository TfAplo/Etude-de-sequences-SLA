from fastapi import APIRouter

#fichier de définition des routes demandées par l'utilisateur

router = APIRouter()

@router.get("/sequences")
def get_users():
    return [{"id": 1, "name": "seq1"}, {"id": 2, "name": "seq2"}]

@router.post("/sequences")
def create_user(seq: dict):
    return {"message": "sequence created", "seq": seq}