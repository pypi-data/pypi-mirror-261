import numpy as np
import librosa
from scipy import signal
import matplotlib.pyplot as plt


class Graph:

    def spectrogram(
        self,
        data: np.array,
        sr: int,
        output_path: str = None,
        title: str = "Spectrogram",
    ):
        """
        Plot and save a spectrogram, the data is necessary the audio was read with Util.read_audio method

        @type data: np.array
        @param data: audio data

        @type sr: int
        @param sr: sample rate

        @type title: str
        @param title: title of the plot

        @rtype: str
        @return: path to the plot
        """

        frequencies, times, spectrogram_data = signal.spectrogram(data, sr)

        plt.figure(figsize=(10, 5))
        plt.pcolormesh(times, frequencies, np.log10(spectrogram_data))
        plt.xlabel("Time [s]")
        plt.ylabel("Frequency [Hz]")
        plt.title(title)
        plt.colorbar(label="Intensity [dB]")

        if output_path is None:
            output_path = "spectrogram.png"

        plt.savefig(output_path)

        plt.close()

        return output_path

    def log_mel_spectrogram(
        self,
        data: np.array,
        sr: int,
        output_path: str = None,
        title: str = "log_mel_spectrogram",
    ):
        """
        Plot and save a log-mel spectrogram, the data is necessary the audio was read with Util.read_audio method

        @type data: np.array
        @param data: audio data

        @type sr: int
        @param sr: sample rate

        @type output_path: str
        @param output_path: path to save the plot

        @type title: str
        @param title: title of the plot
        """

        # Calcular el log-mel espectrograma
        mel_spectrogram = librosa.feature.melspectrogram(y=data, sr=sr)
        log_mel_spectrogram = librosa.power_to_db(mel_spectrogram, ref=np.max)

        # Plotear el log-mel espectrograma
        plt.figure(figsize=(10, 5))
        librosa.display.specshow(
            log_mel_spectrogram, sr=sr, x_axis="time", y_axis="mel"
        )
        plt.colorbar(format="%+2.0f dB")
        plt.title(title)
        plt.tight_layout()

        if output_path is None:
            output_path = "log_mel_spectrogram.png"

        plt.savefig(output_path)
        plt.close()

        return output_path
