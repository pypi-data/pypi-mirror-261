"""
Based on builtin module webbrowser, simple_webbrowser makes it way easier for you to search something online using Python.
"""

# [i] simple_webbrowser by MF366
# [*] Based on built-in module: webbrowser

# [i] Python imports
import webbrowser
from typing import Literal, Any
from urllib import parse as parser

# [i] Local imports
from linkdatatypes import LinkBytes, LinkString
from constants import *
# [!?] this has only been imported like this because its for the developer that is using this module use the constants without an additional import


def website(url: str | LinkString | LinkBytes, new: Literal[0, 1, 2] = 0, autoraise: bool = True, link_rule: Literal['normal', 'plus'] = 'normal', browser: webbrowser.BaseBrowser | Any = webbrowser) -> bool:        
    """
    website opens a website using webbrowser

    Args:
        url (str | LinkString | LinkBytes): a representation of an URL. If it's a LinkString or a LinkBytes, the encoded version of it will be considered the URL.
        new (Literal[0, 1, 2], optional): whether to use the current browser (default), a new window or a new browser page. Defaults to 0.
        autoraise (bool, optional): whether to focus the browser or not. Defaults to True.
        link_rule (Literal[NORMAL, PLUS], optional): if using a LinkString as url and this is set to 'plus', use encoded_link_plus instead of encoded_link. When set to 'normal' or anything else really, use encoded_link. This argument is compatible with the NORMAL and PLUS constants. Defaults to 'normal'.
        browser (webbrowser.BaseBrowser | webbrowser, optional): the browser class or module that will open the URL. Defaults to the webbrowser module (a.k.a.: webbrowser will use the default browser).
    
    Returns:
        bool: return value of the open operation
    """
    
    link = url
    
    if isinstance(url, LinkString):
        if link_rule == 'plus':
            link = url.encoded_link_plus
            
        else:
            link = url.encoded_link
            
    elif isinstance(url, LinkBytes):
        link = url.encoded_link

    return browser.open(link, new, autoraise)


def build_search_url(common: str, query: str | LinkString | LinkBytes, link_rule: Literal['normal', 'plus'] = 'normal') -> str:
    """
    build_search_url combines the common part of the URL and the parsed query into a search URL

    NOTE: the `common` argument is not parsed and must be a string, not LinkString nor LinkBytes!
    
    Args:
        common (str): the common search part. Examples: simple_webbrowser constants ending with COMMON.
        query (str | LinkString | LinkBytes): a representation of the already parsed URL. If it's a LinkString or a LinkBytes, the encoded version of it will be considered the URL.
        link_rule ('normal', 'plus'], optional): if using a LinkString as url and this is set to 'plus', use encoded_link_plus instead of encoded_link. When set to 'normal' or anything else really, use encoded_link. This argument is compatible with the NORMAL and PLUS constants. Defaults to 'normal'.

    Returns:
        str: the combined search URL
    """
    
    parsed_query = query
    
    if isinstance(query, LinkString):
        if link_rule == 'plus':
            parsed_query = query.encoded_link_plus
            
        else:
            parsed_query = query.encoded_link
            
    elif isinstance(query, LinkBytes):
        parsed_query = query.encoded_link
    
    return f"{common}{parsed_query}"


Website = website
BuildSearchURL = build_search_url
get_browser_class = webbrowser.get
register_connector = webbrowser.register

Google = lambda query: website(build_search_url(GOOGLE_COMMON, parser.quote(query, 'utf-8')))
Bing = lambda query: website(build_search_url(BING_COMMON, parser.quote(query, 'utf-8')))
Brave = lambda query: website(build_search_url(BRAVE_COMMON, parser.quote(query, 'utf-8')))
Yahoo = lambda query: website(build_search_url(YAHOO_COMMON, parser.quote(query, 'utf-8')))
DuckDuckGo = lambda query: website(build_search_url(DUCKDUCKGO_COMMON, parser.quote(query, 'utf-8')))
YouTube = lambda query: website(build_search_url(YOUTUBE_COMMON, parser.quote(query, 'utf-8')))
Ecosia = lambda query: website(build_search_url(ECOSIA_COMMON, parser.quote(query, 'utf-8')))
StackOverflow = lambda query: website(build_search_url(STACKOVERFLOW_COMMON, parser.quote(query, 'utf-8')))
SoundCloud = lambda query: website(build_search_url(SOUNDCLOUD_COMMON, parser.quote(query, 'utf-8')))
Archive = lambda query: website(build_search_url(ARCHIVE_ORG_COMMON, parser.quote(query, 'utf-8')))
Qwant = lambda query: website(build_search_url(QWANT_COMMON, parser.quote(query, 'utf-8')))
SpotifyOnline = lambda query: website(build_search_url(SPOTIFY_COMMON, parser.quote(query, 'utf-8')))
GitLab = lambda query: website(build_search_url(GITLAB_COMMON, parser.quote(query, 'utf-8')))
GitHub = lambda query: website(build_search_url(GITHUB_COMMON, parser.quote(query, 'utf-8')))

OpenSpotify = SpotifyOnline


class ExtraEngines:
    def __init__(self, browser = webbrowser) -> None:
        self._browser = browser
        self.DoomWorld = lambda query: website(build_search_url(DOOMWORLD_COMMON, parser.quote(query, 'utf-8')), browser=self._browser)
        self.Twitch = lambda query: website(build_search_url(TWITCH_COMMON, parser.quote(query, 'utf-8')), browser=self._browser)

    def DeepL(self, query: str, _lang: str = "en"):
        Website(BuildSearchURL(f"https://www.deepl.com/translator#{_lang}/", query, "%20"), browser=self.browser)
    
    @property
    def browser(self):
        return self._browser
    
extras = ExtraEngines()
