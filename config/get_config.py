import os, sys
import yaml

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    def __init__(self):
        yaml_path = os.path.join(basedir, "config.yaml")
        # Initialize config
        with open(yaml_path, 'r') as yamlfile:
            cfg = yaml.load(yamlfile)

        self.Tensorflow = cfg["Tensorflow"]
        self.VGG_16 = cfg["VGG_16"]
        self.Inception_v3 = cfg["Inception_v3"]
        self.Inception_v4 = cfg["Inception_v4"]
        self.Models = [
            self.VGG_16,
            self.Inception_v3,
            self.Inception_v4
        ]
