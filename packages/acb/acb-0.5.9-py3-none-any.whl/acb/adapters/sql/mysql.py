import typing as t

from acb.depends import depends
from ._base import SqlBase
from ._base import SqlBaseSettings


class SqlSettings(SqlBaseSettings):
    _driver: str = "mysql+mysqldb"
    _async_driver: str = "mysql+asyncmy"
    pool_pre_ping: t.Optional[bool] = True


class Sql(SqlBase): ...


depends.set(Sql)
