from pydantic import BaseModel, Field


class EletrodomesticoCreate(BaseModel):
    residencia_id: int
    comodo_id: int
    nome: str
    consumo: float = Field(..., gt=0)
    uso_diario: float = Field(..., ge=0, le=24)


class EletrodomesticoUpdate(BaseModel):
    nome: str | None
    consumo: int | None = Field(None, gt=0)
    uso_diario: int | None = Field(None, ge=0, le=24)


class EletrodomesticoRead(BaseModel):
    id: int
    residencia_id: int
    comodo_id: int
    nome: str
    consumo: float
    uso_diario: float

    class Config:
        from_attributes = True
