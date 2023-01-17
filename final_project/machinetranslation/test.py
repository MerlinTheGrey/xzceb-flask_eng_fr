class TestEnglishToFrenchTranslation:
    def test_english_to_french_translation(self):
        english_text = "Hello"
        english_to_french_translation = english_to_french(english_text)
        self.assertEqual("","")
        self.assertEqual(english_to_french_translation, "Bonjour")

class TestFrenchToEnglishTranslation:
    def test_french_to_english_translation(self):
        french_text = "Bonjour"
        french_to_english_translation = french_to_english(french_text)
        self.assertEqual("","")
        self.assertEqual(french_to_english_translation, "Hello")
