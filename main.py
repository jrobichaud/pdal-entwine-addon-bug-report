#!/usr/bin/env python3

import pdal


def main():
    with open("pipeline_entwine.json") as pipeline_json:
        json_pipeline = pipeline_json.read()
    pipeline = pdal.Pipeline(json_pipeline)
    pipeline.loglevel = 8  # really noisy
    pipeline.execute()


if __name__ == "__main__":
    main()
