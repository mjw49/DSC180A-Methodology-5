#!/usr/bin/env python3

import numpy as np

from src import k_clusters

def main(targets):
    if 'data' in targets:
        with open('config/k-clusters-params.json') as fh:
            data_params = json.load(fh)
        k_clusters(**data_params)

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)
