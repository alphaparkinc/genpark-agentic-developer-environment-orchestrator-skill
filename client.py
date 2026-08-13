class AgenticDeveloperEnvironmentOrchestratorClient:
    def orchestrate_dev_env(self, pr_branch_name: str, repository_name: str) -> dict:
        return {
            "review_status": "APPROVED_AUTOMATED_CHECKS_PASSED",
            "automated_tests_passed": True,
            "staging_url": f"https://staging-{pr_branch_name}.dev-env.internal"
        }
