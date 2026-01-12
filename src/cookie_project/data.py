import torch
from pathlib import Path
from torch.utils.data import Dataset

class MyDataset(Dataset):
    """My custom dataset."""

    def __init__(self, data_path: Path) -> None:
        self.data_path = data_path

    def __len__(self) -> int:
        # Hvis vi loader alt på forhånd
        return len(torch.load(self.data_path / "train_images.pt"))

    def __getitem__(self, index: int):
        images = torch.load(self.data_path / "train_images.pt")
        targets = torch.load(self.data_path / "train_target.pt")
        return images[index], targets[index]

    def preprocess(self, output_folder: Path) -> None:
        output_folder.mkdir(parents=True, exist_ok=True)
        train_images, train_target = [], []

        for i in range(6):
            train_images.append(torch.load(self.data_path / f"train_images_{i}.pt"))
            train_target.append(torch.load(self.data_path / f"train_target_{i}.pt"))

        train_images = torch.cat(train_images).unsqueeze(1).float()
        train_target = torch.cat(train_target).long()
        train_images = (train_images - train_images.mean()) / train_images.std()

        torch.save(train_images, output_folder / "train_images.pt")
        torch.save(train_target, output_folder / "train_target.pt")

        # ✨ Tilføj test-data
        test_images = torch.load(self.data_path / "test_images.pt").unsqueeze(1).float()
        test_target = torch.load(self.data_path / "test_target.pt").long()
        test_images = (test_images - test_images.mean()) / test_images.std()

        torch.save(test_images, output_folder / "test_images.pt")
        torch.save(test_target, output_folder / "test_target.pt")



def corrupt_mnist():
    """Return train and test datasets from processed data."""
    import torch
    from torch.utils.data import TensorDataset

    train_images = torch.load("data/processed/train_images.pt")
    train_target = torch.load("data/processed/train_target.pt")
    test_images = torch.load("data/processed/test_images.pt")
    test_target = torch.load("data/processed/test_target.pt")

    train_set = TensorDataset(train_images, train_target)
    test_set = TensorDataset(test_images, test_target)
    return train_set, test_set


import typer
def main(raw_dir: str, processed_dir: str):
    dataset = MyDataset(Path(raw_dir))
    dataset.preprocess(Path(processed_dir))

if __name__ == "__main__":
    typer.run(main)

