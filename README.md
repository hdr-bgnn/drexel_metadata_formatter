[![DOI](https://zenodo.org/badge/554906817.svg)](https://zenodo.org/badge/latestdoi/554906817)

# drexel_metadata_formatter
Reformats the metadata output file from the [drexel_metadata repo](https://github.com/hdr-bgnn/drexel_metadata/).

## Requirements
- [Python 3](https://www.python.org/)


## Usage
```
usage: dm_formatter.py [-h] input output

Convert metadata json file to BGNN minnow project format.

positional arguments:
  input       Path of input drexel_metadata format JSON metadata file.
  output      Path of output BGNN minnow format JSON metadata file.

optional arguments:
  -h, --help  show this help message and exit
 ```

## Testing
The unit tests can be run with the following command:
```
python3 -m unittest discover .
```
