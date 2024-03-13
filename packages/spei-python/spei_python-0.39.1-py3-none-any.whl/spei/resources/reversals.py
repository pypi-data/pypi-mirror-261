from spei import types
from spei.resources.orden import Orden


class DevolucionNoAcreditada(Orden):
    op_cd_clave = types.TipoDevolucionOrdenPago


class DevolucionExtemporaneaNoAcreditada(Orden):
    op_tc_clave_ord: types.TipoCuentaOrdenPago
    op_cuenta_ord: str

    op_concepto_pag_2: str
    op_ref_numerica: str

    op_cd_clave: types.TipoDevolucionOrdenPago

    op_folio_ori: int = None
    paq_folio_ori: int = None

    op_fecha_oper_ori: int
    op_rastreo_ori: str
    op_monto_intereses: float
    op_monto_ori: float


class DevolucionAcreditada(Orden):
    op_rastreo_ori: str


class DevolucionExtemporaneaAcreditada(Orden):
    op_cuenta_ord: str

    op_concepto_pag_2: str
    op_ref_numerica: str

    op_folio_ori: int = None
    paq_folio_ori: int = None

    op_fecha_oper_ori: int
    op_rastreo_ori: str
    op_monto_ori: float


class DevolucionEspecialAcreditada(Orden):
    op_rastreo_ori: str
    op_monto_ori: float

    op_indica_ben_rec: int = None


class DevolucionExtemporaneaEspecialAcreditada(Orden):
    op_tc_clave_ord: types.TipoCuentaOrdenPago
    op_cuenta_ord: str

    op_concepto_pag_2: str
    op_ref_numerica: str

    op_folio_ori: int = None
    paq_folio_ori: int = None

    op_fecha_oper_ori: int
    op_rastreo_ori: str
    op_monto_ori: float

    op_indica_ben_rec: int = None
