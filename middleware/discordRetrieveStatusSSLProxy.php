<?php
//This is a small utility to help you not break your SSL, and keep CORS off on a website that you implement this on.
$id = $_GET["discordId"];

$sanitizedID = filter_var($id, FILTER_SANITIZE_STRING);

$response = file_get_contents('http://{HOST IP}:{HOST PORT}/retrieveStatus?discordId='.$sanitizedID);
echo $response;
?>