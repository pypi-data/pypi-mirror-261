#!/usr/bin/env python3
from typing import List


class TermColor:
    decorations = dict(
        BLACK="\033[30m",
        BLACK_BG="\033[40m",
        WHITE="\033[97m",
        WHITE_BG="\033[107m",
        RED="\033[91m",
        RED_BG="\033[101m",
        GREEN="\033[32m",
        GREEN_BG="\033[42m",
        YELLO="\033[33m",
        YELLO_BG="\033[43m",
        BLUE="\033[34m",
        BLUE_BG="\033[44m",
        MAGENTA="\033[35m",
        MAGENTA_BG="\033[45m",
        CYAN="\033[36m",
        CYAN_BG="\033[46m",
        DEFAULT="\033[39m",
        DEFAULT_BG="\033[49m",
        RESET="\033[m0",
        BOLD="\033[1m",
        UNDERLINE="\033[4m",
        ITALIC="\033[3m",
        END="\033[0m",
    )

    @classmethod
    def list(cls) -> List[str]:
        return list(cls.decorations.keys())

    @classmethod
    def decorate(cls, string: str, decorations: List[str]):
        res = ""
        for dec in decorations:
            try:
                res += cls.decorations[dec.upper()]
            except KeyError as e:
                raise AttributeError(f"Unknown decorator '{dec}'")

        res += string
        res += cls.decorations["END"]
        return res
