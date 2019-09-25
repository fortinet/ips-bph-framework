#include <Debug.au3>
#include <MsgBoxConstants.au3>

Example()

Func Example()

	; Create 1D array to display
	Local $aArray_1D[5] = ["Item 0", "Item 1", "A longer Item 2 to show column expansion", "Item 3", "Item 4"]

	_DebugArrayDisplay($aArray_1D, "1D display")

	; Create 2D array to display
	Local $aArray_2D[25][15]
	For $i = 0 To UBound($aArray_2D) - 1
		For $j = 0 To UBound($aArray_2D, 2) - 1
			$aArray_2D[$i][$j] = "Item " & StringFormat("%02i", $i) & StringFormat("%02i", $j)
		Next
	Next

	_DebugArrayDisplay($aArray_2D, "2D display")

	$aArray_2D[5][5] = "A longer item to show column expansion"
	_DebugArrayDisplay($aArray_2D, "Expanded column - custom titles - no buttons or 'Row' column", Default, 32 + 64, Default, "AA|BB|CC|DD|EE|FF|GG|HH|II|JJ")

	; Assign the user function to a variable to pass as a parameter
	Local $hUserFunction = _UserFunc

	$aArray_2D[5][5] = "Column alignment set to right"
	_DebugArrayDisplay($aArray_2D, "Range set - right align - copy column width - user function", "3:7|4:9", 2, 15, "AA|BB|CC|DD|EE|FF", Default, $hUserFunction)
	_DebugArrayDisplay($aArray_2D, "Range set - transposed", "3:7|4:9", 1, Default, "AA|BB|CC|DD|EE|FF") ; Note no col names as transposed

	$aArray_2D[5][5] = "Column alignment set to left"
	Opt("GUIDataSeparatorChar", "!")
	_DebugArrayDisplay($aArray_2D, "! Header separator", "3:7|4:9", Default, Default, "AA!BB!CC!DD!EE!FF")

	; Create non-array variable to force error - MsgBox displayed as $iFlags set
	Local $vVar = 0, $iRet, $iError
	$iRet = _DebugArrayDisplay($vVar, "No MsgBox on Error")
	$iError = @error
	MsgBox(0, "_DebugArrayDisplay() Error", "return without internal Msgbox $iret =" & $iRet & " @error=" & $iError)

	$iRet = _DebugArrayDisplay($vVar, "MsgBox on Error", Default, 8)
	$iError = @error
	MsgBox(0, "_DebugArrayDisplay() Error", "return internal Msgbox with no force Exit $iret =" & $iRet & " @error=" & $iError)

EndFunc    ;==>Example

; Note that the user function MUST have TWO parameters even if you do not intend to use both of them
Func _UserFunc($aArray_2D, $aSelected)

	; But if a parameter is not used do this to prevent an Au3Check warning
	#forceref $aArray_2D

	_DebugArrayDisplay($aSelected, "Selected cols")

EndFunc    ;==>_UserFunc
