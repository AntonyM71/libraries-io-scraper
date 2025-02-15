from libraries_io_scraper.models import Dependency


DependenciesDict = dict[str, list[Dependency]]


def get_dependencies_sourcerank(dependencies: DependenciesDict) -> None:

    for k, v in dependencies.items():
        for d in v:
            d.get_sourcerank('pypi')

    return None
