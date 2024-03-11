/******************************************************************************
 *
 * File:            PdfTools_PdfToolsCryptoProvidersGlobalSignDss.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSCRYPTOPROVIDERSGLOBALSIGNDSS_H__
#define PDFTOOLS_PDFTOOLSCRYPTOPROVIDERSGLOBALSIGNDSS_H__

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
#define PdfToolsCryptoProvidersGlobalSignDss_Session_New PdfToolsCryptoProvidersGlobalSignDss_Session_NewW
#define PdfToolsCryptoProvidersGlobalSignDss_Session_CreateSignatureForDynamicIdentity \
    PdfToolsCryptoProvidersGlobalSignDss_Session_CreateSignatureForDynamicIdentityW

#else
#define PdfToolsCryptoProvidersGlobalSignDss_Session_New PdfToolsCryptoProvidersGlobalSignDss_Session_NewA
#define PdfToolsCryptoProvidersGlobalSignDss_Session_CreateSignatureForDynamicIdentity \
    PdfToolsCryptoProvidersGlobalSignDss_Session_CreateSignatureForDynamicIdentityA

#endif

/******************************************************************************
 * SignatureConfiguration
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsCrypto_HashAlgorithm PDFTOOLS_CALL
PdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration_GetHashAlgorithm(
    TPdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration* pSignatureConfiguration);
PDFTOOLS_EXPORT TPdfToolsCrypto_SignaturePaddingType PDFTOOLS_CALL
PdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration_GetSignaturePaddingType(
    TPdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration* pSignatureConfiguration);
PDFTOOLS_EXPORT TPdfToolsCrypto_SignatureFormat PDFTOOLS_CALL
PdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration_GetSignatureFormat(
    TPdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration* pSignatureConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration_SetSignatureFormat(
    TPdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration* pSignatureConfiguration,
    TPdfToolsCrypto_SignatureFormat                               iSignatureFormat);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration_GetAddTimestamp(
    TPdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration* pSignatureConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration_SetAddTimestamp(
    TPdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration* pSignatureConfiguration, BOOL bAddTimestamp);
PDFTOOLS_EXPORT TPdfToolsCrypto_ValidationInformation PDFTOOLS_CALL
PdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration_GetValidationInformation(
    TPdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration* pSignatureConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration_SetValidationInformation(
    TPdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration* pSignatureConfiguration,
    TPdfToolsCrypto_ValidationInformation                         iValidationInformation);

/******************************************************************************
 * TimestampConfiguration
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsCrypto_HashAlgorithm PDFTOOLS_CALL
PdfToolsCryptoProvidersGlobalSignDss_TimestampConfiguration_GetHashAlgorithm(
    TPdfToolsCryptoProvidersGlobalSignDss_TimestampConfiguration* pTimestampConfiguration);

/******************************************************************************
 * Session
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersGlobalSignDss_Session* PDFTOOLS_CALL
PdfToolsCryptoProvidersGlobalSignDss_Session_NewA(const char* szUrl, const char* szApi_key, const char* szApi_secret,
                                                  TPdfTools_HttpClientHandler* pHttpClientHandler);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersGlobalSignDss_Session* PDFTOOLS_CALL
PdfToolsCryptoProvidersGlobalSignDss_Session_NewW(const WCHAR* szUrl, const WCHAR* szApi_key, const WCHAR* szApi_secret,
                                                  TPdfTools_HttpClientHandler* pHttpClientHandler);

PDFTOOLS_EXPORT TPdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersGlobalSignDss_Session_CreateSignatureForStaticIdentity(
    TPdfToolsCryptoProvidersGlobalSignDss_Session* pSession);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersGlobalSignDss_Session_CreateSignatureForDynamicIdentityA(
    TPdfToolsCryptoProvidersGlobalSignDss_Session* pSession, const char* szIdentity);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersGlobalSignDss_SignatureConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersGlobalSignDss_Session_CreateSignatureForDynamicIdentityW(
    TPdfToolsCryptoProvidersGlobalSignDss_Session* pSession, const WCHAR* szIdentity);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersGlobalSignDss_TimestampConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersGlobalSignDss_Session_CreateTimestamp(TPdfToolsCryptoProvidersGlobalSignDss_Session* pSession);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSCRYPTOPROVIDERSGLOBALSIGNDSS_H__ */
