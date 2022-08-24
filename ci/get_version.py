from semver import bump_patch
from requests import get
from bs4 import BeautifulSoup as s


def finder(url, package):
    c = get(url)
    raw = c.text
    soup = s(raw, "html.parser")
    vers_raw = soup.find_all(class_="package-header__name")[0].text

    vers = vers_raw[vers_raw.find(f"{package}") + len(package)+1:vers_raw.find(f"{package}") + len(package) + 6]
    return vers


def bump(latest):
    # TODO decide what to bump
    # Then use bump_patch, bump_minor or bump_major
    return bump_patch(latest)

if __name__=="__main__":
    package = "lightning-py"
    latest_version = finder(url="https://test.pypi.org/project/lightning-py/", package=package)
    v = bump(latest_version)
    # print(f"'{v}'")
    with open("about_version.py", "w") as file:
        file.write(f"__version__ = '{v}'")