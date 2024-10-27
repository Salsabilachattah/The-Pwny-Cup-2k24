<?php
session_start();
highlight_file(__FILE__);

//pretty sure that this is secure, but wait...
if(isset($_GET["Tradition"])){
    $_SESSION["FLAG"]=$_GET["Tradition"];
    include($_GET["Tradition"]);
}
?>