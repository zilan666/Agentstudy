from pydantic import BaseModel, Field


class ScenicSpot(BaseModel):
    id: int = Field(...,gt=0, description="The unique identifier of the scenic spot")
    name: str = Field(...,min_length=1,max_length=50)
    ticket_price: float = Field(default=0.0,ge=0, description="The price of the scenic spot ticket")
    city: str = Field(...,min_length=1,max_length=20, description="The city where the scenic spot is located")
    rating: float = Field(..., ge=0, le=5, description="The rating of the scenic spot (0 to 5)")
    tags: list[str] = []