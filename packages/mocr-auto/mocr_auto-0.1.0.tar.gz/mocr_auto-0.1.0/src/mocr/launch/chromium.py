import os
import shutil
import sys
import tempfile
import time
from copy import copy
from urllib.parse import urlparse

from mocr.constants import INSTALL_PATH
from mocr.launch.base import Launcher


CHROMIUM_PROFILE_PATH = INSTALL_PATH / '.dev_profile'

DEFAULT_CHROMIUM_ARGS = [
    '--disable-background-networking',
    '--disable-background-timer-throttling',
    '--disable-breakpad',
    '--disable-browser-side-navigation',
    '--disable-client-side-phishing-detection',
    '--disable-default-apps',
    '--disable-dev-shm-usage',
    '--disable-extensions',
    '--disable-features=site-per-process',
    '--disable-hang-monitor',
    '--disable-popup-blocking',
    '--disable-prompt-on-repost',
    '--disable-sync',
    '--disable-translate',
    '--metrics-recording-only',
    '--no-first-run',
    '--safebrowsing-disable-auto-update',
    '--enable-automation',
    '--password-store=basic',
    '--use-mock-keychain',
    '--enable-features=NetworkServiceInProcess2',
]


class ChromiumLauncher(Launcher):
    kind = "chromium"

    def _parse_proxy(self, proxy: str) -> None:
        proxy_parts = urlparse(proxy)
        scheme = proxy_parts.scheme
        host = proxy_parts.hostname
        port = proxy_parts.port
        if proxy.startswith("socks"):
            args = [
                f'--proxy-server={proxy}',
                f'--host-resolver-rules="MAP * ~NOTFOUND , EXCLUDE {host}"',
            ]
        else:
            proxy = f"{scheme}://{host}:{port}"
            args = [f'--proxy-server={proxy}']
        self.browser_arguments.extend(args)
        credentials = {}
        credentials["proxy"] = proxy
        if proxy_parts.username:
            credentials["username"] = proxy_parts.username
        if proxy_parts.password:
            credentials["password"] = proxy_parts.password
        return credentials

    def _custom_default_args(
        self,
        headless: bool = None,
        user_data_dir: str = None,
        devtools: bool = False,
    ):
        browser_arguments = copy(DEFAULT_CHROMIUM_ARGS)
        if user_data_dir:
            browser_arguments.append(f'--user-data-dir={user_data_dir}')
        if devtools:
            browser_arguments.append('--auto-open-devtools-for-tabs')
        if headless:
            browser_arguments.extend(
                ('--headless=new', '--hide-scrollbars', '--mute-audio')
            )
            if sys.platform.startswith('win'):
                browser_arguments.append('--disable-gpu')
        
        return browser_arguments

    def _compute_launch_args(
        self,
        headless: bool = None,
        user_data_dir: str = None,
        devtools: bool = False,
        ignore_default_args: bool | list[str] = False,
        proxy: str = None,
        args: list[str] = None,
    ):
        super()._compute_launch_args(
            headless=headless,
            user_data_dir=user_data_dir,
            devtools=devtools,
            ignore_default_args=ignore_default_args,
            proxy=proxy,
            args=args,
        )
        self.proxy_credentials = self._parse_proxy(proxy) if proxy else None
        self.temp_user_data_dir = None
        if not any(
            arg for arg in self.browser_arguments
            if arg.startswith('--remote-debugging-')
        ):
            self.browser_arguments.append(
                f'--remote-debugging-port={self.port}'
            )
        if not any(
            arg for arg in self.browser_arguments
            if arg.startswith('--user-data-dir')
        ):
            if not CHROMIUM_PROFILE_PATH.exists():
                CHROMIUM_PROFILE_PATH.mkdir(parents=True)
            self.temp_user_data_dir = tempfile.mkdtemp(
                dir=str(CHROMIUM_PROFILE_PATH)
            )
            self.browser_arguments.append(
                f'--user-data-dir={self.temp_user_data_dir}'
            )
    
    def _clean_restore_data_dirs(self) -> None:
        for _ in range(100):
            if self.temp_user_data_dir and os.path.exists(
                self.temp_user_data_dir
            ):
                shutil.rmtree(self.temp_user_data_dir, ignore_errors=True)
                if os.path.exists(self.temp_user_data_dir):
                    time.sleep(0.01)
            else:
                return
        else:
            raise IOError(
                'Unable to remove temporary user data dir'
                f' at {self.temp_user_data_dir}'
            )