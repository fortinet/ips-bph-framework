<?php

# Folder configuration for session files
define('BPH_SESSION_FOLDER', '/home/bph/bph-framework/session/');

$debug = false;
$md5 = $_POST['md5'];
$project_name = $_POST['project_name'];
$sid = $_POST['sid'];
$rid = $_POST['rid'];
$tool_name = $_POST['tool']; 
$dir = $_POST['dir'];

// File related variables
$file = $_FILES['file'];
$file_name = $_FILES['file']['name'];
$file_size = $_FILES['file']['size'];
$file_tmp = $_FILES['file']['tmp_name'];
$file_type = $_FILES['file']['type'];
$file_ext = strtolower(end(explode('.',$file_name)));
    
if ( $debug == true )
{
    echo "\nFile_name: " . $file_name . "\n";
    echo "File_size: " . $file_size . "\n"; 
    echo "File_tmp: " . $file_tmp . "\n";
    echo "File_type: " . $file_type . "\n";
    echo "File_ext: " . $file_ext . "\n";
    echo "Directory: " . $dir . "\n";
}

// /home/bph/<bph_folder>/session/<md5>/<sid>
$base_dir = BPH_SESSION_FOLDER . $project_name . "/" . $md5 . "/" . $sid;

// /home/bph/<bph_folder>/session/<md5>/<sid>/<tool>/<rid>
$report_dir = BPH_SESSION_FOLDER . $project_name . "/" . $md5 . "/" . $sid . "/" . $tool_name . "/" . $rid;

echo $base_dir . "\n\n";
echo $report_dir . "\n";

// Verify if base directory exists
if ( is_dir($base_dir) == 1 )
{
    // Create report directories if not exist.
    if( !is_dir($report_dir) )
    {
        if ($debug) { echo $new_dir . "\n"; }
        mkdir($report_dir, 0755, true);
    }

    // file and dir are required parameters for this script. If those do not exist, then exit.
    if( isset($file) && isset($dir))        
    {   
        if ( $file_ext == "log" && $file_name == $tool_name . "." . $file_ext)
        {
            echo "\nProcessing log file: " . $file_name . "\n";            
            move_file($file_tmp, $report_dir . "/" . $file_name);
            
        } else {
            echo "\nProcessing Non-log file: " . $file_name . "\n";
            
            $new_dir = $report_dir . $dir;
            if ($debug) { echo "New dir:" . $new_dir . "\n"; }

            if ($debug) { echo "Creating new directories now..." . $new_dir; }
            
            mkdir($new_dir, 0755, true);
            $new_file = $new_dir . "/" . $file_name;
            if ($debug) { echo $new_file; }
            move_file($file_tmp, $new_file);
            
            // Decompress ZIP file into the new directory.
            extract_zip($new_file, $new_dir);
            // Deletes the old zip file.
            unlink($new_file);
        }
    } 
} else {
    echo "BASE TOOL FOLDER DOES NOT EXIST";
}

function extract_zip($zip_file_abs_path, $dest_folder)
{           
    $zip = new ZipArchive;
    if ($zip->open($zip_file_abs_path) === TRUE) {
        $zip->extractTo($dest_folder);
        $zip->close();
        echo 'zip decompress ok';
    } else {
        echo 'zip decompress failed';
    }
}

function move_file($source_file, $target_file)
{
    if( move_uploaded_file($source_file, $target_file) )
    {
        $status = "OK";
    } else {
        $status = "FAILED";
    }
    echo $status . ": " . $source_file . "=>" . $target_file . "\n";
}
?>
