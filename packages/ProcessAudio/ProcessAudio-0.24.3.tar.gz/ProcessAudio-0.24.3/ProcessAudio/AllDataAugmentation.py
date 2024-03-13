from ProcessAudio.AudioAugmentation import AudioAugmentation
from ProcessAudio.Features import Features


class AllDataAugmentation(AudioAugmentation):

    def __init__(
        self, file_path, label: list = None, path_save: str = "", to_graph: bool = False
    ):
        """
        Initialize the class with the file path and the label
        """

        super().__init__(file_path, save=path_save, graph=to_graph)
        self.label = label

    def build_all(self, extract_features: bool = False):
        """
        Build all data augmentation and extract features if it's necessary

        @type extract_features: bool
        @param extract_features: if True, extract features from all data

        @rtype: list
        @return: all data and all labels
        """

        all_data = [
            self.get_original(),
            self.add_noise(noise_factor=0.05),
            self.add_noise2(),
            self.stretch(rate_stretch=0.8),
            self.shift(),
            self.add_crop(),
            self.loudness(),
            self.speed(),
            self.normalizer(),
            self.polarizer(),
        ]

        all_data = [x for x in all_data if x is not None]

        if extract_features:
            print("Extracting features to", self.audio_file)
            all_data = self.extract_features(all_data)

        all_label = [self.label for _ in range(len(all_data))]
        return all_data, all_label

    def extract_features(self, all_data) -> list:
        """
        Extract features from all data

        @type all_data: list
        @param all_data: list of audio data

        @rtype: list
        @return: list of features
        """

        features = Features()

        for i in range(len(all_data)):

            info_audio = (all_data[i], self.rate)
            features.set_data(info_audio)

            all_data[i] = features.build_basic()

        return all_data
