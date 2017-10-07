<?php 
return "succ";
$command = escapeshellcmd('/../python/main.py');
$output = shell_exec($command);
return "success"
?>
