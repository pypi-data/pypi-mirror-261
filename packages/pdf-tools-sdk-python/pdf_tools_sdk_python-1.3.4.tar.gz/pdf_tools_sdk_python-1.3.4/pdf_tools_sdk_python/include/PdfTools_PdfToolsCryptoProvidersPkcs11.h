/******************************************************************************
 *
 * File:            PdfTools_PdfToolsCryptoProvidersPkcs11.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSCRYPTOPROVIDERSPKCS11_H__
#define PDFTOOLS_PDFTOOLSCRYPTOPROVIDERSPKCS11_H__

#ifndef PDFTOOLS_CALL
#if defined(WIN32)
#define PDFTOOLS_CALL __stdcall
#else
#define PDFTOOLS_CALL
#endif
#endif

#include "PdfTools_Types.h"
#include "PdfTools_PdfToolsSys.h"

#ifdef __cplusplus
extern "C"
{
#endif

#ifdef _UNICODE
#define PdfToolsCryptoProvidersPkcs11_Module_Load PdfToolsCryptoProvidersPkcs11_Module_LoadW

#define PdfToolsCryptoProvidersPkcs11_Device_CreateSession PdfToolsCryptoProvidersPkcs11_Device_CreateSessionW

#define PdfToolsCryptoProvidersPkcs11_Device_GetDescription PdfToolsCryptoProvidersPkcs11_Device_GetDescriptionW

#define PdfToolsCryptoProvidersPkcs11_Device_GetManufacturerID PdfToolsCryptoProvidersPkcs11_Device_GetManufacturerIDW

#define PdfToolsCryptoProvidersPkcs11_Session_Login PdfToolsCryptoProvidersPkcs11_Session_LoginW
#define PdfToolsCryptoProvidersPkcs11_Session_CreateSignatureFromName \
    PdfToolsCryptoProvidersPkcs11_Session_CreateSignatureFromNameW
#define PdfToolsCryptoProvidersPkcs11_Session_CreateSignatureFromKeyLabel \
    PdfToolsCryptoProvidersPkcs11_Session_CreateSignatureFromKeyLabelW

#define PdfToolsCryptoProvidersPkcs11_Session_GetTimestampUrl PdfToolsCryptoProvidersPkcs11_Session_GetTimestampUrlW
#define PdfToolsCryptoProvidersPkcs11_Session_SetTimestampUrl PdfToolsCryptoProvidersPkcs11_Session_SetTimestampUrlW

#else
#define PdfToolsCryptoProvidersPkcs11_Module_Load PdfToolsCryptoProvidersPkcs11_Module_LoadA

#define PdfToolsCryptoProvidersPkcs11_Device_CreateSession PdfToolsCryptoProvidersPkcs11_Device_CreateSessionA

#define PdfToolsCryptoProvidersPkcs11_Device_GetDescription PdfToolsCryptoProvidersPkcs11_Device_GetDescriptionA

#define PdfToolsCryptoProvidersPkcs11_Device_GetManufacturerID PdfToolsCryptoProvidersPkcs11_Device_GetManufacturerIDA

#define PdfToolsCryptoProvidersPkcs11_Session_Login PdfToolsCryptoProvidersPkcs11_Session_LoginA
#define PdfToolsCryptoProvidersPkcs11_Session_CreateSignatureFromName \
    PdfToolsCryptoProvidersPkcs11_Session_CreateSignatureFromNameA
#define PdfToolsCryptoProvidersPkcs11_Session_CreateSignatureFromKeyLabel \
    PdfToolsCryptoProvidersPkcs11_Session_CreateSignatureFromKeyLabelA

#define PdfToolsCryptoProvidersPkcs11_Session_GetTimestampUrl PdfToolsCryptoProvidersPkcs11_Session_GetTimestampUrlA
#define PdfToolsCryptoProvidersPkcs11_Session_SetTimestampUrl PdfToolsCryptoProvidersPkcs11_Session_SetTimestampUrlA

#endif

/******************************************************************************
 * SignatureConfiguration
 *****************************************************************************/
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersPkcs11_SignatureConfiguration_AddCertificate(
    TPdfToolsCryptoProvidersPkcs11_SignatureConfiguration* pSignatureConfiguration,
    const TPdfToolsSys_StreamDescriptor*                   pCertificate);

