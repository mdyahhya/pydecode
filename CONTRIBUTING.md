# Contributing to PyExplain

Thank you for considering contributing to PyExplain! 🎉

## 🚀 How Can I Contribute?

### Reporting Bugs 🐛

Create an issue with:
- Clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS
- Code samples

### Suggesting Features 💡

- Check if already suggested
- Create issue with `enhancement` label
- Describe feature and benefits
- Include use cases

### Adding Exception Mappings 📝

Edit `pyexplain/mapping.py`:


"ExceptionName": {
"simple_explanation": "2-3 line beginner explanation with emoji",
"fix_suggestion": "One-line fix suggestion",
"tags": ["tag1", "tag2"],
"emoji": "🔥",
"rich": {"img": None, "audio": None}
}


---

## 🛠️ Development Setup


Clone repository
git clone https://github.com/mdyahhya/pyexplain.git
cd pyexplain

Create virtual environment
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

Install development dependencies
pip install -e ".[dev]"

Create branch
git checkout -b feature/your-feature-name


---

## ✅ Development Workflow

### 1. Make Changes
- Write clear, readable code
- Follow existing code style
- Add docstrings

### 2. Write Tests

def test_your_feature():
result = your_function(test_input)
assert result == expected_output


### 3. Run Tests


pytest
pytest --cov=pyexplain --cov-report=html


### 4. Format Code

black pyexplain tests examples


### 5. Lint Code

ruff check pyexplain tests


### 6. Commit

git add .
git commit -m "Add feature: description"


**Commit Message Format:**
- Use present tense
- Be descriptive
- Reference issues if applicable

### 7. Push and Create PR
git push origin feature/your-feature-name


---

## 📋 Pull Request Checklist

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] New tests added
- [ ] Code formatted with Black
- [ ] Code passes Ruff linting
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
- [ ] Clear commit messages

---

## 🎨 Code Style

- Follow PEP 8
- Use Black (line length: 100)
- Use type hints
- Write docstrings

---

## 💬 Questions?

- Open an issue
- Email: yahyabuilds@gmail.com

---

**Powered by PyExplain ● Created by Yahya**

