/******************************************************************************
 *
 * File:            PdfTools_PdfToolsPdf.h
 *
 * Description:     Sub Header file for Pdftools SDK
 *
 * Author:          PDF Tools AG
 *
 * Copyright:       Copyright (C) 2023 - 2024 PDF Tools AG, Switzerland
 *                  All rights reserved.
 *
 *****************************************************************************/

#ifndef PDFTOOLS_PDFTOOLSPDF_H__
#define PDFTOOLS_PDFTOOLSPDF_H__

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
#define PdfToolsPdf_MetadataSettings_GetTitle    PdfToolsPdf_MetadataSettings_GetTitleW
#define PdfToolsPdf_MetadataSettings_SetTitle    PdfToolsPdf_MetadataSettings_SetTitleW
#define PdfToolsPdf_MetadataSettings_GetAuthor   PdfToolsPdf_MetadataSettings_GetAuthorW
#define PdfToolsPdf_MetadataSettings_SetAuthor   PdfToolsPdf_MetadataSettings_SetAuthorW
#define PdfToolsPdf_MetadataSettings_GetSubject  PdfToolsPdf_MetadataSettings_GetSubjectW
#define PdfToolsPdf_MetadataSettings_SetSubject  PdfToolsPdf_MetadataSettings_SetSubjectW
#define PdfToolsPdf_MetadataSettings_GetKeywords PdfToolsPdf_MetadataSettings_GetKeywordsW
#define PdfToolsPdf_MetadataSettings_SetKeywords PdfToolsPdf_MetadataSettings_SetKeywordsW
#define PdfToolsPdf_MetadataSettings_GetCreator  PdfToolsPdf_MetadataSettings_GetCreatorW
#define PdfToolsPdf_MetadataSettings_SetCreator  PdfToolsPdf_MetadataSettings_SetCreatorW
#define PdfToolsPdf_MetadataSettings_GetProducer PdfToolsPdf_MetadataSettings_GetProducerW
#define PdfToolsPdf_MetadataSettings_SetProducer PdfToolsPdf_MetadataSettings_SetProducerW

#define PdfToolsPdf_Encryption_New            PdfToolsPdf_Encryption_NewW
#define PdfToolsPdf_Encryption_SetPermissions PdfToolsPdf_Encryption_SetPermissionsW

#define PdfToolsPdf_Encryption_GetUserPassword  PdfToolsPdf_Encryption_GetUserPasswordW
#define PdfToolsPdf_Encryption_SetUserPassword  PdfToolsPdf_Encryption_SetUserPasswordW
#define PdfToolsPdf_Encryption_GetOwnerPassword PdfToolsPdf_Encryption_GetOwnerPasswordW

#define PdfToolsPdf_Document_Open PdfToolsPdf_Document_OpenW

#define PdfToolsPdf_Metadata_GetTitle PdfToolsPdf_Metadata_GetTitleW

#define PdfToolsPdf_Metadata_GetAuthor PdfToolsPdf_Metadata_GetAuthorW

#define PdfToolsPdf_Metadata_GetSubject PdfToolsPdf_Metadata_GetSubjectW

#define PdfToolsPdf_Metadata_GetKeywords PdfToolsPdf_Metadata_GetKeywordsW

#define PdfToolsPdf_Metadata_GetCreator PdfToolsPdf_Metadata_GetCreatorW

#define PdfToolsPdf_Metadata_GetProducer PdfToolsPdf_Metadata_GetProducerW

#define PdfToolsPdf_SignatureField_GetFieldName PdfToolsPdf_SignatureField_GetFieldNameW

#define PdfToolsPdf_SignedSignatureField_GetName PdfToolsPdf_SignedSignatureField_GetNameW

#define PdfToolsPdf_Signature_GetLocation PdfToolsPdf_Signature_GetLocationW

#define PdfToolsPdf_Signature_GetReason PdfToolsPdf_Signature_GetReasonW

#define PdfToolsPdf_Signature_GetContactInfo PdfToolsPdf_Signature_GetContactInfoW

