# Activate.ps1 <venv_suffix>
$command = '.\.venv' + $args[0] + '\Scripts\Activate.ps1'
Invoke-Expression $command 