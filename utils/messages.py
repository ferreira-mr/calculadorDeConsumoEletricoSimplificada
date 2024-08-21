from fastapi import status
from fastapi.responses import JSONResponse


def eletrodomesticod_delete_message():
    return JSONResponse(
        content={'message': 'Comodo deletado com sucesso!'},
        status_code=status.HTTP_202_ACCEPTED,
    )


def comodo_deleted_message():
    return JSONResponse(
        content={'message': 'Comodo deletado com sucesso!'},
        status_code=status.HTTP_202_ACCEPTED,
    )


def residenci_deleted_message():
    return JSONResponse(
        content={'message': 'Comodo deletado com sucesso!'},
        status_code=status.HTTP_202_ACCEPTED,
    )
