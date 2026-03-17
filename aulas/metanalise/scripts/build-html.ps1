# build-html.ps1 — Concatena slides/ em index.html
# Le a ordem de _manifest.js (source of truth).
# Run: powershell -ExecutionPolicy Bypass -File aulas/metanalise/scripts/build-html.ps1
$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$slidesDir = Join-Path $root "slides"
$template = Join-Path $root "index.template.html"
$output = Join-Path $root "index.html"
$manifestPath = Join-Path $slidesDir "_manifest.js"

if (-not (Test-Path $manifestPath)) {
  Write-Error "Manifest not found: $manifestPath"
  exit 1
}

$manifestContent = Get-Content $manifestPath -Raw -Encoding UTF8
$files = [regex]::Matches($manifestContent, "file:\s*'([^']+)'") | ForEach-Object { $_.Groups[1].Value }

if ($files.Count -eq 0) {
  Write-Error "No slide files found in manifest"
  exit 1
}

foreach ($f in $files) {
  $p = Join-Path $slidesDir $f
  if (-not (Test-Path $p)) {
    Write-Error "Missing slide file: $f"
    exit 1
  }
}

$slides = ($files | ForEach-Object {
  Get-Content (Join-Path $slidesDir $_) -Raw -Encoding UTF8
}) -join "`n"

$html = (Get-Content $template -Raw -Encoding UTF8) -replace '%%SLIDES%%', $slides
Set-Content -Path $output -Value $html -NoNewline -Encoding UTF8
Write-Host "Built index.html ($($files.Count) slides from _manifest.js)"
