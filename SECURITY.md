# Security Policy

## 🔒 Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | ✅ Yes             |
| < 1.0   | ❌ No              |

---

## 🚨 Reporting a Vulnerability

**Please DO NOT report security vulnerabilities through public GitHub issues.**

Report via email to: **yahyabuilds@gmail.com**

**Subject:** `[SECURITY] PyExplain Vulnerability Report`

### What to Include

- Type of vulnerability
- Full paths of affected source files
- Location of source code (tag/branch/commit)
- Step-by-step reproduction instructions
- Proof-of-concept or exploit code
- Impact assessment
- Suggested fix (if available)

### Response Timeline

- **Initial Response:** Within 48 hours
- **Status Update:** Within 7 days
- **Fix Timeline:**
  - Critical: Within 7 days
  - High: Within 30 days
  - Medium: Within 60 days
  - Low: Within 90 days

---

## 🛡️ Security Best Practices

### For Users

1. **Always Update:**

pip install --upgrade pyexplain


2. **Validate Input:** Be cautious with untrusted code in `safe_run()`

Safe: Your own code
my_code = "x = 10; print(x)"
result = pyexplain.safe_run(my_code)

Unsafe: Untrusted user input - DON'T DO THIS
user_code = request.form['code']
result = pyexplain.safe_run(user_code) # DANGEROUS


3. **Limit Permissions:** Run with minimal required permissions

### For Contributors

- No hardcoded secrets
- Validate and sanitize input
- Use type hints
- Write security tests
- Review dependencies (we use zero)

---

## 🔐 Known Security Considerations

### Code Execution in `safe_run()`

⚠️ **Do not** run untrusted code in production  
⚠️ **Do not** use with user-provided code from unknown sources  
✅ **Do** use for debugging your own code  
✅ **Do** use in educational environments with trusted code

### Traceback Information Disclosure

Tracebacks may contain:
- File paths
- Function names
- Variable names

**Mitigation:** Review output before sharing publicly

---

## 📞 Contact

**Security Issues:** yahyabuilds@gmail.com  
**General Questions:** GitHub Issues  
**Company:** Dominal Group (https://dominal.in)

---

**Last Updated:** 2025-11-23

**Powered by PyExplain ● Created by Yahya**
