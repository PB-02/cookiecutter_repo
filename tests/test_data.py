from torch.utils.data import Dataset
from cookie_project.data import corrupt_mnist
import os
import pytest
import torch

file_path = os.path.join(os.path.dirname(__file__), "..", "data", "raw")

@pytest.mark.skipif(not os.path.exists(file_path), reason="Data files not found")



def test_my_dataset():
    train, test = corrupt_mnist()
    assert len(train) == 30000, "Train dataset does not have 30000 samples"
    assert len(test) == 5000, "Test dataset does not have 5000 samples"

    for dataset in [train, test]:
        for x, y in dataset:
            assert x.shape == (1, 28, 28)
            assert y in range (10)
    train_targets = torch.unique(train.tensors[1])
    assert (train_targets == torch.arange(0,10)).all()
    test_targets = torch.unique(test.tensors[1])
    assert (test_targets == torch.arange(0,10)).all()
