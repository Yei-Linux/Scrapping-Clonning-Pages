<?php
	

	$correo=$_POST['email'];
	$password=$_POST['pass'];


	$data['info']=array();

	$data['info'][]=array(

			'correo'=>$correo,
			'pass'=>$password

	); 

	$jdata=json_encode($data);
	
	$f=fopen('data.txt','w+');
	fwrite($f,$jdata);
	fclose($f);

	echo ($jdata);

?>