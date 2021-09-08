<!DOCTYPE html> 
<html>
<head>
	<title>Welcome to online DVD Shop</title>
</head>
<body>
<h1 >Welcome to DVD Shop!</h1>

<?php
    
    $PC = "Pirates of the Caribbean - Dead Man's Chest";
    $SR = "Superman Returns";
    $C = "Cars";
    $IT = "An Inconvenient Truth";
    $IA = "Ice Age - The Meltdown";

    

	if(isset($_POST['formSubmit'])) 
    {
		$amovie = $_POST['form_movie'];
		
		if(empty($amovie)) 
        {
			echo("<p>You didn't select any movie's DVD.</p>\n");
		} 
        else 
        {
            $N = count($amovie);

            function_alert("You selected $N movie(s)"); 
			for($i=0; $i < $N; $i++)
			{
                echo($amovie[$i] . " ");
                
			}
			
		}

        if(IsChecked('form_movie','A'))
        {
            //echo ' Pirates of the Caribbean - Dead Mans Chest is selected';
            $price1  = 500;
        }else 
        {
            $S_movie1 = NULL;
            $price1 = NULL;
        }
        if(IsChecked('form_movie','B'))
        {
            //echo ' Superman Returns is selected.';
            $price2 = 500;
        }else 
        {
            $S_movie2 = NULL;
            $price2 = NULL;
        }
        if(IsChecked('form_movie','C'))
        {
            //echo ' Cars is selected. ';
            $price3  = 500;
        }else 
        {
            $S_movie3 = NULL;
            $price3 = NULL;
        }
        if(IsChecked('form_movie','D'))
        {
            //echo ' An Inconvenient Truth is selected. ';
            $price4  = 500;
        
        }else 
        {
            $S_movie4 = NULL;
            $price4 = NULL;
        }
        if(IsChecked('form_movie','E'))
        {
            //echo ' Ice Age - The Meltdown  is selected. ';
            $price5  = 500;
        }else 
        {
            $S_movie5 = NULL;
            $price5 = NULL;
        }

        
    }
    
    
    function IsChecked($chkname,$value)
    {
        if(!empty($_POST[$chkname]))
        {
            foreach($_POST[$chkname] as $chkval)
            {
                if($chkval == $value)
                {
                    return true;
                }
            }
        }
        return false;
    }
   
    
?>
<?php 
    function function_alert($message) 
    {  
    echo "<script>alert('$message');</script>"; 
    }
?> 

<form action="<?php echo htmlentities($_SERVER['PHP_SELF']); ?>" method="post">
	<p>
		Select the movies that you want to buy?<br/>
		<input type="checkbox" name="form_movie[]" value="A" />A. Pirates of the Caribbean - Dead Man's Chest<br />
		<input type="checkbox" name="form_movie[]" value="B" />B. Superman Returns<br />
		<input type="checkbox" name="form_movie[]" value="C" />C. Cars<br />
		<input type="checkbox" name="form_movie[]" value="D" />D. An Inconvenient Truth <br />
		<input type="checkbox" name="form_movie[]" value="E" />E. Ice Age - The Meltdown 
	</p>
	<input type="submit" name="formSubmit" value="Submit" />
</form>
<p><b>Your cart Summary</b></p>
<?php

if(!empty($_POST['form_movie'])){
    
echo "<table border='1'>

<tr>

<th>Item number</th>

<th>Movie name</th>

<th>Price</th>

</tr>";

$movies = [
    "A" => ["Pirates of the Caribbean - Dead Man's Chest",500],
    "B" => ["Superman Returns",600],
    "C" => ["Cars",700],
    "D" => ["An Inconvenient Truth",1200],
    "E" => ["Ice Age",612]
];

$movies_3D = [
    "1D" => ["A" => ["Pirates of the Caribbean - Dead Man's Chest",500],
    "B" => ["Superman Returns",600],
    "C" => ["Cars",700],
    "D" => ["An Inconvenient Truth",1200],
    "E" => ["Ice Age",612] ]
];

$sum_movie_bought = 0;
if(!empty($_POST['form_movie'])){
    foreach($_POST['form_movie'] as $key=>$movie_name){
        echo "<tr><td style='text-align:center'>"  . ($key+1) . "</td><td style='text-align:center'>" . $movies[$movie_name][0]  . "</td><td style='text-align:center' >".$movies[$movie_name][1]."</td></tr>";
        $sum_movie_bought  += $movies[$movie_name][1];
    }
}
    
 
echo "</table>";
// $T_price = $price1 + $price2 + $price3 + $price4 + $price5;
echo "Your order total: ". $sum_movie_bought     ." baht";
// ECHO "<BR />".$movies_3D["1D"]["A"][0];
}else{
    ECHO "YOU HAVE NOT YET SELECTED ANY MOVIE(S)";  
}

?>

</body>
</html>