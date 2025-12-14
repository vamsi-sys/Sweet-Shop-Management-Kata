from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional

from app.core.dependencies import (
    get_db,
    get_current_user,
    get_admin_user
)
from app.models.sweet import Sweet
from app.schemas.sweet import (
    SweetCreate,
    SweetOut,
    SweetUpdate
)
from app.services.sweet_service import (
    create_sweet,
    purchase_sweet,
    update_sweet,
    delete_sweet,
    restock_sweet
)

router = APIRouter(prefix="/sweets", tags=["Sweets"])


# -------------------------------------------------
# Create sweet (Protected)
# -------------------------------------------------
@router.post(
    "",
    response_model=SweetOut,
    status_code=status.HTTP_201_CREATED
)
def add_sweet(
    data: SweetCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    sweet = Sweet(**data.dict())
    return create_sweet(db, sweet)


# -------------------------------------------------
# List all sweets (Protected)
# -------------------------------------------------
@router.get(
    "",
    response_model=List[SweetOut]
)
def list_sweets(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return db.query(Sweet).all()


# -------------------------------------------------
# Search sweets (Protected)
# -------------------------------------------------
@router.get(
    "/search",
    response_model=List[SweetOut]
)
def search_sweets(
    name: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    min_price: Optional[float] = Query(None, ge=0),
    max_price: Optional[float] = Query(None, ge=0),
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    query = db.query(Sweet)

    if name:
        query = query.filter(Sweet.name.ilike(f"%{name}%"))

    if category:
        query = query.filter(Sweet.category.ilike(f"%{category}%"))

    if min_price is not None:
        query = query.filter(Sweet.price >= min_price)

    if max_price is not None:
        query = query.filter(Sweet.price <= max_price)

    return query.all()


# -------------------------------------------------
# Update sweet (Admin only)
# -------------------------------------------------
@router.put(
    "/{sweet_id}",
    response_model=SweetOut
)
def update_sweet_api(
    sweet_id: int,
    data: SweetUpdate,
    db: Session = Depends(get_db),
    admin=Depends(get_admin_user)
):
    return update_sweet(db, sweet_id, data)


# -------------------------------------------------
# Delete sweet (Admin only)
# -------------------------------------------------
@router.delete(
    "/{sweet_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_sweet_api(
    sweet_id: int,
    db: Session = Depends(get_db),
    admin=Depends(get_admin_user)
):
    delete_sweet(db, sweet_id)
    return None


# -------------------------------------------------
# Purchase sweet (Protected)
# -------------------------------------------------
@router.post(
    "/{sweet_id}/purchase",
    response_model=SweetOut
)
def purchase_sweet_api(
    sweet_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return purchase_sweet(db, sweet_id)


# -------------------------------------------------
# Restock sweet (Admin only)
# -------------------------------------------------
@router.post(
    "/{sweet_id}/restock",
    response_model=SweetOut
)
def restock_sweet_api(
    sweet_id: int,
    amount: int = Query(..., gt=0),
    db: Session = Depends(get_db),
    admin=Depends(get_admin_user)
):
    return restock_sweet(db, sweet_id, amount)
