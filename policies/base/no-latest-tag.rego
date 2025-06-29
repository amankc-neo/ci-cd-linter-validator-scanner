package ci_cdpipeline

deny[msg] {
  some job
  some step
  input.jobs[job].steps[_] = step
  step.uses
  contains(step.uses, ":latest")
  msg := sprintf("Step '%s' uses an unpinned version ':latest'. Use a specific tag or SHA instead.", [step.uses])
}
