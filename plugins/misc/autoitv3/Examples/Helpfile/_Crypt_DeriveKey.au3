#include <Crypt.au3>
#include <MsgBoxConstants.au3>

Example()

Func Example()
	Local $aStringsToEncrypt[6] = ["AutoIt", "SciTE", "Crypt", ".au3", 42, "42"]
	Local $sOutput = ""

	Local $hKey = _Crypt_DeriveKey("CryptPassword", $CALG_RC4) ; Declare a password string and algorithm to create a cryptographic key.

	For $vText In $aStringsToEncrypt
		$sOutput &= $vText & @TAB & " = " & _Crypt_EncryptData($vText, $hKey, $CALG_USERKEY) & @CRLF ; Encrypt the text with the cryptographic key.
	Next

	MsgBox($MB_SYSTEMMODAL, "Encrypted data", $sOutput)

	_Crypt_DestroyKey($hKey) ; Destroy the cryptographic key.
EndFunc   ;==>Example
