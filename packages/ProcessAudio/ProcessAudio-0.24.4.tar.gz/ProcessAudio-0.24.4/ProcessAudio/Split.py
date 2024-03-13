import os
import pydub
import uuid


class Split:
    audio: pydub.AudioSegment
    audio_path: str
    output_path: str

    def __init__(self, audio_path: str, output_path: str, try_forced: bool = False):
        """
        @type audio_path: str
        @param audio_path: path to the audio file

        @type output_path: str
        @param output_path: path to save the audio files

        @type try_forced: bool
        @param try_forced: if True, the audio is tried to be read with the pydub.AudioSegment.from_file method
        """

        self.audio_path = audio_path
        self.output_path = output_path

        if audio_path.endswith(".mp3"):
            self.audio = pydub.AudioSegment.from_mp3(audio_path)
        elif audio_path.endswith(".wav"):
            self.audio = pydub.AudioSegment.from_wav(audio_path)
        else:
            if try_forced:
                self.audio = pydub.AudioSegment.from_file(audio_path)
            else:
                raise ValueError("File format not supported, please use .mp3 or .wav")

    def split(self, start: int, end: int, save: bool = False):

        output_path = os.path.join(self.output_path, f"{uuid.uuid4()}.wav")

        audio = self.audio[start:end]
        if save:
            audio.export(output_path, format="wav")

        return audio, output_path if save else None

    def split_by_seconds(self, seconds: int, save: bool = False):
        """
        Split the audio in seconds

        @type seconds: int
        @param seconds: seconds to split the audio

        @type save: bool
        @param save: if True, the audio is saved in the output path

        @rtype: Union[list, str]
        @return: list of audios or list of paths where the audios are saved
        """

        audio_duration = len(self.audio)
        audios = []

        for start in range(0, audio_duration, seconds * 1000):
            end = start + seconds * 1000
            if end > audio_duration:
                end = audio_duration
            audios.append(self.split(start, end)[0])

        if save:
            audios_saved = []
            for audio_id, audio in enumerate(audios):
                name = uuid.uuid4().hex.lower()

                output_path = os.path.join(self.output_path, f"{name}_{audio_id}.wav")
                audio.export(output_path, format="wav")

                audios_saved.append(output_path)

            audios = audios_saved

        return audios
