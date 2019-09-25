#include <WinAPIConv.au3>
Global Const $CP_SHIFT_JIS = 932

Local $sTest
Local $sText = "データのダウンロードに失敗しました。"

$sTest = _WinAPI_WideCharToMultiByte($sText, $CP_SHIFT_JIS, True, False)
MsgBox($MB_SYSTEMMODAL, "Title Sring",$sText & @CRLF & VarGetType($sTest) & " " & StringLen($sTest) & ": '" & $sTest & "'")

$sTest = _WinAPI_WideCharToMultiByte($sText, $CP_SHIFT_JIS, True, True)
MsgBox($MB_SYSTEMMODAL, "Title Binary",$sText & @CRLF & VarGetType($sTest) & " " & StringLen($sTest) & ": '" & $sTest & "'")