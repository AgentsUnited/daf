<?php
header("content-type:application/json");

require 'vendor/autoload.php';

$which = $_GET['which'];
$client = new MongoDB\Client("mongodb://mongodb:27017");

try{
  $collection = $client->couch_content->{$which};

  if(isset($_GET['action'])){
    if($_GET['action']=="save"){
      $id = $_GET['id'];
      $r = $collection->updateOne(['id' => (int)$id], ['$set' => json_decode($_POST['content'])]);
      echo json_encode($r,JSON_PRETTY_PRINT);
    }
  }else{
    $result = $collection->find()->toArray();
    $toReturn = Array("id" => $result[0]["id"]);
    unset($result[0]["_id"]);
    unset($result[0]["id"]);
    $toReturn["content"] = $result[0];

    echo json_encode($toReturn,JSON_PRETTY_PRINT);
  }
}catch(Exception $e){
  echo json_encode(Array("error"=>"collection not found"));
}

?>
