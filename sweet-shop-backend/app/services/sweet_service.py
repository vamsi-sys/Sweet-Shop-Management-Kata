from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.sweet import Sweet


# -------------------------------------------------
# Create sweet
# -------------------------------------------------
def create_sweet(db: Session, sweet: Sweet):
    db.add(sweet)
    db.commit()
    db.refresh(sweet)
    return sweet


# -------------------------------------------------
# Purchase sweet
# -------------------------------------------------
def purchase_sweet(db: Session, sweet_id: int):
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()

    if not sweet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sweet not found"
        )

    if sweet.quantity <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Sweet out of stock"
        )

    sweet.quantity -= 1
    db.commit()
    db.refresh(sweet)
    return sweet


# -------------------------------------------------
# Update sweet (Admin)
# -------------------------------------------------
def update_sweet(db: Session, sweet_id: int, data):
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()

    if not sweet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sweet not found"
        )

    for field, value in data.dict(exclude_unset=True).items():
        setattr(sweet, field, value)

    db.commit()
    db.refresh(sweet)
    return sweet


# -------------------------------------------------
# Delete sweet (Admin)
# -------------------------------------------------
def delete_sweet(db: Session, sweet_id: int):
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()

    if not sweet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sweet not found"
        )

    db.delete(sweet)
    db.commit()


# -------------------------------------------------
# Restock sweet (Admin)
# -------------------------------------------------
def restock_sweet(db: Session, sweet_id: int, amount: int):
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()

    if not sweet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sweet not found"
        )

    if amount <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Restock amount must be greater than zero"
        )

    sweet.quantity += amount
    db.commit()
    db.refresh(sweet)
    return sweet
