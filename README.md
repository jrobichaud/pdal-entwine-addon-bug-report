## Setup

```bash
git clone https://github.com/jrobichaud/pdal-entwine-addon-bug-report.git
cd pdal-entwine-addon-bug-report
wget https://github.com/PDAL/data/raw/master/liblas/LASFile_1.laz
docker-compose run --rm entwine_convert
```

## Run with PDAL cli

```bash
> docker-compose run --rm pdal_entwine_cli
> echo $?
0
> ls output/cli/LASFile_1_entwine_addon/ept_x/ept-addon.json
output/cli/LASFile_1_entwine_addon/ept_x/ept-addon.json
```

## Run with PDAL python

```bash
> docker-compose run --rm pdal_entwine_python
> echo $?
139
> ls output/python/LASFile_1_entwine_addon/ept_x/ept-addon.json
ls: output/python/LASFile_1_entwine_addon/ept_x/ept-addon.json: No such file or directory
```
