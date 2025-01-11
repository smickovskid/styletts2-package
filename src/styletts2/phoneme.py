from phonemizer.backend import EspeakBackend
from phonemizer import phonemize


class PhonemeConverter:
    def phonemize(self, text):
        pass


class PhonemizerPhonemizer(PhonemeConverter):
    def phonemize(self, text, lang="en-us"):
        # Use the phonemizer library to generate phonemes
        phonemized_text = phonemize(
            text,
            language=lang,
            backend="espeak",
            strip=True,
            preserve_punctuation=True,
        )
        return phonemized_text


class PhonemeConverterFactory:
    @staticmethod
    def load_phoneme_converter(name: str, **kwargs):
        if name == "phonemizer":
            return PhonemizerPhonemizer()
        else:
            raise ValueError("Invalid phoneme converter.")

