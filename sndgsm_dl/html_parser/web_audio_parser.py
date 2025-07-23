"""
File in charge of parsing the page where the audio is.
"""
import logging
import re
from bs4 import BeautifulSoup

AUDIO_URL_PATTERN = r'\"https://\S+\.\S+\"'


class WebAudioParser:
    """
    Class for parsing HTML from audio web page.
    """

    def __init__(self, html: str) -> None:
        self.__html = html

        # Properties.
        self.__audio_url = ''

        try:
            self.__parse()
        except Exception as e:
            logging.debug(e)
            raise ValueError('Invalid HTML') from e

    def __parse(self) -> None:
        soup = BeautifulSoup(self.__html, 'html.parser')

        jscript = soup.find_all('script')[-1].get_text()

        url_raw = re.findall(AUDIO_URL_PATTERN, jscript)[0]

        self.__audio_url = url_raw.replace('"', '')

    @property
    def audio(self) -> str:
        """
        Return the URL with the file.
        """
        return self.__audio_url
