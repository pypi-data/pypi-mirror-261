/******************************************************************************
 *
 * File:            PdfTools_PdfToolsSignatureValidationProfiles.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSSIGNATUREVALIDATIONPROFILES_H__
#define PDFTOOLS_PDFTOOLSSIGNATUREVALIDATIONPROFILES_H__

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
#else
#endif

/******************************************************************************
 * Profile
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsSignatureValidationProfiles_ValidationOptions* PDFTOOLS_CALL
PdfToolsSignatureValidationProfiles_Profile_GetValidationOptions(
    TPdfToolsSignatureValidationProfiles_Profile* pProfile);
PDFTOOLS_EXPORT TPdfToolsSignatureValidationProfiles_TrustConstraints* PDFTOOLS_CALL
PdfToolsSignatureValidationProfiles_Profile_GetSigningCertTrustConstraints(
    TPdfToolsSignatureValidationProfiles_Profile* pProfile);
PDFTOOLS_EXPORT TPdfToolsSignatureValidationProfiles_TrustConstraints* PDFTOOLS_CALL
PdfToolsSignatureValidationProfiles_Profile_GetTimeStampTrustConstraints(
    TPdfToolsSignatureValidationProfiles_Profile* pProfile);
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_CustomTrustList* PDFTOOLS_CALL
PdfToolsSignatureValidationProfiles_Profile_GetCustomTrustList(TPdfToolsSignatureValidationProfiles_Profile* pProfile);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSignatureValidationProfiles_Profile_SetCustomTrustList(
    TPdfToolsSignatureValidationProfiles_Profile* pProfile,
    TPdfToolsSignatureValidation_CustomTrustList* pCustomTrustList);

PDFTOOLS_EXPORT TPdfToolsSignatureValidationProfiles_ProfileType PDFTOOLS_CALL
PdfToolsSignatureValidationProfiles_Profile_GetType(TPdfToolsSignatureValidationProfiles_Profile* pProfile);
/******************************************************************************
 * ValidationOptions
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_TimeSource PDFTOOLS_CALL
PdfToolsSignatureValidationProfiles_ValidationOptions_GetTimeSource(
    TPdfToolsSignatureValidationProfiles_ValidationOptions* pValidationOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSignatureValidationProfiles_ValidationOptions_SetTimeSource(
    TPdfToolsSignatureValidationProfiles_ValidationOptions* pValidationOptions,
    TPdfToolsSignatureValidation_TimeSource                 iTimeSource);
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_DataSource PDFTOOLS_CALL
PdfToolsSignatureValidationProfiles_ValidationOptions_GetCertificateSources(
    TPdfToolsSignatureValidationProfiles_ValidationOptions* pValidationOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSignatureValidationProfiles_ValidationOptions_SetCertificateSources(
    TPdfToolsSignatureValidationProfiles_ValidationOptions* pValidationOptions,
    TPdfToolsSignatureValidation_DataSource                 iCertificateSources);
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_DataSource PDFTOOLS_CALL
PdfToolsSignatureValidationProfiles_ValidationOptions_GetRevocationInformationSources(
    TPdfToolsSignatureValidationProfiles_ValidationOptions* pValidationOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsSignatureValidationProfiles_ValidationOptions_SetRevocationInformationSources(
    TPdfToolsSignatureValidationProfiles_ValidationOptions* pValidationOptions,
    TPdfToolsSignatureValidation_DataSource                 iRevocationInformationSources);

/******************************************************************************
 * TrustConstraints
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsSignatureValidation_DataSource PDFTOOLS_CALL
PdfToolsSignatureValidationProfiles_TrustConstraints_GetTrustSources(
    TPdfToolsSignatureValidationProfiles_TrustConstraints* pTrustConstraints);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSignatureValidationProfiles_TrustConstraints_SetTrustSources(
    TPdfToolsSignatureValidationProfiles_TrustConstraints* pTrustConstraints,
    TPdfToolsSignatureValidation_DataSource                iTrustSources);
PDFTOOLS_EXPORT TPdfToolsSignatureValidationProfiles_RevocationCheckPolicy PDFTOOLS_CALL
PdfToolsSignatureValidationProfiles_TrustConstraints_GetRevocationCheckPolicy(
    TPdfToolsSignatureValidationProfiles_TrustConstraints* pTrustConstraints);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSignatureValidationProfiles_TrustConstraints_SetRevocationCheckPolicy(
    TPdfToolsSignatureValidationProfiles_TrustConstraints*     pTrustConstraints,
    TPdfToolsSignatureValidationProfiles_RevocationCheckPolicy iRevocationCheckPolicy);

/******************************************************************************
 * Default
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsSignatureValidationProfiles_Default* PDFTOOLS_CALL
PdfToolsSignatureValidationProfiles_Default_New(void);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSSIGNATUREVALIDATIONPROFILES_H__ */
