# Security Policy

## Supported Versions

| Version | Supported |
|---------|----------|
| 1.0.x   | Yes      |

## Reporting a Vulnerability

If you discover a security vulnerability in this repository, please report it responsibly.

### How to Report

1. **Do NOT open a public issue** for security vulnerabilities
2. Email: **alpha.one.hq@proton.me** with subject: `[SECURITY] awesome-ai-index`
3. Include a detailed description of the vulnerability
4. Provide steps to reproduce if applicable

### What to Expect

- **Acknowledgment** within 48 hours
- **Assessment** within 7 days
- **Fix timeline** communicated within 14 days

### Scope

This policy covers:
- Data integrity issues in JSON datasets
- Validation script vulnerabilities
- GitHub Actions workflow security
- Supply chain concerns in dependencies

### Out of Scope

- Publicly available data accuracy disputes (use Issues instead)
- Feature requests

## Security Best Practices

When using this data:
- Always validate JSON before parsing in production
- Pin to specific release tags rather than `main`
- Verify data checksums when available

## Attribution

This security policy follows industry best practices for open-source data repositories.
