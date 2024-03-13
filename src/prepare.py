from pathlib import Path

import pandas as pd

import Augmentor

import os
import shutil

repo_path = Path(__file__).parent.parent
data_path = repo_path / "data"
train_path = data_path / "raw/train"
mapFolder = {}
for item in os.listdir(train_path):
    mapFolder[item] = item.replace(' ', '_').lower()

FOLDERS_TO_LABELS = mapFolder


def get_files_and_labels(source_path):
    images = []
    labels = []
    for image_path in source_path.rglob("*/*.jpg"):
        filename = image_path.absolute()
        folder = image_path.parent.name
        if folder in FOLDERS_TO_LABELS:
            images.append(filename)
            label = FOLDERS_TO_LABELS[folder]
            labels.append(label)
    return images, labels


def save_as_csv(filenames, labels, destination):
    data_dictionary = {"filename": filenames, "label": labels}
    data_frame = pd.DataFrame(data_dictionary)
    data_frame.to_csv(destination)


def aug(path_to_save):
    Path(path_to_save).mkdir(parents=True, exist_ok=True)

    for item in os.listdir(path_to_save):
        shutil.rmtree(path_to_save/item)

    p = Augmentor.Pipeline(train_path, output_directory=path_to_save)
    p.rotate(probability=1, max_left_rotation=5, max_right_rotation=5)
    p.flip_left_right(probability=0.5)
    p.zoom_random(probability=0.5, percentage_area=0.8)
    p.flip_top_bottom(probability=0.5)
    p.sample(10)

def main(repo_path):
    data_path = repo_path / "data"
    train_path = data_path / "raw/train"
    aug_path = data_path / "raw/aug"

    aug(aug_path)


    test_path = data_path / "raw/valid"
    train_files, train_labels = get_files_and_labels(train_path)
    aug_files, aug_labels = get_files_and_labels(aug_path)
    test_files, test_labels = get_files_and_labels(test_path)
    prepared = data_path / "prepared"
    save_as_csv(train_files + aug_files, train_labels + aug_labels , prepared / "train.csv")
    save_as_csv(test_files, test_labels, prepared / "test.csv")


if __name__ == "__main__":
    repo_path = Path(__file__).parent.parent
    main(repo_path)
