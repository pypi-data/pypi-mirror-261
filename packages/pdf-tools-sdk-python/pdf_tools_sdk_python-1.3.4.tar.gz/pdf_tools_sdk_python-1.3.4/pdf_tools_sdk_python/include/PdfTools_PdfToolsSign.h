/******************************************************************************
 *
 * File:            PdfTools_PdfToolsSign.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSSIGN_H__
#define PDFTOOLS_PDFTOOLSSIGN_H__

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
#define PdfToolsSign_CustomTextVariableMap_Get      PdfToolsSign_CustomTextVariableMap_GetW
#define PdfToolsSign_CustomTextVariableMap_GetKey   PdfToolsSign_CustomTextVariableMap_GetKeyW
#define PdfToolsSign_CustomTextVariableMap_GetValue PdfToolsSign_CustomTextVariableMap_GetValueW
#define PdfToolsSign_CustomTextVariableMap_Set      PdfToolsSign_CustomTextVariableMap_SetW
#define PdfToolsSign_CustomTextVariableMap_SetValue PdfToolsSign_CustomTextVariableMap_SetValueW

#define PdfToolsSign_SignatureConfiguration_GetFieldName PdfToolsSign_SignatureConfiguration_GetFieldNameW
#define PdfToolsSign_SignatureConfiguration_SetFieldName PdfToolsSign_SignatureConfiguration_SetFieldNameW
#define PdfToolsSign_SignatureConfiguration_GetName      PdfToolsSign_SignatureConfiguration_GetNameW

#define PdfToolsSign_SignatureConfiguration_GetLocation    PdfToolsSign_SignatureConfiguration_GetLocationW
#define PdfToolsSign_SignatureConfiguration_SetLocation    PdfToolsSign_SignatureConfiguration_SetLocationW
#define PdfToolsSign_SignatureConfiguration_GetReason      PdfToolsSign_SignatureConfiguration_GetReasonW
#define PdfToolsSign_SignatureConfiguration_SetReason      PdfToolsSign_SignatureConfiguration_SetReasonW
#define PdfToolsSign_SignatureConfiguration_GetContactInfo PdfToolsSign_SignatureConfiguration_GetContactInfoW
#define PdfToolsSign_SignatureConfiguration_SetContactInfo PdfToolsSign_SignatureConfiguration_SetContactInfoW

#define PdfToolsSign_TimestampConfiguration_GetFieldName PdfToolsSign_TimestampConfiguration_GetFieldNameW
#define PdfToolsSign_TimestampConfiguration_SetFieldName PdfToolsSign_TimestampConfiguration_SetFieldNameW

#define PdfToolsSign_SignatureFieldOptions_GetFieldName PdfToolsSign_SignatureFieldOptions_GetFieldNameW
#define PdfToolsSign_SignatureFieldOptions_SetFieldName PdfToolsSign_SignatureFieldOptions_SetFieldNameW

#define TPdfToolsSign_Signer_Warning             TPdfToolsSign_Signer_WarningW
#define PdfToolsSign_Signer_AddWarningHandler    PdfToolsSign_Signer_AddWarningHandlerW
#define PdfToolsSign_Signer_RemoveWarningHandler PdfToolsSign_Signer_RemoveWarningHandlerW

#else
#define PdfToolsSign_CustomTextVariableMap_Get      PdfToolsSign_CustomTextVariableMap_GetA
#define PdfToolsSign_CustomTextVariableMap_GetKey   PdfToolsSign_CustomTextVariableMap_GetKeyA
#define PdfToolsSign_CustomTextVariableMap_GetValue PdfToolsSign_CustomTextVariableMap_GetValueA
#define PdfToolsSign_CustomTextVariableMap_Set      PdfToolsSign_CustomTextVariableMap_SetA
#define PdfToolsSign_CustomTextVariableMap_SetValue PdfToolsSign_CustomTextVariableMap_SetValueA

#define PdfToolsSign_SignatureConfiguration_GetFieldName PdfToolsSign_SignatureConfiguration_GetFieldNameA
#define PdfToolsSign_SignatureConfiguration_SetFieldName PdfToolsSign_SignatureConfiguration_SetFieldNameA
#define PdfToolsSign_SignatureConfiguration_GetName      PdfToolsSign_SignatureConfiguration_GetNameA

#define PdfToolsSign_SignatureConfiguration_GetLocation    PdfToolsSign_SignatureConfiguration_GetLocationA
#define PdfToolsSign_SignatureConfiguration_SetLocation    PdfToolsSign_SignatureConfiguration_SetLocationA
#define PdfToolsSign_SignatureConfiguration_GetReason      PdfToolsSign_SignatureConfiguration_GetReasonA
#define PdfToolsSign_SignatureConfiguration_SetReason      PdfToolsSign_SignatureConfiguration_SetReasonA
#define PdfToolsSign_SignatureConfiguration_GetContactInfo PdfToolsSign_SignatureConfiguration_GetContactInfoA
#define PdfToolsSign_SignatureConfiguration_SetContactInfo PdfToolsSign_SignatureConfiguration_SetContactInfoA

#define PdfToolsSign_TimestampConfiguration_GetFieldName PdfToolsSign_TimestampConfiguration_GetFieldNameA
#define PdfToolsSign_TimestampConfiguration_SetFieldName PdfToolsSign_TimestampConfiguration_SetFieldNameA

#define PdfToolsSign_SignatureFieldOptions_GetFieldName PdfToolsSign_SignatureFieldOptions_GetFieldNameA
#define PdfToolsSign_SignatureFieldOptions_SetFieldName PdfToolsSign_SignatureFieldOptions_SetFieldNameA

#define TPdfToolsSign_Signer_Warning             TPdfToolsSign_Signer_WarningA
#define PdfToolsSign_Signer_AddWarningHandler    PdfToolsSign_Signer_AddWarningHandlerA
#define PdfToolsSign_Signer_RemoveWarningHandler PdfToolsSign_Signer_RemoveWarningHandlerA

#endif

typedef void(PDFTOOLS_CALL* TPdfToolsSign_Signer_WarningA)(void* pContext, const char* szMessage,
                                                           TPdfToolsSign_WarningCategory iCategory,
                                                           const char*                   szContext);
typedef void(PDFTOOLS_CALL* TPdfToolsSign_Signer_WarningW)(void* pContext, const WCHAR* szMessage,
                                                           TPdfToolsSign_WarningCategory iCategory,
                                                           const WCHAR*                  szContext);

/******************************************************************************
 * CustomTextVariableMap
 *****************************************************************************/
