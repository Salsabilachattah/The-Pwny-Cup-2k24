<?php

$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';


if ($username === "admin1" || $username === "2admin" ) {
    echo "\nYou are lying, you are not an admin.\n";
    die(); 
}

$hash = hash('sha256', $password);

if ($hash == "0" && (( (int)$username === (int)"admin1" and (int)$username != 0 ) or (int)$username === (int)"2admin" )) {
   
    echo "\nLogged in \n";

    $flagFilePath = "/flag.txt";
    if (file_exists($flagFilePath)) {
        $flag = file_get_contents($flagFilePath);
        echo "Flag: " . htmlspecialchars($flag);
    } else {
        echo "Flag file not found.";
    }
} else {
    echo "\nNooooooooooo Bye Bye\n";
}
?>