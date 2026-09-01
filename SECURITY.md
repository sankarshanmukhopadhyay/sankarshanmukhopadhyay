# Security Policy

This profile repository does not ship production software. Security-relevant issues may nevertheless arise in workflows, generated pages, validation scripts, links, or published metadata.

## Reporting

Do not open a public issue for a vulnerability that could expose credentials, permit workflow abuse, or materially mislead users about assurance status. Use GitHub private vulnerability reporting where available.

## Scope

In scope:

- workflow injection or unsafe permissions;
- malicious or misleading generated portfolio state;
- validation bypasses affecting published assurance claims;
- exposed credentials or sensitive configuration.

## Assurance publisher boundary

The portfolio assurance workflow has write capability solely to publish generated assurance evidence in the governed output paths documented in `GOVERNANCE.md`. Any ability to use that automation to modify governance declarations, relationship metadata, workflows, source code, schemas, configuration, or authority records is a security defect and should be reported privately.

Project-specific implementation vulnerabilities must be reported to the affected member repository.
