<?php
$ip = $_SERVER['REMOTE_ADDR'];
include("SxGeo.php");
$SxGeo = new SxGeo('SxGeo/SxGeoCity.dat');
$city = $SxGeo->getCity($ip); // повертає з короткою інформацією, без назви регіону і часового поясу
$countryid = $SxGeo->getCountryId($ip); //повертає номер країни
$country = $SxGeo->getCountry($ip); // повертає двозначний ISO-код країни
$region = $SxGeo->getCityFull($ip); // повертає Область

// Відображені дані початок
echo "<b>Ваша країна:</b> ";
echo ($region['country']['name_ru']); // Країна
echo "<br>";
echo "<b>Ваш регион:</b> ";
echo ($region['region']['name_ru']); // Область
echo "<br>";
echo "<b>Ви зараз перебуваєте в";
echo " ";
echo "м.</b>";
echo " ";
echo ($city['city']['name_ru']); // Місто
echo "<br>";
echo "<b>Ваша IP Адреса:</b> ";
echo $_SERVER['REMOTE_ADDR']; // IP адреса
echo "<br>";
echo "<b>Код вашої країни:</b> ";
echo ($country); // Код країни
echo "<br>";
echo "<b>Номер вашої країни:</b> ";
echo ($countryid); // Номер країни
echo "<br>";
// Відображені дані кінець
?>
