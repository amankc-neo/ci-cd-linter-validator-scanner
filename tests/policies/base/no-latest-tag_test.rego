package ci_cdpipeline

test_latest_tag_violation {
  input := {
    "jobs": {
      "build": {
        "steps": [
          {"uses": "actions/setup-node@latest"}
        ]
      }
    }
  }

  result := deny[_]
  result == "Step 'actions/setup-node@latest' uses an unpinned version ':latest'. Use a specific tag or SHA instead."
}
