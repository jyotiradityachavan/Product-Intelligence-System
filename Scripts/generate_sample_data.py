import json
from pathlib import Path
import pandas as pd


BASE_DIR = Path("data/raw")


def write_text(filename: str, content: str):
    path = BASE_DIR / filename
    path.write_text(content.strip(), encoding="utf-8")


def main():
    BASE_DIR.mkdir(parents=True, exist_ok=True)

    tickets = [
        {
            "ticket_id": "TCK-1001",
            "customer": "Acme Finance",
            "plan": "Enterprise",
            "category": "Performance",
            "severity": "High",
            "text": "Dashboard load time has increased from 3 seconds to 18 seconds after the March release. The customer says executives use this dashboard daily.",
        },
        {
            "ticket_id": "TCK-1002",
            "customer": "Northstar Retail",
            "plan": "Business",
            "category": "Integration",
            "severity": "Medium",
            "text": "Slack notifications fail intermittently when more than 20 alerts are triggered in one hour.",
        },
        {
            "ticket_id": "TCK-1003",
            "customer": "ZenHealth",
            "plan": "Enterprise",
            "category": "Security",
            "severity": "Critical",
            "text": "Customer requested SAML SSO audit logs. Their compliance team needs exportable sign-in history for quarterly review.",
        },
        {
            "ticket_id": "TCK-1004",
            "customer": "BrightOps",
            "plan": "Startup",
            "category": "Usability",
            "severity": "Low",
            "text": "Users are confused by the new workflow builder. They want templates and a guided setup checklist.",
        },
        {
            "ticket_id": "TCK-1005",
            "customer": "LogiCore",
            "plan": "Enterprise",
            "category": "Reliability",
            "severity": "High",
            "text": "Webhook delivery failures increased after API v2 migration. Customer reports missing warehouse status updates.",
        },
    ]

    pd.DataFrame(tickets).to_csv(BASE_DIR / "customer_support_tickets.csv", index=False)

    feature_requests = [
        {
            "id": "FR-201",
            "title": "Role-based dashboards",
            "votes": 43,
            "segment": "Enterprise",
            "description": "Admins want different dashboard views for executives, analysts, and support managers.",
        },
        {
            "id": "FR-202",
            "title": "Bulk edit automations",
            "votes": 31,
            "segment": "Business",
            "description": "Operations teams need to update multiple automation rules at once.",
        },
        {
            "id": "FR-203",
            "title": "Native Microsoft Teams integration",
            "votes": 55,
            "segment": "Enterprise",
            "description": "Several customers use Teams instead of Slack and want alert delivery there.",
        },
        {
            "id": "FR-204",
            "title": "Workflow templates",
            "votes": 27,
            "segment": "Startup",
            "description": "New users want prebuilt templates for common customer support workflows.",
        },
    ]

    with open(BASE_DIR / "feature_requests.json", "w", encoding="utf-8") as f:
        json.dump(feature_requests, f, indent=2)

    write_text(
        "meeting_notes_q2.txt",
        """
        Q2 Product Review Meeting Notes

        Main themes:
        - Enterprise customers continue to ask for better compliance capabilities.
        - Performance concerns are growing around executive dashboards.
        - Sales says Microsoft Teams integration is blocking three expansion deals.
        - Support says workflow builder confusion is causing onboarding friction.
        - Engineering warns that webhook reliability needs investment before adding more integrations.

        Decisions:
        - Prioritize dashboard performance investigation.
        - Scope SAML audit log export.
        - Research Microsoft Teams integration demand.
        - Create onboarding templates for common workflows.
        """,
    )

    write_text(
        "prd_audit_logs.txt",
        """
        Product Requirements Document: SAML Audit Log Export

        Problem:
        Enterprise compliance teams need exportable SAML SSO sign-in history.

        Goals:
        - Allow admins to export sign-in events by date range.
        - Include user email, identity provider, timestamp, IP address, and status.
        - Support CSV export in MVP.
        - Retain logs for 180 days for Enterprise plans.

        Non-goals:
        - Real-time anomaly detection.
        - SIEM integrations.

        Success metrics:
        - Reduce compliance-related support tickets by 30%.
        - Improve Enterprise renewal confidence.
        """,
    )

    write_text(
        "github_issues.txt",
        """
        GitHub Issues Summary

        #442 Dashboard query runs full table scan for large accounts.
        Severity: High
        Labels: performance, backend

        #451 Webhook retry queue loses messages after worker restart.
        Severity: Critical
        Labels: reliability, infrastructure

        #466 Slack rate-limit handling is incomplete.
        Severity: Medium
        Labels: integration, alerts

        #470 Workflow builder empty state lacks guidance.
        Severity: Low
        Labels: ux, onboarding

        #482 Missing audit event model for SAML exports.
        Severity: Medium
        Labels: security, compliance
        """,
    )

    write_text(
        "competitor_analysis.txt",
        """
        Competitor Analysis

        Competitor A:
        - Strong Microsoft Teams integration.
        - Offers role-based dashboards.
        - Weakness: expensive implementation services.

        Competitor B:
        - Strong compliance reporting.
        - Has audit log export and SIEM integrations.
        - Weakness: poor workflow automation UX.

        Competitor C:
        - Excellent onboarding templates.
        - Fast dashboard experience for mid-market teams.
        - Weakness: limited enterprise controls.

        Market implication:
        The product is exposed in Enterprise deals where Teams integration,
        audit logs, and role-based dashboards are expected.
        """,
    )

    write_text(
        "sales_feedback.txt",
        """
        Sales Feedback

        Recent lost or delayed deals:
        - Horizon Bank delayed expansion due to missing Microsoft Teams integration.
        - DeltaMed asked for audit log exports before legal approval.
        - ShopVerse requested role-based executive dashboards.
        - Titan Logistics asked about webhook reliability guarantees.

        Sales priority ranking:
        1. Microsoft Teams integration
        2. Audit log export
        3. Role-based dashboards
        4. Webhook reliability
        """,
    )

    write_text(
        "customer_interviews.txt",
        """
        Customer Interview Notes

        Interview 1: Acme Finance
        They rely on the executive dashboard during Monday leadership meetings.
        Slow dashboard performance damages trust in the product.

        Interview 2: ZenHealth
        Compliance reporting is a renewal risk. They need CSV audit log export
        before the next quarterly review.

        Interview 3: BrightOps
        New admins do not know where to start with workflow automation.
        They asked for examples and templates.

        Interview 4: LogiCore
        Webhook failures create operational blind spots in warehouse workflows.
        They care more about reliability than new integrations.
        """,
    )

    write_text(
        "roadmap_draft.txt",
        """
        Roadmap Draft

        Candidate initiatives:
        - Improve dashboard query performance.
        - Build SAML audit log CSV export.
        - Add Microsoft Teams alert integration.
        - Improve webhook retry reliability.
        - Add workflow builder templates.
        - Create role-based dashboard views.

        Constraints:
        - Backend team has limited capacity this quarter.
        - Security review is required for audit log features.
        - Integrations team is already handling Slack reliability work.
        """,
    )

    print(f"Sample data generated in {BASE_DIR}")


if __name__ == "__main__":
    main()
