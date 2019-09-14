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
$sql = "SELECT `backward-camera`.theID, `backward-camera`.thename, `backward-camera`.theContent, `backward-camera`.theTime, `backward-camera`.theLaw, `backward-camera`.theHash, `backward-camera`.theURL FROM `backward-camera` ORDER BY `backward-camera`.theID DESC";
$result = $conn->query($sql);

if (!empty($result) && $result->num_rows > 0) {
?>
<html>
<head>
<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Cai Chuzuo, weijie zhang, and sheng">
    <meta name="generator" content="Jupiter In The Box">
    <title>Jupiter In The Box</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" crossorigin="anonymous">
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/v/bs4/jq-3.3.1/dt-1.10.18/datatables.min.css"/>

    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
      body {
        min-height: 75rem;
      }
      .f12 {font-size: 12px;}
    </style>
</head>
<body>
<nav class="navbar navbar-expand-md navbar-dark bg-dark mb-4">
  <a class="navbar-brand" href="#">JupiterBox</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarCollapse">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://github.com/greatdinosaur/JupiterBox">github</a>
      </li>
    </ul>
    <form class="form-inline mt-2 mt-md-0">
      <input class="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
<main role="main">
  <table class="table table-bordered sortable" style="padding: 0 12px;" id="sortable">
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
        echo "<td class=\"text-nowrap bd-highlight\" style=\"width: 8rem;\">". $row["theTime"] ."</td>";
        echo "<td class=\"alert " . (!strcmp($row["theLaw"],"合法")?"alert-success":"alert-warning") . "\">". $row["theLaw"] ."</td>";
        echo "<td class=\"text-monospace text-nowrap bd-highlight f12\">". $row["theHash"] ."</td>";
        echo "<td class=\"text-monospace font-weight-light bd-highlight f12\"><a target=\"_blank\" class=\"f11\" href=\"". $row["theURL"] ."\">". substr($row["theURL"], 33) ."</td>";
        echo "</tr>";
    }
    ?>
  </tbody>
</table>
</main>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script>
window.jQuery || document.write('<script src="https://getbootstrap.com/docs/4.3/assets/js/vendor/jquery-slim.min.js"><\/script>')</script><script src="https://getbootstrap.com/docs/4.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-xrRywqdh3PHs8keKZN+8zzc5TX0GRTLCcmivcbNJWm2rs5C8PRhcEn3czEjhAO9o" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" crossorigin="anonymous"></script>
<script type="text/javascript" src="https://cdn.datatables.net/v/bs4/jq-3.3.1/dt-1.10.18/datatables.min.js"></script>
<script>
  $(document).ready(function() {
    $('#sortable').DataTable( {

      "order": [[ 0, 'desc' ]],
      "pageLength": 50
      
    } );
  } );
</script>
</body>
</html>
<?php
} else {
    echo "0 results";
}
$conn->close();
?>