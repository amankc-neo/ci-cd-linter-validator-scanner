package ci_cdpipeline

deny[msg] {
  some job
  some step
  input.jobs[job].steps[_] = step
  step.env[var]
  contains(lower(var), "secret")
  not startswith(step.env[var], "${{ secrets.")
  msg := sprintf("Possible hardcoded secret in environment variable '%s' in job '%s'. Use GitHub Secrets.", [var, job])
}