#else
#define PdfToolsPdf_MetadataSettings_GetTitle    PdfToolsPdf_MetadataSettings_GetTitleA
#define PdfToolsPdf_MetadataSettings_SetTitle    PdfToolsPdf_MetadataSettings_SetTitleA
#define PdfToolsPdf_MetadataSettings_GetAuthor   PdfToolsPdf_MetadataSettings_GetAuthorA
#define PdfToolsPdf_MetadataSettings_SetAuthor   PdfToolsPdf_MetadataSettings_SetAuthorA
#define PdfToolsPdf_MetadataSettings_GetSubject  PdfToolsPdf_MetadataSettings_GetSubjectA
#define PdfToolsPdf_MetadataSettings_SetSubject  PdfToolsPdf_MetadataSettings_SetSubjectA
#define PdfToolsPdf_MetadataSettings_GetKeywords PdfToolsPdf_MetadataSettings_GetKeywordsA
#define PdfToolsPdf_MetadataSettings_SetKeywords PdfToolsPdf_MetadataSettings_SetKeywordsA
#define PdfToolsPdf_MetadataSettings_GetCreator  PdfToolsPdf_MetadataSettings_GetCreatorA
#define PdfToolsPdf_MetadataSettings_SetCreator  PdfToolsPdf_MetadataSettings_SetCreatorA
#define PdfToolsPdf_MetadataSettings_GetProducer PdfToolsPdf_MetadataSettings_GetProducerA
#define PdfToolsPdf_MetadataSettings_SetProducer PdfToolsPdf_MetadataSettings_SetProducerA

#define PdfToolsPdf_Encryption_New            PdfToolsPdf_Encryption_NewA
#define PdfToolsPdf_Encryption_SetPermissions PdfToolsPdf_Encryption_SetPermissionsA

#define PdfToolsPdf_Encryption_GetUserPassword  PdfToolsPdf_Encryption_GetUserPasswordA
#define PdfToolsPdf_Encryption_SetUserPassword  PdfToolsPdf_Encryption_SetUserPasswordA
#define PdfToolsPdf_Encryption_GetOwnerPassword PdfToolsPdf_Encryption_GetOwnerPasswordA

#define PdfToolsPdf_Document_Open PdfToolsPdf_Document_OpenA

#define PdfToolsPdf_Metadata_GetTitle PdfToolsPdf_Metadata_GetTitleA

#define PdfToolsPdf_Metadata_GetAuthor PdfToolsPdf_Metadata_GetAuthorA

#define PdfToolsPdf_Metadata_GetSubject PdfToolsPdf_Metadata_GetSubjectA

#define PdfToolsPdf_Metadata_GetKeywords PdfToolsPdf_Metadata_GetKeywordsA

#define PdfToolsPdf_Metadata_GetCreator PdfToolsPdf_Metadata_GetCreatorA

#define PdfToolsPdf_Metadata_GetProducer PdfToolsPdf_Metadata_GetProducerA

#define PdfToolsPdf_SignatureField_GetFieldName PdfToolsPdf_SignatureField_GetFieldNameA

#define PdfToolsPdf_SignedSignatureField_GetName PdfToolsPdf_SignedSignatureField_GetNameA

#define PdfToolsPdf_Signature_GetLocation PdfToolsPdf_Signature_GetLocationA

#define PdfToolsPdf_Signature_GetReason PdfToolsPdf_Signature_GetReasonA

#define PdfToolsPdf_Signature_GetContactInfo PdfToolsPdf_Signature_GetContactInfoA

#endif

