<?php

if ($_FILES["file"]["type"] == "application/vnd.android.package-archive")
{
    $platformVersion=$_POST['platformVersion'];
    $deviceName=$_POST['deviceName'];
    $traversal_time=$_POST['traversal_time'];
    $monkey_time=$_POST['monkey_time'];
    $schedule=$_POST['schedule'];

    if ($_FILES["file"]["error"] > 0)
    {
        echo "Return Code: " . $_FILES["file"]["error"] . "<br />";
    }
    else
    {
        move_uploaded_file($_FILES["file"]["tmp_name"],"temp/" . "android-debug.apk");
        $file=realpath("temp/" . "android-debug.apk");

        if (preg_match("/[A-Z0-9\*]+\.[A-Z0-9\*]+\.[A-Z0-9\*]+\.[A-Z0-9\*]+\.[A-Z0-9\*]+/", $schedule))
        {
            $test_type = "Scheduled_Test/";
            $command = "python2.7 run_scheduled_tests.py $platformVersion $deviceName $traversal_time $monkey_time $file $schedule";
        }
        else
        {
            $test_type = "Immediately_Test/";
            $command = "python2.7 run_immediate_tests.py $platformVersion $deviceName $traversal_time $monkey_time $file";
        }
        $output = intval(shell_exec($command));
        $url = 'http://localhost:8080/job/'.$test_type.$output.'/console';
        header('Location: ' . $url);
    }
}
else
{
    echo "Invalid file";
}
?>
