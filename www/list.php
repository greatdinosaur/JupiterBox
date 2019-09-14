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
$sql = "SELECT `backward-camera`.theID, `backward-camera`.thename, `backward-camera`.theContent, `backward-camera`.theTime, `backward-camera`.theLaw, `backward-camera`.theHash, `backward-camera`.theURL FROM `backward-camera`";
$result = $conn->query($sql);

if (!empty($result) && $result->num_rows > 0) {
?>
<html>
<head>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</head>
<body>
<table class="table">
  <thead class="thead-dark">
    <tr>
      <th scope="col">#</th>
      <th scope="col">thename</th>
      <th scope="col">theContent</th>
      <th scope="col">theTime</th>
      <th scope="col">theLaw</th>
      <th scope="col">theHash</th>
      <th scope="col">theURL</th>
    </tr>
  </thead>
  <tbody>
    <?php
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<tr><th scope=\"row\">" . $row["theID"]. "</th>";
        echo "<td>". $row["thename"] ."</td>";
        echo "<td>". $row["theContent"] ."</td>";
        echo "<td>". $row["theTime"] ."</td>";
        echo "<td>". $row["theLaw"] ."</td>";
        echo "<td>". $row["theHash"] ."</td>";
        echo "<td colspan=\"4\"><a href=\"". $row["theURL"] ."\">". $row["theURL"] ."</td>";
        echo "</tr>";
    }
    ?>
  </tbody>
</table>
</body>
</html>
<?php
} else {
    echo "0 results";
}
$conn->close();
?>