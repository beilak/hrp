from dependency_injector import containers, providers
from pydantic.env_settings import BaseSettings
from hrp.org.org.controllers import UserFactory, UnitFactory


class OrgContainer(containers.DeclarativeContainer):
    """Org. container"""

    config: providers.Configuration = providers.Configuration()

    user_factory: providers.Factory = providers.Factory(
        UserFactory,
    )

    unit_factory: providers.Factory = providers.Factory(
        UnitFactory,
    )

    @staticmethod
    def create_container(settings: BaseSettings) -> 'OrgContainer':
        """ Org container crater"""
        container: OrgContainer = OrgContainer()
        container.config.from_pydantic(settings)
        return container
