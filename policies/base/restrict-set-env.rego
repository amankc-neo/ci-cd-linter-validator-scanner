package ci_cdpipeline

deny[msg] {
  some job
  some step
  input.jobs[job].steps[_] = step
  step.run
  contains(step.run, "set-env") or contains(step.run, "add-path")
  msg := sprintf("Unsafe usage of deprecated command '%s' in step '%s'. Use environment files instead.", [step.run, job])
}
