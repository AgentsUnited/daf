<?php
header("Content-type: application/json");
$json = json_decode(file_get_contents("php://input"));
$args = implode(",",$json->arguments);
$newAttacks = array();

if(empty($json->attacks)){
	$atts = "none";
}else{

	foreach($json->attacks as $att){
		$match = preg_match('/\(([^)]+)\)/',$att,$output);
		if(sizeof($output) > 1){
			//$newAttacks[] = str_replace(",",">",$output[1]);
			$newAttacks[] = $output[0];
		}
	}

	$atts = implode(";",$newAttacks);
}
$semantics = (isset($json->semantics)) ? $json->semantics : "grounded";

ob_start();
	passthru ('java -jar /dungomatic/dungomatic.jar "' . $args . '" "' . $atts . '" "' . $semantics . '"');
	$result = ob_get_contents();
ob_end_clean();

$jsonResult = json_decode($result);
$tempAttacks = array();

// foreach($jsonResult->attacks as $att){
// 	$tempAttacks[] = "(" . str_replace(">",",",$att) . ")";
// }
//
// $jsonResult->attacks = $tempAttacks;

if(($result = json_encode($jsonResult))!="null"){
	echo $result;
}else{
	echo json_encode(array("message" => "error"));
}

?>
