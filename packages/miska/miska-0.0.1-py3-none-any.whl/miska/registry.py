import typing as t


class RegistryNotFoundError(Exception):
    pass


class BaseRegistry:

    __repo_map: dict[str, dict[str, type]] = {}

    __repo_type__: str

    def __init_subclass__(cls, **kwargs: t.Any):
        super().__init_subclass__(**kwargs)
        BaseRegistry.__repo_map.setdefault(cls.__repo_type__, {}
                                           )[cls.__name__] = cls

    @classmethod
    def get_repo_by_name(cls, class_name: str) -> type:
        mapping = cls.__repo_map[cls.__repo_type__]
        if class_name not in mapping:
            raise RegistryNotFoundError(class_name)
        return mapping[class_name]