/******************************************************************************
 * MetadataSettings
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf_MetadataSettings* PDFTOOLS_CALL PdfToolsPdf_MetadataSettings_New(void);

PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_MetadataSettings_GetTitleA(
    TPdfToolsPdf_MetadataSettings* pMetadataSettings, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_MetadataSettings_GetTitleW(
    TPdfToolsPdf_MetadataSettings* pMetadataSettings, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsPdf_MetadataSettings_SetTitleA(TPdfToolsPdf_MetadataSettings* pMetadataSettings, const char* szTitle);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsPdf_MetadataSettings_SetTitleW(TPdfToolsPdf_MetadataSettings* pMetadataSettings, const WCHAR* szTitle);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_MetadataSettings_GetAuthorA(
    TPdfToolsPdf_MetadataSettings* pMetadataSettings, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_MetadataSettings_GetAuthorW(
    TPdfToolsPdf_MetadataSettings* pMetadataSettings, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsPdf_MetadataSettings_SetAuthorA(TPdfToolsPdf_MetadataSettings* pMetadataSettings, const char* szAuthor);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsPdf_MetadataSettings_SetAuthorW(TPdfToolsPdf_MetadataSettings* pMetadataSettings, const WCHAR* szAuthor);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_MetadataSettings_GetSubjectA(
    TPdfToolsPdf_MetadataSettings* pMetadataSettings, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_MetadataSettings_GetSubjectW(
    TPdfToolsPdf_MetadataSettings* pMetadataSettings, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsPdf_MetadataSettings_SetSubjectA(TPdfToolsPdf_MetadataSettings* pMetadataSettings, const char* szSubject);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsPdf_MetadataSettings_SetSubjectW(TPdfToolsPdf_MetadataSettings* pMetadataSettings, const WCHAR* szSubject);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_MetadataSettings_GetKeywordsA(
    TPdfToolsPdf_MetadataSettings* pMetadataSettings, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_MetadataSettings_GetKeywordsW(
    TPdfToolsPdf_MetadataSettings* pMetadataSettings, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsPdf_MetadataSettings_SetKeywordsA(TPdfToolsPdf_MetadataSettings* pMetadataSettings, const char* szKeywords);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsPdf_MetadataSettings_SetKeywordsW(TPdfToolsPdf_MetadataSettings* pMetadataSettings, const WCHAR* szKeywords);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_MetadataSettings_GetCreatorA(
    TPdfToolsPdf_MetadataSettings* pMetadataSettings, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_MetadataSettings_GetCreatorW(
    TPdfToolsPdf_MetadataSettings* pMetadataSettings, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsPdf_MetadataSettings_SetCreatorA(TPdfToolsPdf_MetadataSettings* pMetadataSettings, const char* szCreator);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsPdf_MetadataSettings_SetCreatorW(TPdfToolsPdf_MetadataSettings* pMetadataSettings, const WCHAR* szCreator);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_MetadataSettings_GetProducerA(
    TPdfToolsPdf_MetadataSettings* pMetadataSettings, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_MetadataSettings_GetProducerW(
    TPdfToolsPdf_MetadataSettings* pMetadataSettings, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsPdf_MetadataSettings_SetProducerA(TPdfToolsPdf_MetadataSettings* pMetadataSettings, const char* szProducer);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL
PdfToolsPdf_MetadataSettings_SetProducerW(TPdfToolsPdf_MetadataSettings* pMetadataSettings, const WCHAR* szProducer);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf_MetadataSettings_GetCreationDate(
    TPdfToolsPdf_MetadataSettings* pMetadataSettings, TPdfToolsSys_Date* pCreationDate);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf_MetadataSettings_SetCreationDate(
    TPdfToolsPdf_MetadataSettings* pMetadataSettings, const TPdfToolsSys_Date* pCreationDate);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf_MetadataSettings_GetModificationDate(
    TPdfToolsPdf_MetadataSettings* pMetadataSettings, TPdfToolsSys_Date* pModificationDate);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf_MetadataSettings_SetModificationDate(
    TPdfToolsPdf_MetadataSettings* pMetadataSettings, const TPdfToolsSys_Date* pModificationDate);

/******************************************************************************
 * Encryption
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf_Encryption* PDFTOOLS_CALL PdfToolsPdf_Encryption_NewA(
    const char* szUserPassword, const char* szOwnerPassword, TPdfToolsPdf_Permission iPermissions);
PDFTOOLS_EXPORT TPdfToolsPdf_Encryption* PDFTOOLS_CALL PdfToolsPdf_Encryption_NewW(
    const WCHAR* szUserPassword, const WCHAR* szOwnerPassword, TPdfToolsPdf_Permission iPermissions);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf_Encryption_SetPermissionsA(TPdfToolsPdf_Encryption* pEncryption,
                                                                          const char*              szOwnerPassword,
                                                                          TPdfToolsPdf_Permission  iPermissions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf_Encryption_SetPermissionsW(TPdfToolsPdf_Encryption* pEncryption,
                                                                          const WCHAR*             szOwnerPassword,
                                                                          TPdfToolsPdf_Permission  iPermissions);

PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Encryption_GetUserPasswordA(TPdfToolsPdf_Encryption* pEncryption,
                                                                             char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Encryption_GetUserPasswordW(TPdfToolsPdf_Encryption* pEncryption,
                                                                             WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL   PdfToolsPdf_Encryption_SetUserPasswordA(TPdfToolsPdf_Encryption* pEncryption,
                                                                             const char*              szUserPassword);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL   PdfToolsPdf_Encryption_SetUserPasswordW(TPdfToolsPdf_Encryption* pEncryption,
                                                                             const WCHAR*             szUserPassword);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Encryption_GetOwnerPasswordA(TPdfToolsPdf_Encryption* pEncryption,
                                                                              char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Encryption_GetOwnerPasswordW(TPdfToolsPdf_Encryption* pEncryption,
                                                                              WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT TPdfToolsPdf_Permission PDFTOOLS_CALL
PdfToolsPdf_Encryption_GetPermissions(TPdfToolsPdf_Encryption* pEncryption);

/******************************************************************************
 * OutputOptions
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf_OutputOptions* PDFTOOLS_CALL PdfToolsPdf_OutputOptions_New(void);

PDFTOOLS_EXPORT TPdfToolsPdf_Encryption* PDFTOOLS_CALL
                                   PdfToolsPdf_OutputOptions_GetEncryption(TPdfToolsPdf_OutputOptions* pOutputOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf_OutputOptions_SetEncryption(TPdfToolsPdf_OutputOptions* pOutputOptions,
                                                                           TPdfToolsPdf_Encryption*    pEncryption);
PDFTOOLS_EXPORT TPdfToolsPdf_MetadataSettings* PDFTOOLS_CALL
PdfToolsPdf_OutputOptions_GetMetadataSettings(TPdfToolsPdf_OutputOptions* pOutputOptions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf_OutputOptions_SetMetadataSettings(
    TPdfToolsPdf_OutputOptions* pOutputOptions, TPdfToolsPdf_MetadataSettings* pMetadataSettings);

PDFTOOLS_EXPORT TPdfToolsPdf_OutputOptionsType PDFTOOLS_CALL
PdfToolsPdf_OutputOptions_GetType(TPdfToolsPdf_OutputOptions* pOutputOptions);
/******************************************************************************
 * Document
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf_Document* PDFTOOLS_CALL
PdfToolsPdf_Document_OpenA(const TPdfToolsSys_StreamDescriptor* pStreamDesc, const char* szPassword);
PDFTOOLS_EXPORT TPdfToolsPdf_Document* PDFTOOLS_CALL
PdfToolsPdf_Document_OpenW(const TPdfToolsSys_StreamDescriptor* pStreamDesc, const WCHAR* szPassword);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf_Document_GetConformance(TPdfToolsPdf_Document*    pDocument,
                                                                       TPdfToolsPdf_Conformance* pConformance);
PDFTOOLS_EXPORT int PDFTOOLS_CALL  PdfToolsPdf_Document_GetPageCount(TPdfToolsPdf_Document* pDocument);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf_Document_GetPermissions(TPdfToolsPdf_Document*   pDocument,
                                                                       TPdfToolsPdf_Permission* pPermissions);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf_Document_IsLinearized(TPdfToolsPdf_Document* pDocument);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf_Document_IsSigned(TPdfToolsPdf_Document* pDocument);
PDFTOOLS_EXPORT TPdfToolsPdf_SignatureFieldList* PDFTOOLS_CALL
PdfToolsPdf_Document_GetSignatureFields(TPdfToolsPdf_Document* pDocument);
PDFTOOLS_EXPORT TPdfToolsPdf_XfaType PDFTOOLS_CALL   PdfToolsPdf_Document_GetXfa(TPdfToolsPdf_Document* pDocument);
PDFTOOLS_EXPORT TPdfToolsPdf_Metadata* PDFTOOLS_CALL PdfToolsPdf_Document_GetMetadata(TPdfToolsPdf_Document* pDocument);

PDFTOOLS_EXPORT TPdfToolsPdf_DocumentType PDFTOOLS_CALL PdfToolsPdf_Document_GetType(TPdfToolsPdf_Document* pDocument);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL                      PdfToolsPdf_Document_Close(TPdfToolsPdf_Document* pObject);
/******************************************************************************
 * Metadata
 *****************************************************************************/
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Metadata_GetTitleA(TPdfToolsPdf_Metadata* pMetadata, char* pBuffer,
                                                                    size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Metadata_GetTitleW(TPdfToolsPdf_Metadata* pMetadata, WCHAR* pBuffer,
                                                                    size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Metadata_GetAuthorA(TPdfToolsPdf_Metadata* pMetadata, char* pBuffer,
                                                                     size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Metadata_GetAuthorW(TPdfToolsPdf_Metadata* pMetadata, WCHAR* pBuffer,
                                                                     size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Metadata_GetSubjectA(TPdfToolsPdf_Metadata* pMetadata, char* pBuffer,
                                                                      size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Metadata_GetSubjectW(TPdfToolsPdf_Metadata* pMetadata, WCHAR* pBuffer,
                                                                      size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Metadata_GetKeywordsA(TPdfToolsPdf_Metadata* pMetadata, char* pBuffer,
                                                                       size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Metadata_GetKeywordsW(TPdfToolsPdf_Metadata* pMetadata, WCHAR* pBuffer,
                                                                       size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Metadata_GetCreatorA(TPdfToolsPdf_Metadata* pMetadata, char* pBuffer,
                                                                      size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Metadata_GetCreatorW(TPdfToolsPdf_Metadata* pMetadata, WCHAR* pBuffer,
                                                                      size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Metadata_GetProducerA(TPdfToolsPdf_Metadata* pMetadata, char* pBuffer,
                                                                       size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Metadata_GetProducerW(TPdfToolsPdf_Metadata* pMetadata, WCHAR* pBuffer,
                                                                       size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL   PdfToolsPdf_Metadata_GetCreationDate(TPdfToolsPdf_Metadata* pMetadata,
                                                                          TPdfToolsSys_Date*     pCreationDate);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL   PdfToolsPdf_Metadata_GetModificationDate(TPdfToolsPdf_Metadata* pMetadata,
                                                                              TPdfToolsSys_Date*     pModificationDate);

/******************************************************************************
 * SignatureField
 *****************************************************************************/
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_SignatureField_GetFieldNameA(
    TPdfToolsPdf_SignatureField* pSignatureField, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_SignatureField_GetFieldNameW(
    TPdfToolsPdf_SignatureField* pSignatureField, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT int PDFTOOLS_CALL
PdfToolsPdf_SignatureField_GetPageNumber(TPdfToolsPdf_SignatureField* pSignatureField);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf_SignatureField_GetBoundingBox(
    TPdfToolsPdf_SignatureField* pSignatureField, TPdfToolsGeomUnits_Rectangle* pBoundingBox);

PDFTOOLS_EXPORT TPdfToolsPdf_SignatureFieldType PDFTOOLS_CALL
PdfToolsPdf_SignatureField_GetType(TPdfToolsPdf_SignatureField* pSignatureField);
/******************************************************************************
 * SignedSignatureField
 *****************************************************************************/
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_SignedSignatureField_GetNameA(
    TPdfToolsPdf_SignedSignatureField* pSignedSignatureField, char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_SignedSignatureField_GetNameW(
    TPdfToolsPdf_SignedSignatureField* pSignedSignatureField, WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf_SignedSignatureField_GetDate(
    TPdfToolsPdf_SignedSignatureField* pSignedSignatureField, TPdfToolsSys_Date* pDate);
PDFTOOLS_EXPORT TPdfToolsPdf_Revision* PDFTOOLS_CALL
PdfToolsPdf_SignedSignatureField_GetRevision(TPdfToolsPdf_SignedSignatureField* pSignedSignatureField);

PDFTOOLS_EXPORT TPdfToolsPdf_SignedSignatureFieldType PDFTOOLS_CALL
PdfToolsPdf_SignedSignatureField_GetType(TPdfToolsPdf_SignedSignatureField* pSignedSignatureField);
/******************************************************************************
 * Signature
 *****************************************************************************/
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Signature_GetLocationA(TPdfToolsPdf_Signature* pSignature,
                                                                        char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Signature_GetLocationW(TPdfToolsPdf_Signature* pSignature,
                                                                        WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Signature_GetReasonA(TPdfToolsPdf_Signature* pSignature, char* pBuffer,
                                                                      size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Signature_GetReasonW(TPdfToolsPdf_Signature* pSignature,
                                                                      WCHAR* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Signature_GetContactInfoA(TPdfToolsPdf_Signature* pSignature,
                                                                           char* pBuffer, size_t nBufferSize);
PDFTOOLS_EXPORT size_t PDFTOOLS_CALL PdfToolsPdf_Signature_GetContactInfoW(TPdfToolsPdf_Signature* pSignature,
                                                                           WCHAR* pBuffer, size_t nBufferSize);

PDFTOOLS_EXPORT TPdfToolsPdf_SignatureType PDFTOOLS_CALL
PdfToolsPdf_Signature_GetType(TPdfToolsPdf_Signature* pSignature);
/******************************************************************************
 * CertificationSignature
 *****************************************************************************/
PDFTOOLS_EXPORT TPdfToolsPdf_MdpPermissions PDFTOOLS_CALL
PdfToolsPdf_CertificationSignature_GetPermissions(TPdfToolsPdf_CertificationSignature* pCertificationSignature);

/******************************************************************************
 * SignatureFieldList
 *****************************************************************************/
PDFTOOLS_EXPORT int PDFTOOLS_CALL
PdfToolsPdf_SignatureFieldList_GetCount(TPdfToolsPdf_SignatureFieldList* pSignatureFieldList);
PDFTOOLS_EXPORT TPdfToolsPdf_SignatureField* PDFTOOLS_CALL
PdfToolsPdf_SignatureFieldList_Get(TPdfToolsPdf_SignatureFieldList* pSignatureFieldList, int iIndex);

/******************************************************************************
 * Revision
 *****************************************************************************/
PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf_Revision_Write(TPdfToolsPdf_Revision*               pRevision,
                                                              const TPdfToolsSys_StreamDescriptor* pStreamDesc);

PDFTOOLS_EXPORT BOOL PDFTOOLS_CALL PdfToolsPdf_Revision_IsLatest(TPdfToolsPdf_Revision* pRevision);

PDFTOOLS_EXPORT TPdfToolsPdf_Conformance PDFTOOLS_CALL PdfToolsPdf_Conformance_ParseW(const WCHAR* szConformanceString);
PDFTOOLS_EXPORT TPdfToolsPdf_Conformance PDFTOOLS_CALL PdfToolsPdf_Conformance_ParseA(const char* szConformanceString);
PDFTOOLS_EXPORT const WCHAR* PDFTOOLS_CALL PdfToolsPdf_Conformance_ToStringW(TPdfToolsPdf_Conformance iConformance);
PDFTOOLS_EXPORT const char* PDFTOOLS_CALL  PdfToolsPdf_Conformance_ToStringA(TPdfToolsPdf_Conformance iConformance);

#ifdef __cplusplus
}
#endif

#endif /* PDFTOOLS_PDFTOOLSPDF_H__ */
