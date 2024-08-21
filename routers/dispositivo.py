from fastapi import APIRouter, Query

from models.dispositivo import DispositivoEletrico
from models.comodo import Comodo
from models.residencia import Residencia

from schemas.dispositivo import EletrodomesticoCreate, EletrodomesticoUpdate, EletrodomesticoRead

from utils.messages import eletrodomesticod_delete_message
from utils.erros import comodo_not_found_error, residencia_not_found_error, eletrodomestico_not_found_error
from utils.enuns import EnumGetEletrodomesticos


router = APIRouter(prefix="/eletrodomesticos", tags=["Eletrodomésticos"])

@router.post("/", response_model=EletrodomesticoRead)
def create_eletrodomestico(eletrodomestico: EletrodomesticoCreate):

    comodo = Comodo.get_or_none(Comodo.id == eletrodomestico.comodo_id)

    if not comodo:
        return comodo_not_found_error()

    residencia = Residencia.get_or_none(Residencia.id == comodo.residencia)

    if not residencia:
        return residencia_not_found_error()

    new_eletrodomestico = DispositivoEletrico.create(
        **eletrodomestico.model_dump()
    )
    return new_eletrodomestico

@router.get("/", response_model=EletrodomesticoRead | list[EletrodomesticoRead])
# @router.get("/")
def get_item(
    item_type: EnumGetEletrodomesticos = Query(...),
    item_id: int = Query(...),
):
    if item_type == EnumGetEletrodomesticos.eletrodomestico:
        eletrodomestico = DispositivoEletrico.get_or_none(DispositivoEletrico.id == item_id)

        if not eletrodomestico:
            raise eletrodomestico_not_found_error()

        return eletrodomestico

    elif item_type == EnumGetEletrodomesticos.comodo:
        comodo = Comodo.get_or_none(Comodo.id == item_id)

        if not comodo:
            raise comodo_not_found_error()

        eletrodomesticos_do_comodo = DispositivoEletrico.select().where(DispositivoEletrico.comodo == item_id)

        return list(eletrodomesticos_do_comodo)

    elif item_type == EnumGetEletrodomesticos.residencia:

        residencia  = Residencia.get_or_none(Residencia.id == item_id)

        if not residencia:
            raise residencia_not_found_error()

        eletrodomesticos_da_residencia = DispositivoEletrico.select().where(DispositivoEletrico.residencia == item_id)

        return list(eletrodomesticos_da_residencia)


@router.put("/{eletrodomestico_id}", response_model=EletrodomesticoRead)
def update_eletrodomestico(eletrodomestico_id: int, eletrodomestico_update: EletrodomesticoUpdate):
    eletrodomestico_db = DispositivoEletrico.get_or_none(DispositivoEletrico.id == eletrodomestico_id)

    if not eletrodomestico_db:
        return eletrodomestico_not_found_error()

    update_data = eletrodomestico_update.model_dump(exclude_unset=True)
    DispositivoEletrico.update(**update_data).where(DispositivoEletrico.id == eletrodomestico_id).execute()

    return DispositivoEletrico.get_by_id(eletrodomestico_id)


@router.delete("/{eletrodomestico_id}")
def delete_eletrodomestico(eletrodomestico_id: int):

    eletrodomestico = DispositivoEletrico.get_or_none(DispositivoEletrico.id == eletrodomestico_id)

    if not eletrodomestico:
        return eletrodomestico_not_found_error()

    eletrodomestico.delete_instance()

    return eletrodomesticod_delete_message()