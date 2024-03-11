/******************************************************************************
 *
 * File:            PdfTools_PdfToolsSignatureValidation.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSSIGNATUREVALIDATION_H__
#define PDFTOOLS_PDFTOOLSSIGNATUREVALIDATION_H__

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
#define PdfToolsSignatureValidation_ConstraintResult_GetMessage PdfToolsSignatureValidation_ConstraintResult_GetMessageW

#define TPdfToolsSignatureValidation_Validator_Constraint TPdfToolsSignatureValidation_Validator_ConstraintW
#define PdfToolsSignatureValidation_Validator_AddConstraintHandler \
    PdfToolsSignatureValidation_Validator_AddConstraintHandlerW
#define PdfToolsSignatureValidation_Validator_RemoveConstraintHandler \
    PdfToolsSignatureValidation_Validator_RemoveConstraintHandlerW
#define PdfToolsSignatureValidation_Certificate_GetSubjectName PdfToolsSignatureValidation_Certificate_GetSubjectNameW

#define PdfToolsSignatureValidation_Certificate_GetIssuerName PdfToolsSignatureValidation_Certificate_GetIssuerNameW

#define PdfToolsSignatureValidation_Certificate_GetFingerprint PdfToolsSignatureValidation_Certificate_GetFingerprintW

#define PdfToolsSignatureValidation_CustomTrustList_AddArchive PdfToolsSignatureValidation_CustomTrustList_AddArchiveW

#else
#define PdfToolsSignatureValidation_ConstraintResult_GetMessage PdfToolsSignatureValidation_ConstraintResult_GetMessageA

#define TPdfToolsSignatureValidation_Validator_Constraint TPdfToolsSignatureValidation_Validator_ConstraintA
#define PdfToolsSignatureValidation_Validator_AddConstraintHandler \
    PdfToolsSignatureValidation_Validator_AddConstraintHandlerA
#define PdfToolsSignatureValidation_Validator_RemoveConstraintHandler \
    PdfToolsSignatureValidation_Validator_RemoveConstraintHandlerA
#define PdfToolsSignatureValidation_Certificate_GetSubjectName PdfToolsSignatureValidation_Certificate_GetSubjectNameA

#define PdfToolsSignatureValidation_Certificate_GetIssuerName PdfToolsSignatureValidation_Certificate_GetIssuerNameA

#define PdfToolsSignatureValidation_Certificate_GetFingerprint PdfToolsSignatureValidation_Certificate_GetFingerprintA

#define PdfToolsSignatureValidation_CustomTrustList_AddArchive PdfToolsSignatureValidation_CustomTrustList_AddArchiveA

#endif

typedef void(PDFTOOLS_CALL* TPdfToolsSignatureValidation_Validator_ConstraintA)(
    void* pContext, const char* szMessage, TPdfToolsSignatureValidation_Indication iIndication,
    TPdfToolsSignatureValidation_SubIndication iSubIndication, TPdfToolsPdf_SignedSignatureField* pSignature,
    const char* szDataPart);
typedef void(PDFTOOLS_CALL* TPdfToolsSignatureValidation_Validator_ConstraintW)(
    void* pContext, const WCHAR* szMessage, TPdfToolsSignatureValidation_Indication iIndication,
    TPdfToolsSignatureValidation_SubIndication iSubIndication, TPdfToolsPdf_SignedSignatureField* pSignature,
    const WCHAR* szDataPart);

/******************************************************************************
 * ConstraintResult
 *****************************************************************************/
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSignatureValidation_ConstraintResult_GetMessageA(
    TPdfToolsSignatureValidation_ConstraintResult* pConstraintResult, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSignatureValidation_ConstraintResult_GetMessageW(
    TPdfToolsSignatureValidation_ConstraintResult* pConstraintResult, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_Indication PDFTOOLS_CALL
PdfToolsSignatureValidation_ConstraintResult_GetIndication(
    TPdfToolsSignatureValidation_ConstraintResult* pConstraintResult);
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_SubIndication PDFTOOLS_CALL
PdfToolsSignatureValidation_ConstraintResult_GetSubIndication(
    TPdfToolsSignatureValidation_ConstraintResult* pConstraintResult);

/******************************************************************************
 * Validator
 *****************************************************************************/
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSignatureValidation_Validator_AddConstraintHandlerA(
    TPdfToolsSignatureValidation_Validator* pValidator, void* pContext,
    TPdfToolsSignatureValidation_Validator_ConstraintA pFunction);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSignatureValidation_Validator_AddConstraintHandlerW(
    TPdfToolsSignatureValidation_Validator* pValidator, void* pContext,
    TPdfToolsSignatureValidation_Validator_ConstraintW pFunction);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSignatureValidation_Validator_RemoveConstraintHandlerA(
    TPdfToolsSignatureValidation_Validator* pValidator, void* pContext,
    TPdfToolsSignatureValidation_Validator_ConstraintA pFunction);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSignatureValidation_Validator_RemoveConstraintHandlerW(
    TPdfToolsSignatureValidation_Validator* pValidator, void* pContext,
    TPdfToolsSignatureValidation_Validator_ConstraintW pFunction);

PDFTOOLS_EXPORT TPdfToolsSignatureValidation_Validator* PDFTOOLS_CALL PdfToolsSignatureValidation_Validator_New(void);

PDFTOOLS_EXPORT TPdfToolsSignatureValidation_ValidationResults* PDFTOOLS_CALL
PdfToolsSignatureValidation_Validator_Validate(TPdfToolsSignatureValidation_Validator*        pValidator,
                                               TPdfToolsPdf_Document*                         pDocument,
                                               TPdfToolsSignatureValidationProfiles_Profile*  pProfile,
                                               TPdfToolsSignatureValidation_SignatureSelector iSelector);

/******************************************************************************
 * Certificate
 *****************************************************************************/
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSignatureValidation_Certificate_GetSubjectNameA(
    TPdfToolsSignatureValidation_Certificate* pCertificate, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSignatureValidation_Certificate_GetSubjectNameW(
    TPdfToolsSignatureValidation_Certificate* pCertificate, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSignatureValidation_Certificate_GetIssuerNameA(
    TPdfToolsSignatureValidation_Certificate* pCertificate, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSignatureValidation_Certificate_GetIssuerNameW(
    TPdfToolsSignatureValidation_Certificate* pCertificate, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSignatureValidation_Certificate_GetNotAfter(
    TPdfToolsSignatureValidation_Certificate* pCertificate, TPdfToolsSys_Date* pNotAfter);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSignatureValidation_Certificate_GetNotBefore(
    TPdfToolsSignatureValidation_Certificate* pCertificate, TPdfToolsSys_Date* pNotBefore);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSignatureValidation_Certificate_GetFingerprintA(
    TPdfToolsSignatureValidation_Certificate* pCertificate, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSignatureValidation_Certificate_GetFingerprintW(
    TPdfToolsSignatureValidation_Certificate* pCertificate, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSignatureValidation_Certificate_GetRawData(
    TPdfToolsSignatureValidation_Certificate* pCertificate, unsigned char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_DataSource PDFTOOLS_CALL
PdfToolsSignatureValidation_Certificate_GetSource(TPdfToolsSignatureValidation_Certificate* pCertificate);
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_ConstraintResult* PDFTOOLS_CALL
PdfToolsSignatureValidation_Certificate_GetValidity(TPdfToolsSignatureValidation_Certificate* pCertificate);

/******************************************************************************
 * CertificateChain
 *****************************************************************************/
PDFTOOLS_EXPORT int PDFTOOLS_CALL
PdfToolsSignatureValidation_CertificateChain_GetCount(TPdfToolsSignatureValidation_CertificateChain* pCertificateChain);
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_Certificate* PDFTOOLS_CALL
PdfToolsSignatureValidation_CertificateChain_Get(TPdfToolsSignatureValidation_CertificateChain* pCertificateChain,
                                                 int                                            iIndex);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSignatureValidation_CertificateChain_IsComplete(
    TPdfToolsSignatureValidation_CertificateChain* pCertificateChain);

/******************************************************************************
 * ValidationResults
 *****************************************************************************/
PDFTOOLS_EXPORT int PDFTOOLS_CALL PdfToolsSignatureValidation_ValidationResults_GetCount(
    TPdfToolsSignatureValidation_ValidationResults* pValidationResults);
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_ValidationResult* PDFTOOLS_CALL
PdfToolsSignatureValidation_ValidationResults_Get(TPdfToolsSignatureValidation_ValidationResults* pValidationResults,
                                                  int                                             iIndex);

/******************************************************************************
 * ValidationResult
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf_SignedSignatureField* PDFTOOLS_CALL
PdfToolsSignatureValidation_ValidationResult_GetSignatureField(
    TPdfToolsSignatureValidation_ValidationResult* pValidationResult);
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_SignatureContent* PDFTOOLS_CALL
PdfToolsSignatureValidation_ValidationResult_GetSignatureContent(
    TPdfToolsSignatureValidation_ValidationResult* pValidationResult);

/******************************************************************************
 * SignatureContent
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_ConstraintResult* PDFTOOLS_CALL
PdfToolsSignatureValidation_SignatureContent_GetValidity(
    TPdfToolsSignatureValidation_SignatureContent* pSignatureContent);

PDFTOOLS_EXPORT TPdfToolsSignatureValidation_SignatureContentType PDFTOOLS_CALL
PdfToolsSignatureValidation_SignatureContent_GetType(TPdfToolsSignatureValidation_SignatureContent* pSignatureContent);
/******************************************************************************
 * CmsSignatureContent
 *****************************************************************************/
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSignatureValidation_CmsSignatureContent_GetValidationTime(
    TPdfToolsSignatureValidation_CmsSignatureContent* pCmsSignatureContent, TPdfToolsSys_Date* pValidationTime);
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_TimeSource PDFTOOLS_CALL
PdfToolsSignatureValidation_CmsSignatureContent_GetValidationTimeSource(
    TPdfToolsSignatureValidation_CmsSignatureContent* pCmsSignatureContent);
PDFTOOLS_EXPORT TPdfToolsCrypto_HashAlgorithm PDFTOOLS_CALL
PdfToolsSignatureValidation_CmsSignatureContent_GetHashAlgorithm(
    TPdfToolsSignatureValidation_CmsSignatureContent* pCmsSignatureContent);
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_TimeStampContent* PDFTOOLS_CALL
PdfToolsSignatureValidation_CmsSignatureContent_GetTimeStamp(
    TPdfToolsSignatureValidation_CmsSignatureContent* pCmsSignatureContent);
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_Certificate* PDFTOOLS_CALL
PdfToolsSignatureValidation_CmsSignatureContent_GetSigningCertificate(
    TPdfToolsSignatureValidation_CmsSignatureContent* pCmsSignatureContent);
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_CertificateChain* PDFTOOLS_CALL
PdfToolsSignatureValidation_CmsSignatureContent_GetCertificateChain(
    TPdfToolsSignatureValidation_CmsSignatureContent* pCmsSignatureContent);

/******************************************************************************
 * TimeStampContent
 *****************************************************************************/
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSignatureValidation_TimeStampContent_GetValidationTime(
    TPdfToolsSignatureValidation_TimeStampContent* pTimeStampContent, TPdfToolsSys_Date* pValidationTime);
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_TimeSource PDFTOOLS_CALL
PdfToolsSignatureValidation_TimeStampContent_GetValidationTimeSource(
    TPdfToolsSignatureValidation_TimeStampContent* pTimeStampContent);
PDFTOOLS_EXPORT TPdfToolsCrypto_HashAlgorithm PDFTOOLS_CALL
PdfToolsSignatureValidation_TimeStampContent_GetHashAlgorithm(
    TPdfToolsSignatureValidation_TimeStampContent* pTimeStampContent);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSignatureValidation_TimeStampContent_GetDate(
    TPdfToolsSignatureValidation_TimeStampContent* pTimeStampContent, TPdfToolsSys_Date* pDate);
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_Certificate* PDFTOOLS_CALL
PdfToolsSignatureValidation_TimeStampContent_GetSigningCertificate(
    TPdfToolsSignatureValidation_TimeStampContent* pTimeStampContent);
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_CertificateChain* PDFTOOLS_CALL
PdfToolsSignatureValidation_TimeStampContent_GetCertificateChain(
    TPdfToolsSignatureValidation_TimeStampContent* pTimeStampContent);

/******************************************************************************
 * CustomTrustList
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_CustomTrustList* PDFTOOLS_CALL
PdfToolsSignatureValidation_CustomTrustList_New(void);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSignatureValidation_CustomTrustList_AddCertificates(
    TPdfToolsSignatureValidation_CustomTrustList* pCustomTrustList, const TPdfToolsSys_StreamDescriptor* pCertificate);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSignatureValidation_CustomTrustList_AddArchiveA(
    TPdfToolsSignatureValidation_CustomTrustList* pCustomTrustList, const TPdfToolsSys_StreamDescriptor* pStreamDesc,
    const char* szPassword);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSignatureValidation_CustomTrustList_AddArchiveW(
    TPdfToolsSignatureValidation_CustomTrustList* pCustomTrustList, const TPdfToolsSys_StreamDescriptor* pStreamDesc,
    const WCHAR* szPassword);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSSIGNATUREVALIDATION_H__ */
