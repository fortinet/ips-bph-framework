#include <GDIPlus.au3>
#include <GUIConstantsEx.au3>
#include <MsgBoxConstants.au3>

_Example()

Func _Example()
    If Not _GDIPlus_Startup() Or @extended < 6 Then
		MsgBox($MB_SYSTEMMODAL, "ERROR", "GDIPlus.dll v1.1 not available")
		Return
	EndIf

	Local $sFile = FileOpenDialog("Select an image", "", "Images (*.bmp;*.png;*.jpg;*.gif;*.tif)")
	If @error Or Not FileExists($sFile) Then Return

	Local $hImage = _GDIPlus_ImageLoadFromFile($sFile)

	Local $iWidth = 600
	Local $iHeight = _GDIPlus_ImageGetHeight($hImage) * 600 / _GDIPlus_ImageGetWidth($hImage)

	Local $hGui = GUICreate("GDI+ v1.1 (" & @ScriptName & ")", $iWidth, $iHeight)
	Local $hGraphics = _GDIPlus_GraphicsCreateFromHWND($hGui)
	GUISetState(@SW_SHOW)

	Local $aColorLUT[256][4]
	For $i = 0 To 255
		$aColorLUT[$i][0] = $i
		$aColorLUT[$i][1] = 0
		$aColorLUT[$i][2] = 0
		$aColorLUT[$i][3] = $i
	Next

	Local $hEffect = _GDIPlus_EffectCreateColorLUT($aColorLUT)
	_GDIPlus_BitmapApplyEffect($hImage, $hEffect)

	_GDIPlus_GraphicsDrawImageRect($hGraphics, $hImage, 0, 0, $iWidth, $iHeight)

	Do
	Until GUIGetMsg() = $GUI_EVENT_CLOSE

	_GDIPlus_EffectDispose($hEffect)
	_GDIPlus_ImageDispose($hImage)
	_GDIPlus_GraphicsDispose($hGraphics)
	_GDIPlus_Shutdown()
EndFunc   ;==>_Example
