package ci_cdpipeline

deny[msg] {
  some job
  some step
  input.jobs[job].steps[_] = step
  step.uses
  startswith(step.uses, "actions/")
  not contains(step.uses, "@")
  msg := sprintf("Step '%s' in job '%s' does not pin an action version (e.g., '@v3' or SHA).", [step.uses, job])
}
