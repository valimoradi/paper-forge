# Optional: auto-commit watcher for the manuscript

Purpose: when several agents (or humans) edit the paper, a file watcher that
commits `paper.tex` + `paper.pdf` on every change gives fine-grained version
control without relying on anyone remembering to commit.

## PowerShell example (Windows)

```powershell
# auto_commit_paper.ps1 — watch and commit the manuscript on change
$paperDir = "<repo>\paper"
$files = @("paper.tex", "paper.pdf")
$last = @{}
while ($true) {
    Start-Sleep -Seconds 20
    $changed = $false
    foreach ($f in $files) {
        $p = Join-Path $paperDir $f
        if (Test-Path $p) {
            $t = (Get-Item $p).LastWriteTimeUtc
            if (-not $last.ContainsKey($f) -or $last[$f] -ne $t) { $last[$f] = $t; $changed = $true }
        }
    }
    if ($changed) {
        git -C $paperDir add $files
        git -C $paperDir commit -m ("auto-snapshot: paper @ " + (Get-Date -Format "yyyy-MM-dd HH:mm:ss")) --quiet
        git -C $paperDir push --quiet
    }
}
```

Run detached; write the PID to a file so it can be stopped.

## Caveats (learned the hard way)

- The watcher does NOT compile. The editor must recompile before the PDF is
  worth committing; otherwise tex and pdf diverge silently and the user sees
  stale output.
- `git push` needs credentials cached: do one manual push first so the
  credential manager stores them; otherwise the daemon hangs on an auth
  prompt.
- Auto-snapshot commits are noisy by design; squash or keep on a working
  branch, and still make named commits at section boundaries.
