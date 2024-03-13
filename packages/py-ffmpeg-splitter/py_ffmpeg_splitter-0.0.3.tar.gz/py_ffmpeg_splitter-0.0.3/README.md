# A simple python library used to split media files.


## Examples

*From the command line*
``` bash
python ffmpeg_splitter --help
python ffmpeg_splitter.py source.mp4 1000000000 -t "out.mp4" # Will split `source.mp4` into files of 1GiB size (named out-x.mp4).
```

*From Python*
``` python
from ffmpeg_splitter import split_by_size

if __name__ == "__main__":
    split_by_size("my_file.mp4", 1000000000, print_function=print) # Will also print output and useful information
```