PDFTOOLS_EXPORT TPdfToolsCrypto_HashAlgorithm PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_SignatureConfiguration_GetHashAlgorithm(
    TPdfToolsCryptoProvidersPkcs11_SignatureConfiguration* pSignatureConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersPkcs11_SignatureConfiguration_SetHashAlgorithm(
    TPdfToolsCryptoProvidersPkcs11_SignatureConfiguration* pSignatureConfiguration,
    TPdfToolsCrypto_HashAlgorithm                          iHashAlgorithm);
PDFTOOLS_EXPORT TPdfToolsCrypto_SignaturePaddingType PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_SignatureConfiguration_GetSignaturePaddingType(
    TPdfToolsCryptoProvidersPkcs11_SignatureConfiguration* pSignatureConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersPkcs11_SignatureConfiguration_SetSignaturePaddingType(
    TPdfToolsCryptoProvidersPkcs11_SignatureConfiguration* pSignatureConfiguration,
    TPdfToolsCrypto_SignaturePaddingType                   iSignaturePaddingType);
PDFTOOLS_EXPORT TPdfToolsCrypto_SignatureFormat PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_SignatureConfiguration_GetSignatureFormat(
    TPdfToolsCryptoProvidersPkcs11_SignatureConfiguration* pSignatureConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersPkcs11_SignatureConfiguration_SetSignatureFormat(
    TPdfToolsCryptoProvidersPkcs11_SignatureConfiguration* pSignatureConfiguration,
    TPdfToolsCrypto_SignatureFormat                        iSignatureFormat);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersPkcs11_SignatureConfiguration_GetAddTimestamp(
    TPdfToolsCryptoProvidersPkcs11_SignatureConfiguration* pSignatureConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersPkcs11_SignatureConfiguration_SetAddTimestamp(
    TPdfToolsCryptoProvidersPkcs11_SignatureConfiguration* pSignatureConfiguration, BOOL bAddTimestamp);
PDFTOOLS_EXPORT TPdfToolsCrypto_ValidationInformation PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_SignatureConfiguration_GetValidationInformation(
    TPdfToolsCryptoProvidersPkcs11_SignatureConfiguration* pSignatureConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersPkcs11_SignatureConfiguration_SetValidationInformation(
    TPdfToolsCryptoProvidersPkcs11_SignatureConfiguration* pSignatureConfiguration,
    TPdfToolsCrypto_ValidationInformation                  iValidationInformation);

/******************************************************************************
 * TimestampConfiguration
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsCrypto_HashAlgorithm PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_TimestampConfiguration_GetHashAlgorithm(
    TPdfToolsCryptoProvidersPkcs11_TimestampConfiguration* pTimestampConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersPkcs11_TimestampConfiguration_SetHashAlgorithm(
    TPdfToolsCryptoProvidersPkcs11_TimestampConfiguration* pTimestampConfiguration,
    TPdfToolsCrypto_HashAlgorithm                          iHashAlgorithm);

/******************************************************************************
 * Module
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersPkcs11_Module* PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_Module_LoadA(const char* szLibrary);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersPkcs11_Module* PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_Module_LoadW(const WCHAR* szLibrary);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_Module_GetEnableFullParallelization(TPdfToolsCryptoProvidersPkcs11_Module* pModule);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersPkcs11_Module_SetEnableFullParallelization(
    TPdfToolsCryptoProvidersPkcs11_Module* pModule, BOOL bEnableFullParallelization);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersPkcs11_DeviceList* PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_Module_GetDevices(TPdfToolsCryptoProvidersPkcs11_Module* pModule);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_Module_Close(TPdfToolsCryptoProvidersPkcs11_Module* pObject);
/******************************************************************************
 * Device
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersPkcs11_Session* PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_Device_CreateSessionA(TPdfToolsCryptoProvidersPkcs11_Device* pDevice,
                                                    const char*                            szPassword);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersPkcs11_Session* PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_Device_CreateSessionW(TPdfToolsCryptoProvidersPkcs11_Device* pDevice,
                                                    const WCHAR*                           szPassword);

PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsCryptoProvidersPkcs11_Device_GetDescriptionA(
    TPdfToolsCryptoProvidersPkcs11_Device* pDevice, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsCryptoProvidersPkcs11_Device_GetDescriptionW(
    TPdfToolsCryptoProvidersPkcs11_Device* pDevice, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsCryptoProvidersPkcs11_Device_GetManufacturerIDA(
    TPdfToolsCryptoProvidersPkcs11_Device* pDevice, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsCryptoProvidersPkcs11_Device_GetManufacturerIDW(
    TPdfToolsCryptoProvidersPkcs11_Device* pDevice, WCHAR* pBuffer, size_t nBufferSize);

/******************************************************************************
 * Session
 *****************************************************************************/
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_Session_LoginA(TPdfToolsCryptoProvidersPkcs11_Session* pSession, const char* szPassword);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_Session_LoginW(TPdfToolsCryptoProvidersPkcs11_Session* pSession, const WCHAR* szPassword);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersPkcs11_SignatureConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_Session_CreateSignature(TPdfToolsCryptoProvidersPkcs11_Session* pSession,
                                                      TPdfToolsCryptoProviders_Certificate*   pCertificate);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersPkcs11_SignatureConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_Session_CreateSignatureFromNameA(TPdfToolsCryptoProvidersPkcs11_Session* pSession,
                                                               const char*                             szName);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersPkcs11_SignatureConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_Session_CreateSignatureFromNameW(TPdfToolsCryptoProvidersPkcs11_Session* pSession,
                                                               const WCHAR*                            szName);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersPkcs11_SignatureConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_Session_CreateSignatureFromKeyId(TPdfToolsCryptoProvidersPkcs11_Session* pSession,
                                                               const unsigned char* pId, size_t nIds,
                                                               const TPdfToolsSys_StreamDescriptor* pCertificate);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersPkcs11_SignatureConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_Session_CreateSignatureFromKeyLabelA(TPdfToolsCryptoProvidersPkcs11_Session* pSession,
                                                                   const char*                             szLabel,
                                                                   const TPdfToolsSys_StreamDescriptor* pCertificate);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersPkcs11_SignatureConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_Session_CreateSignatureFromKeyLabelW(TPdfToolsCryptoProvidersPkcs11_Session* pSession,
                                                                   const WCHAR*                            szLabel,
                                                                   const TPdfToolsSys_StreamDescriptor* pCertificate);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersPkcs11_TimestampConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_Session_CreateTimestamp(TPdfToolsCryptoProvidersPkcs11_Session* pSession);

PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsCryptoProvidersPkcs11_Session_GetTimestampUrlA(
    TPdfToolsCryptoProvidersPkcs11_Session* pSession, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsCryptoProvidersPkcs11_Session_GetTimestampUrlW(
    TPdfToolsCryptoProvidersPkcs11_Session* pSession, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersPkcs11_Session_SetTimestampUrlA(
    TPdfToolsCryptoProvidersPkcs11_Session* pSession, const char* szTimestampUrl);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersPkcs11_Session_SetTimestampUrlW(
    TPdfToolsCryptoProvidersPkcs11_Session* pSession, const WCHAR* szTimestampUrl);
PDFTOOLS_EXPORT TPdfToolsCryptoProviders_CertificateList* PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_Session_GetCertificates(TPdfToolsCryptoProvidersPkcs11_Session* pSession);

/******************************************************************************
 * DeviceList
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersPkcs11_Device* PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_DeviceList_GetSingle(TPdfToolsCryptoProvidersPkcs11_DeviceList* pDeviceList);
PDFTOOLS_EXPORT int PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_DeviceList_GetCount(TPdfToolsCryptoProvidersPkcs11_DeviceList* pDeviceList);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersPkcs11_Device* PDFTOOLS_CALL
PdfToolsCryptoProvidersPkcs11_DeviceList_Get(TPdfToolsCryptoProvidersPkcs11_DeviceList* pDeviceList, int iIndex);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSCRYPTOPROVIDERSPKCS11_H__ */
