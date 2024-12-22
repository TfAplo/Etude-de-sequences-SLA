from app.models.Sequence import SequenceBase, SequenceCreate, SequenceRead

#fichier de définition des fonctions liées aux séquences à partir des models et utilisés dans routers

# def get_user_by_id(db: Session, user_id: int) -> Optional[SequenceRead]:
#     """
#     Récupère un utilisateur par son ID.
#     """
#     seq = db.query(Sequence).filter(Sequence.id == sequence_id).first()
#     return SequenceRead.from_orm(sequence) if sequence else None

