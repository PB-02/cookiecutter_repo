import pytest
import os
from cookie_project.train import train  # eller hvad din træningsfunktion hedder
from tests import _PATH_DATA

def test_train():
    train(lr=1e-3, batch_size=2, epochs=1)
    assert True
