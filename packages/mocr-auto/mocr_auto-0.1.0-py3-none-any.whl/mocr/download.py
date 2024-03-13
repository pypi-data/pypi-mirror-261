import stat
import sys
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

import requests
from tqdm import tqdm

from mocr.constants import CHROMIUM_VERSION, FIREFOX_BUILD, INSTALL_PATH


CHROMIUM_DL_HOST = 'https://gsdview.appspot.com/chromium-browser-snapshots'
FIREFOX_DL_HOST = "https://archive.mozilla.org/pub/firefox/nightly/2024/01/2024-01-21-20-40-46-mozilla-central"  # noqa

CR_DOWNLOAD_URLS = {
    'linux': f'{CHROMIUM_DL_HOST}/Linux_x64/{CHROMIUM_VERSION}/chrome-linux.zip',
    'darwin': f'{CHROMIUM_DL_HOST}/Mac/{CHROMIUM_VERSION}/chrome-mac.zip',
    'win32': f'{CHROMIUM_DL_HOST}/Win_x64/{CHROMIUM_VERSION}/chrome-win.zip',
}
FF_DOWNLOAD_URLS = {
    "linux": f"{FIREFOX_DL_HOST}/firefox-{FIREFOX_BUILD}.en-US.LINUX-x86_64.tar.bz2",
    "darwin": f"{FIREFOX_DL_HOST}/firefox-{FIREFOX_BUILD}.en-US.mac.dmg",
    "win32": f"{FIREFOX_DL_HOST}/firefox-{FIREFOX_BUILD}.en-US.win64.zip",
}

CR_BINARY_NAMES = {
    'linux': INSTALL_PATH / CHROMIUM_VERSION / 'chrome-linux' / 'chromium',
    'darwin': INSTALL_PATH / CHROMIUM_VERSION / 'chrome-mac' / 'Chromium.app' / 'Contents' / 'MacOS' / 'Chromium',  # noqa
    'win32': INSTALL_PATH / CHROMIUM_VERSION / 'chrome-win' / 'chrome.exe',
}
FF_BINARY_NAMES = {
    "linux": INSTALL_PATH / FIREFOX_BUILD / 'firefox' / 'firefox',
    "darwin": INSTALL_PATH / FIREFOX_BUILD / 'Firefox Nightly.app' / 'Contents' / 'MacOS' / 'firefox',
    "win32": INSTALL_PATH / FIREFOX_BUILD / 'firefox' /'firefox.exe',
}
CR_BINARY_PATHS = {
    k: v.expanduser().absolute() for k, v in CR_BINARY_NAMES.items()
}
FF_BINARY_PATHS = {
    k: v.expanduser().absolute() for k, v in FF_BINARY_NAMES.items()
}


def download_zip(browser_type: str, url: str) -> BytesIO:
    """
    Download browser from the given `url`.

    Args:
        browser_type (str): Target browser type, of "chromium" or "firefox".
        url (str): URL to download from.

    Raises:
        requests.HTTPError: Raised if response is bad (status code over 399).

    Returns:
        BytesIO: The browser content as a BytesIO object.
    """
    print(f'Starting {browser_type.title()} download.')
    data = BytesIO()
    with requests.get(url, stream=True) as response:
        if response.status_code >= 400:
            raise requests.HTTPError(f"Bad response from server at: {url}")
        try:
            total_length = int(response.headers['content-length'])
        except (KeyError, ValueError, AttributeError):
            total_length = 0
        process_bar = tqdm(total=total_length, unit_scale=True, unit='b')
        for chunk in response.iter_content(chunk_size=8192):
            data.write(chunk)
            process_bar.update(len(chunk))
        process_bar.close()
    return data


def browser_binary(browser_type: str) -> Path:
    """
    Get path of the system target browser binary.

    Args:
        browser_type (str): Target browser type, of "chromium" or "firefox".

    Returns:
        Path: Browser binary Path object.
    """
    types_to_maps = {
        "chromium": CR_BINARY_PATHS,
        "firefox": FF_BINARY_PATHS,
    }
    mapping = types_to_maps[browser_type]
    return mapping[sys.platform]


def ensure_binary(browser_type: str) -> bool:
    """
    Ensure the target browser exists on this machine.

    Args:
        browser_type (str): Target browser type, of "chromium" or "firefox".

    Returns:
        bool: True if binary exists, otherwise False.
    """
    return browser_binary(browser_type).exists()


def extract_zip(browser_type: str, data: BytesIO, path: Path) -> None:
    """
    Extract given loaded zip file to target `path`.

    Args:
        browser_type (str): Target browser type, of "chromium" or "firefox".
        data (BytesIO): Zip file as BytesIO.
        path (Path): Destination path to extract to.

    Raises:
        IOError: Raised if an unhandled error occurs and the browser simply
            doesn't end up extracted to the target.
    """
    # On mac zipfile module cannot extract correctly, so use unzip instead.
    print(f'Beginning {browser_type.title()} extraction.')
    if sys.platform == 'darwin':
        import shutil
        import subprocess
        zip_path = path / 'chrome.zip'
        if not path.exists():
            path.mkdir(parents=True)
        with zip_path.open('wb') as f:
            f.write(data.getvalue())
        if not shutil.which('unzip'):
            raise FileNotFoundError(
                'Cannot find unzip command on path.'
                f' You can unzip manually at: {zip_path}'
            )
        proc = subprocess.run(
            ['unzip', str(zip_path)],
            cwd=str(path),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        if proc.returncode != 0:
            print(proc.stdout.decode())
            raise subprocess.CalledProcessError(
                f'Failed to unzip file at: {zip_path}'
            )
        if ensure_binary() and zip_path.exists():
            zip_path.unlink()
    else:
        with ZipFile(data) as zf:
            for member in tqdm(zf.infolist()):
                zf.extract(member, str(path))
    if not ensure_binary(browser_type):
        raise IOError('Failed to extract browser.')
    browser_binary(browser_type).chmod(
        browser_binary(browser_type).stat(
        ).st_mode | stat.S_IXOTH | stat.S_IXGRP | stat.S_IXUSR
    )
    print(f'{browser_type.title()} successfully extracted to: {path}')


def install_binary(browser_type: str) -> None:
    """
    Download and extract binary.
    
    Args:
        browser_type (str): Target browser type, of "chromium" or "firefox".
    """
    type_to_infos = {
        "chromium": (CR_DOWNLOAD_URLS, CHROMIUM_VERSION),
        "firefox": (FF_DOWNLOAD_URLS, FIREFOX_BUILD),
    }
    download_urls, version = type_to_infos[browser_type]
    extract_zip(
        browser_type,
        download_zip(browser_type, download_urls[sys.platform]),
        INSTALL_PATH / version
    )
