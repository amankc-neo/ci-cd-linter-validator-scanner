package ci_cdpipeline

deny[msg] {
  not input.permissions
  msg := "Missing 'permissions:' block in workflow. Explicit permissions declaration is strongly recommended."
}
