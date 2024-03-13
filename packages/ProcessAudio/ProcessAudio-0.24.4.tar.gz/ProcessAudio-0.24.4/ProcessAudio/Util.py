import os
import tempfile
import noisereduce as nr
import numpy as np
import librosa
import pydub
import uuid
from scipy.io import wavfile


class Util:

    def read_audio(self, file_path: str, force_convert_wav: bool = False):
        """
        Read a wav file, it's necessary the file is in wav format
        if not in wav format, you have to set force_convert_wav to True

        @type file_path: str
        @param file_path: path to the audio file

        @type force_convert_wav: bool
        @param force_convert_wav: if True, the audio is converted to wav format
        """

        try:
            if force_convert_wav:
                with tempfile.TemporaryDirectory(
                    prefix="audio_aumentation_"
                ) as temp_dir_audio:
                    output_path = os.path.join(temp_dir_audio, f"{uuid.uuid4()}.wav")

                    self.convert_wav(file_path, output_path)

                    data, sr = librosa.load(output_path)
            else:
                data, sr = librosa.load(file_path)

            return data, sr
        except Exception as e:
            print(f"Error to read file {file_path}: {e}")
            return None, None

    def __read_audio_pydub(self, audio_path: str):
        """
        Read an audio file with pydub

        @type audio_path: str
        @param audio_path: path to the audio file

        @rtype: pydub.AudioSegment
        @return: audio file
        """

        if audio_path.endswith(".mp3"):
            audio = pydub.AudioSegment.from_mp3(audio_path)
        elif audio_path.endswith(".wav"):
            audio = pydub.AudioSegment.from_wav(audio_path)
        else:
            audio = pydub.AudioSegment.from_file(audio_path)

        return audio

    def audio_convert_wav(self, audio_path: str, output_path: str):
        """
        Convert an audio file to wav format

        @type audio_path: str
        @param audio_path: path to the audio file

        @type output_path: str
        @param output_path: path to save the audio file

        @rtype: str
        @return: path to the audio file
        """

        audio = self.__read_audio_pydub(audio_path)

        audio.export(output_path, format="wav")

        return output_path

    def denoise_audio(self, data: np.array, sr: int):
        """
        Denoise an audio file, the data is necessary the audio was read with librosa.load method

        @type data: np.array
        @param data: audio data

        @type sr: int
        @param sr: sample rate

        @rtype: np.array, int
        @return: audio data, sample rate
        """

        # https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=a9cd99c6a8f26964de07b26c31ea9a4a412e06ae
        # https://github.com/timsainb/noisereduce
        # https://ankurdhuriya.medium.com/audio-enhancement-and-denoising-methods-3644f0cad85b

        with tempfile.TemporaryDirectory(prefix="audio_aumentation_") as temp_dir_audio:
            audio_path = os.path.join(temp_dir_audio, f"{uuid.uuid4()}.wav")

            reduced_noise = nr.reduce_noise(y=data, sr=sr, verbose=False)
            wavfile.write(audio_path, sr, reduced_noise)
            data, rate = librosa.load(audio_path)

            return data, rate