PDFTOOLS_EXPORT int PDFTOOLS_CALL
PdfToolsSign_CustomTextVariableMap_GetCount(TPdfToolsSign_CustomTextVariableMap* pCustomTextVariableMap);
PDFTOOLS_EXPORT int PDFTOOLS_CALL PdfToolsSign_CustomTextVariableMap_GetSize(
    TPdfToolsSign_CustomTextVariableMap* pCustomTextVariableMap); // Deprecated in Version 2.11.0.
PDFTOOLS_EXPORT int PDFTOOLS_CALL
PdfToolsSign_CustomTextVariableMap_GetBegin(TPdfToolsSign_CustomTextVariableMap* pCustomTextVariableMap);
PDFTOOLS_EXPORT int PDFTOOLS_CALL
PdfToolsSign_CustomTextVariableMap_GetEnd(TPdfToolsSign_CustomTextVariableMap* pCustomTextVariableMap);
PDFTOOLS_EXPORT int PDFTOOLS_CALL
PdfToolsSign_CustomTextVariableMap_GetNext(TPdfToolsSign_CustomTextVariableMap* pCustomTextVariableMap, int it);
PDFTOOLS_EXPORT int PDFTOOLS_CALL
PdfToolsSign_CustomTextVariableMap_GetA(TPdfToolsSign_CustomTextVariableMap* pCustomTextVariableMap, const char* szKey);
PDFTOOLS_EXPORT int PDFTOOLS_CALL PdfToolsSign_CustomTextVariableMap_GetW(
    TPdfToolsSign_CustomTextVariableMap* pCustomTextVariableMap, const WCHAR* szKey);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSign_CustomTextVariableMap_GetKeyA(
    TPdfToolsSign_CustomTextVariableMap* pCustomTextVariableMap, int it, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSign_CustomTextVariableMap_GetKeyW(
    TPdfToolsSign_CustomTextVariableMap* pCustomTextVariableMap, int it, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSign_CustomTextVariableMap_GetValueA(
    TPdfToolsSign_CustomTextVariableMap* pCustomTextVariableMap, int it, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSign_CustomTextVariableMap_GetValueW(
    TPdfToolsSign_CustomTextVariableMap* pCustomTextVariableMap, int it, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_CustomTextVariableMap_SetA(
    TPdfToolsSign_CustomTextVariableMap* pCustomTextVariableMap, const char* szKey, const char* szValue);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_CustomTextVariableMap_SetW(
    TPdfToolsSign_CustomTextVariableMap* pCustomTextVariableMap, const WCHAR* szKey, const WCHAR* szValue);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_CustomTextVariableMap_SetValueA(
    TPdfToolsSign_CustomTextVariableMap* pCustomTextVariableMap, int it, const char* szValue);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_CustomTextVariableMap_SetValueW(
    TPdfToolsSign_CustomTextVariableMap* pCustomTextVariableMap, int it, const WCHAR* szValue);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsSign_CustomTextVariableMap_Clear(TPdfToolsSign_CustomTextVariableMap* pCustomTextVariableMap);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsSign_CustomTextVariableMap_Remove(TPdfToolsSign_CustomTextVariableMap* pCustomTextVariableMap, int it);

/******************************************************************************
 * Appearance
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsSign_Appearance* PDFTOOLS_CALL
PdfToolsSign_Appearance_CreateFromJson(const TPdfToolsSys_StreamDescriptor* pStreamDesc);
PDFTOOLS_EXPORT TPdfToolsSign_Appearance* PDFTOOLS_CALL
PdfToolsSign_Appearance_CreateFromXml(const TPdfToolsSys_StreamDescriptor* pStreamDesc);
PDFTOOLS_EXPORT TPdfToolsSign_Appearance* PDFTOOLS_CALL
PdfToolsSign_Appearance_CreateFieldBoundingBox(const TPdfToolsGeomUnits_Size* pSize);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_Appearance_GetPageNumber(TPdfToolsSign_Appearance* pAppearance,
                                                                         int*                      pPageNumber);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_Appearance_SetPageNumber(TPdfToolsSign_Appearance* pAppearance,
                                                                         const int*                pPageNumber);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_Appearance_GetTop(TPdfToolsSign_Appearance* pAppearance, double* pTop);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_Appearance_SetTop(TPdfToolsSign_Appearance* pAppearance,
                                                                  const double*             pTop);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_Appearance_GetRight(TPdfToolsSign_Appearance* pAppearance,
                                                                    double*                   pRight);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_Appearance_SetRight(TPdfToolsSign_Appearance* pAppearance,
                                                                    const double*             pRight);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_Appearance_GetBottom(TPdfToolsSign_Appearance* pAppearance,
                                                                     double*                   pBottom);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_Appearance_SetBottom(TPdfToolsSign_Appearance* pAppearance,
                                                                     const double*             pBottom);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_Appearance_GetLeft(TPdfToolsSign_Appearance* pAppearance,
                                                                   double*                   pLeft);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_Appearance_SetLeft(TPdfToolsSign_Appearance* pAppearance,
                                                                   const double*             pLeft);
PDFTOOLS_EXPORT TPdfToolsSign_CustomTextVariableMap* PDFTOOLS_CALL
PdfToolsSign_Appearance_GetCustomTextVariables(TPdfToolsSign_Appearance* pAppearance);

/******************************************************************************
 * SignatureConfiguration
 *****************************************************************************/
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSign_SignatureConfiguration_GetFieldNameA(
    TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSign_SignatureConfiguration_GetFieldNameW(
    TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_SignatureConfiguration_SetFieldNameA(
    TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration, const char* szFieldName);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_SignatureConfiguration_SetFieldNameW(
    TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration, const WCHAR* szFieldName);
PDFTOOLS_EXPORT TPdfToolsSign_Appearance* PDFTOOLS_CALL
PdfToolsSign_SignatureConfiguration_GetAppearance(TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_SignatureConfiguration_SetAppearance(
    TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration, TPdfToolsSign_Appearance* pAppearance);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSign_SignatureConfiguration_GetNameA(
    TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSign_SignatureConfiguration_GetNameW(
    TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSign_SignatureConfiguration_GetLocationA(
    TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSign_SignatureConfiguration_GetLocationW(
    TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_SignatureConfiguration_SetLocationA(
    TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration, const char* szLocation);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_SignatureConfiguration_SetLocationW(
    TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration, const WCHAR* szLocation);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSign_SignatureConfiguration_GetReasonA(
    TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSign_SignatureConfiguration_GetReasonW(
    TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_SignatureConfiguration_SetReasonA(
    TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration, const char* szReason);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_SignatureConfiguration_SetReasonW(
    TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration, const WCHAR* szReason);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSign_SignatureConfiguration_GetContactInfoA(
    TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSign_SignatureConfiguration_GetContactInfoW(
    TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_SignatureConfiguration_SetContactInfoA(
    TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration, const char* szContactInfo);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_SignatureConfiguration_SetContactInfoW(
    TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration, const WCHAR* szContactInfo);

PDFTOOLS_EXPORT TPdfToolsSign_SignatureConfigurationType PDFTOOLS_CALL
PdfToolsSign_SignatureConfiguration_GetType(TPdfToolsSign_SignatureConfiguration* pSignatureConfiguration);
/******************************************************************************
 * TimestampConfiguration
 *****************************************************************************/
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSign_TimestampConfiguration_GetFieldNameA(
    TPdfToolsSign_TimestampConfiguration* pTimestampConfiguration, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSign_TimestampConfiguration_GetFieldNameW(
    TPdfToolsSign_TimestampConfiguration* pTimestampConfiguration, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_TimestampConfiguration_SetFieldNameA(
    TPdfToolsSign_TimestampConfiguration* pTimestampConfiguration, const char* szFieldName);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_TimestampConfiguration_SetFieldNameW(
    TPdfToolsSign_TimestampConfiguration* pTimestampConfiguration, const WCHAR* szFieldName);
PDFTOOLS_EXPORT TPdfToolsSign_Appearance* PDFTOOLS_CALL
PdfToolsSign_TimestampConfiguration_GetAppearance(TPdfToolsSign_TimestampConfiguration* pTimestampConfiguration);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_TimestampConfiguration_SetAppearance(
    TPdfToolsSign_TimestampConfiguration* pTimestampConfiguration, TPdfToolsSign_Appearance* pAppearance);

PDFTOOLS_EXPORT TPdfToolsSign_TimestampConfigurationType PDFTOOLS_CALL
PdfToolsSign_TimestampConfiguration_GetType(TPdfToolsSign_TimestampConfiguration* pTimestampConfiguration);
/******************************************************************************
 * OutputOptions
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsSign_OutputOptions* PDFTOOLS_CALL PdfToolsSign_OutputOptions_New(void);

PDFTOOLS_EXPORT TPdfToolsSign_SignatureRemoval PDFTOOLS_CALL
PdfToolsSign_OutputOptions_GetRemoveSignatures(TPdfToolsSign_OutputOptions* pOutputOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_OutputOptions_SetRemoveSignatures(
    TPdfToolsSign_OutputOptions* pOutputOptions, TPdfToolsSign_SignatureRemoval iRemoveSignatures);
PDFTOOLS_EXPORT TPdfToolsSign_AddValidationInformation PDFTOOLS_CALL
PdfToolsSign_OutputOptions_GetAddValidationInformation(TPdfToolsSign_OutputOptions* pOutputOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_OutputOptions_SetAddValidationInformation(
    TPdfToolsSign_OutputOptions* pOutputOptions, TPdfToolsSign_AddValidationInformation iAddValidationInformation);

/******************************************************************************
 * MdpPermissionOptions
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsSign_MdpPermissionOptions* PDFTOOLS_CALL
PdfToolsSign_MdpPermissionOptions_New(TPdfToolsPdf_MdpPermissions iPermissions);

PDFTOOLS_EXPORT TPdfToolsPdf_MdpPermissions PDFTOOLS_CALL
PdfToolsSign_MdpPermissionOptions_GetPermissions(TPdfToolsSign_MdpPermissionOptions* pMdpPermissionOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_MdpPermissionOptions_SetPermissions(
    TPdfToolsSign_MdpPermissionOptions* pMdpPermissionOptions, TPdfToolsPdf_MdpPermissions iPermissions);

/******************************************************************************
 * SignatureFieldOptions
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsSign_SignatureFieldOptions* PDFTOOLS_CALL
PdfToolsSign_SignatureFieldOptions_New(TPdfToolsSign_Appearance* pBoundingBox);

PDFTOOLS_EXPORT TPdfToolsSign_Appearance* PDFTOOLS_CALL
PdfToolsSign_SignatureFieldOptions_GetBoundingBox(TPdfToolsSign_SignatureFieldOptions* pSignatureFieldOptions);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSign_SignatureFieldOptions_GetFieldNameA(
    TPdfToolsSign_SignatureFieldOptions* pSignatureFieldOptions, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSign_SignatureFieldOptions_GetFieldNameW(
    TPdfToolsSign_SignatureFieldOptions* pSignatureFieldOptions, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_SignatureFieldOptions_SetFieldNameA(
    TPdfToolsSign_SignatureFieldOptions* pSignatureFieldOptions, const char* szFieldName);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_SignatureFieldOptions_SetFieldNameW(
    TPdfToolsSign_SignatureFieldOptions* pSignatureFieldOptions, const WCHAR* szFieldName);

/******************************************************************************
 * PreparedDocument
 *****************************************************************************/
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsSign_PreparedDocument_GetHash(
    TPdfToolsSign_PreparedDocument* pPreparedDocument, TPdfToolsCrypto_HashAlgorithm iAlgorithm, unsigned char* pBuffer,
    size_t nBufferSize);

/******************************************************************************
 * Signer
 *****************************************************************************/
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_Signer_AddWarningHandlerA(TPdfToolsSign_Signer* pSigner, void* pContext,
                                                                          TPdfToolsSign_Signer_WarningA pFunction);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_Signer_AddWarningHandlerW(TPdfToolsSign_Signer* pSigner, void* pContext,
                                                                          TPdfToolsSign_Signer_WarningW pFunction);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_Signer_RemoveWarningHandlerA(TPdfToolsSign_Signer*         pSigner,
                                                                             void*                         pContext,
                                                                             TPdfToolsSign_Signer_WarningA pFunction);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsSign_Signer_RemoveWarningHandlerW(TPdfToolsSign_Signer*         pSigner,
                                                                             void*                         pContext,
                                                                             TPdfToolsSign_Signer_WarningW pFunction);

PDFTOOLS_EXPORT TPdfToolsSign_Signer* PDFTOOLS_CALL PdfToolsSign_Signer_New(void);

PDFTOOLS_EXPORT TPdfToolsPdf_Document* PDFTOOLS_CALL
PdfToolsSign_Signer_Sign(TPdfToolsSign_Signer* pSigner, TPdfToolsPdf_Document* pDocument,
                         TPdfToolsSign_SignatureConfiguration* pConfiguration,
                         const TPdfToolsSys_StreamDescriptor* pStreamDesc, TPdfToolsSign_OutputOptions* pOutputOptions);
PDFTOOLS_EXPORT TPdfToolsPdf_Document* PDFTOOLS_CALL PdfToolsSign_Signer_Certify(
    TPdfToolsSign_Signer* pSigner, TPdfToolsPdf_Document* pDocument,
    TPdfToolsSign_SignatureConfiguration* pConfiguration, const TPdfToolsSys_StreamDescriptor* pStreamDesc,
    TPdfToolsSign_MdpPermissionOptions* pPermissions, TPdfToolsSign_OutputOptions* pOutputOptions);
PDFTOOLS_EXPORT TPdfToolsPdf_Document* PDFTOOLS_CALL PdfToolsSign_Signer_AddTimestamp(
    TPdfToolsSign_Signer* pSigner, TPdfToolsPdf_Document* pDocument,
    TPdfToolsSign_TimestampConfiguration* pConfiguration, const TPdfToolsSys_StreamDescriptor* pStreamDesc,
    TPdfToolsSign_OutputOptions* pOutputOptions);
PDFTOOLS_EXPORT TPdfToolsPdf_Document* PDFTOOLS_CALL PdfToolsSign_Signer_AddSignatureField(
    TPdfToolsSign_Signer* pSigner, TPdfToolsPdf_Document* pDocument, TPdfToolsSign_SignatureFieldOptions* pOptions,
    const TPdfToolsSys_StreamDescriptor* pStreamDesc, TPdfToolsSign_OutputOptions* pOutputOptions);
PDFTOOLS_EXPORT TPdfToolsSign_PreparedDocument* PDFTOOLS_CALL PdfToolsSign_Signer_AddPreparedSignature(
    TPdfToolsSign_Signer* pSigner, TPdfToolsPdf_Document* pDocument,
    TPdfToolsSign_SignatureConfiguration* pConfiguration, const TPdfToolsSys_StreamDescriptor* pStreamDesc,
    TPdfToolsSign_OutputOptions* pOutputOptions);
PDFTOOLS_EXPORT TPdfToolsPdf_Document* PDFTOOLS_CALL PdfToolsSign_Signer_SignPreparedSignature(
    TPdfToolsSign_Signer* pSigner, TPdfToolsPdf_Document* pDocument,
    TPdfToolsSign_SignatureConfiguration* pConfiguration, const TPdfToolsSys_StreamDescriptor* pStreamDesc);
PDFTOOLS_EXPORT TPdfToolsPdf_Document* PDFTOOLS_CALL PdfToolsSign_Signer_Process(
    TPdfToolsSign_Signer* pSigner, TPdfToolsPdf_Document* pDocument, const TPdfToolsSys_StreamDescriptor* pStreamDesc,
    TPdfToolsSign_OutputOptions* pOutputOptions, TPdfToolsCryptoProviders_Provider* pProvider);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSSIGN_H__ */
