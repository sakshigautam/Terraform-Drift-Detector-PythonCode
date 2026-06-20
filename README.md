**Architecture Diagram**


┌──────────────────────────────────────────────┐
│ **GitHub Actions / Jenkins / Cron Scheduler**│
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│ scripts/run_scan.sh                          │
│                                              │
│ python app/main.py                           │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│ app/main.py                                  │
│                                              │
│ Loads config/config.yaml                     │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│ app/terraform_runner.py                      │
│                                              │
│ terraform plan -refresh-only                 │
│ terraform show -json                         │
│                                              │
│ Generates drift.json                         │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│ app/drift_parser.py                          │
│                                              │
│ Reads resource_changes                       │
│ Extracts:                                   │
│  - resource name                            │
│  - action                                   │
│  - before state                             │
│  - after state                              │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
         ┌───────────────────┐
         │ Drift Detected ?  │
         └───────┬───────────┘
                 │
        ┌────────┴────────┐
        │                 │
        ▼                 ▼
     NO DRIFT          DRIFT FOUND
        │                 │
        ▼                 ▼
     EXIT          app/openai_analyzer.py
                         │
                         ▼
┌──────────────────────────────────────────────┐
│ OpenAI GPT-5                                 │
│                                              │
│ Analyze Drift                                │
│ Classify Severity                            │
│ Determine Intent                             │
│ Assess Risk                                  │
│ Generate Terraform Fix Script                │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│ app/remediation_generator.py                 │
│                                              │
│ Creates:                                     │
│ reports/analysis.json                        │
│ reports/remediation.sh                       │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│ Operations Team                              │
│                                              │
│ Reviews AI Recommendation                    │
│ Reviews Generated Script                     │
└──────────────────┬───────────────────────────┘
                   │
                   ▼
┌──────────────────────────────────────────────┐
│ Manual Execution                             │
│                                              │
│ bash reports/remediation.sh                  │
└──────────────────────────────────────────────┘
