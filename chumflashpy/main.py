import re
from functools import reduce
from repositories.category_repo import CategoryRepo
from repositories.flash_card_repo import FlashCardRepo
from repositories.user_data import UserData
from presentation.user_interface import UserInterface


from database import create_tables

USER_DATA_FILE_NAME = "user_data.txt"

create_tables()


def main() -> None:
    UserInterface(
        cr=CategoryRepo(),
        fcr=FlashCardRepo(),
        user_data=UserData(USER_DATA_FILE_NAME),
        func_fix_space=fix_space,
        func_calc_complexity=calc_complexity,
        func_clean_tag_list=clean_tag_list,
    ).main_menu()


def fix_space(s: str) -> str:
    """
    Fixes spaces of a phrase.

    Removes leading and trailing spaces.
    Removes extra spaces between words.
    Removes any space before punctuations(.,:;?!).
    Ensures space after punctuations(.,:;?!) and before alphanumeric characters.

    Parameters
    -------------
    s: str
        Input string.

    Returns
    -------------
    str
        Cleaned output string.
    """

    if not s:
        return ""

    # Removes extra spaces between words
    s = re.sub(r"\s+", " ", s)

    # Removes any space before punctuations(.,:;?!)
    s = re.sub(r"\s(?=[.,:;?!])", "", s)

    # Ensures space after punctuations(.,:;?!) and before alphanumeric characters
    s = re.sub(r"([.,:;?!])([a-zA-Z0-9])", r"\1 \2", s)

    # Removes leading and trailing spaces
    s = s.strip()
    return s


def calc_complexity(s: str) -> int:
    """
    Calculates complexity of the input phrase based on the number of letters

    Counts the total number of alphabetical characters
    in words without any numbers

    Parameters
    -------------
    s: str
        Input string.

    Returns
    -------------
    int
        Number of letters.
    """

    if not s:
        return 0
    parts = re.split(" ", s)
    cnt = 0
    for part in parts:
        part = part.strip()
        if re.search(r"^[^0-9]+$", part):
            cnt += len(re.findall(r"[a-zA-Z]", part))
    return cnt


def clean_tag_list(taglist: list[str]) -> str:
    """
    Cleans the tag list used for a flash card

    converts them to lowercase string
    Removes leading and trailing spaces
    removes empty tags from the tag list
    removes duplicates from the tag list
    sorts them alphabetically
    use dash to separate them

    Parameters
    -------------
    taglist: List[str]
        List of sting tags

    Returns
    -------------
    str
        A string representing dash separated sorted cleaned lowercased tag list
    """
    if not taglist:
        return ""
    tagmap = map(lambda s: s.lower().strip() if s else "", taglist)
    tagfilter = filter(lambda x: bool(x), tagmap)
    taglist = sorted(list(set(tagfilter)))
    if not taglist:
        return ""
    result = reduce(lambda x, y: x + "-" + y, taglist)
    return result


if __name__ == "__main__":
    main()
