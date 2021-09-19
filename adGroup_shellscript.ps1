Get-ADGroup SP_Sup_Collagen -Properties Description | New-ADGroup -Name "SP_Sup_Collagen_INV" `
    -SamAccountName "SP_Sup_Collagen_INV" `
    -Description "SharePoint - Supplier Invoice Folder Access" `
    -PassThru
# query the groups you want
$groups = Get-ADGroup -Filter {(Name -like "SP_Sup_*") ` #using back ticks for 'template literals'breaksto next line for easier reading
     -and (Name -Notlike "*Doc" ) `
     -and  (Name -notlike "*RPT") `
     -and (Name -notlike "*INV")}

# write them out to a file (for editing)
$groups.name | out-file C:\Users\dibenedt\Desktop\gnames.txt

# shortcut to open file for editing)
Invoke-Item C:\Users\dibenedt\Desktop\gnames.txt
<#
$groups.name[15]
$x = for($i=16;$i -lt $groups.count; $i++) {$groups.name[$i]}

$y = get-content C:\Users\dibenedt\Desktop\gnames.txt

($groups.name[15]).GetType()
$groups.GetType()
compare-object $y $x
#>

(Get-ADGroup -Filter {name -like "*inv"}).count

Foreach($thing in $y){
    $newname = $thing + "_INV"
    Get-ADGroup $thing -Properties Description | New-ADGroup -Name $newname `
        -SamAccountName $newname `
        -Description "SharePoint - Supplier Invoice Folder Access" `
        -PassThru
}