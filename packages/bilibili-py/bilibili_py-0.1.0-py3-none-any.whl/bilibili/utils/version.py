import re
from typing import ClassVar


class Version:
    """PEP 440 compliant version number."""

    pattern: ClassVar[str] = r"^(\d+)\.(\d+)\.(\d+)(\.dev\d+)?"

    def __init__(self, major: int, minor: int, micro: int, dev: int = 0, /):
        self.major = major
        self.minor = minor
        self.micro = micro
        self.dev = dev
        self._tuple = (major, minor, micro, dev)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(major={self.major}, minor={self.minor}, micro={self.micro}, dev={self.dev})"
        )

    def __str__(self) -> str:
        """PEP 440 compliant string.

        main:  X.Y[.Z]  - for release segment
        sub:   [.devN]  - for dev release segment
        """
        sub = f".dev{self.dev}" if self.dev else ""
        return f"{self.major}.{self.minor}.{self.micro}{sub}"

    def __eq__(self, other: "Version"):
        if not isinstance(other, Version):
            raise TypeError("Expected Version instance for comparison")

        return self._tuple == other._tuple

    def __lt__(self, other: "Version"):
        if not isinstance(other, Version):
            raise TypeError("Expected Version instance for comparison")

        return self._tuple < other._tuple

    def __gt__(self, other: "Version"):
        if not isinstance(other, Version):
            raise TypeError("Expected Version instance for comparison")
        return self._tuple > other._tuple

    @staticmethod
    def parse(version_string: str):
        """Parse a version string into a Version object."""

        match = re.match(Version.pattern, version_string)

        major, minor, micro = int(match.group(1)), int(match.group(2)), int(match.group(3))
        dev = int(match.group(4)[4:]) if match.group(4) else 0

        return Version(major, minor, micro, dev)
