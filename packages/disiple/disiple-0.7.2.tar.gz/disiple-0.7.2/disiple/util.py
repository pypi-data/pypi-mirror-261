import shutil
from urllib.request import urlopen
from pathlib import Path
import IPython.display
import numpy as np


class Audio(IPython.display.Audio):

    def __init__(self, data=None, filename=None, url=None, embed=None, rate=None, autoplay=False, normalize=False):
        if not normalize and data is not None:
            data_array = np.asarray(data)
            # convert non-floating point data to floating point in interval [-1, 1]
            if np.issubdtype(data_array.dtype, np.signedinteger):
                data = 1 / 2**(8*data_array.dtype.itemsize-1) * data_array
            elif np.issubdtype(data_array.dtype, np.unsignedinteger):
                data = 1 / 2**(8*data_array.dtype.itemsize-1) * data_array - 1
        try:
            super().__init__(data=data, filename=filename, url=url, embed=embed, rate=rate, autoplay=autoplay, normalize=normalize)
        except TypeError:
            if not normalize and data is not None:
                s = list(data.shape)
                s[-1] = 1
                data = np.append(data, np.ones(s), axis=-1)
            super().__init__(data=data, filename=filename, url=url, embed=embed, rate=rate, autoplay=autoplay)        


def download_file(url, file_path, verbose=False, overwrite=False):
    dst_path = Path(file_path)
    if dst_path.is_dir():
        dst_path /= Path(url).name
    if not dst_path.exists() or overwrite:
        if verbose:
            print(f'Downloading to {dst_path}', end='')
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        with urlopen(url) as r:
            dst_path.write_bytes(r.read())
        if verbose:
            print(' - done')
    elif verbose:
        print(f'File "{dst_path}" already exists, pass "overwrite=True" to force download')


def download_and_extract_archive(url, extract_path, verbose=False, overwrite=False, keep_archive=False):
    archive_path = Path(extract_path) / Path(url).name
    download_file(url, archive_path, verbose, overwrite)
    shutil.unpack_archive(archive_path, extract_path)
    if not keep_archive:
        archive_path.unlink()


def nextpow2(n: int):
    return 1<<(n-1).bit_length()
