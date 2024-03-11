/******************************************************************************
 *
 * File:            PdfTools_PdfToolsCryptoProvidersSwisscomSigSrv.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSCRYPTOPROVIDERSSWISSCOMSIGSRV_H__
#define PDFTOOLS_PDFTOOLSCRYPTOPROVIDERSSWISSCOMSIGSRV_H__

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
#define TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp_ConsentRequired \
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp_ConsentRequiredW
#define PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_AddConsentRequiredHandler \
    PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_AddConsentRequiredHandlerW
#define PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_RemoveConsentRequiredHandler \
    PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_RemoveConsentRequiredHandlerW
#define PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_New        PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_NewW
#define PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_GetMSISDN  PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_GetMSISDNW
#define PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_SetMSISDN  PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_SetMSISDNW
#define PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_GetMessage PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_GetMessageW
#define PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_SetMessage PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_SetMessageW
#define PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_GetLanguage \
    PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_GetLanguageW
#define PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_SetLanguage \
    PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_SetLanguageW

#define PdfToolsCryptoProvidersSwisscomSigSrv_Session_New PdfToolsCryptoProvidersSwisscomSigSrv_Session_NewW
#define PdfToolsCryptoProvidersSwisscomSigSrv_Session_CreateSignatureForStaticIdentity \
    PdfToolsCryptoProvidersSwisscomSigSrv_Session_CreateSignatureForStaticIdentityW
#define PdfToolsCryptoProvidersSwisscomSigSrv_Session_CreateSignatureForOnDemandIdentity \
    PdfToolsCryptoProvidersSwisscomSigSrv_Session_CreateSignatureForOnDemandIdentityW
#define PdfToolsCryptoProvidersSwisscomSigSrv_Session_CreateTimestamp \
    PdfToolsCryptoProvidersSwisscomSigSrv_Session_CreateTimestampW

#else
#define TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp_ConsentRequired \
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp_ConsentRequiredA
#define PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_AddConsentRequiredHandler \
    PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_AddConsentRequiredHandlerA
#define PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_RemoveConsentRequiredHandler \
    PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_RemoveConsentRequiredHandlerA
#define PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_New        PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_NewA
#define PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_GetMSISDN  PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_GetMSISDNA
#define PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_SetMSISDN  PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_SetMSISDNA
#define PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_GetMessage PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_GetMessageA
#define PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_SetMessage PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_SetMessageA
#define PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_GetLanguage \
    PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_GetLanguageA
#define PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_SetLanguage \
    PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_SetLanguageA

#define PdfToolsCryptoProvidersSwisscomSigSrv_Session_New PdfToolsCryptoProvidersSwisscomSigSrv_Session_NewA
#define PdfToolsCryptoProvidersSwisscomSigSrv_Session_CreateSignatureForStaticIdentity \
    PdfToolsCryptoProvidersSwisscomSigSrv_Session_CreateSignatureForStaticIdentityA
#define PdfToolsCryptoProvidersSwisscomSigSrv_Session_CreateSignatureForOnDemandIdentity \
    PdfToolsCryptoProvidersSwisscomSigSrv_Session_CreateSignatureForOnDemandIdentityA
#define PdfToolsCryptoProvidersSwisscomSigSrv_Session_CreateTimestamp \
    PdfToolsCryptoProvidersSwisscomSigSrv_Session_CreateTimestampA

#endif

typedef void(PDFTOOLS_CALL* TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp_ConsentRequiredA)(void*       pContext,
                                                                                            const char* szUrl);
typedef void(PDFTOOLS_CALL* TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp_ConsentRequiredW)(void*        pContext,
                                                                                            const WCHAR* szUrl);

/******************************************************************************
 * SignatureConfiguration
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsCrypto_HashAlgorithm PDFTOOLS_CALL
PdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration_GetHashAlgorithm(
    TPdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration* pSignatureConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration_SetHashAlgorithm(
    TPdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration* pSignatureConfiguration,
    TPdfToolsCrypto_HashAlgorithm                                  iHashAlgorithm);
PDFTOOLS_EXPORT TPdfToolsCrypto_SignatureFormat PDFTOOLS_CALL
PdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration_GetSignatureFormat(
    TPdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration* pSignatureConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration_SetSignatureFormat(
    TPdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration* pSignatureConfiguration,
    TPdfToolsCrypto_SignatureFormat                                iSignatureFormat);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration_GetAddTimestamp(
    TPdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration* pSignatureConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration_SetAddTimestamp(
    TPdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration* pSignatureConfiguration, BOOL bAddTimestamp);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration_GetEmbedValidationInformation(
    TPdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration* pSignatureConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration_SetEmbedValidationInformation(
    TPdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration* pSignatureConfiguration,
    BOOL                                                           bEmbedValidationInformation);

/******************************************************************************
 * TimestampConfiguration
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsCrypto_HashAlgorithm PDFTOOLS_CALL
PdfToolsCryptoProvidersSwisscomSigSrv_TimestampConfiguration_GetHashAlgorithm(
    TPdfToolsCryptoProvidersSwisscomSigSrv_TimestampConfiguration* pTimestampConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_TimestampConfiguration_SetHashAlgorithm(
    TPdfToolsCryptoProvidersSwisscomSigSrv_TimestampConfiguration* pTimestampConfiguration,
    TPdfToolsCrypto_HashAlgorithm                                  iHashAlgorithm);

/******************************************************************************
 * StepUp
 *****************************************************************************/
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_AddConsentRequiredHandlerA(
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp* pStepUp, void* pContext,
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp_ConsentRequiredA pFunction);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_AddConsentRequiredHandlerW(
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp* pStepUp, void* pContext,
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp_ConsentRequiredW pFunction);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_RemoveConsentRequiredHandlerA(
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp* pStepUp, void* pContext,
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp_ConsentRequiredA pFunction);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_RemoveConsentRequiredHandlerW(
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp* pStepUp, void* pContext,
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp_ConsentRequiredW pFunction);

