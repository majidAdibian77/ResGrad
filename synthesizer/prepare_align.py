import argparse

from .preprocessor import persian
from ..utils import load_yaml_file


def main(config):
    if "Persian" in config["dataset"]:
        persian.prepare_align(config)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=str, help="path to config.yaml")
    args = parser.parse_args()

    config = load_yaml_file(args.config)
    main(config['synthesizer']['preprocess'])