from client import AgenticDeveloperEnvironmentOrchestratorClient

def main():
    client = AgenticDeveloperEnvironmentOrchestratorClient()
    res = client.orchestrate_dev_env("feat-agent-flow", "alphaparkinc/genpark-app")
    print(f"Review Status: {res['review_status']}")
    print(f"Staging URL: {res['staging_url']}")

if __name__ == "__main__":
    main()
