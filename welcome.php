<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Untitled Document</title>
</head>

<body>
<?php
session_start();
$time = $_SERVER['REQUEST_TIME'];
$timeout_duration = 10;
if (isset($_SESSION['LAST_ACTIVITY']) && 
   ($time - $_SESSION['LAST_ACTIVITY']) > $timeout_duration) {
    session_unset();
    session_destroy();
	session_start();
	header("Location:login.php");
	exit();
}
else if($_SESSION['LAST_ACTIVITY'])
{
	echo '<h1>WELCOME TO MY WEB PAGE</h1>';
}
else
{
	header("Location:login.php");
}
?>
</body>
</html>