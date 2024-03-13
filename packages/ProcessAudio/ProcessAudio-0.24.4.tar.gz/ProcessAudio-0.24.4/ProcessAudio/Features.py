from typing import Union
import matplotlib.pyplot as plt
import librosa.display
import librosa
import numpy as np


class Features:
    data = None

    def __init__(self, complete_answer: bool = False):
        """
        @type complete_answer: bool
        @param complete_answer: if True, the features are returned in a single line
                                if not the features are returned in a single array meaning
        """

        self.mfcc = None
        self.zcr = None
        self.rolloff = None
        self.spec_bw = None
        self.spec_cent = None
        self.rmse = None
        self.chroma_stft = None

        self.complete_answer = complete_answer

    def set_data(self, data_audio: Union[str, tuple]):
        """
        Set the data audio to process

        @type data_audio: Union[str, tuple]
        @param data_audio: audio data or tuple with audio data and sample rate
        """

        if isinstance(data_audio, str):
            rate: int = 44100
            (data, rate) = librosa.core.load(data_audio)
            self.data = data
            self.sr = rate

        if isinstance(data_audio, tuple):
            self.data = data_audio[0]
            self.sr = data_audio[1]

    def display_waveform(self, data: np.array = None, sr: int = None):
        """
        Display the waveform of the audio

        @type data: np.array
        @param data: audio data
        @type sr: int
        @param sr: sample rate
        """

        if data is not None and sr is not None:
            plt.figure(figsize=(14, 5))
            librosa.display.waveplot(data, sr=sr)

        else:
            if self.data is None:
                return None

            # display waveform
            plt.figure(figsize=(14, 5))
            librosa.display.waveplot(self.data, sr=self.sr)

    def get_croma(self):
        """
        Chroma feature to represent the energy distribution of the pitch classes

        @rtype: np.array
        @return: chroma features
        """

        if self.data is None:
            return None

        self.chroma_stft = librosa.feature.chroma_stft(y=self.data, sr=self.sr)

        if self.complete_answer:
            self.chroma_stft = np.ravel(self.chroma_stft)

        return self.chroma_stft

    def get_rms(self):
        """
        Root Mean Square Energy (RMSE)
        which is the square root of the mean of the squared signal values.

        @rtype: np.array
        @return: rmse features
        """

        if self.data is None:
            return None

        self.rmse = librosa.feature.rms(y=self.data)

        if self.complete_answer:
            self.rmse = np.ravel(self.rmse)

        return self.rmse

    def get_spectral_centroid(self):
        """
        The center of mass of the spectrum.

        @rtype: np.array
        @return: spectral centroid features
        """

        if self.data is None:
            return None

        self.spec_cent = librosa.feature.spectral_centroid(y=self.data, sr=self.sr)

        if self.complete_answer:
            self.spec_cent = np.ravel(self.spec_cent)

        return self.spec_cent

    def get_spectral_bandwidth(self):
        """
        The bandwidth is the width of the band of frequencies
        where most of the energy of the signal is concentrated.

        @rtype: np.array
        @return: spectral bandwidth features
        """

        if self.data is None:
            return None

        self.spec_bw = librosa.feature.spectral_bandwidth(y=self.data, sr=self.sr)

        if not self.complete_answer:
            self.spec_bw = np.ravel(self.spec_bw)

        return self.spec_bw

    def get_rolloff(self):
        """
        Also known as spectral reduction in frequency.
        where is 85% of the signal energy

        @rtype: np.array
        @return: rolloff features
        """

        if self.data is None:
            return None
        self.rolloff = librosa.feature.spectral_rolloff(y=self.data, sr=self.sr)

        if self.complete_answer:
            self.rolloff = np.ravel(self.rolloff)

        return self.rolloff

    def get_zero_crossing(self):
        """
        Zero crossing rate

        @rtype: np.array
        @return: zero crossing rate features
        """

        if self.data is None:
            return None

        self.zcr = librosa.feature.zero_crossing_rate(self.data)

        if self.complete_answer:
            self.zcr = np.ravel(self.zcr)

        return self.zcr

    def get_mfcc(self):
        """
        Mel-frequency cepstral coefficients (MFCCs)
        coefficients that collectively make up the mel-frequency cepstrum

        @rtype: np.array
        @return: mfcc features
        """

        if self.data is None:
            return None

        self.mfcc = librosa.feature.mfcc(y=self.data, sr=self.sr)

        if self.complete_answer:
            self.mfcc = np.ravel(self.mfcc)

        return self.mfcc

    def get_tonnetz(self):
        """
        Compute tonnetz features from the harmonic component of a song

        @rtype: np.array
        @return: tonnetz features
        """

        if self.data is None:
            return None
        self.tonnetz = librosa.feature.tonnetz(y=self.data, sr=self.sr)

        if self.complete_answer:
            self.tonnetz = np.ravel(self.tonnetz)

        return self.tonnetz

    def build_basic(self) -> list:
        if self.data is None:
            return []

        self.get_croma()
        self.get_rms()
        self.get_spectral_centroid()
        self.get_spectral_bandwidth()
        self.get_rolloff()
        self.get_zero_crossing()
        self.get_mfcc()

        if not self.complete_answer:
            data_compresed = f"{np.mean(self.chroma_stft)} {np.mean(self.rmse)} {np.mean(self.spec_cent)} {np.mean(self.spec_bw)} {np.mean(self.rolloff)} {np.mean(self.zcr)}"
            for e in self.mfcc:
                data_compresed += f" {np.mean(e)}"
        else:
            complete = np.concatenate(
                [
                    self.chroma_stft,
                    self.rmse,
                    self.spec_cent,
                    self.spec_bw,
                    self.rolloff,
                    self.zcr,
                    self.mfcc,
                ]
            )
            data_compresed = complete.tolist()

        return data_compresed.split()
