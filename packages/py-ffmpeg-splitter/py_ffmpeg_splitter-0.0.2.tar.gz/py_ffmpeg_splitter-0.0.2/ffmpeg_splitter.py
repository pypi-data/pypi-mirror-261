import os
import subprocess
import sys
import plac
from plac import opt, pos
from typing import Callable
from typing import Optional


def split_by_size(filepath: str, size_bytes: int, target: str = "", print_function: Optional[Callable] = None) -> None:
    """
    Takes a media file and uses system-scope ffmpeg + ffprobe to split it into multiple files
    :param filepath: The file to split
    :param size_bytes: The desired output file size. Warning! Output file can be larger. Use with tolerance.
    :param target: The target filepath / directory, defaults to the value of `filepath` (provided as \"\").
    :param print_function: Function to print useful debug messages. By default, None - printing is disabled (except for ffmpeg output).
    :raises RuntimeError: Raises exception when either the source file was not found or the target directory was not found.
    """

    def remove_prefix(source: str, prefix: str) -> str:
        if source.startswith(prefix):
            return source[len(prefix):]
        return source

    def p(*args) -> None:
        if print_function is not None:
            print_function(*args)

    def get_duration(file: str) -> int:
        duration_cmd: str = "ffprobe -i \"{input_file}\" -show_entries format=duration -v quiet -of default=noprint_wrappers=1:nokey=1|cut -d. -f1"
        p(f"Running duration command `{duration_cmd}`")
        duration = int(subprocess.check_output(duration_cmd.format(input_file=file), shell=True).decode())
        p(f"Received duration `{duration}`")
        return duration

    if not os.path.isfile(filepath):
        raise RuntimeError(f"ffmpeg_splitter::split_by_size | `{filepath}` is not a valid filepath")

    if target == "":
        target = filepath
    else:
        if not os.path.isdir(target):
            target_dir = os.path.dirname(target)
            if not os.path.isdir(target_dir):
                error_msg = f"ffmpeg_splitter::split_by_size | `{target}` is in non-existent directory `{target_dir}`"
                if os.path.isabs(target_dir):
                    raise RuntimeError(error_msg)
                else:
                    target_dir = os.path.dirname(os.path.join(os.curdir, target))
                if not os.path.isdir(target_dir):
                    raise RuntimeError(error_msg)
        splits = os.path.splitext(target)
        if not splits[1]:
            target = splits[0] + os.path.splitext(filepath)[1]

    full_duration: int = get_duration(filepath)
    cur_duration: int = 0
    if os.path.isdir(target):
        _ext = os.path.splitext(filepath)
        basepath = target
        path_symbol = "/"
        if sys.platform == "win32":
            path_symbol = "\\"
        if not basepath.endswith(path_symbol):
            basepath = basepath + path_symbol

        basepath += os.path.splitext(os.path.basename(filepath))[0]
        extension: str = remove_prefix(_ext[1], ".")
    else:
        _ext = os.path.splitext(target)
        basepath = _ext[0]
        extension: str = remove_prefix(_ext[1], ".")

    i: int = 1

    ffmpeg_args = "-c copy"
    while cur_duration < full_duration:
        next_file = "{}-{}.{}".format(basepath, i, extension)
        encode_cmd = f"ffmpeg -y -ss {cur_duration} -i \"{filepath}\" -fs {size_bytes} {ffmpeg_args} \"{next_file}\""
        p(f"Running encode command `{encode_cmd}`")
        subprocess.check_call(encode_cmd, shell=True)

        new_duration: int = get_duration(next_file)
        cur_duration += new_duration

        i += 1

        next_file = "{}-{}.{}".format(basepath, i, extension)

@pos("source_path", "The media file to split")
@pos("desired_size", "The desired maximum size per output file")
@opt("target_file", "The target filepath / directory to output the files", abbrev="t")
def _run_cli(source_path: str, desired_size: int, target_file: str = ""):
    # if target_file and not os.path.exists(target_file):
    #     target_file = os.path.join(os.curdir, target_file)
    split_by_size(source_path, desired_size, target_file, print)

if __name__ == "__main__":
    plac.call(_run_cli)
