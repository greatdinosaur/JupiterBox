<?php
$servername = "mysql.rdsm7htgcrx38if.rds.bj.baidubce.com";
$username = "hackathon2019";
$password = "hackathon2019";
$dbname = "hackathon2019";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$field1 = mysqli_real_escape_string($conn, $_POST['thename']);
$field2 = mysqli_real_escape_string($conn, $_POST['theContent']);
$field3 = mysqli_real_escape_string($conn, $_POST['theTime']);
$field4 = mysqli_real_escape_string($conn, $_POST['theLaw']);
$field5 = mysqli_real_escape_string($conn, $_POST['theHash']);
$field6 = mysqli_real_escape_string($conn, $_POST['theURL']);

$sql = "INSERT INTO backward-camera (`backward-camera`.thename, `backward-camera`.theContent, `backward-camera`.theTime, `backward-camera`.theLaw, `backward-camera`.theHash, `backward-camera`.theURL)
            VALUES ('{$field1}','{$field2}','{$field3}','{$field4}','{$field5}','{$field6}')";
 
if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}
$conn->close();
?>