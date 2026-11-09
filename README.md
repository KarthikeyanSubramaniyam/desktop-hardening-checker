# Desktop & Workstation Security Posture Auditor

<p align="center">
  <img src="https://img.shields.io/badge/Security-Defensive_Auditor-blue?style=flat" alt="Type">
  <img src="https://img.shields.io/badge/Status-Architectural_Showcase-success?style=flat" alt="Status">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
</p>

> 🔒 **Technical Showcase & Architecture Specification**  
> *This repository provides public architectural documentation, system specifications, and implementation summaries. Full production source code, internal test suites, and proprietary algorithms are maintained in a secure private repository.*

---

## 📌 Executive Summary

**Category**: Endpoint Hardening & CIS Benchmarks  
**Tech Stack**: `Python 3.10+ · Endpoint Hardening · CIS Workstation Benchmarks · Posture Auditing`  

Read-only security evaluation tool assessing workstation configurations against hardened endpoint benchmarks (BitLocker, UAC, Firewall, Defender).

---

## 🎯 The Problem It Solves

Unmanaged or misconfigured workstations expose internal corporate networks. Security teams need lightweight, non-invasive posture auditing tools.

---

## ⚙️ How the Engine Works

1. **System Configuration Ingestion**: Ingests normalized endpoint security states without requiring administrative runtime agents.
2. **Core Control Verification**: Evaluates critical endpoint security controls:
   - Full Disk Encryption status (BitLocker / FileVault enabled and active)
   - User Account Control (UAC) enforcement levels (flags disabled or reduced notification modes)
   - Host Firewall status across all active network profiles
   - Anti-malware real-time protection and definition freshness
   - Screen lock and idle timeout policies
3. **CIS Benchmark Alignment**: Compares settings against CIS Workstation Benchmark recommendations.
4. **Remediation Script Generation**: Outputs corrective PowerShell / Bash commands to remediate failing controls.

---

## 🚀 Key Capabilities

- Non-invasive, read-only endpoint security posture assessment
- Verification of full disk encryption, UAC, and host firewall states
- Identification of risky local security policy exceptions
- Outputs automated remediation scripts to restore compliant configurations

---

## 🏗️ System Data Flow & Architecture

```
+-----------------------------------+
|  Target Input / Configuration    |
|  (JSON Snapshots / Policies)      |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|  1. Schema Normalization Engine   |
|  Validates types & formats        |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|  2. Core Analytical Pipeline      |
|  Heuristic rule evaluation,       |
|  invariant checks & drift diffs   |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|  3. Risk Classification           |
|  Assigns severity: INFO / HIGH    |
+-----------------+-----------------+
                  |
                  v
+-----------------------------------+
|  4. Structured Findings & Report  |
|  Root cause, evidence &           |
|  actionable remediation steps     |
+-----------------------------------+
```

---

## 📄 Findings Output Structure

The engine generates structured, machine-parsable JSON reports adhering to this standard audit schema:

```json
{
  "results": [
    {
      "resource": "resource-identifier",
      "severity": "HIGH",
      "check": "CHECK_IDENTIFIER",
      "detail": "Descriptive analysis of the identified security posture issue.",
      "remediation": "Actionable step-by-step guidance to restore compliant state.",
      "evidence": {
        "observed_field": "value",
        "required_policy": "enforced_policy"
      }
    }
  ],
  "count": 1,
  "scope": "Comprehensive defensive security audit"
}
```

---

## 🔒 Source Code & Enterprise Inquiries

To protect proprietary intellectual property and client operational security:
* **Public Repository**: Contains comprehensive architecture specifications, schemas, and design overviews.
* **Private Repository**: Contains the complete production implementation, continuous integration pipelines, and full regression test suites.

For architectural questions or enterprise inquiries, connect via [LinkedIn](https://www.linkedin.com/in/karthikeyansubramaniam04/) or visit the [Portfolio Site](https://karthikeyansubramaniyam.github.io).
