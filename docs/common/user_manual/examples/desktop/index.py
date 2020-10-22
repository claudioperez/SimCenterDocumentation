#! usr/bin/env python

import os
from pathlib import Path
import yaml


# for dir in os.listdir():
#     for exp in os.listdir(dir):
#         pass


def make_meta():
    with open('index.yaml') as f: idx = yaml.load(f,Loader=yaml.Loader)
    for app in idx:
        for exp in idx[app]:
            print(app, exp)
            with open(Path('./'+app)/exp['id']/'meta.yaml','w+') as f:
                f.write(yaml.dump(exp))

if __name__ == "__main__":
    make_meta()
