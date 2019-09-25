#include <Excel.au3>
#include <MsgBoxConstants.au3>

; Create application object and create a new workbook
Local $oExcel = _Excel_Open()
If @error Then Exit MsgBox($MB_SYSTEMMODAL, "Excel UDF: _Excel_RangeWrite Example", "Error creating the Excel application object." & @CRLF & "@error = " & @error & ", @extended = " & @extended)
Local $oWorkbook = _Excel_BookNew($oExcel)
If @error Then
	MsgBox($MB_SYSTEMMODAL, "Excel UDF: _Excel_RangeWrite Example", "Error creating the new workbook." & @CRLF & "@error = " & @error & ", @extended = " & @extended)
	_Excel_Close($oExcel)
	Exit
EndIf

; Write a 1D array to the active sheet in the active workbook
Local $aArray1D[3] = ["AA", "BB", "CC"]
_Excel_RangeWrite($oWorkbook, $oWorkbook.Activesheet, $aArray1D, "A3")
If @error Then Exit MsgBox($MB_SYSTEMMODAL, "Excel UDF: _Excel_RangeWrite Example 2", "Error writing to worksheet." & @CRLF & "@error = " & @error & ", @extended = " & @extended)
MsgBox($MB_SYSTEMMODAL, "Excel UDF: _Excel_RangeWrite Example 2", "1D array successfully written.")
