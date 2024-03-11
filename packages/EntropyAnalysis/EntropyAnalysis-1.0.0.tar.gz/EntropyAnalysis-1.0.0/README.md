![EntropyAnalysis](https://mauricelambert.github.io/info/python/security/EntropyAnalysis.gif "EntropyAnalysis")

# EntropyAnalysis

## Description

This package analyzes file entropy (shannon entropy) for forensic or
malware analysis

## Requirements

This package require:
 - python3
 - python3 Standard Library

Optional:
 - matplotlib (matplotlib is not installed by EntropyAnalysis, if you want GUI charts you should install it.)

## Installation

```bash
python3 -m pip install EntropyAnalysis

# The following line is optional (requirements for GUI charts)
python3 -m pip install matplotlib
```

```bash
git clone "https://github.com/mauricelambert/EntropyAnalysis.git"
cd "EntropyAnalysis"
python3 -m pip install .
```

## Usages

### Command line

```bash
EntropyAnalysis              # Using CLI package executable
python3 -m EntropyAnalysis   # Using python module
python3 EntropyAnalysis.pyz  # Using python executable
EntropyAnalysis.exe          # Using python Windows executable

EntropyAnalysis packed.exe
EntropyAnalysis -c packed.exe
EntropyAnalysis --all-characters packed.exe
EntropyAnalysis -f -C packed.exe
EntropyAnalysis -p 1024 packed.exe
EntropyAnalysis -o -k 4096 packed.exe
EntropyAnalysis -k 4096 -p 1024 packed.exe
EntropyAnalysis -u https://github.com/mauricelambert/FastRC4/releases/download/v0.0.1/librc4.so
```

### Python script

```python
from EntropyAnalysis import *
from urllib.request import urlopen

get_full_file_entropy(open('packed.exe', 'rb'))

charts_chunks_file_entropy(open('packed.exe', 'rb'))
charts_chunks_file_entropy(urlopen('https://github.com/mauricelambert/FastRC4/releases/download/v0.0.1/librc4.dll'), chunk_size=2048, part_size=512)

for score in get_chunks_file_entropy(open('packed.exe', 'rb')):
    print(score)

for score in get_chunks_file_entropy(urlopen('https://github.com/mauricelambert/FastRC4/releases/download/v0.0.1/librc4.dll'), chunk_size=2048):
    print(score)

print_chunks_file_entropy(open('packed.exe', 'rb'))
print_parts_chunks_file_entropy(open('packed.exe', 'rb'))

print_chunks_file_entropy(urlopen('https://github.com/mauricelambert/FastRC4/releases/download/v0.0.1/librc4.dll'), chunk_size=2048, colors=True)
print_parts_chunks_file_entropy(urlopen('https://github.com/mauricelambert/FastRC4/releases/download/v0.0.1/librc4.dll'), chunk_size=2048, part_size=512, colors=True)
```

## Links

 - [Pypi](https://pypi.org/project/EntropyAnalysis)
 - [Github](https://github.com/mauricelambert/EntropyAnalysis)
 - [Documentation](https://mauricelambert.github.io/info/python/security/EntropyAnalysis.html)
 - [Python executable](https://mauricelambert.github.io/info/python/security/EntropyAnalysis.pyz)
 - [Python Windows executable](https://mauricelambert.github.io/info/python/security/EntropyAnalysis.exe)

## License

Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).
