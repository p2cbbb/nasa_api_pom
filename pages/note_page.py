from .base_page import BasePage
from .locators import NotePageLocators


class NotePage(BasePage):
    def checking_note_text(self):
        expected_text = "Why is Betelgeuse fading?  No one knows."
        actual_text = self.browser.find_element(*NotePageLocators.note_text).text
        assert expected_text in actual_text, "Notes text are note the same"
        
        
        
