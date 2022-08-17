from src.pages.psf.psf_landing_page import PsfLandingPage
from src.steps.base_steps import BaseSteps


class PsfLandingPageSteps(BaseSteps):
    @property
    def psf_landing_page(self) -> PsfLandingPage:
        return PsfLandingPage(self.driver)

    def psf_about_open(self):
        assert self.psf_landing_page.about_psf_nav.text == 'About', 'Text is not correct'
        self.psf_landing_page.about_psf_nav.click()

    def psf_grants_open(self):
        assert self.psf_landing_page.grants_psf_nav.text == 'Grants', 'Text is not correct'
        self.psf_landing_page.grants_psf_nav.click()
