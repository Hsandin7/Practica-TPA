import pytest
import runpy


def test_main():
    try:
        runpy.run_module("main.py", run_name="__main__")
    except SystemExit:
        pass
    except Exception as e:
        pytest.fail(f"El juego lanzó un error inesperado: {e}")
