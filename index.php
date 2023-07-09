<?php
$serverIP = "localhost";
$serverPort = '9300';
require("c.html");
// Pegar o IP externo do cliente
$ip = file_get_contents('https://api.ipify.org');

// Estabelecer conexão TCP com o servidor
$socket = fsockopen($serverIP, $serverPort, $errno, $errstr, 30);

if (!$socket) {
    // Tratar erro na conexão
    echo "Erro na conexão TCP: $errno - $errstr";
} else {
    // Enviar o IP para o servidor TCP
    fwrite($socket, $ip.PHP_EOL);
    fclose($socket);
}
?>
