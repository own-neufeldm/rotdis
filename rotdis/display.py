from dataclasses import dataclass

import win32api
import win32con


@dataclass(frozen=True)
class Display:
    """Windows 10 display."""
    _handle: int  # _win32typing.PyHANDLE

    def _get_info(self):  # _win32typing._MonitorInfo
        return win32api.GetMonitorInfo(self._handle)

    def _get_device(self) -> str:
        return self._get_info()["Device"]

    def _get_device_modew(self):  # _win32typing.PyDEVMODEW
        return win32api.EnumDisplaySettings(
            self._get_device(),
            win32con.ENUM_CURRENT_SETTINGS
        )

    def is_primary(self) -> bool:
        """Checks if this display is configured as primary."""
        return self._get_info()["Flags"] == 1  # wtf

    def get_rotation(self) -> int:
        """Returns the current rotation of this display."""
        return self._get_device_modew().DisplayOrientation * 90

    def set_rotation(self, degree: int) -> None:
        """Sets the rotation of this display
        
        Args:
            degree: The degree of rotation, must be one of [0, 90, 180, 270].
        """
        if degree == 0:
            orientation = win32con.DMDO_DEFAULT
        elif degree == 90:
            orientation = win32con.DMDO_90
        elif degree == 180:
            orientation = win32con.DMDO_180
        elif degree == 270:
            orientation = win32con.DMDO_270
        else:
            raise ValueError(
                f"Degree ({degree}) must be one of [0, 90, 180, 270]."
            )
        dmw = self._get_device_modew()
        if (dmw.DisplayOrientation + orientation) % 2 == 1:
            height, width = dmw.PelsHeight, dmw.PelsWidth
            dmw.PelsWidth, dmw.PelsHeight = height, width  # type: ignore
        dmw.DisplayOrientation = orientation  # type: ignore
        win32api.ChangeDisplaySettingsEx(
            self._get_device(),
            dmw  # type: ignore
        )
        return None


def get_displays() -> list[Display]:
    """Returns a list of all connected displays."""
    return [
        Display(handle)  # type: ignore
        for handle, _, _ in win32api.EnumDisplayMonitors()
    ]


def get_primary_display() -> Display:
    """Returns the primary display."""
    for display in get_displays():
        if display.is_primary():
            return display
    raise ValueError("Primary display not found.")
