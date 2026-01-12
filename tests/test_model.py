import pytest
from cookie_project.model import MyAwesomeModel
import torch

@pytest.mark.parametrize("batch_size", [32, 64])
def test_model(batch_size: int) -> None:
    model = MyAwesomeModel()
    x = torch.randn(batch_size, 1, 28, 28)
    y = model(x)
    assert y.shape == (batch_size, 10)

def test_error_on_wrong_shape():
    model = MyAwesomeModel()

    # Forkert antal kanaler: RuntimeError kommer stadig
    with pytest.raises(RuntimeError):
        model(torch.randn(1, 2, 28, 28))  # 2 kanaler, model forventer 1
