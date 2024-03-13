from joblib import dump
from pathlib import Path

import numpy as np
import pandas as pd
from skimage.io import imread_collection
from skimage.transform import resize
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier

from sklearn.linear_model import SGDClassifier



def load_images(data_frame, column_name):
    filelist = data_frame[column_name].to_list()
    image_list = imread_collection(filelist)
    return image_list


def load_labels(data_frame, column_name):
    label_list = data_frame[column_name].to_list()
    return label_list


def preprocess(image):
    resized = resize(image, (100, 100, 3))
    reshaped = resized.reshape((1, 30000))
    return reshaped


def load_data(data_path):
    df = pd.read_csv(data_path)
    labels = load_labels(data_frame=df, column_name="label")
    raw_images = load_images(data_frame=df, column_name="filename")
    processed_images = [preprocess(image) for image in raw_images]
    data = np.concatenate(processed_images, axis=0)
    return data, labels


def main(repo_path):
    train_csv_path = repo_path / "data/prepared/train.csv"
    train_data, labels = load_data(train_csv_path)


    models = {
        'etc': ExtraTreesClassifier(n_estimators=15, min_samples_leaf=15, max_depth=20),
        'rfc': RandomForestClassifier(min_samples_leaf=20, max_samples=30, random_state=1),
        'sgd': SGDClassifier(max_iter=15, random_state=1),
    }

    for name, model in models.items():
        trained_model = model.fit(train_data, labels)
        dump(trained_model, repo_path / f"models/{name}.joblib")



if __name__ == "__main__":
    repo_path = Path(__file__).parent.parent
    main(repo_path)