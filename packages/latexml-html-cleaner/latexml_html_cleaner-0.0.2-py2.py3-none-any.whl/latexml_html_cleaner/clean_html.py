import contextlib
import logging
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup

_logger = logging.getLogger(__name__)
import contextlib


@contextlib.contextmanager
def smart_open(filename=None):
    if filename and filename.as_posix() != "-":
        fh = open(filename, mode="w", encoding="utf-8")
    else:
        fh = sys.stdout

    try:
        yield fh
    finally:
        if fh is not sys.stdout:
            fh.close()


def to_lijst(values):
    """Converteer een string of een lijst van strings naar een lijst van strings"""
    if not isinstance(values, list):
        lijst_values = [values]
    else:
        lijst_values = values
    return lijst_values


class HTMLCleaner:
    def __init__(
        self,
        filename,
        skip_tags=None,
        overwrite=False,
        find_and_replace_patterns=None,
        clear_default_patterns=False,
        output_filename=None,
    ):

        self.filename = Path(filename)
        self.clean_soup = None
        _logger.debug(f"Make filename for {filename}")
        file_basename = self.filename.with_suffix("")
        if not overwrite:
            file_basename = Path("_".join([file_basename.as_posix(), "clean"]))
        if output_filename is None:
            self.output_file = file_basename.with_suffix(".html")
        else:
            self.output_file = Path(output_filename)
        _logger.debug(f"Cleaning from {filename} to {self.output_file}")

        # default find en place: haal alle dubbele witte regels altijd weg
        if clear_default_patterns:
            self.find_and_replace_patterns = {}
        else:
            # begin met wat default strings die we gaan verwijderen
            self.find_and_replace_patterns = {
                "\n{2,}": "\n\n",
                "<span>•</span>": "",
                "<span><span>–</span></span>": "",
                "title=": "<b>Intermezzo:</b> ",
                "Â": "",
            }

        if find_and_replace_patterns is not None:
            for find, replace in find_and_replace_patterns.items():
                self.find_and_replace_patterns[find] = replace

        # default worden alle attributen die met ltx beginnen overgeslagen
        # skip_tags kan hele <> omgevingen laten vallen op basis van de omgevingen naam (de
        # key van de dict) en dan een lijst van attributes key/values paren. Als zo'n key/value
        # pair voorkomt, wordt de hele tag <> weggegooid. Hier onder definiëren we een default lijst
        # in dit voorbeeld, wordt bijvoorbeeld een tag
        # <span class="ltx_bibblock ltx_bib_cited">Cited by etc </span>
        # in zijn geheel weggegooid (inclusief alle nested values
        # we kunnen de values van een key/value paar ook in een lijst opgegeven als er meerdere
        # tags zijn met dezelfde key namen, maar verschillende values
        if skip_tags is None:
            self.skip_tags = {
                "span": {
                    "class": ["ltx_bibblock ltx_bib_cited", "ltx_tag ltx_tag_item"]
                },
                "link": {"rel": None},
                "meta": {"content": None},
                "div": {"class": "ltx_dates"},
                "footer": {None: None},
                "header": {None: None},
            }
        else:
            self.skip_tags = skip_tags

        self.skip_tag_attributes = {
            "a": {
                "href": ["^(A|Ch)\d+.html$", ".*[\d\w\.%]#[\d\w\.%].*", "^#.*"],
                "title": "",
            },
            "li": {"style": None},
            "span": {"style": None},
            None: {None: "ltx_", "id": None},
        }

        self.clean_html()

    @staticmethod
    def skip_this_tag(tag, attribute_key, attribute_values, skip_tags, combined=False):
        """Verzamel alle tags en attributes die we willen verwijderen"""
        attributes = " ".join(attribute_values)
        tags_to_skip = {}
        for skip_tag_name, skip_tag_attributes in skip_tags.items():
            if skip_tag_name == tag.name or skip_tag_name is None:
                for skip_atr_key, skip_atr_value in skip_tag_attributes.items():
                    if skip_atr_key == attribute_key or skip_atr_key is None:
                        for skip_value in to_lijst(skip_atr_value):
                            if combined:
                                # Als combined waar is dan moet je match gelden voor de gecombineerd
                                # attr string, zoals bijvoorbeeld 'ltx_bibblock ltx_bib_cited'
                                if skip_value is None or skip_value == attributes:
                                    tags_to_skip[attribute_key] = attribute_values
                            else:
                                # Als combined niet waar is krijgen we per item in de lijst of
                                # er een match is op basis van een regular expression. Alle matches
                                # worden verwijderd
                                for av in attribute_values:
                                    try:
                                        add = (
                                            av is None
                                            or skip_value is None
                                            or re.match(skip_value, av) is not None
                                        )
                                    except TypeError:
                                        _logger.warning(
                                            f"Failed to do regular expression for {skip_value}"
                                        )
                                    else:
                                        if add:
                                            try:
                                                tags_to_skip[attribute_key].append(av)
                                            except KeyError:
                                                tags_to_skip[attribute_key] = [av]
        return tags_to_skip

    def clean_html(self):
        # immediately import html

        with open(file=self.filename, mode="r", encoding="utf-8") as stream:
            html = stream.read()
        soup = BeautifulSoup(html, "html.parser")
        _logger.debug(f"Start cleaning ")
        _logger.debug(soup)

        # verwijder alle attributes die met ltx beginnen (dat zijn latexml definities)
        for tags in soup.findAll(True):
            new_attrs = {}
            for attr_key, attr_value in tags.attrs.items():
                attributes = to_lijst(attr_value)

                skip_this = self.skip_this_tag(
                    tag=tags,
                    attribute_key=attr_key,
                    attribute_values=attributes,
                    skip_tags=self.skip_tags,
                    combined=True,
                )
                if skip_this:
                    # deze tag wordt in zijn geheel overgeslagen
                    _logger.debug(f"Dropping complete tag  {attr_key} {attr_value}")
                    tags.extract()
                    continue

                skip_this = self.skip_this_tag(
                    tag=tags,
                    attribute_key=attr_key,
                    attribute_values=attributes,
                    skip_tags=self.skip_tag_attributes,
                )

                # we hebben de attributes in skip_this verzameld. Verwijder deze nu uit de
                # attributes  van de huidige tag

                # av zijn de huidige attributes van onze tag
                av = set(attributes)
                try:
                    sv = set(skip_this[attr_key])
                except KeyError:
                    sv = {}
                # sv bevat de tags die we willen verwijderen. Trek deze van de huidige af
                new_attrs_values = av.difference(sv)
                if new_attrs_values:
                    # als we nog attributes over houden stoppen we deze in de nieuwe attributes
                    new_attrs[attr_key] = list(new_attrs_values)
                else:
                    # we hebben niks meer over, dus kunnen we deze attr key weglaten
                    _logger.debug(f"Dropping {attr_key} from {tags.name}")

            # overschrijf de oude attributes met onze nieuwe
            tags.attrs = new_attrs

        # hier kunnen we nog elementen op basis van normale string matches verwijderen
        self.clean_soup = str(soup)
        for find, replace in self.find_and_replace_patterns.items():
            _logger.debug(f"replacing {find} with {replace}")
            self.clean_soup = re.sub(find, replace, self.clean_soup)

        _logger.info(f"Cleaning: {self.filename} -> {self.output_file}")

        with smart_open(self.output_file) as stream:
            stream.write(self.clean_soup)
