import re
from typing import *

class FilterError(Exception):
    pass

class Filter:
    def __init__(self, include: Union[str, list] = None, exclude: Union[str, list] = None) -> None:
        """
        Initializes the Filter object with include and exclude patterns.

        Parameters:
        - include: Union[str, list], optional: The inclusion pattern(s).
        - exclude: Union[str, list], optional: The exclusion pattern(s).
        
        """
        if type(include) not in [str, list] and include is not None:
            raise FilterError("Type of parameter include MUST be str, list or None.")
        elif type(exclude) not in [str, list] and exclude is not None:
            raise FilterError("Type of parameter exclude MUST be str, list or None.")
        self.incl = [include] if type(include) == str else include
        self.excl = [exclude] if type(exclude) == str else exclude

    def _preprocess_pattern(self, pattern: str) -> str:
        """
        Preprocesses the input pattern for matching.

        Parameters:
        - pattern: str: The pattern to preprocess.

        Returns:
        - str: The preprocessed pattern.
        """
        escaped_pattern = re.escape(pattern)
        processed_pattern = escaped_pattern.replace(r"\*", ".*")
        return "^" + processed_pattern + "$"
    
    def matches_pattern(self, pattern: str, dest: str) -> bool:
        """
        Checks if the given destination matches the specified pattern.

        Parameters:
        - pattern: str: The pattern to match against.
        - dest: str: The destination string to match.

        Returns:
        - bool: True if the destination matches the pattern, False otherwise.
        """
        return bool(re.search(self._preprocess_pattern(pattern), dest))

    def matches_patterns(self, pattern: List[str], dest: str) -> bool:
        """
        Checks if the given destination matches any of the specified patterns.

        Parameters:
        - pattern: List[str]: The list of patterns to match against.
        - dest: str: The destination string to match.

        Returns:
        - bool: True if the destination matches any of the patterns, False otherwise.
        """
        for pat in pattern:
            if self.matches_pattern(pat, dest):
                return pat
        return False