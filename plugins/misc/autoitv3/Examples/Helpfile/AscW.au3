#include <MsgBoxConstants.au3>

Local $iCode = AscW("�")
MsgBox($MB_SYSTEMMODAL, "", "Unicode code for �: U+" & Hex($iCode, 6))
