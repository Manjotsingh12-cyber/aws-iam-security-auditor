# 🔐 AWS IAM Security Auditor

Automated AWS security scanner that detects IAM and S3 misconfigurations, scores risk levels, and sends real-time alerts via SNS — with a Flask dashboard to visualize results.

## 📺 Video Tutorial

[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch%20Tutorial-red?style=for-the-badge&logo=youtube)](https://youtu.be/Eib_sykgyrs?si=vfmv5xNb3mMYO8Iv)

---

## 🏗️ Architecture

```
EventBridge Scheduler (every 5 min)
        ↓
AWS Lambda — scans IAM + S3
        ↓
Risk Scoring Engine (HIGH / MEDIUM / LOW)
        ↓
Amazon S3 — stores scan-results.json
        ↓
    ↙           ↘
SNS Alert     Flask Dashboard
(email)       localhost:5000
```

---

## ✅ What It Checks

**IAM Users:**
| Check | Risk Score |
|---|---|
| No MFA enabled | +30 |
| Access key older than 90 days | +20 |
| Admin policy attached | +40 |

**S3 Buckets:**
| Check | Risk Score |
|---|---|
| Public ACL (AllUsers) | +50 |
| Public access block disabled | +20 |
| Bucket policy allows `*` | +40 |

**Risk Levels:**
- 🔴 HIGH → score ≥ 50
- 🟡 MEDIUM → score ≥ 20
- 🟢 LOW → score < 20

---

## 📁 Project Structure

```
aws-iam-security-auditor/
├── lambda/
│   └── iam_scanner.py        # Lambda function (IAM + S3 scanner)
├── dashboard/
│   ├── app.py                # Flask app
│   └── templates/
│       └── index.html        # Dashboard UI
├── infra/
│   └── lambda_policy.json    # IAM policy for Lambda
└── README.md
```

---

## 🚀 Setup Guide

### 1. Lambda Function

- Runtime: **Python 3.12**
- Timeout: **1 minute**
- Memory: **256 MB**
- Upload code from `lambda/iam_scanner.py`

### 2. IAM Policy

- Go to IAM → Policies → Create policy
- Paste contents of `infra/lambda_policy.json`
- Name it `iam-auditor-lambda-policy`
- Attach to your Lambda execution role

### 3. S3 Bucket

- Create a bucket: `bucket-for-result-of-iam-checker`
- Region: `ap-south-1`
- Keep all public access blocked

### 4. SNS Topic

- Create topic: `iam-auditor-alerts` (Standard)
- Add email subscription and confirm it
- ARN: `arn:aws:sns:ap-south-1:YOUR_ACCOUNT_ID:iam-auditor-alerts`

### 5. EventBridge Scheduler

- Schedule: `rate(5 minutes)`
- Target: your Lambda function

### 6. Flask Dashboard (local)

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install flask boto3

# Configure AWS credentials
aws configure

# Run dashboard
python dashboard/app.py
```

Open browser → `http://localhost:5000`

---

## 🔧 Tech Stack

- AWS Lambda (Python 3.12)
- Amazon EventBridge Scheduler
- Amazon S3
- Amazon SNS
- Flask

---

## 📄 License

MIT
