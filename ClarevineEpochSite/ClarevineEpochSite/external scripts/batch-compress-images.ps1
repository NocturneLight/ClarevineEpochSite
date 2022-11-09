# Uses imagemagick to programatically create thumbnails for a folder of images.

$path = Read-Host -Prompt "Insert path of files you want to make thumbnails for (For example: D:\My Game Assets\Aqua Project Assets\Game\Art\Finished\CG)"

Start-Sleep -Seconds 1
Write-Host "`n$path" -NoNewLine -ForegroundColor Red; Write-Host " is the path you provided.";

$folderName = Read-Host -Prompt "`nInsert path, including a folder name, for the folder you want thumbnails to be created in (For example: C:\Users\Requi\source\repos\ClarevineEpochSite\ClarevineEpochSite\ClarevineEpochSite\static\images\cg\thumbnails\)"

Start-Sleep -Seconds 1
Write-Host "`n$folderName" -NoNewLine -ForegroundColor Red; Write-Host " is where your thumbnails will be created."

Start-Sleep -Seconds 1
"`nCreating a folder for the thumbnails to be created."
if (!(Test-Path $folderName -PathType Container))
{
	New-Item -Path $folderName -ItemType Directory
}

Start-Sleep -Seconds 1
"`nGenerating thumbnails."
Get-ChildItem $path | foreach {
	$fullname = $_.FullName
	$partialname = $_.BaseName

	magick convert $fullname -thumbnail 150x150 -strip -quality 85 -colors 50 "$folderName\$partialname.webp"
}

"`nThumbnails created!"

Read-Host -Prompt "`nPress enter to exit."