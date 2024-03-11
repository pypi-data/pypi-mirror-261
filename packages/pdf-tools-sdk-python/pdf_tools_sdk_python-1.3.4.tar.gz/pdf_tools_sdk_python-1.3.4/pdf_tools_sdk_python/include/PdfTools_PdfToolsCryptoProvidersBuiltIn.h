/******************************************************************************
 *
 * File:            PdfTools_PdfToolsCryptoProvidersBuiltIn.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSCRYPTOPROVIDERSBUILTIN_H__
#define PDFTOOLS_PDFTOOLSCRYPTOPROVIDERSBUILTIN_H__

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
#define PdfToolsCryptoProvidersBuiltIn_Provider_CreateSignatureFromCertificate \
    PdfToolsCryptoProvidersBuiltIn_Provider_CreateSignatureFromCertificateW
#define PdfToolsCryptoProvidersBuiltIn_Provider_CreatePreparedSignature \
    PdfToolsCryptoProvidersBuiltIn_Provider_CreatePreparedSignatureW

#define PdfToolsCryptoProvidersBuiltIn_Provider_GetTimestampUrl PdfToolsCryptoProvidersBuiltIn_Provider_GetTimestampUrlW
#define PdfToolsCryptoProvidersBuiltIn_Provider_SetTimestampUrl PdfToolsCryptoProvidersBuiltIn_Provider_SetTimestampUrlW

#else
#define PdfToolsCryptoProvidersBuiltIn_Provider_CreateSignatureFromCertificate \
    PdfToolsCryptoProvidersBuiltIn_Provider_CreateSignatureFromCertificateA
#define PdfToolsCryptoProvidersBuiltIn_Provider_CreatePreparedSignature \
    PdfToolsCryptoProvidersBuiltIn_Provider_CreatePreparedSignatureA

#define PdfToolsCryptoProvidersBuiltIn_Provider_GetTimestampUrl PdfToolsCryptoProvidersBuiltIn_Provider_GetTimestampUrlA
#define PdfToolsCryptoProvidersBuiltIn_Provider_SetTimestampUrl PdfToolsCryptoProvidersBuiltIn_Provider_SetTimestampUrlA

#endif

/******************************************************************************
 * SignatureConfiguration
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsCrypto_HashAlgorithm PDFTOOLS_CALL
PdfToolsCryptoProvidersBuiltIn_SignatureConfiguration_GetHashAlgorithm(
    TPdfToolsCryptoProvidersBuiltIn_SignatureConfiguration* pSignatureConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersBuiltIn_SignatureConfiguration_SetHashAlgorithm(
    TPdfToolsCryptoProvidersBuiltIn_SignatureConfiguration* pSignatureConfiguration,
    TPdfToolsCrypto_HashAlgorithm                           iHashAlgorithm);
PDFTOOLS_EXPORT TPdfToolsCrypto_SignaturePaddingType PDFTOOLS_CALL
PdfToolsCryptoProvidersBuiltIn_SignatureConfiguration_GetSignaturePaddingType(
    TPdfToolsCryptoProvidersBuiltIn_SignatureConfiguration* pSignatureConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersBuiltIn_SignatureConfiguration_SetSignaturePaddingType(
    TPdfToolsCryptoProvidersBuiltIn_SignatureConfiguration* pSignatureConfiguration,
    TPdfToolsCrypto_SignaturePaddingType                    iSignaturePaddingType);
PDFTOOLS_EXPORT TPdfToolsCrypto_SignatureFormat PDFTOOLS_CALL
PdfToolsCryptoProvidersBuiltIn_SignatureConfiguration_GetSignatureFormat(
    TPdfToolsCryptoProvidersBuiltIn_SignatureConfiguration* pSignatureConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersBuiltIn_SignatureConfiguration_SetSignatureFormat(
    TPdfToolsCryptoProvidersBuiltIn_SignatureConfiguration* pSignatureConfiguration,
    TPdfToolsCrypto_SignatureFormat                         iSignatureFormat);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersBuiltIn_SignatureConfiguration_GetAddTimestamp(
    TPdfToolsCryptoProvidersBuiltIn_SignatureConfiguration* pSignatureConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersBuiltIn_SignatureConfiguration_SetAddTimestamp(
    TPdfToolsCryptoProvidersBuiltIn_SignatureConfiguration* pSignatureConfiguration, BOOL bAddTimestamp);
PDFTOOLS_EXPORT TPdfToolsCrypto_ValidationInformation PDFTOOLS_CALL
PdfToolsCryptoProvidersBuiltIn_SignatureConfiguration_GetValidationInformation(
    TPdfToolsCryptoProvidersBuiltIn_SignatureConfiguration* pSignatureConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersBuiltIn_SignatureConfiguration_SetValidationInformation(
    TPdfToolsCryptoProvidersBuiltIn_SignatureConfiguration* pSignatureConfiguration,
    TPdfToolsCrypto_ValidationInformation                   iValidationInformation);

/******************************************************************************
 * TimestampConfiguration
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsCrypto_HashAlgorithm PDFTOOLS_CALL
PdfToolsCryptoProvidersBuiltIn_TimestampConfiguration_GetHashAlgorithm(
    TPdfToolsCryptoProvidersBuiltIn_TimestampConfiguration* pTimestampConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersBuiltIn_TimestampConfiguration_SetHashAlgorithm(
    TPdfToolsCryptoProvidersBuiltIn_TimestampConfiguration* pTimestampConfiguration,
    TPdfToolsCrypto_HashAlgorithm                           iHashAlgorithm);

/******************************************************************************
 * Provider
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersBuiltIn_Provider* PDFTOOLS_CALL
PdfToolsCryptoProvidersBuiltIn_Provider_New(void);

PDFTOOLS_EXPORT TPdfToolsCryptoProvidersBuiltIn_SignatureConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersBuiltIn_Provider_CreateSignatureFromCertificateA(
    TPdfToolsCryptoProvidersBuiltIn_Provider* pProvider, const TPdfToolsSys_StreamDescriptor* pStreamDesc,
    const char* szPassword);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersBuiltIn_SignatureConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersBuiltIn_Provider_CreateSignatureFromCertificateW(
    TPdfToolsCryptoProvidersBuiltIn_Provider* pProvider, const TPdfToolsSys_StreamDescriptor* pStreamDesc,
    const WCHAR* szPassword);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersBuiltIn_TimestampConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersBuiltIn_Provider_CreateTimestamp(TPdfToolsCryptoProvidersBuiltIn_Provider* pProvider);
PDFTOOLS_EXPORT TPdfToolsSign_SignatureConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersBuiltIn_Provider_CreatePreparedSignatureA(TPdfToolsCryptoProvidersBuiltIn_Provider* pProvider,
                                                                 int iSize, const char* szFormat, const char* szName);
PDFTOOLS_EXPORT TPdfToolsSign_SignatureConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersBuiltIn_Provider_CreatePreparedSignatureW(TPdfToolsCryptoProvidersBuiltIn_Provider* pProvider,
                                                                 int iSize, const WCHAR* szFormat, const WCHAR* szName);
PDFTOOLS_EXPORT TPdfToolsSign_SignatureConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersBuiltIn_Provider_ReadExternalSignature(TPdfToolsCryptoProvidersBuiltIn_Provider* pProvider,
                                                              const unsigned char* pSignature, size_t nSignatures);

PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsCryptoProvidersBuiltIn_Provider_GetTimestampUrlA(
    TPdfToolsCryptoProvidersBuiltIn_Provider* pProvider, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsCryptoProvidersBuiltIn_Provider_GetTimestampUrlW(
    TPdfToolsCryptoProvidersBuiltIn_Provider* pProvider, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersBuiltIn_Provider_SetTimestampUrlA(
    TPdfToolsCryptoProvidersBuiltIn_Provider* pProvider, const char* szTimestampUrl);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersBuiltIn_Provider_SetTimestampUrlW(
    TPdfToolsCryptoProvidersBuiltIn_Provider* pProvider, const WCHAR* szTimestampUrl);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSCRYPTOPROVIDERSBUILTIN_H__ */