PDFTOOLS_EXPORT TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp* PDFTOOLS_CALL
PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_NewA(const char* szMsisdn, const char* szMessage, const char* szLanguage);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp* PDFTOOLS_CALL
PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_NewW(const WCHAR* szMsisdn, const WCHAR* szMessage,
                                                  const WCHAR* szLanguage);

PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_GetMSISDNA(
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp* pStepUp, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_GetMSISDNW(
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp* pStepUp, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_SetMSISDNA(
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp* pStepUp, const char* szMSISDN);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_SetMSISDNW(
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp* pStepUp, const WCHAR* szMSISDN);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_GetMessageA(
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp* pStepUp, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_GetMessageW(
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp* pStepUp, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_SetMessageA(
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp* pStepUp, const char* szMessage);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_SetMessageW(
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp* pStepUp, const WCHAR* szMessage);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_GetLanguageA(
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp* pStepUp, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_GetLanguageW(
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp* pStepUp, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_SetLanguageA(
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp* pStepUp, const char* szLanguage);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsCryptoProvidersSwisscomSigSrv_StepUp_SetLanguageW(
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp* pStepUp, const WCHAR* szLanguage);

/******************************************************************************
 * Session
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersSwisscomSigSrv_Session* PDFTOOLS_CALL
PdfToolsCryptoProvidersSwisscomSigSrv_Session_NewA(const char* szUrl, TPdfTools_HttpClientHandler* pHttpClientHandler);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersSwisscomSigSrv_Session* PDFTOOLS_CALL
PdfToolsCryptoProvidersSwisscomSigSrv_Session_NewW(const WCHAR* szUrl, TPdfTools_HttpClientHandler* pHttpClientHandler);

PDFTOOLS_EXPORT TPdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersSwisscomSigSrv_Session_CreateSignatureForStaticIdentityA(
    TPdfToolsCryptoProvidersSwisscomSigSrv_Session* pSession, const char* szIdentity, const char* szName);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersSwisscomSigSrv_Session_CreateSignatureForStaticIdentityW(
    TPdfToolsCryptoProvidersSwisscomSigSrv_Session* pSession, const WCHAR* szIdentity, const WCHAR* szName);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersSwisscomSigSrv_Session_CreateSignatureForOnDemandIdentityA(
    TPdfToolsCryptoProvidersSwisscomSigSrv_Session* pSession, const char* szIdentity, const char* szDistinguishedName,
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp* pStepUp);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersSwisscomSigSrv_SignatureConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersSwisscomSigSrv_Session_CreateSignatureForOnDemandIdentityW(
    TPdfToolsCryptoProvidersSwisscomSigSrv_Session* pSession, const WCHAR* szIdentity, const WCHAR* szDistinguishedName,
    TPdfToolsCryptoProvidersSwisscomSigSrv_StepUp* pStepUp);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersSwisscomSigSrv_TimestampConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersSwisscomSigSrv_Session_CreateTimestampA(TPdfToolsCryptoProvidersSwisscomSigSrv_Session* pSession,
                                                               const char* szIdentity);
PDFTOOLS_EXPORT TPdfToolsCryptoProvidersSwisscomSigSrv_TimestampConfiguration* PDFTOOLS_CALL
PdfToolsCryptoProvidersSwisscomSigSrv_Session_CreateTimestampW(TPdfToolsCryptoProvidersSwisscomSigSrv_Session* pSession,
                                                               const WCHAR* szIdentity);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSCRYPTOPROVIDERSSWISSCOMSIGSRV_H__ */
