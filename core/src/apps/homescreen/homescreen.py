from trezor.ui.layouts import homescreen as homescreen_layout

from apps.base import lock_device


async def homescreen() -> None:
    await homescreen_layout()
    lock_device()
