from dependency_injector import containers
from dependency_injector.providers import Configuration, Singleton
from pydantic.env_settings import BaseSettings
from .controllers import UserFactory, UnitFactory


class OrgContainer(containers.DeclarativeContainer):
    """Org. container"""

    wiring_config = containers.WiringConfiguration(modules=[".route.user", ".route.unit"])

    config: Configuration = Configuration()

    user_factory: Singleton[UserFactory] = Singleton(
        UserFactory,
    )

    unit_factory: Singleton[UnitFactory] = Singleton(
        UnitFactory,
    )

    @staticmethod
    def create_container(settings: BaseSettings) -> 'OrgContainer':
        """ Org container crater"""
        container: OrgContainer = OrgContainer()
        container.config.from_pydantic(settings)
        return container
