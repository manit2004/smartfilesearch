$directory = "E:\"  # You can change this to any directory you want to scan
$items = Get-ChildItem -Path $directory -Recurse | Select-Object FullName, Name
# Export to a single CSV file to the current working directory
$items | Export-Csv -Path ".\file_list.csv" -NoTypeInformation
