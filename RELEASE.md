# Release Instructions

This document describes how to release a new version of PyExplain to PyPI.

## Prerequisites

- PyPI account with access to pyexplain package
- GitHub repository access
- Python 3.8+ installed
- `build` and `twine` installed

pip install build twine

---

## Release Checklist

### 1. Update Version

Edit `pyexplain/_version.py`:


version = "1.1.0" # Update version number
release_date = "2025-12-01" # Update date

### 2. Update CHANGELOG.md

Add new version section:


[1.1.0] - 2025-12-01
Added
New feature description

Fixed
Bug fix description

### 3. Run Tests


Run full test suite
pytest

Check coverage
pytest --cov=pyexplain --cov-report=html

All tests must pass!

### 4. Format and Lint


Format code
black pyexplain tests examples

Check linting
ruff check pyexplain tests

Type checking
mypy pyexplain

### 5. Commit Changes


git add .
git commit -m "Release v1.1.0"
git push origin main

### 6. Create Git Tag


git tag v1.1.0
git push origin v1.1.0

### 7. Build Package


Clean old builds
rm -rf dist/ build/ *.egg-info

Build distribution
python -m build

This creates:
- `dist/pyexplain-1.1.0.tar.gz` (source)
- `dist/pyexplain-1.1.0-py3-none-any.whl` (wheel)

### 8. Test Package Locally


Create test environment
python -m venv test_env
source test_env/bin/activate # Windows: test_env\Scripts\activate

Install from local wheel
pip install dist/pyexplain-1.1.0-py3-none-any.whl

Test import
python -c "import pyexplain; print(pyexplain.version)"

Deactivate
deactivate

### 9. Upload to TestPyPI (Optional)


Upload to test repository
twine upload --repository testpypi dist/*

Test installation
pip install --index-url https://test.pypi.org/simple/ pyexplain


### 10. Upload to PyPI


Upload to production PyPI
twine upload dist/*

Enter credentials when prompted

### 11. Verify on PyPI

Visit: https://pypi.org/project/pyexplain/

Check:
- Version number is correct
- README displays properly
- Links work
- Metadata is accurate

### 12. Test Installation


Create fresh environment
python -m venv verify_env
source verify_env/bin/activate

Install from PyPI
pip install pyexplain

Verify
python -c "import pyexplain; pyexplain.print_version_info()"

Test CLI
pyexplain --version

### 13. Create GitHub Release

1. Go to: https://github.com/mdyahhya/pyexplain/releases
2. Click "Create a new release"
3. Choose tag: `v1.1.0`
4. Release title: `PyExplain v1.1.0`
5. Description: Copy from CHANGELOG.md
6. Attach distribution files (optional)
7. Click "Publish release"

### 14. Announce Release

- Update README badges (if needed)
- Post on social media (optional)
- Notify contributors

---

## Rollback (if needed)

If there's a critical issue:


Delete PyPI version (contact PyPI support)
Revert git tag
git tag -d v1.1.0
git push origin :refs/tags/v1.1.0

Revert commit
git revert HEAD
git push origin main


---

## Version Numbering

Follow Semantic Versioning (SemVer):

- **MAJOR** (1.x.x): Breaking changes
- **MINOR** (x.1.x): New features, backward compatible
- **PATCH** (x.x.1): Bug fixes, backward compatible

Examples:
- `1.0.0` → `1.0.1`: Bug fix
- `1.0.0` → `1.1.0`: New feature
- `1.0.0` → `2.0.0`: Breaking change

---

## PyPI Credentials

Store credentials in `~/.pypirc`:


[pypi]
username = token
password = pypi-AgEIcHlwaS5vcmc...

[testpypi]
username = token
password = pypi-AgENdGVzdC5weXBp...


**Never commit this file!**

---

## Automation (Future)

Consider GitHub Actions for automated releases:
- Auto-build on tag push
- Auto-upload to PyPI
- Auto-create GitHub release

---

**Powered by PyExplain ● Created by Yahya**


