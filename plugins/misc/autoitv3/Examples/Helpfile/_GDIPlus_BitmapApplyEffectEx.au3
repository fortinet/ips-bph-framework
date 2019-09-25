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
	Local $iImgW = _GDIPlus_ImageGetWidth($hImage)
	Local $iImgH = _GDIPlus_ImageGetHeight($hImage)

	Local $iWidth = 600
	Local $iHeight = $iImgH * 600 / $iImgW

	Local $hGui = GUICreate("GDI+ v1.1 (" & @ScriptName & ")", $iWidth, $iHeight)
	Local $hGraphics = _GDIPlus_GraphicsCreateFromHWND($hGui)
	GUISetState(@SW_SHOW)

	Local $hEffect = _GDIPlus_EffectCreateHueSaturationLightness(0, -100, 0)
	_GDIPlus_BitmapApplyEffectEx($hImage, $hEffect, $iImgW * 0.25, $iImgH * 0.25, $iImgW * 0.5, $iImgH * 0.5)

	_GDIPlus_GraphicsDrawImageRect($hGraphics, $hImage, 0, 0, $iWidth, $iHeight)

	Do
	Until GUIGetMsg() = $GUI_EVENT_CLOSE

	_GDIPlus_EffectDispose($hEffect)
	_GDIPlus_ImageDispose($hImage)
	_GDIPlus_GraphicsDispose($hGraphics)
	_GDIPlus_Shutdown()
EndFunc   ;==>_Example
