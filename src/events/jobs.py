from typing import Protocol,ParamSpecArgs, ParamSpecKwargs

from dependency_injector.wiring import Provide, inject

from src.tools.di import Container
from src.warehouse.reposiotores.flags_repo import FlagsRepo



async def first_run_configs():

    flags_repo : FlagsRepo = await Container.flags_repo()

    await flags_repo.config_flags()


