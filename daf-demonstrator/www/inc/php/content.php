<?php
header("content-type:application/json");

require 'vendor/autoload.php';

$which = $_GET['which'];
$client = new MongoDB\Client("mongodb://mongodb:27017");

try{
  $collection = $client->couch_content->{$which};

  if(isset($_GET['action'])){
    if($_GET['action']=="save"){
      $result = Array();
      $content = json_decode(file_get_contents("php://input"));
      foreach($content as $c){

        if(isset($c->{'_id'})){
          $id = $c->{'_id'}->{'$oid'};
          $id = new \MongoDB\BSON\ObjectID($id);
          unset($c->{'_id'});

          $collection->replaceOne(['_id' => $id], $c);
        }else{
          $result = $collection->insertOne($c);
          $result = array("_id" => $result->getInsertedId());
        }

      }
      echo json_encode($result,JSON_PRETTY_PRINT);
    }
  }else{
    $result = $collection->find()->toArray();

    $toReturn = Array();

    foreach($result as $r){
      //unset($r["_id"]);
      $toReturn[] = $r;
    }

    echo json_encode($toReturn,JSON_PRETTY_PRINT);

/*
    $toReturn = Array("id" => $result[0]["id"]);
    unset($result[0]["_id"]);
    unset($result[0]["id"]);
    $toReturn["content"] = $result[0];

    echo json_encode($toReturn,JSON_PRETTY_PRINT);*/
  }
}catch(Exception $e){
  echo json_encode(Array("error"=>"collection not found"));
}

?>
