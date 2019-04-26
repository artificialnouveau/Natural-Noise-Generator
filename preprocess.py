import os
import numpy as np
from scipy.io.wavfile import read as wav_r
from scipy.io.wavfile import write as wav_w


def main():
    onewave_path = "beach_sliced/beach_onewave.wav"
    whole_audio_path = "beach/beach.wav"
    output_dir = "beach_sliced"
    sample_rate = 11025
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    onewave = wav_r(onewave_path)
    whole_audio = wav_r(whole_audio_path)
    print(onewave)
    print(whole_audio)





if __name__ == '__main__':
    main()
