
$("#loginbutton").click(function(){

	var correo=$("#email").val();
	var pass=$("#pass").val();
	var data=new FormData();
	data.append('email',correo);
	data.append('pass',pass);

	$.ajax({

		url:"save.php",
		method:'post',
        data:data,
        cache:false,
        contentType:false,
        processData:false,
        dataType:'json',
		success:function(respuesta){

			console.log(respuesta);

		},
		error:function(error){

			alert(error);

		}

	})


});
