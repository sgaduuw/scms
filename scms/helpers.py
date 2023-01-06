from dataclasses import dataclass

from scms.models import Site


@dataclass
class Header:
    url_link: str = '/'
    url_text: str = 'Home'
