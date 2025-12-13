# PowerShell — Beginner Path (Free)

## Install PowerShell 7
- MSI (x64): https://github.com/PowerShell/PowerShell/releases/latest
- After install, open PowerShell 7 and check:
```powershell
$PSVersionTable.PSVersion
```

## Learn Path (free)
- Microsoft Learn — Get started with Windows PowerShell  https://learn.microsoft.com/training/paths/get-started-windows-powershell/
- Introduction to PowerShell  https://learn.microsoft.com/training/modules/introduction-to-powershell/
- Write your first PowerShell code  https://learn.microsoft.com/training/modules/powershell-write-first/
- PowerShell 101 (PS 7.5 docs “book”)  https://learn.microsoft.com/powershell/scripting/learn/ps101/00-introduction?view=powershell-7.5
- John Savill — Master Class playlist  https://www.youtube.com/playlist?list=PLlVtbbG169nFq_hR7FcMYg32xsSAObuq8
- PowerShell for Beginners — Full course  https://www.youtube.com/watch?v=UVUd9_k9C6A

## Daily Basics
```powershell
Get-Help Get-Process -Online
Get-Command *service*
Get-Module
Get-ExecutionPolicy -List
```

## Safe execution (session only)
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned -Force
```

## Update help (once)
```powershell
Update-Help -UICulture en-US -ErrorAction SilentlyContinue
```
<!-- updated: 2025-09-30T22:13:34 -->
