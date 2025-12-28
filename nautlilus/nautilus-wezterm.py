#!/usr/bin/env python3
import os
from urllib.parse import unquote
from gi.repository import Nautilus, GObject
from typing import List


class OpenWezTermExtension(GObject.GObject, Nautilus.MenuProvider):
    def _open_wezterm(self, file: Nautilus.FileInfo) -> None:
        filename = unquote(file.get_uri()[7:])

        os.chdir(filename)
        os.system("wezterm .")

    def menu_activate_cb(
        self,
        menu: Nautilus.MenuItem,
        file: Nautilus.FileInfo,
    ) -> None:
        self._open_wezterm(file)

    def menu_background_activate_cb(
        self,
        menu: Nautilus.MenuItem,
        file: Nautilus.FileInfo,
    ) -> None:
        self._open_wezterm(file)

    def get_file_items(
        self,
        files: List[Nautilus.FileInfo],
    ) -> List[Nautilus.MenuItem]:
        if len(files) != 1:
            return []

        file = files[0]
        if not file.is_directory() or file.get_uri_scheme() != "file":
            return []

        item = Nautilus.MenuItem(
            name="NautilusPython::openwezterm_file_item",
            label="Open in WezTerm",
        )
        item.connect("activate", self.menu_activate_cb, file)

        return [
            item,
        ]

    def get_background_items(
        self,
        current_folder: Nautilus.FileInfo,
    ) -> List[Nautilus.MenuItem]:
        item = Nautilus.MenuItem(
            name="NautilusPython::openwezterm_file_item2",
            label="Open in WezTerm",
        )
        item.connect("activate", self.menu_background_activate_cb, current_folder)

        return [
            item,
        ]
