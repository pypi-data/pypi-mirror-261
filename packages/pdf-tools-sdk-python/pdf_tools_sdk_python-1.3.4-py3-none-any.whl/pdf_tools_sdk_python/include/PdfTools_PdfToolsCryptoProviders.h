/******************************************************************************
 *
 * File:            PdfTools_PdfToolsCryptoProviders.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSCRYPTOPROVIDERS_H__
#define PDFTOOLS_PDFTOOLSCRYPTOPROVIDERS_H__

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
#define PdfToolsCryptoProviders_Certificate_GetName PdfToolsCryptoProviders_Certificate_GetNameW

#define PdfToolsCryptoProviders_Certificate_GetIssuer PdfToolsCryptoProviders_Certificate_GetIssuerW

#define PdfToolsCryptoProviders_Certificate_GetFingerprint PdfToolsCryptoProviders_Certificate_GetFingerprintW

#else
#define PdfToolsCryptoProviders_Certificate_GetName PdfToolsCryptoProviders_Certificate_GetNameA

#define PdfToolsCryptoProviders_Certificate_GetIssuer PdfToolsCryptoProviders_Certificate_GetIssuerA

#define PdfToolsCryptoProviders_Certificate_GetFingerprint PdfToolsCryptoProviders_Certificate_GetFingerprintA

#endif

PDFTOOLS_EXPORT TPdfToolsCryptoProviders_ProviderType PDFTOOLS_CALL
PdfToolsCryptoProviders_Provider_GetType(TPdfToolsCryptoProviders_Provider* pProvider);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProviders_Provider_Close(TPdfToolsCryptoProviders_Provider* pObject);
/******************************************************************************
 * Certificate
 *****************************************************************************/
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsCryptoProviders_Certificate_GetNameA(
    TPdfToolsCryptoProviders_Certificate* pCertificate, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsCryptoProviders_Certificate_GetNameW(
    TPdfToolsCryptoProviders_Certificate* pCertificate, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsCryptoProviders_Certificate_GetIssuerA(
    TPdfToolsCryptoProviders_Certificate* pCertificate, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsCryptoProviders_Certificate_GetIssuerW(
    TPdfToolsCryptoProviders_Certificate* pCertificate, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsCryptoProviders_Certificate_GetFingerprintA(
    TPdfToolsCryptoProviders_Certificate* pCertificate, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsCryptoProviders_Certificate_GetFingerprintW(
    TPdfToolsCryptoProviders_Certificate* pCertificate, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsCryptoProviders_Certificate_GetHasPrivateKey(TPdfToolsCryptoProviders_Certificate* pCertificate);

/******************************************************************************
 * CertificateList
 *****************************************************************************/
PDFTOOLS_EXPORT int PDFTOOLS_CALL
PdfToolsCryptoProviders_CertificateList_GetCount(TPdfToolsCryptoProviders_CertificateList* pCertificateList);
PDFTOOLS_EXPORT TPdfToolsCryptoProviders_Certificate* PDFTOOLS_CALL
PdfToolsCryptoProviders_CertificateList_Get(TPdfToolsCryptoProviders_CertificateList* pCertificateList, int iIndex);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSCRYPTOPROVIDERS_H__ */
