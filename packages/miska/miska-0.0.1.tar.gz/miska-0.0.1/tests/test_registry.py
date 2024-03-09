from miska import registry


def test_registry():
    class Registry(registry.BaseRegistry):
        __repo_type__ = "things"

    result = Registry.get_repo_by_name("Registry")

    assert result == Registry
