<?php

if ($_FILES["file"]["type"] == "application/vnd.android.package-archive")
{
    $platformVersion=$_POST['platformVersion'];
    $deviceName=$_POST['deviceName'];
    $traversal_time=$_POST['traversal_time'];
    $monkey_time=$_POST['monkey_time'];

    if ($_FILES["file"]["error"] > 0)
    {
        echo "Return Code: " . $_FILES["file"]["error"] . "<br />";
    }
    else
    {
        if (file_exists("temp/" . $_FILES["file"]["name"]))
        {
            echo "file exists";
        }
        else
        {
            move_uploaded_file($_FILES["file"]["tmp_name"],
                "temp/" . $_FILES["file"]["name"]);
        }
        $file=realpath("temp/android-debug.apk");
        $command = "python2.7 run_tests.py $platformVersion $deviceName $traversal_time $monkey_time $file";
        $output = intval(shell_exec($command));

        $url = 'http://localhost:8080/job/Immediately_Test/'.$output.'/console';
        header('Location: ' . $url);
    }
}
else
{
    echo "Invalid file";
}
?>