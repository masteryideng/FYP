<!DOCTYPE html>
<html lang="en" class="no-js">

<head>
    <meta charset="utf-8">
    <title>Test Result</title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/templatemo-style.css">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:100,200,300,400,500,600,700,800,900" rel="stylesheet">
</head>

<body>

<?php

function status($test)
{
    $productFile = file_get_contents('temp/result.txt');
    $products = str_word_count($productFile, 1);
    $status = $test;

    $found = false;
    foreach ($products as $product)
    {
        if (strpos($status,$product) !== false) {
            $found = true;
            break;
        }
    }
    if ($found) {
        return 'img/pass.png';
    }
    else {
        return 'img/fail.png';
    }
}

$workspace = '/Users/Shared/Jenkins/Home/workspace/Immediately_Test/fyp/';
copy($workspace.'bvt_report.html', 'temp/bvt_report.html');
copy($workspace.'security_test_report.html', 'temp/security_test_report.html');
copy($workspace.'monkey_test_report.html', 'temp/monkey_test_report.html');
copy($workspace.'result.txt', 'temp/result.txt');

$command = "python2.7 last_build.py";
$output = shell_exec($command);
$ui = status('ui');
$traversal = status('traversal');
$stress = status('stress');
$security = status('security');

?>

<div class="overlay"></div>

<section class="cd-hero">

    <div class="cd-slider-nav">
        <nav>
            <span class="cd-marker item-1"></span>
            <ul>
                <li class="selected"><a href="temp/monkey_test_report.html" target="_blank"><div class="image-icon"><img src=<?php echo $stress ?>></div><h6>Stress Test</h6></a></li>
                <li><a href="temp/security_test_report.html" target="_blank"><div class="image-icon"><img src=<?php echo $security ?>></div><h6>Security Test</h6></a></li>
                <li><a href="#0"><div class="image-icon"><img src=<?php echo $ui ?>></div><h6>UI Test</h6></a></li>
                <li><a href="#0"><div class="image-icon"><img src=<?php echo $traversal ?>></div><h6>Traversal Test</h6></a></li>
            </ul>
        </nav>
    </div> <!-- .cd-slider-nav -->

    <div class="heading">
        <h1><a href='temp/bvt_report.html' target="_blank">Test Report</a></h1>
    </div>
    <div class="cd-full-width first-slide">
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <div class="content first-content">
                        <h4>Console Output</h4>
                        <p><?php echo "<pre>".$output."</pre>" ?></p>
                    </div>
                </div>
            </div>
        </div>
    </div>

</section> <!-- .cd-hero -->

</body>
</html>