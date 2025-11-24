"""
PyDefine Version Management Module

This module contains version information for the PyDefine library.
It follows Semantic Versioning (SemVer): MAJOR.MINOR.PATCH

- MAJOR: Incompatible API changes
- MINOR: Add functionality in a backwards compatible manner
- PATCH: Backwards compatible bug fixes

Author: Md. Yahya Ab. Wahid Mundewadi
Email: yahyabuilds@gmail.com
Organization: Dominal Group
Website: https://dominal.in
License: MIT
"""

# Version information
__version__ = "1.0.0"
__version_info__ = tuple(int(i) for i in __version__.split("."))

# Package metadata
__title__ = "PyDefine"
__description__ = "Convert Python errors into beginner-friendly explanations"
__url__ = "https://github.com/mdyahhya/pydefine"
__author__ = "Md. Yahya Ab. Wahid Mundewadi"
__author_email__ = "yahyabuilds@gmail.com"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2025 Md. Yahya Ab. Wahid Mundewadi (Dominal Group)"

# Company information
__company__ = "Dominal Group"
__company_url__ = "https://dominal.in"

# Branding
__branding__ = "Powered by PyDefine ● Created by Yahya"

# Python version requirements
__python_requires__ = ">=3.8"

# Supported Python versions
__python_versions__ = [
    "3.8",
    "3.9",
    "3.10",
    "3.11",
    "3.12",
    "3.13"
]

# Release information
__status__ = "Production/Stable"
__release_date__ = "2025-11-23"

# API version (for future backwards compatibility tracking)
__api_version__ = "1.0"

# All public version attributes
__all__ = [
    "__version__",
    "__version_info__",
    "__title__",
    "__description__",
    "__url__",
    "__author__",
    "__author_email__",
    "__license__",
    "__copyright__",
    "__company__",
    "__company_url__",
    "__branding__",
    "__python_requires__",
    "__python_versions__",
    "__status__",
    "__release_date__",
    "__api_version__"
]


def get_version() -> str:
    """
    Get the current version of PyDefine.
    
    Returns:
        str: Version string in format MAJOR.MINOR.PATCH
        
    Example:
        >>> from pydefine._version import get_version
        >>> print(get_version())
        1.0.0
    """
    return __version__


def get_version_info() -> dict:
    """
    Get detailed version and package information.
    
    Returns:
        dict: Dictionary containing all version metadata
        
    Example:
        >>> from pydefine._version import get_version_info
        >>> info = get_version_info()
        >>> print(info['version'])
        1.0.0
        >>> print(info['author'])
        Md. Yahya Ab. Wahid Mundewadi
    """
    return {
        "version": __version__,
        "version_info": __version_info__,
        "title": __title__,
        "description": __description__,
        "url": __url__,
        "author": __author__,
        "author_email": __author_email__,
        "license": __license__,
        "copyright": __copyright__,
        "company": __company__,
        "company_url": __company_url__,
        "branding": __branding__,
        "python_requires": __python_requires__,
        "python_versions": __python_versions__,
        "status": __status__,
        "release_date": __release_date__,
        "api_version": __api_version__
    }


def print_version_info() -> None:
    """
    Print formatted version information to console.
    
    This is useful for debugging and support requests.
    
    Example:
        >>> from pydefine._version import print_version_info
        >>> print_version_info()
        ╔══════════════════════════════════════════════════════════╗
        ║                   PyDefine v1.0.0                        ║
        ╚══════════════════════════════════════════════════════════╝
        ...
    """
    info = get_version_info()
    
    print("╔══════════════════════════════════════════════════════════╗")
    print(f"║          {info['title']} v{info['version']}                           ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print()
    print(f"Description : {info['description']}")
    print(f"Author      : {info['author']}")
    print(f"Email       : {info['author_email']}")
    print(f"Company     : {info['company']}")
    print(f"Website     : {info['company_url']}")
    print(f"Repository  : {info['url']}")
    print(f"License     : {info['license']}")
    print(f"Status      : {info['status']}")
    print(f"Released    : {info['release_date']}")
    print(f"Python      : {info['python_requires']}")
    print()
    print(f"✨ {info['branding']}")
    print()


if __name__ == "__main__":
    # When run directly, print version information
    print_version_info()
