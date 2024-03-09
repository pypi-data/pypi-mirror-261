"""Functions to download trade data and code tables"""


import ssl
import sys
import time
from pathlib import Path
from urllib import error, request

from comexdown.tables import AUX_TABLES, TABLES

CANON_URL = "https://balanca.economia.gov.br/balanca/bd/"


def is_more_recent(response: request.Request, dest: Path) -> bool:
    """Check if the file is more recent than the one in `dest`"""
    # Check Last-Modified header
    last_modified = response.headers.get("Last-Modified")
    if last_modified is not None:
        last_modified = time.mktime(
            time.strptime(last_modified, "%a, %d %b %Y %H:%M:%S %Z")
        )
        if dest.stat().st_mtime < last_modified:
            return True
    return False


def download_file(
    url: str,
    filepath: Path = None,
    retry: int = 3,
    blocksize: int = 1024,
) -> Path | None:
    """Downloads the file in `url` and saves it in `path`

    Parameters
    ----------
    url: str
        The resource's URL to download
    filepath: Path, optional
        The destination path of downloaded file
    retry: int [default=3]
        Number of retries until raising exception
    blocksize: int [default=1024]
        The block size of requests

    returns: Path

    """

    if filepath is not None:
        if not filepath.parent.exists():
            filepath.parent.makedirs(parents=True)
        dest = filepath
    else:
        dest = Path(url.rsplit("/", maxsplit=1)[1])
    for x in range(retry):
        sys.stdout.write(f"Downloading: {url:<50} --> {dest}\n")
        sys.stdout.flush()
        try:
            resp = request.urlopen(url, context=ssl.SSLContext())

            if not is_more_recent(resp, dest):
                sys.stdout.write(f"             {dest} is up to date.\n")
                sys.stdout.flush()
                return

            # Download file
            length = resp.getheader("content-length")
            if length:
                length = int(length)

            size = 0
            with open(dest, "wb") as f:
                while True:
                    buf1 = resp.read(blocksize)
                    if not buf1:
                        break
                    f.write(buf1)
                    size += len(buf1)
                    p = size / length
                    bar = "[{:<70}]".format("=" * int(p * 70))
                    if size > 2**20:
                        size_txt = "{: >9.2f} MiB".format(size / 2**20)
                    else:
                        size_txt = "{: >9.2f} KiB".format(size / 2**10)
                    if length:
                        sys.stdout.write(
                            f"{bar} {p*100: >5.1f}% {size_txt}\r")
                        sys.stdout.flush()

        except error.URLError as e:
            sys.stdout.write(f"\nError... {e}")
            sys.stdout.flush()
            time.sleep(3)
            if x == retry - 1:
                raise

        else:
            sys.stdout.write("\n")
            sys.stdout.flush()
            break

    return dest


def table(table_name: str, path: Path) -> Path | None:
    url = CANON_URL + "tabelas/" + AUX_TABLES[table_name]
    filepath = download_file(url, path)
    return filepath


def exp(year: int, path: Path) -> Path | None:
    """Downloads a exp file

    Parameters
    ----------
    year: int
        exp year to download
    path: str
        Destination path directory to save file

    """
    url = CANON_URL + "comexstat-bd/ncm/EXP_{year}.csv".format(year=year)
    filepath = download_file(url, path)
    return filepath


def imp(year: int, path: Path) -> Path | None:
    """Downloads a imp file

    Parameters
    ----------
    year: int
        imp year to download
    path: str
        Destination path directory to save file

    """
    url = CANON_URL + "comexstat-bd/ncm/IMP_{year}.csv".format(year=year)
    filepath = download_file(url, path)
    return filepath


def exp_mun(year: int, path: Path) -> Path | None:
    """Downloads a exp_mun file

    Parameters
    ----------
    year: int
        exp_mun year to download
    path: str
        Destination path directory to save file

    """
    url = CANON_URL + "comexstat-bd/mun/EXP_{year}_MUN.csv".format(year=year)
    filepath = download_file(url, path)
    return filepath


def imp_mun(year: int, path: Path) -> Path | None:
    """Downloads a imp_mun file

    Parameters
    ----------
    year: int
        imp_mun year to download
    path: str
        Destination path directory to save file

    """
    url = CANON_URL + "comexstat-bd/mun/IMP_{year}_MUN.csv".format(year=year)
    filepath = download_file(url, path)
    return filepath


def exp_nbm(year: int, path: Path) -> Path | None:
    """Downloads a exp_nbm file

    Parameters
    ----------
    year: int
        exp_nbm year to download
    path: str
        Destination path directory to save file

    """
    url = CANON_URL + "comexstat-bd/nbm/EXP_{year}_NBM.csv".format(year=year)
    filepath = download_file(url, path)
    return filepath


def imp_nbm(year: int, path: Path) -> Path | None:
    """Downloads a imp_nbm file

    Parameters
    ----------
    year: int
        imp_nbm year to download
    path: str
        Destination path directory to save file

    """
    url = CANON_URL + "comexstat-bd/nbm/IMP_{year}_NBM.csv".format(year=year)
    filepath = download_file(url, path)
    return filepath


def exp_complete(path: Path) -> Path | None:
    """Downloads the file with complete data of exp

    Parameters
    ----------
    path : str
        Destination path directory to save file

    """
    url = CANON_URL + "comexstat-bd/ncm/EXP_COMPLETA.zip"
    filepath = download_file(url, path)
    return filepath


def imp_complete(path: Path) -> Path | None:
    """Downloads the file with complete data of imp

    Parameters
    ----------
    path : str
        Destination path directory to save file

    """
    url = CANON_URL + "comexstat-bd/ncm/IMP_COMPLETA.zip"
    filepath = download_file(url, path)
    return filepath


def exp_mun_complete(path: Path) -> Path | None:
    """Downloads the file with complete data of exp_mun

    Parameters
    ----------
    path : str
        Destination path directory to save file

    """
    url = CANON_URL + "comexstat-bd/mun/EXP_COMPLETA_MUN.zip"
    filepath = download_file(url, path)
    return filepath


def imp_mun_complete(path: Path) -> Path | None:
    """Downloads the file with complete data of imp_mun

    Parameters
    ----------
    path : str
        Destination path directory to save file

    """
    url = CANON_URL + "comexstat-bd/mun/IMP_COMPLETA_MUN.zip"
    filepath = download_file(url, path)
    return filepath


def agronegocio(path: Path) -> Path | None:
    """Downloads agronegocio file

    Parameters
    ----------
    path : str
        Destination path directory to save file

    """
    url = TABLES["agronegocio"]["url"]
    filepath = download_file(url, path)
    return filepath
