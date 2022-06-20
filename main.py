import os
import sys
sys.path.append(os.path.relpath('./MillionSongCode'))
import MillionSongCode.hdf5_getters as hdf5_getters
from hdf5_getters import get_artist_name, open_h5_file_read

million_song_folder_path = './MillionSongSubset'
assert os.path.isdir(million_song_folder_path), 'Incorrect path'

def apply_to_all_files(basedir, func=lambda x: x, ext='.h5'):
    count = 0
    for root, dirs, files in os.walk(basedir):
        for filename in files:
            if filename.endswith(ext):
                count += 1
                func(filename)
                print(get_artist_name(open_h5_file_read(os.path.join(root, filename))).decode('UTF-8'))
                if count > 10:
                    return count
    return count

print(apply_to_all_files(million_song_folder_path))